import os
import shutil
import re

SOURCE_CURRICULUM_DIR = r"C:\DualTrackLearning_Online\curriculum"
BACKEND_VAULT_OUTPUT = r"C:\DualTrackLearning_Online\backend_vault"

# Ensure the target vault output folder is active on disk
os.makedirs(BACKEND_VAULT_OUTPUT, exist_ok=True)

def extract_exact_metadata_from_path(file_path, file_name):
    """
    Scans the folder path to convert labels like grade_k, grade_5, 
    and grade_12 into clean prefixes like gk, g5, and g12.
    """
    clean_name = file_name.lower()
    parts = file_path.lower().replace("\\", "/").split("/")
    
    # 1. Parse the exact individual folder name to determine the short grade prefix
    short_grade = "gk"
    for part in parts:
        if "grade_" in part:
            grade_val = part.split("grade_")[1]
            if grade_val == "k":
                short_grade = "gk"
            else:
                short_grade = f"g{grade_val}"
            break

    # 2. Identify the true day number directly from the file name (e.g., day_8 -> 8)
    day_match = re.search(r'day_(\d+)', clean_name)
    day_number = day_match.group(1) if day_match else "1"
        
    # 3. Identify the subject based on the folder name it lives in
    subject = "electives"
    if "math" in parts or "arithmetic" in parts:
        subject = "math"
    elif "english" in parts or "reading" in parts or "language" in parts:
        subject = "reading"
    elif "science" in parts:
        subject = "science"
    elif "social" in parts or "history" in parts:
        subject = "social_studies"
        
    return short_grade, subject, day_number
def run_exact_grade_naming_inversion():
    print(f"Scanning curriculum paths at: {SOURCE_CURRICULUM_DIR}")
    if not os.path.exists(SOURCE_CURRICULUM_DIR):
        print(f"ERROR: Target directory {SOURCE_CURRICULUM_DIR} does not exist!")
        return

    processed_count = 0
    print("Beginning exact individual grade file conversion...")
    
    for root, dirs, files in os.walk(SOURCE_CURRICULUM_DIR):
        for current_file in files:
            if current_file.lower().endswith(".json"):
                full_source_path = os.path.join(root, current_file)
                
                # Extract customized short grade, subject name, and day digits
                short_grade, subject, day_num = extract_exact_metadata_from_path(full_source_path, current_file)
                
                # Build the precise name format requested: e.g., g5_math_day_7.json
                standardized_name = f"{short_grade}_{subject}_day_{day_num}.json"
                final_destination_path = os.path.join(BACKEND_VAULT_OUTPUT, standardized_name)
                
                try:
                    shutil.copy2(full_source_path, final_destination_path)
                    print(f" SUCCESS ROUTED: {current_file} -> {standardized_name}")
                    processed_count += 1
                except Exception as e:
                    print(f" Error processing item {current_file}: {str(e)}")
                    
    print(f"\nOperation complete. Successfully synchronized {processed_count} files with exact grade labels.")

if __name__ == "__main__":
    run_grade_aware_naming_inversion()
