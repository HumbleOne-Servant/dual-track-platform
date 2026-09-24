import os
import json
import time
from openai import OpenAI

# Target database path matching your project specifications
AUDIT_VAULT_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

LAYOUT_GROUPS = {
    "gk": "k5", "g1": "k5", "g2": "k5", "g3": "k5", "g4": "k5", "g5": "k5",
    "g6": "68", "g7": "68", "g8": "68",
    "g9": "912", "g10": "912", "g11": "912", "g12": "912"
}

# ----------------------------------------------------------------------
# SECURE DIRECT OPENAI API KEY PASSTHROUGH
# Replace YOUR_OPENAI_API_KEY_HERE with your secret key starting with sk-
# ----------------------------------------------------------------------
client = OpenAI(api_key="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")

def verify_vault_directory_path(group, grade, subject, unit):
    """Guarantees the target nested structure is physically active on disk."""
    path = os.path.join(AUDIT_VAULT_ROOT, group, grade, subject, unit)
    os.makedirs(path, exist_ok=True)
    return path
def ask_curricullm_to_generate_lesson(grade, subject, unit, day):
    """
    Sends a precise prompt to OpenAI and prints out the exact network error 
    on the screen if the server rejects the request.
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
        # Pinging the intelligent OpenAI model layer for data structure parameters
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
            timeout=20
        )
        return json.loads(response.choices.message.content)
    except Exception as e:
        # CRITICAL UPDATE: Stop hiding errors and print the exact reason to the screen
        print(f"\n❌ SERVER CONNECTION ERROR ON DAY {day}: {str(e)}\n")
        return {
            "lesson_body": "CRITICAL CAPTURE ERROR: The AI server rejected the connection request. Check the error log printed above in your terminal.",
            "interactive_assignment": "Verify API key status and trial credit balance.",
            "daily_assessment": "Error code logged inside command prompt window."
        }
def run_curricullm_distribution_engine():
    print("Initializing live OpenAI CurricuLLM ingestion pipeline...")
    file_counter = 0
    
    # Target a test run batch first (Grade K Mathematics) to check the error output instantly
    active_grades = ["gk"] 
    active_subjects = ["mathematics"]
    active_units = ["unit_4_counting_base"]
    
    # Make sure old bad files are wiped from the test space first
    for grade in active_grades:
        group = LAYOUT_GROUPS[grade]
        for subject in active_subjects:
            for unit in active_units:
                target_dir = verify_vault_directory_path(group, grade, subject, unit)
                for f in os.listdir(target_dir):
                    try: os.remove(os.path.join(target_dir, f))
                    except: pass
                
                # Loop through your targeted days sequentially (Testing first 3 days live)
                for day in range(1, 4): 
                    print(f" -> Contacting OpenAI to generate custom textbook assets for {grade.upper()} | {subject.title()} | Day {day}...")
                    
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
                    
                    file_name = f"day_{day}.json"
                    with open(os.path.join(target_dir, file_name), 'w', encoding='utf-8') as f:
                        json.dump(final_json_payload, f, indent=2, ensure_ascii=False)
                        
                    file_counter += 1
                    time.sleep(0.5)
                    
    print("\n========================================================================")
    print("             CURRICULLM LIVE DIAGNOSTIC COMPLETE                        ")
    print("========================================================================")
    print(f" Staged Test Operation Complete. Review any red text error flags above.")
    print("========================================================================")

if __name__ == "__main__":
    run_curricullm_distribution_engine()
