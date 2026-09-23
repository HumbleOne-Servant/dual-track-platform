# [File: convert_raw_curriculum.py - Box 1 of 4: Environment & Folder Tree Setup]
import os
import json

def initialize_vault_folders(root_dir):
    """Ensures all specific track subdirectories exist on disk before transformer operations."""
    paths = [
        os.path.join(root_dir, "K5_elementary"),
        os.path.join(root_dir, "68_middleschool"),
        os.path.join(root_dir, "912_highschool")
    ]
    for p in paths:
        os.makedirs(p, exist_ok=True)
    return paths

def transform_raw_lesson(raw_text_data, target_grade_band, vault_root):
    """
    Transforms raw public textbook fields into clean structured JSON assets
    matching the unique grade requirements from your Feature Matrix.
    """
    initialize_vault_folders(vault_root)
    day_number = raw_text_data.get("day", 1)
    subject = raw_text_data.get("subject", "science").lower()
    file_name = f"{subject}_day_{day_number}.json"
# [File: convert_raw_curriculum.py - Box 2 of 4: Grade Band Transformer Engines]
    structured_payload = {
        "grade_level": target_grade_band,
        "day": day_number,
        "subject": subject,
        "title": raw_text_data.get("title", f"Lesson Day {day_number}"),
        "alignment_triggers": raw_text_data.get("alignment_triggers", {})
    }

    # 1. Transform for K-5: Focus on Audio and Simplified Layouts
    if target_grade_band == "K-5":
        structured_payload["audio_instructions"] = f"Welcome! Let's listen to today's short text: {raw_text_data.get('summary', '')}"
        structured_payload["public_core_concept"] = raw_text_data.get("core_text", "")[:300] # Kept short
        structured_payload["visual_assets"] = ["interactive_drawing_board"]
        structured_payload["retention_questions"] = [{"text": "Draw or write what you observed about today's lesson boundary parameters."}]
        target_folder = "K5_elementary"

    # 2. Transform for 6-8: Focus on Split Panel Layouts
    elif target_grade_band == "6-8":
        structured_payload["left_content_panel"] = {
            "title": "Instructional Reading Material",
            "body_text": raw_text_data.get("core_text", "")
        }
        structured_payload["right_workspace_fields"] = {
            "instructions": "Complete the measurement and input paths.",
            "fields_type": "dropdown_and_typing"
        }
        structured_payload["retention_questions"] = [
            {"text": "Explain the calculation variance within the tracking matrix grid."},
            {"text": "How do parameters verify structural laws?"}
        ]
        target_folder = "68_middleschool"
# [File: convert_raw_curriculum.py - Box 3 of 4: High School Matrix Conversion]
    # 3. Transform for 9-12: Focus on Advanced Essays and Rubrics
    else:
        structured_payload["public_core_concept"] = raw_text_data.get("core_text", "")
        structured_payload["essay_prompt"] = f"Formulate a critical thesis evaluation defending: {raw_text_data.get('summary', '')}"
        structured_payload["grading_rubric"] = {
            "analytical_rigor": "40%",
            "biblical_framework_integration": "40%",
            "citation_accuracy": "20%"
        }
        structured_payload["retention_questions"] = [{"text": "Submit your completed essay documentation down below."}]
        target_folder = "912_highschool"

    # Save the transformed payload to its proper vault folder
    final_output_path = os.path.join(vault_root, target_folder, file_name)
    with open(final_output_path, 'w', encoding='utf-8') as stream:
        json.dump(structured_payload, stream, indent=2, ensure_ascii=False)
    print(f"✅ Successfully converted and routed curriculum asset to: {final_output_path}")
# [File: convert_raw_curriculum.py - Box 4 of 4: Core Simulation Test Execution]
if __name__ == "__main__":
    # Simulated Raw Ingestion Content
    mock_raw_scrape = {
        "day": 6,
        "subject": "science",
        "title": "Thermodynamic Matrix Fields & Parameters",
        "core_text": "Every physical system requires tracking limits to trace structural adjustments inside boundary rows.",
        "summary": "Investigating physical system changes, properties, and design variables.",
        "alignment_triggers": {
            "parameters": {
                "biblical_truth": "Job 38:10 — I set bars and doors.",
                "alternative_framework": "Limits protect design values.",
                "game_word": "DECREED PLACE"
            }
        }
    }
    
    VAULT_ROOT = r"C:\DualTrackLearning_Online\backend\vault"
    
    # Run simulation: Convert the same raw data into 3 different target tracks instantly
    transform_raw_lesson(mock_raw_scrape, "K-5", VAULT_ROOT)
    transform_raw_lesson(mock_raw_scrape, "6-8", VAULT_ROOT)
    transform_raw_lesson(mock_raw_scrape, "9-12", VAULT_ROOT)
