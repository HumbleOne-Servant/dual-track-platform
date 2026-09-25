# ========================================================================
# FILE: inspect_lesson.py (Updated to scaled_curriculum_root)
# ========================================================================
import os
import json

# Corrected Local Disk Storage Root Directory Target
VAULT_DIR = "scaled_curriculum_root"

def look_up_lesson(grade: str, subject: str, day: int):
    # Setup pathing configurations pointing directly inside your active folder root
    path_with_unit = os.path.join(VAULT_DIR, grade, subject, "unit_1_foundations", f"day_{day}.json")
    path_direct = os.path.join(VAULT_DIR, grade, subject, f"day_{day}.json")
    
    if os.path.exists(path_with_unit):
        final_path = path_with_unit
    elif os.path.exists(path_direct):
        final_path = path_direct
    else:
        print(f"❌ Error: No file found at target paths inside [ {VAULT_DIR} ].")
        print(f"   Checked 1: {path_with_unit}")
        print(f"   Checked 2: {path_direct}")
        return
        
    with open(final_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Safely extract internal configurations and nested asset maps
    coaching = data.get("guided_learning_coaching", {})
    titles = coaching.get("american_title_objectives", {})
    history = data.get("historical_connections", {})
    steps_list = data.get("interactive_assignment_sequence", [])
        
    print(f"\n========================================================================")
    print(f"🌐 ENGINE TERMINAL INTERFACE: {data.get('grade_prefix', '').upper()} | {data.get('subject_track', '').upper()} | DAY {data.get('day')}")
    print(f"📋 NATIONAL STANDARD CODE:   {data.get('national_standard_code')}")
    print(f"========================================================================")
    print(f"🔹 LESSON TITLE:       {data.get('lesson_title')}")
    print(f"🔹 AUTOMATED INTERACTIVE SEQUENCE ({len(steps_list)} Steps Found):")
    for step_item in steps_list:
        print(f"   [Step {step_item.get('step', 1)}] Action: {step_item.get('student_action_required', 'N/A')}")
        print(f"            Speech: \"{step_item.get('voice_synthesis_phrase', 'N/A')}\"")
    print(f"🔹 AMERICAN LOCALIZATIONS:")
    print(f"   - Validation Gate:  {titles.get('validation_gate', 'N/A')}")
    print(f"   - Remediation Tree: {titles.get('remediation_tree', 'N/A')}")
    print(f"🔹 PARALLEL TIMELINE:  {history.get('biblical_epoch_match', 'N/A')} ({history.get('calendar_year', 'N/A')})")
    print(f"🔹 HISTORIC AXIOM:     \"{history.get('primary_source_excerpt', 'N/A')}\"")
    print(f"========================================================================")

if __name__ == "__main__":
    print("💡 Enter search parameters (Example: gk mathematics 1):")
    raw_input = input("> ").strip()
    
    # Automatically scrub out extra chevron characters from terminal stream
    cleaned_input = raw_input.replace(">", "").strip()
    
    try:
        g, s, d = cleaned_input.split()
        look_up_lesson(g, s, int(d))
    except ValueError:
        print(f"❌ Input Parsing Error. System intercepted text: '{raw_input}'")
        print("💡 Please type the parameters manually with single spaces: gk mathematics 1")
