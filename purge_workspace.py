import os
import shutil

# Target directory channels scheduled for absolute deletion
FOLDERS_TO_REMOVE = [
    r"C:\DualTrackLearning_Online\pure_curriculum_vault",
    r"C:\DualTrackLearning_Online\backend_vault",
    r"C:\DualTrackLearning_Online\backend",
    r"C:\DualTrackLearning_Online\curriculum"
]

FILES_TO_REMOVE = [
    r"C:\DualTrackLearning_Online\curricullm_engine.py",
    r"C:\DualTrackLearning_Online\sort_handouts.py",
    r"C:\DualTrackLearning_Online\build_vault.py",
    r"C:\DualTrackLearning_Online\verify_vault_matrix.py",
    r"C:\DualTrackLearning_Online\server.py"
]

def purge_legacy_clutter():
    print("========================================================================")
    print("🧹 EXECUTING TOTAL PLATFORM WORKSPACE PURGE... LOCKING TARGETS")
    print("========================================================================")
    
    # 1. Clean out the historical folder structures completely
    for folder in FOLDERS_TO_REMOVE:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f" 🔥 Successfully deleted legacy directory: {folder}")
            except Exception as e:
                print(f" ❌ Failed to strip directory {folder}: {str(e)}")
                
    # 2. Strip out all legacy background loop scripts
    for file_path in FILES_TO_REMOVE:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f" 🗑️ Successfully removed legacy script: {file_path}")
            except Exception as e:
                print(f" ❌ Failed to erase file {file_path}: {str(e)}")
                
    print("========================================================================")
    print("✅ SUCCESS: Workspace completely scrubbed. Reverting to pure frontend mode.")
    print("========================================================================")

if __name__ == "__main__":
    purge_legacy_clutter()
