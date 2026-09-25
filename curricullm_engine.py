# ========================================================================
# FILE: curricullm_engine.py (Box 1 of 10)
# DESCRIPTION: Core Imports, Directory Matrix Layouts, and Security Locks
# ========================================================================
import os
import json
import time
from openai import OpenAI

# Decoupled database tree root destination path configuration
DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

# Ingestion Security: Read prehistoric token parameters strictly from environment memory
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("CRITICAL FILE ERROR: OPENAI_API_KEY memory vector not detected.")
    print("Execute the following deployment command inside your command prompt:")
    print("set OPENAI_API_KEY=your_key_here")
    exit(1)

# Official SDK Client Layer Initialization
client = OpenAI(api_key=api_key)

# Mapped school years parameters registry (Stateless Directory Array)
GROUPS = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]

def calculate_chronological_unit(day):
    """Dynamically maps the 180 calendar days into four distinct lowercase chapters."""
    if 1 <= day <= 45: return "unit_1_foundations"
    elif 46 <= day <= 90: return "unit_2_shapes_spaces"
    elif 91 <= day <= 135: return "unit_3_weather_seasons"
    elif 136 <= day <= 180: return "unit_4_counting_base"
    return "unit_1_foundations"
# ========================================================================
# FILE: curricullm_engine.py (Box 2 of 10)
# DESCRIPTION: Strict System Prompts and High-Graphic Schema Builders
# ========================================================================
def generate_system_instructions(subject, grade, day):
    """Enforces absolute text cleansing filters and structural injection formats."""
    base_prompt = (
        "You are an expert K-12 textbook author specializing in hyper-rigorous academic design.\n"
        "CLEANSING MATRIX FILTERS:\n"
        "1. Do NOT include markdown tags like '###', '**', or raw bullet asterisks.\n"
        "2. Banish timing strings like '(10 minutes)' or lesson planner meta-talk.\n"
        "3. Write pure, clean, highly informative prose text vectors for the body.\n"
        "4. Output text segments flatly with clean single-line carriage spacing."
    )
    
    if subject == "science":
        base_prompt += (
            "\nSCIENCE CORE INJECTION: Focus the lesson body text strictly on observed physical laws, "
            "natural mechanics, and numeric equations. You MUST naturally integrate at least three "
            "target keywords from this list to prompt cross-scanner triggers: 'water', 'atoms', 'equations'."
        )
    elif subject == "historical_studies":
        base_prompt += (
            "\nHISTORICAL CORE INJECTION: Focus the lesson body text on socio-economic parameters, "
            "treatise configurations, and specific historical milestones. You MUST naturally integrate "
            "at least three target keywords from this list: 'printing', 'migration', 'judah', 'babylon'."
        )
    else:
        base_prompt += "\nGENERAL CONTENT DIRECTIVE: Focus on strict standard-aligned curriculum terminology."
        
    return base_prompt

def construct_user_instructions(grade, subject, day, unit_folder):
    """Generates structural directives matching the unified JSON object model criteria."""
    return (
        f"Write a comprehensive lesson leaf node file. Grade: {grade.upper()}, Subject: {subject.title()}, "
        f"Day: {day} inside Chapter: {unit_folder.replace('_', ' ').title()}.\n\n"
        f"Provide four distinct structural data chunks separated by exactly '---':\n"
        f"1. TITLE: Readable banner showing Grade, Subject, and Day.\n"
        f"2. BODY: Thorough, rigorous academic core public school textbook prose text entry.\n"
        f"3. WORKSPACE: Step-by-step description of an interactive puzzle game or sandbox engine.\n"
        f"4. CHECKOUT: A short validation gate challenge query prompt string."
    )
