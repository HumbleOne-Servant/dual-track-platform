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

# Upgraded SDK Data Parser: Native v1.0 Array Element Extraction
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
        # FIXED: Added array bracket [0] to match modern Python SDK specifications
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"   [API Handshake Postponed] Delaying thread: {str(e)}")
        return None

def build_prompt_blueprint(group, grade, subject, unit, day):
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, "Age-appropriate national curriculum guidelines and logical ordering proofs.")
    
    # DYNAMIC BRAIN ROUTER: Changes prompt rules based on the active age bracket
    if group == "k5":
        activity_instruction_rule = (
            "Write direct instructions for a Kindergarten/Elementary child. Tell them exactly what numbered crayon node (1, 2, or 3) "
            "to select from their palette box and which graphic chart canvas zone (Zone 1, Zone 2, or Zone 3) to fill to verify the count."
        )
    elif group == "68":
        activity_instruction_rule = (
            "Write clear instructions for a Middle School student. Command them to analyze the textbook equation or science data tracking line, "
            "formulate the balanced sum step-by-step, and input the precise solution integer directly into the 'Isolate Unknown Token Variable (X)' console input box."
        )
    else:
        activity_instruction_rule = (
            "Write advanced academic instructions for a High School student. Command them to analyze the thesis layout statements "
            "and input a multi-paragraph analytical summary evidence proof directly into the Estonian Matrix Optimizer text arena."
        )

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
        "lesson_body": "Write direct textbook prose introducing the concept. Tailor it exactly to Grade {grade.upper()}.",
        "interactive_assignment": "{activity_instruction_rule}",
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
