import os
import shutil
import re

SOURCE_CURRICULUM_DIR = r"C:\DualTrackLearning_Online\curriculum"
BACKEND_VAULT_OUTPUT = r"C:\DualTrackLearning_Online\backend_vault"

def parse_deep_curriculum_path(file_path):
    """
    Analyzes the complete folder structure to extract the correct group bucket,
    the exact grade code, the mapped subject, and the day tracking digit.
    """
    normalized_path = file_path.lower().replace("\\", "/")
    parts = normalized_path.split("/")
    
    exact_grade = "gk"
    subject = "science"
    day_number = "1"
    layout_bucket = "k5"
    
    # 1. Parse the folder level name for the exact grade layer code
    for part in parts:
        if "grade_" in part:
            raw_grade = part.replace("grade_", "").strip()
            if raw_grade == "k":
                exact_grade = "gk"
                layout_bucket = "k5"
            else:
                exact_grade = f"g{raw_grade}"
                try:
                    num_grade = int(raw_grade)
                    if 6 <= num_grade <= 8:
                        layout_bucket = "68"
                    elif 9 <= num_grade <= 12:
                        layout_bucket = "912"
                    else:
                        layout_bucket = "k5"
                except ValueError:
                    layout_bucket = "k5"
            break

    # 2. Parse the subject folder level name matching your system options
    subject_map = {
        "biblical_studies": "biblical",
        "historical_social_studies": "social_studies",
        "laguage_arts": "reading",
        "language_arts": "reading",
        "mathematics": "math",
        "science": "science"
    }
    
    for part in parts:
        if part in subject_map:
            subject = subject_map[part]
            break

    # 3. Parse the day folder level tracking digit
    for part in parts:
        if "day_" in part and part.replace("day_", "").isdigit():
            day_number = part.replace("day_", "").strip()
            break
            
    return layout_bucket, exact_grade, subject, day_number
def run_nested_layout_distribution():
    print(f"Scanning deep curriculum folder structure at: {SOURCE_CURRICULUM_DIR}")
    if not os.path.exists(SOURCE_CURRICULUM_DIR):
        print(f"ERROR: Target directory {SOURCE_CURRICULUM_DIR} does not exist!")
        return

    processed_count = 0
    print("Beginning structural file parsing, unique renaming, and bucket routing...")
    
    for root, dirs, files in os.walk(SOURCE_CURRICULUM_DIR):
        for current_file in files:
            if current_file.lower().endswith(".json"):
                full_source_path = os.path.join(root, current_file)
                
                # Extract metadata features directly from the folder paths
                layout_bucket, exact_grade, subject, day_num = parse_deep_curriculum_path(full_source_path)
                
                # Group files cleanly into k5, 68, and 912 subfolders
                target_folder_path = os.path.join(BACKEND_VAULT_OUTPUT, layout_bucket)
                os.makedirs(target_folder_path, exist_ok=True)
                
                # FORCE PRECISE UNIQUE FILE NAME: e.g., g5_math_day_7.json or gk_science_day_1.json
                standardized_name = f"{exact_grade}_{subject}_day_{day_num}.json"
                final_destination_path = os.path.join(target_folder_path, standardized_name)
                
                try:
                    shutil.copy2(full_source_path, final_destination_path)
                    processed_count += 1
                    
                    if processed_count % 1000 == 0:
                        print(f" -> Successfully processed and unique-named {processed_count} files...")
                except Exception as e:
                    print(f" Error transferring file {current_file}: {str(e)}")
                    
    print("\n========================================================================")
    print("           UNIQUE VAULT ROUTING COMPLETION REPORT                       ")
    print("========================================================================")
    print(f" Successfully Organized & Copied: {processed_count} unique-named files")
    print(f" Target Output Folders:           {BACKEND_VAULT_OUTPUT}\\(k5, 68, 912)")
    print("========================================================================")

if __name__ == "__main__":
    run_nested_layout_distribution()
