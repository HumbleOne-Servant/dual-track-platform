# Box 1: Core System Modules and Structural Definition Blueprints
import os
import json
import time
from openai import OpenAI

# Root database path confirmation mapping
DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

# Secure Key Retrieval from terminal environment memory
API_KEY = os.environ.get("OPENAI_API_KEY")

# Complete structural mapping for the entire 13-year curriculum
GROUPS_MAPPING = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]
UNITS = ["unit_1_foundations", "unit_2_shapes_spaces", "unit_3_weather_seasons", "unit_4_counting_base"]
# Box 2: Secure OpenAI API Request Engine (Structured JSON Generator)
def call_generation_model(prompt_text):
    """
    Communicates with gpt-4o-mini via the official OpenAI client SDK.
    Enforces a strict JSON object return profile to guarantee absolute data structuring.
    """
    client = OpenAI(api_key=API_KEY)
    
    retry_delay = 5
    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system", 
                        "content": (
                            "You are a professional children's textbook author specializing in the "
                            "Singapore-Korea-Estonia (SKE) Mastery Framework. You always respond in a strict "
                            "JSON format containing four keys: 'lesson_title', 'lesson_body', "
                            "'interactive_assignment', and 'daily_assessment'. Your text must be purely "
                            "student-facing child reading material. Never include markdown hashes, teacher "
                            "instructions, or lesson plan schedules."
                        )
                    },
                    {"role": "user", "content": prompt_text}
                ],
                temperature=0.3
            )
            
            return response.choices.message.content.strip()
            
        except Exception as e:
            print(f"   [API Exception] Handshake delay hit: {str(e)}")
            time.sleep(retry_delay)
            retry_delay *= 2
            
    return None
# Box 3: Advanced Children's Reader Book Prompt Selector (SKE Framework Mandate)
def build_standards_based_prompt(grade_code, subject, unit, day_num):
    """
    Formulates precise academic requests forcing the model to structure the lesson 
    around the 3-Phase SKE learning sequence (Injection, Algorithmic Puzzle, Validation Gate).
    """
    g_code = grade_code.lower().strip()
    sub = subject.lower().strip()
    
    worldview_guidance = ""
    if sub == "science":
        worldview_guidance = (
            " Cleanly weave in how this physical system demonstrates orderly structural constants, "
            "laws of physical stability, mathematical symmetry, or elements of purposeful design, "
            "incorporating a child-friendly alignment to historical or scriptural worldview context panels."
        )
    elif sub == "historical_studies":
        worldview_guidance = (
            " Highlight clearly the chronological timeline alignments, purposeful historical pathways, "
            "and the preservation and communication of civilizational truth across geographic routes."
        )

    return (
        f"Generate a strict JSON dataset for an SKE Mastery lesson for a student in {g_code} {sub}, Unit: {unit}, Day {day_num}.\n"
        "You must structure the data following these exact rules:\n"
        "1. 'lesson_title': A clear student-facing lesson title string.\n"
        f"2. 'lesson_body': The Phase 1 Core Injection text. Write direct, highly engaging child textbook reading prose. Describe the concept using visual or concrete analogies (Singapore CPA model).{worldview_guidance}\n"
        "3. 'interactive_assignment': The Phase 2 Algorithmic Puzzle parameters. Write step-by-step interactive game directions explaining how the user manipulates sliders, variables, or digital logic puzzles on the screen to solve the challenge.\n"
        "4. 'daily_assessment': The Phase 3 Automated Validation Gate. Write a set of 3 targeted, clear evaluation questions for the student.\n\n"
        "CRITICAL: Write purely as a direct textbook author for the student. Omit all teacher instructions, time tags, or markdown hashes."
    )
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Validates, parses, and writes the structured SKE JSON blocks natively to disk files.
    """
    print(f"Processing Target: Day {day_num} for {grade_code} ({group.upper()}) - {subject}")
    
    prompt = build_standards_based_prompt(grade_code, subject, unit, day_num)
    raw_response = call_generation_model(prompt)
    
    if not raw_response:
        print(f"❌ Failed to generate content for Day {day_num}. Skipping step.")
        return

    try:
        # Validate that the response is clean, perfectly formatted JSON data
        parsed_data = json.loads(raw_response)
        
        # Inject structural path tracking metadata keys for the frontend router
        parsed_data["grade_prefix"] = grade_code
        parsed_data["layout_group"] = group.upper()
        parsed_data["subject_track"] = subject
        parsed_data["unit_folder"] = unit
        parsed_data["day"] = int(day_num)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(parsed_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written structured SKE Node: Day {day_num}")
        
    except json.JSONDecodeError:
        print(f"❌ Data Error: Server returned an invalid JSON string format block on Day {day_num}.")
    except Exception as e:
        print(f"❌ Disk write failure at {file_path}: {str(e)}")
# Box 5: Self-Building Directory Framework Generator
def run_curriculum_batch_engine():
    """
    Loops through the structural blueprint definitions, automatically builds
    any missing folder layers on disk, and processes missing day modules.
    """
    if not API_KEY:
        print("CRITICAL ERROR: The environment variable 'OPENAI_API_KEY' is empty or missing.")
        return
        
    print("🚀 Initializing Dual-Track Learning Hub Self-Building Loop...")
    pacing_delay = 2.0
    
    for group, grades_list in GROUPS_MAPPING.items():
        for grade in grades_list:
            for subject in SUBJECTS:
                for unit in UNITS:
                    unit_path = os.path.join(DATABASE_ROOT, group, grade, subject, unit)
                    if not os.path.exists(unit_path):
                        os.makedirs(unit_path, exist_ok=True)
# Box 6: Timeline Index Loop Execution Block
                    for day_num in range(1, 181):
                        filename = f"day_{day_num}.json"
                        target_file_path = os.path.join(unit_path, filename)
                        
                        # Idempotency Check: Skip completed files instantly to protect tokens
                        if os.path.exists(target_file_path):
                            continue
                            
                        generate_and_save_day_node(target_file_path, group, grade, subject, unit, day_num)
                        time.sleep(pacing_delay)

if __name__ == "__main__":
    run_curriculum_batch_engine()
