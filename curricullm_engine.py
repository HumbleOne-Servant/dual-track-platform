# Box 1: Core System Modules and Structural Definition Blueprints
import os
import json
import time
import urllib.request
import urllib.error

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
# Box 2: Robust OpenAI Network Request Engine (Corrected Flow Control)
def call_generation_model(prompt_text):
    """
    Communicates with gpt-4o-mini via raw network requests to avoid version bugs.
    Includes explicit User-Agent strings and an explicit buffered stream reader.
    """
    url = "https://openai.com"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an expert curriculum developer. You strictly align lesson complexity to national grade-level standards."},
            {"role": "user", "content": prompt_text}
        ],
        "temperature": 0.5
    }
    
    retry_delay = 4
    max_retries = 5
    
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                raw_bytes = response.read()
                raw_data = raw_bytes.decode('utf-8', errors='ignore')
                
                if not raw_data.strip():
                    print("   [Network Alert] Received empty response from OpenAI. Retrying...")
                    time.sleep(5)
                    continue
                    
                res_body = json.loads(raw_data)
                return res_body['choices']['message']['content'].strip()
                
        except urllib.error.HTTPError as e:
            if e.code == 429 or (e.code >= 500 and e.code <= 504):
                print(f"   [API Alert] Code {e.code} hit. Pausing for {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                print(f"   [HTTP Error] Permanent code received: {e.code}")
                try:
                    print(f"   [Server Message] {e.read().decode('utf-8')}")
                except:
                    pass
                return None
        except json.JSONDecodeError:
            # FIXED: Added time delay and loop skip to prevent fall-through failure
            print("   [Data Error] Truncated data stream encountered. Pacing connection and retrying...")
            time.sleep(5)
            continue
        except Exception as e:
            print(f"   [Connection Error] {str(e)}")
            time.sleep(5)
            
    return None
# Box 3: Finer-Grained Grade Level Prompt Selector
def build_standards_based_prompt(grade_code, subject, unit, day_num):
    """
    Inspects individual grade prefixes to apply exact standard criteria,
    ensuring older elementary kids never receive kindergarten visual tasks.
    """
    g_code = grade_code.lower().strip()
    
    if g_code in ["gk", "g1"]:
        return (
            f"Write a standard-aligned lesson for {g_code} {subject}, Unit: {unit}, Day {day_num}.\n"
            "CRITICAL STANDARD: Early elementary level. Keep text blocks brief, highly encouraging, and auditory-focused. "
            "Design the interactive assignment as a basic tactile or visual challenge (such as a color-by-number, drawing basic lines, or counting objects). "
            "Provide one extremely simple single-step check out question."
        )
    elif g_code in ["g2", "g3"]:
        return (
            f"Write a standard-aligned lesson for {g_code} {subject}, Unit: {unit}, Day {day_num}.\n"
            "CRITICAL STANDARD: Mid-elementary level. DO NOT include coloring or kindergarten pond themes. "
            "Write two clear, accessible reading paragraphs. Design the interactive assignment around basic text comprehension, "
            "simple fill-in-the-blanks, or drawing conceptual relationship shapes. Provide a simple two-sentence answer question."
        )
    elif g_code in ["g4", "g5"]:
        return (
            f"Write a standard-aligned lesson for {g_code} {subject}, Unit: {unit}, Day {day_num}.\n"
            "CRITICAL STANDARD: Upper-elementary level. Provide clean, multiple-paragraph informational textbook entries. "
            "Design the interactive assignment around sorting terms, vocabulary matching puzzles, or text-evidence search tasks. "
            "Provide a formal 3-question check out quiz."
        )
    elif g_code in ["g6", "g7", "g8"]:
        return (
            f"Write a standard-aligned lesson for {g_code} {subject}, Unit: {unit}, Day {day_num}.\n"
            "CRITICAL STANDARD: Middle School level. Use rigorous academic concepts, definition trackers, and standard units. "
            "Design the interactive assignment around structured conceptual fill-in-the-blanks, independent research logs, or short summary outlines. "
            "Provide a multi-question critical thinking assessment."
        )
    else: # Grades 9, 10, 11, 12
        return (
            f"Write a standard-aligned lesson for {g_code} {subject}, Unit: {unit}, Day {day_num}.\n"
            "CRITICAL STANDARD: High School level. Provide extensive, high-level academic prose exploring advanced theories, historical sources, or deep formulas. "
            "Design the interactive assignment around high-level analytical essay prompts, data evaluation grids, or logical case studies. "
            "Provide a multi-step comprehensive examination problem."
        )
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Assembles the targeted standard prompt, gathers the AI model response,
    and maps the output keys exactly to the front-end template specifications.
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
        "interactive_assignment": f"Targeted tracking assignment optimized for {grade_code.upper()} active standard requirements.",
        "daily_assessment": f"Age-appropriate milestone checkout question for Day {day_num}."
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson_json_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written: Day {day_num}")
    except Exception as e:
        print(f"❌ Disk write failure at {file_path}: {str(e)}")
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Assembles the targeted standard prompt, gathers the AI model response,
    and maps the output keys exactly to the front-end template specifications.
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
        "interactive_assignment": f"Targeted tracking assignment optimized for {grade_code.upper()} active standard requirements.",
        "daily_assessment": f"Age-appropriate milestone checkout question for Day {day_num}."
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson_json_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written: Day {day_num}")
    except Exception as e:
        print(f"❌ Disk write failure at {file_path}: {str(e)}")
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Assembles the targeted standard prompt, gathers the AI model response,
    and maps the output keys exactly to the front-end template specifications.
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
        "interactive_assignment": f"Targeted tracking assignment optimized for {grade_code.upper()} active standard requirements.",
        "daily_assessment": f"Age-appropriate milestone checkout question for Day {day_num}."
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson_json_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written: Day {day_num}")
    except Exception as e:
        print(f"❌ Disk write failure at {file_path}: {str(e)}")
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Assembles the targeted standard prompt, gathers the AI model response,
    and maps the output keys exactly to the front-end template specifications.
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
        "interactive_assignment": f"Targeted tracking assignment optimized for {grade_code.upper()} active standard requirements.",
        "daily_assessment": f"Age-appropriate milestone checkout question for Day {day_num}."
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(lesson_json_data, f, indent=4, ensure_ascii=False)
        print(f"✅ Successfully written: Day {day_num}")
    except Exception as e:
        print(f"❌ Disk write failure at {file_path}: {str(e)}")
# Box 4: JSON Data Node Constructor
def generate_and_save_day_node(file_path, group, grade_code, subject, unit, day_num):
    """
    Assembles the targeted standard prompt, gathers the AI model response,
    and maps the output keys exactly to the front-end template specifications.
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
        "interactive_assignment": f"Targeted tracking assignment optimized for {grade_code.upper()} active standard requirements.",
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
    
    # Loop Down Level 1: Group Folders defined in mapping blueprint
    for group, grades_list in GROUPS_MAPPING.items():
        
        # Loop Down Level 2: Grade Level Prefixes
        for grade in grades_list:
            
            # Loop Down Level 3: Course Subject Tracks
            for subject in SUBJECTS:
                
                # Loop Down Level 4: Chronological Chapter Units
                for unit in UNITS:
                    # Construct target path location
                    unit_path = os.path.join(DATABASE_ROOT, group, grade, subject, unit)
                    
                    if not os.path.exists(unit_path):
                        os.makedirs(unit_path, exist_ok=True)
# Box 6: Timeline Index Loop Execution Block
                    # Loop Down Level 5: Every Course Timeline Day (1 through 180)
                    for day_num in range(1, 181):
                        filename = f"day_{day_num}.json"
                        target_file_path = os.path.join(unit_path, filename)
                        
                        # Idempotency Check: Skip completed files instantly to protect tokens
                        if os.path.exists(target_file_path):
                            continue
                            
                        # Execute targeted generation and file creation
                        generate_and_save_day_node(target_file_path, group, grade, subject, unit, day_num)
                        time.sleep(pacing_delay)

if __name__ == "__main__":
    run_curriculum_batch_engine()
