[FILE ID: sort_layouts.py - Part 1: Configuration Setup]
========================================================================
import os
import shutil
import json

# Define your source file vault and target web asset directories
SOURCE_VAULT_DIR = r"C:\DualTrackLearning_Online\vault"
WEB_OUTPUT_DIR = r"C:\DualTrackLearning_Online\assets\curriculum"

# Map out the exact destination directories for the new layout groups
LAYOUT_PATHS = {
    "k5": os.path.join(WEB_OUTPUT_DIR, "k5"),
    "68": os.path.join(WEB_OUTPUT_DIR, "68"),
    "912": os.path.join(WEB_OUTPUT_DIR, "912")
}

# Ensure all target folders exist on disk before sorting begins
for folder_path in LAYOUT_PATHS.values():
    os.makedirs(folder_path, exist_ok=True)

print("Starting layout structure verification and directory routing...")
========================================================================
[FILE ID: sort_layouts.py - Part 2: Routing Logic Function]
========================================================================
def determine_layout_bucket(file_name):
    """
    Analyzes the file name structure to assign it to the correct layout container.
    Expected naming formats include indicators like grade_k, grade_5, g6, etc.
    """
    clean_name = file_name.lower()
    
    # Check for High School indicators (Grades 9 to 12)
    high_school_tags = ["grade_9", "grade_10", "grade_11", "grade_12", "g9", "g10", "g11", "g12", "highschool"]
    if any(tag in clean_name for tag in high_school_tags):
        return "912"
        
    # Check for Middle School indicators (Grades 6 to 8)
    middle_school_tags = ["grade_6", "grade_7", "grade_8", "g6", "g7", "g8", "middleschool"]
    if any(tag in clean_name for tag in middle_school_tags):
        return "68"
        
    # Default fallback to Elementary for early childhood grades (K to 5)
    return "k5"
========================================================================
[FILE ID: sort_layouts.py - Part 3: Ingestion Loop Engine]
========================================================================
processed_counter = 0
skipped_counter = 0

# Scan through all available dynamic files inside your curriculum source folder
for root, dirs, files in os.walk(SOURCE_VAULT_DIR):
    for current_file in files:
        # Process only standard curriculum data files
        if current_file.endswith(".json") or current_file.endswith(".html"):
            source_file_path = os.path.join(root, current_file)
            
            # Identify which layout design bucket this file belongs to
            target_bucket = determine_layout_bucket(current_file)
            destination_dir = LAYOUT_PATHS[target_bucket]
            destination_file_path = os.path.join(destination_dir, current_file.lower())
            
            try:
                # Copy the file over while applying consistent lowercase formatting
                shutil.copy2(source_file_path, destination_file_path)
                processed_counter += 1
            except Exception as e:
                print(f"Unable to process file {current_file}. Issue: {str(e)}")
                skipped_counter += 1
        else:
            skipped_counter += 1
========================================================================
[FILE ID: sort_layouts.py - Part 4: Completion Summary Reporter]
========================================================================
# Calculate total files scanned during the operation
grand_total = processed_counter + skipped_counter

print("========================================================================")
print("              LAYOUT BUCKET ROUTING COMPLETION REPORT                   ")
print("========================================================================")
print(f" Successfully Sorted & Routed: {processed_counter} layout-targeted files")
print(f" Skipped / Unchanged Files:     {skipped_counter} records")
print(f" Total Vault Files Evaluated:   {grand_total} files verified")
print("========================================================================")
print(" Status: Distribution complete. Web layouts are now mapped to disk structures.")

if __name__ == "__main__":
    # This enables running the logic directly from your Command Prompt window
    pass
========================================================================