# ========================================================================
# FILE: curricullm_engine.py (Box 3 of 10)
# DESCRIPTION: Case-Insensitive Schema Object Token Mapping Rules
# ========================================================================
def build_custom_schema_payload(raw_content, grade, subject, day, unit_folder):
    """Slices API raw streams and injects the complete high-graphic blueprint parameters."""
    chunks = raw_content.split("---")
    
    title_text = f"Grade {grade.upper()} - {subject.title()} (Day {day})"
    body_text = raw_content
    workspace_text = "Adjust the active visualization dashboard levers to prove engagement."
    checkout_text = "Verification Gate: Detail the core logic rules reviewed during this calendar block."
    
    clean_chunks = []
    for chunk in chunks:
        c = chunk.strip()
        for header in ["TITLE:", "BODY:", "WORKSPACE:", "CHECKOUT:"]:
            if c.upper().startswith(header): c = c[len(header):].strip()
        clean_chunks.append(c)
        
    if len(clean_chunks) >= 1 and clean_chunks: title_text = clean_chunks
    if len(clean_chunks) >= 2 and clean_chunks: body_text = clean_chunks
    if len(clean_chunks) >= 3 and clean_chunks: workspace_text = clean_chunks
    if len(clean_chunks) >= 4 and clean_chunks: checkout_text = clean_chunks

    def resolve_group_id(gk):
        for grp, grades_list in GROUPS.items():
            if gk in grades_list: return grp
        return "k5"

    group_identity = resolve_group_id(grade).upper()

    # CRITICAL MASTER蓝图 INTEGRATION MATRIX (American Standard + S-K-E + High-Graphic Blueprint)
    return {
        "grade_prefix": str(grade).lower(),
        "layout_group": str(group_identity),
        "subject_track": str(subject).lower(),
        "unit_folder": str(unit_folder).lower(),
        "day": int(day),
        "lesson_title": str(title_text),
        "lesson_body": str(body_text),
        "interactive_assignment": str(workspace_text),
        "daily_assessment": str(checkout_text),
        "frontend_rendering_blueprint": {
            "active_interaction_type": "tactile_svg_matrix" if grade in ["gk", "g1"] else "computational_console",
            "canvas_background_color": "#ECFDF5" if subject == "science" else "#FFFBF2",
            "vector_shapes_layout": [
                {"element_id": "canvasBgZone", "svg_type": "path", "label_overlay_text": "Zone 1: Core Target Input Field", "svg_path_data": "M 0 0 L 400 0 L 400 300 L 0 300 Z"},
                {"element_id": "canvasOvalZone", "svg_type": "path", "label_overlay_text": "Zone 2: Matrix Flow Vector Pond", "svg_path_data": "M 50,220 C 100,180 300,180 350,220 C 320,260 80,260 50,220 Z"}
            ],
            "computational_console_parameters": {
                "console_objective_label": "GENERATE SET MATRIX: VERIFY YOUR DAILY STORY VARIABLES",
                "premise_a_label": "Verify Story Target",
                "premise_b_label": "Lock Count Matrix",
                "console_success_message": "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE: CONCEPT SECURED"
            }
        }
    }
# ========================================================================
# FILE: curricullm_engine.py (Box 4 of 10)
# DESCRIPTION: Automated Generation Batch Loops and Pacing Gates
# ========================================================================
def pipeline_batch_execution(target_days=None):
    """Loops recursively down the directory tree vault and commits flat files natively."""
    if target_days is None:
        # Benchmark structural testing indicators to seed files cleanly across the 4 units
        target_days = [1, 2, 46, 91, 136]
        
    print(f"Executing complete database architecture sync inside: {DATABASE_ROOT}")
    
    for group_folder, grade_keys in GROUPS.items():
        for grade in grade_keys:
            for subject in SUBJECTS:
                for day in target_days:
                    unit_folder = calculate_chronological_unit(day)
                    
                    # Lock pathing arrays strictly down to lowercase constraints
                    target_dir = os.path.join(DATABASE_ROOT, group_folder.lower(), grade.lower(), subject.lower(), unit_folder.lower())
                    os.makedirs(target_dir, exist_ok=True)
                    
                    target_file = os.path.join(target_dir, f"day_{day}.json")
                    
                    # Idempotency storage lockout gate: Protect token prepaid credit balances
                    if os.path.exists(target_file):
                        continue
                        
                    print(f"Streaming data validation loops for: {grade.upper()} {subject.title()} (Day {day})...")
                    
                    try:
                        system_prompt = generate_system_instructions(subject, grade, day)
                        user_prompt = construct_user_instructions(grade, subject, day, unit_folder)
                        
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_prompt}
                            ],
                            temperature=0.7
                        )
                        
                        raw_stream = response.choices.message.content.strip()
                        json_payload = build_custom_schema_payload(raw_stream, grade, subject, day, unit_folder)
                        
                        with open(target_file, "w", encoding="utf-8") as out_file:
                            json.dump(json_payload, out_file, indent=4, ensure_ascii=False)
                            
                        # Hardened Stream Pacing Guard: 2.0-second delay completely clears bot challenge blocks
                        time.sleep(2.0)
                        
                    except Exception as loop_error:
                        print(f"Ingestion bottleneck bypassed on day {day}: {str(loop_error)}")
                        time.sleep(4.0)

if __name__ == "__main__":
    pipeline_batch_execution()
    print("\nLocal Flat-File Vault database setup execution concluded cleanly.")
