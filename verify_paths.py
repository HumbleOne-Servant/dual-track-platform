import os

TARGET_VAULT_PATH = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

def synchronize_path_casing_to_lowercase():
    print("========================================================================")
    print("                 CASE SYNCING & ENFORCEMENT ENGINE                      ")
    print("========================================================================")
    
    if not os.path.exists(TARGET_VAULT_PATH):
        print(f"ERROR: Destination folder '{TARGET_VAULT_PATH}' does not exist.")
        return

    renamed_folders_count = 0
    
    # Walk the directory tree from the bottom up to safely rename folders
    for root, dirs, files in os.walk(TARGET_VAULT_PATH, topdown=False):
        for dir_name in dirs:
            # Check if the folder name contains any uppercase letters
            if any(char.isupper() for char in dir_name):
                old_dir_path = os.path.join(root, dir_name)
                lowercase_dir_name = dir_name.lower()
                new_dir_path = os.path.join(root, lowercase_dir_name)
                
                try:
                    os.rename(old_dir_path, new_dir_path)
                    print(f" -> Synchronized Casing: {dir_name} -> {lowercase_dir_name}")
                    renamed_folders_count += 1
                except Exception as e:
                    print(f" Skipped directory {dir_name}: {str(e)}")

    print("========================================================================")
    print(f" SUCCESS: Case syncing complete. Fixed {renamed_folders_count} folder path tags.")
    print("========================================================================")
if __name__ == "__main__":
    synchronize_path_casing_to_lowercase()
