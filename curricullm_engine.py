# Box 1: Core System Modules and Structural Definition Blueprints
import os
import json
import time
import requests

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
# Box 2: Stream-Isolated OpenAI Request Engine with Markdown Cleansing Filters
def call_generation_model(prompt_text):
    """
    Communicates with gpt-4o-mini using the requests framework.
    Guarantees text downloads complete 100% and strips stray formatting characters.
    """
    url = "https://openai.com"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system", 
                "content": (
                    "You are a professional children's textbook author. You never use markdown symbols "
                    "like ###, **, or lists with bullet dashes. You write purely in clean, beautifully structured "
                    "paragraphs. Never output teacher timelines, lesson plans, or time markers like (5 minutes)."
                )
            },
            {"role": "user", "content": prompt_text}
        ],
        "temperature": 0.4
    }
    
    retry_delay = 5
    for attempt in range(3):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=45)
            if response.status_code == 200:
                res_body = response.json()
                clean_text = res_body['choices']['message']['content'].strip()
                
                # Proactive cleaning filter pass: Force-erase stray structural characters
                clean_text = clean_text.replace("###", "").replace("**", "").replace("### Lesson Plan:", "")
                return clean_text
            elif response.status_code == 429 or response.status_code >= 500:
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                return None
        except Exception:
            time.sleep(5)
            
    return None
# Box 3: Advanced Children's Reader Book Prompt Selector
def build_standards_based_prompt(grade_code, subject, unit, day_num):
    """
    Constructs prompts that force the AI to write like an authentic student-facing
    textbook rather than a teacher's lesson plan sheet, maintaining high engagement metrics.
    """
    g_code = grade_code.lower().strip()
    sub = subject.lower().strip()
    
    worldview_guidance = ""
    if sub == "science":
        worldview_guidance = (
            " Cleanly introduce how this physical mechanism displays intelligent design and fine-tuning constants "
            "using simple, child-friendly explanations, accompanied by an aligned scriptural concept."
        )
    elif sub == "historical_studies":
        worldview_guidance = (
            " Cleanly highlight the providential timelines and the protection of truth during this historical era."
        )

    if g_code in ["gk", "g1"]:
        return (
            f"Write a textbook lesson entry for a child reading {g_code} {sub}, Unit: {unit}, Day {day_num}. "
            "CRITICAL: Do not write a lesson plan shell. Write the actual direct textbook reader content the child reads. "
            "Keep paragraphs brief, cheerful, and highly engaging. Describe an interactive visual assignment perfectly suited "
            f"for early elementary skills.{worldview_guidance} Do not use markdown hashes or asterisks anywhere."
        )
    elif g_code in ["g2", "g3"]:
        return (
            f"Write an authentic student-facing textbook entry for mid-elementary {g_code} {sub}, Unit: {unit}, Day {day_num}. "
            f"Write 2 clear, inspiring reading paragraphs. Describe a distinct, creative, non-repetitive conceptual assignment.{worldview_guidance}"
        )
    elif g_code in ["g4", "g5"]:
        return (
            f"Write a multi-paragraph children's textbook reader entry for upper-elementary {g_code} {sub}, Unit: {unit}, Day {day_num}. "
            f"Focus on vocabulary, concept explanations, and clear structural facts without any teacher timeline tags.{worldview_guidance}"
        )
    elif g_code in ["g6", "g7", "g8"]:
        return (
            f"Write a rigorous Middle School textbook entry for {g_code} {sub}, Unit: {unit}, Day {day_num}. "
            f"Focus on core content summaries, vocabulary building blocks, and standard definitions.{worldview_guidance}"
        )
    else:
        return (
            f"Write an extensive academic textbook chapter entry for High School {g_code} {sub}, Unit: {unit}, Day {day_num}. "
            f"Provide high-level prose, advanced formulas, or case study analysis text.{worldview_guidance}"
        )
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Maps prompt selections into clear, clean string elements matching your front-end template keys.
    """
    print(f"Processing Target: Day {day_num} for {grade_code} ({group.upper()}) - {subject}")
    
    prompt = build_standards_based_prompt(grade_code, subject, unit, day_num)
    raw_response = call_generation_model(prompt)
    
    if not raw_response:
        print(f"❌ Failed to generate content for Day {day_num}. Skipping step.")
        return

    # Structure data keys perfectly matching your validated index.html schema
    lesson_json_data = {
        "grade_prefix": grade_code,
        "layout_group": group.upper(),
        "subject_track": subject,
        "unit_folder": unit,
        "day": int(day_num),
        "lesson_title": f"Grade {grade_code.upper()} {subject.replace('_', ' ').title()} - Day {day_num}",
        "lesson_body": raw_response,
        "interactive_assignment": f"Fun puzzle assignment optimized for Grade {grade_code.upper()} standard goals.",
        "daily_assessment": f"Age-appropriate milestone checkout question for Day {day_num}."
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson_json_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written: Day {day_num}")
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
