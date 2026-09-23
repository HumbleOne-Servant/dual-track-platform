import os
import shutil
import re

SOURCE_VAULT_DIR = r"C:\DualTrackLearning_Online\vault"
WEB_OUTPUT_DIR = r"C:\DualTrackLearning_Online\assets\curriculum"

def extract_metadata_from_filename(file_name):
    """
    Parses names like 'science_day_1.json' to dynamically extract 
    the active subject, grade level, and specific day number.
    """
    clean_name = file_name.lower()
    
    # Identify subject component keys
    subject = "electives"
    if "math" in clean_name or "arithmetic" in clean_name:
        subject = "math"
    elif "english" in clean_name or "reading" in clean_name or "language" in clean_name:
        subject = "english"
    elif "science" in clean_name or "thermo" in clean_name:
        subject = "science"
    elif "history" in clean_name or "social" in clean_name:
        subject = "social studies"
        
    # Identify grade bracket parameters
    grade_bucket = "k5"
    if any(tag in clean_name for tag in ["grade_9", "grade_10", "grade_11", "grade_12", "g9", "g10", "g11", "g12", "highschool"]):
        grade_bucket = "912"
    elif any(tag in clean_name for tag in ["grade_6", "grade_7", "grade_8", "g6", "g7", "g8", "middleschool"]):
        grade_bucket = "68"
        
    # Extract the day numeric digit using standard expressions
    day_match = re.search(r'day_(\d+)', clean_name)
    day_number = day_match.group(1) if day_match else "1"
    
    return grade_bucket, subject, day_number
def run_intelligent_vault_distribution():
    print("Beginning structural file parsing operations...")
    file_counter = 0
    
    for root, dirs, files in os.walk(SOURCE_VAULT_DIR):
        for current_file in files:
            if current_file.endswith(".json"):
                source_file_path = os.path.join(root, current_file)
                
                # Parse metadata out of the actual file name elements
                grade_bucket, subject_folder, day_num = extract_metadata_from_filename(current_file)
                
                # Build organized nested tree directory branches
                target_directory = os.path.join(WEB_OUTPUT_DIR, grade_bucket, subject_folder)
                os.makedirs(target_directory, exist_ok=True)
                
                # Standardize output naming: 'science_day_1.json' -> 'day_1.json' inside /science/
                standardized_name = f"day_{day_num}.json"
                final_destination_path = os.path.join(target_directory, standardized_name)
                
                try:
                    shutil.copy2(source_file_path, final_destination_path)
                    print(f"Routed: {current_file} -> {grade_bucket}/{subject_folder}/{standardized_name}")
                    file_counter += 1
                except Exception as e:
                    print(f"Error transferring {current_file}: {str(e)}")
                    
    print(f"\nCompleted operation. Successfully processed {file_counter} curriculum assets.")

if __name__ == "__main__":
    run_intelligent_vault_distribution()
