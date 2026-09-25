import os
import json
import time
from openai import OpenAI

DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"
API_KEY = os.environ.get("OPENAI_API_KEY")

GROUPS_MAPPING = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]

# National Standards Matrix to feed the AI correct milestones dynamically
STANDARDS_VAULT = {
    "mathematics": {
        "gk": "One-to-One Correspondence, Cardinality, Counting up to 20, Basic Geometric Shapes.",
        "g1": "Addition/Subtraction within 20, Place Value Tens/Ones, Measuring lengths layout.",
        "g5": "Fractions Multiplication/Division, Volume Constants, Coordinate Grid Cartesian Planes."
    },
    "science": {
        "gk": "Physical properties of materials, Plant/Animal survival needs, Weather/Seasons cycles.",
        "g1": "Light/Sound waves mechanics, Space patterns moon/stars, Organism structural traits."
    }
}

def call_openai_ske_model(prompt_text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are an expert curriculum writer. You output data strictly in raw, valid JSON matching the user's schema blueprint. "
                        "Never output markdown flags, formatting tags, or text outside the JSON object. Keep language engaging and kid-friendly."
                    )
                },
                {"role": "user", "content": prompt_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        return response.choices.message.content.strip()
    except Exception as e:
        print(f"   [API Handshake Postponed] Delaying thread: {str(e)}")
        return None

def build_prompt_blueprint(group, grade, subject, unit, day):
    # Extract standard milestone guidelines dynamically
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, "Age-appropriate national curriculum guidelines and logical ordering proofs.")
    
    return f"""
    Generate an unbendable, production-ready S-K-E data node for Grade {grade.upper()}, Subject Track: {subject}, Day {day}.
    Target Academic Standard Milestone Focus: {standards_focus}
    
    You must output a single, raw valid JSON object with these exact keys:
    {{
        "grade_prefix": "{grade}",
        "layout_group": "{group.upper()}",
        "subject_track": "{subject}",
        "unit_folder": "{unit}",
        "day": {day},
        "lesson_title": "Grade {grade.upper()} {subject.replace('_', ' ').title()} - Day {day} (SKE Edition)",
        "lesson_body": "Write a 3-sentence lesson text introducing the concept. For K-5, explicitly describe the visual shape zones (Zone 1, Zone 2, Zone 3) on their screen and how they connect to the math standard.",
        "interactive_assignment": "Write direct instructions for the student's task. For K-5 Math, tell them exactly what numbered crayon to select and which canvas zone (1, 2, or 3) to fill.",
        "daily_assessment": "State the short evaluation question or check-out problem that verifies complete ownership of this day's concept.",
        "worldview_track_matrices": {{
            "comparative_insight": "Provide a 1-sentence analytical perspective showing absolute structural design or logical order constants over chaotic randomness.",
            "biblical_alignment": "Weave in an explicit scriptural text quote or design constant that aligns perfectly with this specific structural mechanic."
        }}
    }}
    """

def run_mass_vault_generation(start_day=2, end_day=5):
    if not API_KEY:
        print("❌ ERROR: The environment variable 'OPENAI_API_KEY' is missing on this machine.")
        return
        
    print("========================================================================")
    print("🤖 STARTING AUTOMATED BATCH VAULT INGESTION LOOP")
    print(f"Targeting Days: {start_day} to {end_day} across all 13 Grade Tracks")
    print("========================================================================")
    
    for group, grades in GROUPS_MAPPING.items():
        for grade in grades:
            for subject in SUBJECTS:
                for day_num in range(start_day, end_day + 1):
                    
                    # Chronological Unit Router
                    unit = "unit_1_foundations"
                    if day_num > 45 and day_num <= 90: unit = "unit_2_shapes_spaces"
                    elif day_num > 90 and day_num <= 135: unit = "unit_3_weather_seasons"
                    elif day_num > 135: unit = "unit_4_counting_base"
                    
                    folder_path = os.path.join(DATABASE_ROOT, group, grade, subject, unit)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    target_file = os.path.join(folder_path, f"day_{day_num}.json")
                    
                    # Idempotency lock checks
                    if os.path.exists(target_file):
                        continue
                        
                    print(f"📝 Writing SKE Matrix: Grade {grade.upper()} -> {subject.title()} -> Day {day_num}")
                    prompt = build_prompt_blueprint(group, grade, subject, unit, day_num)
                    raw_json = call_openai_ske_model(prompt)
                    
                    if raw_json:
                        try:
                            # Verify structure before writing to disk
                            parsed_data = json.loads(raw_json)
                            with open(target_file, 'w', encoding='utf-8') as f:
                                json.dump(parsed_data, f, indent=4, ensure_ascii=False)
                        except Exception as parse_error:
                            print(f"   ❌ Syntax mismatch caught, skipping file: {str(parse_error)}")
                            
                    time.sleep(1.2) # Prevent network handshake limits

if __name__ == "__main__":
    # Let's run a safe test batch for Days 2, 3, 4, and 5 to see the folders populate!
    run_mass_vault_generation(start_day=2, end_day=5)
