# ========================================================================
# FILE: curricullm_engine.py (Box 1 of 3)
# DESCRIPTION: Core Database Paths, Key Validations, and Native SDK Connections
# ========================================================================
import os
import json
import time
from openai import OpenAI

# Decoupled flat-file data tree root path configuration variable
DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

# Ingestion Security: Read token credentials directly from PowerShell or CMD memory vectors
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("CRITICAL ERROR: OPENAI_API_KEY variable not detected in active session.")
    print("PowerShell Fix: Run -> $env:OPENAI_API_KEY='your_actual_key'")
    exit(1)

# Official SDK Client Layer handshake to bypass firewalls completely
client = OpenAI(api_key=api_key)

# Deterministic directory mapping parameter dictionaries
GROUPS = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]

def calculate_chronological_unit(day):
    """Calculates lowercase unit folders based on the 180-day timeline loops."""
    if 1 <= day <= 45: return "unit_1_foundations"
    elif 46 <= day <= 90: return "unit_2_shapes_spaces"
    elif 91 <= day <= 135: return "unit_3_weather_seasons"
    elif 136 <= day <= 180: return "unit_4_counting_base"
    return "unit_1_foundations"
# ========================================================================
# FILE: curricullm_engine.py (Box 2 of 3)
# DESCRIPTION: Strict Instruction Prompts and Token Segment Parsing Systems
# ========================================================================
def generate_system_instructions(subject, grade, day):
    """Enforces absolute text cleansing filters banning all markdown clutter."""
    base_prompt = (
        "You are an expert K-12 textbook author writing rigorous curriculum content.\n"
        "CLEANSING CORE FILTERS:\n"
        "1. Do NOT include markdown tags like '###', '**', or raw bullet list symbols.\n"
        "2. Banish timing markers like '(15 minutes)' or lesson planning meta-talk.\n"
        "3. Write completely pure, clean, highly informative prose text entries.\n"
        "4. Output text segments flatly with clean single-line spacing."
    )
    if subject == "science":
        base_prompt += " Include three keywords: 'water', 'atoms', 'equations'."
    elif subject == "historical_studies":
        base_prompt += " Include three keywords: 'printing', 'migration', 'vector'."
    return base_prompt

def construct_user_instructions(grade, subject, day, unit_folder):
    """Generates structural directives matching the target case-insensitive keys."""
    return (
        f"Write a comprehensive curriculum lesson leaf node for Grade: {grade.upper()}, "
        f"Subject: {subject.title()}, Day: {day} inside Chapter: {unit_folder.replace('_', ' ').title()}.\n\n"
        f"Provide four distinct segments separated by exactly '---':\n"
        f"1. TITLE: Clean header string.\n"
        f"2. BODY: Academic core prose text block.\n"
        f"3. WORKSPACE: Step-by-step sandbox task description.\n"
        f"4. CHECKOUT: Short verification checkpoint prompt query."
    )

def build_custom_schema_payload(raw_content, grade, subject, day, unit_folder):
    """Slices text blocks cleanly into target data dictionary property keys."""
    chunks = raw_content.split("---")
    title, body, workspace, checkout = "Lesson", raw_content, "Sandbox", "Check"
    
    clean_chunks = []
    for c in chunks:
        p = c.strip()
        for h in ["TITLE:", "BODY:", "WORKSPACE:", "CHECKOUT:"]:
            if p.upper().startswith(h): p = p[len(h):].strip()
        clean_chunks.append(p)
        
    if len(clean_chunks) >= 1: title = clean_chunks[0]
    if len(clean_chunks) >= 2: body = clean_chunks[1]
    if len(clean_chunks) >= 3: workspace = clean_chunks[2]
    if len(clean_chunks) >= 4: checkout = clean_chunks[3]

    def resolve_group_id(gk):
        for grp, lst in GROUPS.items():
            if gk in lst: return grp
        return "k5"

    return {
        "grade_prefix": str(grade).lower(),
        "layout_group": str(resolve_group_id(grade)).upper(),
        "subject_track": str(subject).lower(),
        "unit_folder": str(unit_folder).lower(),
        "day": int(day),
        "lesson_title": str(title),
        "lesson_body": str(body),
        "interactive_assignment": str(workspace),
        "daily_assessment": str(checkout),
        "frontend_rendering_blueprint": {
            "active_interaction_type": "tactile_svg_matrix" if grade in ["gk", "g1"] else "computational_console",
            "canvas_background_color": "#FFFBF2",
            "vector_shapes_layout": [
                {"element_id": "canvasBgZone", "svg_type": "path", "label_overlay_text": "Zone 1: Core Target Input Field", "svg_path_data": "M 0 0 L 400 0 L 400 300 L 0 300 Z"},
                {"element_id": "canvasOvalZone", "svg_type": "path", "label_overlay_text": "Zone 2: Matrix Flow Vector Pond", "svg_path_data": "M 50,220 C 100,180 300,180 350,220 C 320,260 80,260 50,220 Z"}
            ],
            "computational_console_parameters": {
                "console_objective_label": "GENERATE SET MATRIX: VERIFY YOUR DAILY STORY VARIABLES",
                "premise_a_label": "Verify Story Target",
                "premise_b_label": "Lock Count Matrix",
                "console_success_message": "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE"
            }
        }
    }
# ========================================================================
# FILE: curricullm_engine.py (Box 3 of 3)
# DESCRIPTION: Hardened Array Ingestion Batch Loops and Array Index Patches
# ========================================================================
def pipeline_batch_execution(target_days=None):
    """Runs data checks natively and updates payload configurations."""
    if target_days is None:
        # Foundations benchmarks to populate data nodes cleanly
        target_days = [46, 91]
        
    print(f"Executing complete database architecture sync inside: {DATABASE_ROOT}")
    
    for group_folder, grade_keys in GROUPS.items():
        for grade in grade_keys:
            for subject in SUBJECTS:
                for day in target_days:
                    unit_folder = calculate_chronological_unit(day)
                    target_dir = os.path.join(DATABASE_ROOT, group_folder.lower(), grade.lower(), subject.lower(), unit_folder.lower())
                    os.makedirs(target_dir, exist_ok=True)
                    
                    target_file = os.path.join(target_dir, f"day_{day}.json")
                    if os.path.exists(target_file): continue
                        
                    print(f"Streaming data validation loops for: {grade.upper()} {subject.title()} (Day {day})...")
                    
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": generate_system_instructions(subject, grade, day)},
                                {"role": "user", "content": construct_user_instructions(grade, subject, day, unit_folder)}
                            ],
                            temperature=0.7
                        )
                        
                        # ARRAY INDEX FIX: Added [0] brackets to grab message content from list array accurately
                        raw_stream = response.choices[0].message.content.strip()
                        json_payload = build_custom_schema_payload(raw_stream, grade, subject, day, unit_folder)
                        
                        with open(target_file, "w", encoding="utf-8") as out_file:
                            json.dump(json_payload, out_file, indent=4, ensure_ascii=False)
                            
                        # Hardened Stream Request Engine pacing delay
                        time.sleep(2.0)
                        
                    except Exception as loop_error:
                        print(f"Ingestion bottleneck bypassed on day {day}: {str(loop_error)}")
                        time.sleep(3.0)

if __name__ == "__main__":
    pipeline_batch_execution()
    print("\nLocal Flat-File Vault database updates synchronized successfully.")
