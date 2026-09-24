import os
import json
import time
from openai import OpenAI

# Target vault root folder path matching your project drive configurations
AUDIT_VAULT_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

LAYOUT_GROUPS = {
    "gk": "k5", "g1": "k5", "g2": "k5", "g3": "k5", "g4": "k5", "g5": "k5",
    "g6": "68", "g7": "68", "g8": "68",
    "g9": "912", "g10": "912", "g11": "912", "g12": "912"
}

# HIDES KEY FROM GITHUB: Pulls the key dynamically from the running Command Prompt memory
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def verify_vault_directory_path(group, grade, subject, unit):
    """Guarantees the target nested structure is physically active on disk."""
    path = os.path.join(AUDIT_VAULT_ROOT, group, grade, subject, unit)
    os.makedirs(path, exist_ok=True)
    return path
def ask_curricullm_to_generate_lesson(grade, subject, unit, day):
    """
    Sends a precise prompt to OpenAI to receive a completely unique,
    highly detailed school curriculum dataset with zero placeholders.
    """
    prompt = f"""
    You are an expert K-12 curriculum designer building a comprehensive school system where learning is the #1 priority.
    Generate a highly engaging, age-appropriate, and pedagogically accurate lesson day for:
    - Grade Level: {grade.upper()}
    - Subject: {subject.title()}
    - Current Unit: {unit.replace('_', ' ').title()}
    - Timeline Track: Day {day} of 180

    CRITICAL RULES:
    1. Do NOT use placeholders, template language, or generic filler sentences. Write the actual full text.
    2. The lesson must build on standard school curriculum criteria. Make it appropriate for this specific grade.
    3. Return your final answer ONLY as a valid JSON object with these exact keys:
       - "lesson_body": A comprehensive, multi-paragraph, engaging textbook-style lesson.
       - "interactive_assignment": A dedicated, hands-on activity or project response task.
       - "daily_assessment": A multi-choice question or short-answer test prompt with clear answer choices.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            timeout=25
        )
        return json.loads(response.choices.message.content)
    except Exception as e:
        print(f"\n❌ SERVER CONNECTION BLOCK TRACKED ON DAY {day}: {str(e)}\n")
        return {
            "lesson_body": "Connection hold identified within backend API server logs.",
            "interactive_assignment": "Verify terminal environment variables configuration.",
            "daily_assessment": "Check active command prompt window log values."
        }
def run_curricullm_production_pipeline():
    print("========================================================================")
    print("             LAUNCHING PROTECTED PRODUCTION CURRICULLM GENERATION       ")
    print("========================================================================")
    file_counter = 0
    
    active_grades = ["gk", "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10", "g11", "g12"] 
    active_subjects = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]
    
    grade_units_map = {
        "k5": ["unit_1_foundations", "unit_2_shapes_spaces", "unit_3_weather_seasons", "unit_4_counting_base"],
        "68": ["unit_1_proportional_ratios", "unit_2_ecosystems_energy", "unit_3_sentence_mechanics", "unit_4_world_geography"],
        "912": ["unit_1_calculus_limits", "unit_2_thermodynamics", "unit_3_rhetorical_analysis", "unit_4_civics_government"]
    }
    
    for grade in active_grades:
        group = LAYOUT_GROUPS[grade]
        target_units = grade_units_map[group]
        
        for subject in active_subjects:
            for unit in target_units:
                
                target_dir = verify_vault_directory_path(group, grade, subject, unit)
                print(f"\n[Ingestion Engine] Active Folder Branch: {group}/{grade}/{subject}/{unit}")
                
                # Test run covering the first 3 days to check key validation instantly
                for day in range(1, 4): 
                    file_name = f"day_{day}.json"
                    file_dest = os.path.join(target_dir, file_name)
                    
                    # Prevent duplicating content if file is already populated
                    if os.path.exists(file_dest):
                        continue
                        
                    llm_data = ask_curricullm_to_generate_lesson(grade, subject, unit, day)
                    
                    final_json_payload = {
                        "grade_prefix": grade,
                        "layout_group": group.upper(),
                        "subject_track": subject,
                        "unit_folder": unit,
                        "day": day,
                        "lesson_title": f"Grade {grade.replace('g','').upper()} {subject.replace('_',' ').title()} - Day {day}",
                        "lesson_body": llm_data.get("lesson_body"),
                        "interactive_assignment": llm_data.get("interactive_assignment"),
                        "daily_assessment": llm_data.get("daily_assessment")
                    }
                    
                    with open(file_dest, 'w', encoding='utf-8') as f:
                        json.dump(final_json_payload, f, indent=2, ensure_ascii=False)
                        
                    file_counter += 1
                    time.sleep(0.2)
                    
    print("\n========================================================================")
    print("             PRODUCTION CURRICULLM DIAGNOSTIC COMPLETE                  ")
    print("========================================================================")
    print(f" Initial layout staging batch generated successfully: {file_counter} files.")
    print("========================================================================")

if __name__ == "__main__":
    run_curricullm_production_pipeline()
