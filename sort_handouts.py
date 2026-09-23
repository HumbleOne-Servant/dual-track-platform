# FILE: C:\DualTrackLearning_Online\sort_handouts.py
# BOX 4 OF 4: SEQUENTIAL WORKSHEET FILE RENAMING ENGINE
import os

def rename_subject_handout_batch(grade="grade_k", subject="mathematics"):
    target_dir = f"C:\\DualTrackLearning_Online\\curriculum\\{grade}\\{subject}"
    
    if not os.path.exists(target_dir):
        print(f"❌ Folder track path not found: {target_dir}")
        return
        
    print(f"⏳ Scanning raw downloaded images inside: [{grade.upper()} -> {subject.upper()}]")
    
    # Filter out your existing platform lesson .json files so we only handle raw images
    all_files = [f for f in os.listdir(target_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    # Sort them to keep them in the order they were downloaded or named
    all_files.sort()
    
    if not all_files:
        print("💡 No worksheet images found in this folder. Drop your downloads here first!")
        return
        
    for index, file_name in enumerate(all_files, start=1):
        old_path = os.path.join(target_dir, file_name)
        new_path = os.path.join(target_dir, f"day_{index}.png")
        
        # Prevent collision if the file is already named correctly
        if old_path != new_path:
            os.rename(old_path, new_path)
            
    print(f"✅ Success! Sorted and indexed {len(all_files)} worksheet images to day_X.png tracks.")

if __name__ == "__main__":
    # Change these two labels depending on what folder batch you are dropping downloads into!
    rename_subject_handout_batch(grade="grade_k", subject="mathematics")
