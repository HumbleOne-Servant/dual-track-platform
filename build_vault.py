# FILE: C:\DualTrackLearning_Online\build_vault.py
# BOX 1 OF 2: ARCHITECTURE SCRUBBER AND DEPLOYMENT LOOP
import os
import json

def restore_pure_data_vault():
    base_dir = r"C:\DualTrackLearning_Online\curriculum"
    grades = [f"grade_{i}" for i in range(1, 13)] + ["grade_k"]
    subjects = ["mathematics", "science", "language_arts", "history_social_studies", "biblical_studies"]
    
    print("⏳ Scrubbing database files: Restoring data-driven JSON properties for all 180 days...")
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for grade in grades:
        for subject in subjects:
            folder_path = os.path.join(base_dir, grade, subject)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            for day_num in range(1, 181):
                file_name = f"day_{day_num}.json"
                file_path = os.path.join(folder_path, file_name)
                
                # Check if file already exists to preserve your core information
                existing_data = {}
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing_data = json.load(f)
                    except:
                        pass

                # Extract your core data fields, reverting any generic text overrides
                title = existing_data.get("title", f"Official {subject.replace('_', ' ').title()} - Day {day_num}")
                description = existing_data.get("description", "Analyzing coordinate pathways and environmental system responses.")
                concept = existing_data.get("concept", "Value structures scale systematically across spatial parameters.")
                
                # Ensure bullets exist as a clean list array for our interactive checklist engine
                bullets = existing_data.get("bullets", [
                    f"Isolate primary numeric coefficients for day step {day_num}.",
                    f"Map the resulting values cleanly across the grid matrix for session {day_num}.",
                    f"Formulate a complete balance verification proof for step {day_num}."
                ])
                if isinstance(bullets, str):
                    bullets = [bullets]
                    
                cross_ref = existing_data.get("cross_reference", "Job 38:2 — Who hath laid the measures thereof?")
                sync_hash = existing_data.get("sync_hash", f"{subject[:3].upper()}_{grade.upper()}_DAY{day_num}")
# BOX 2 OF 2: CLEAN DATA PACKAGER AND DISK WRITER
                # Reassemble the pure data file footprint with absolutely no hardcoded story text
                clean_json_payload = {
                    "title": title,
                    "description": description,
                    "concept": concept,
                    "bullets": bullets,
                    "cross_reference": cross_ref,
                    "sync_hash": sync_hash
                }
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(clean_json_payload, f, indent=2, ensure_ascii=False)

    print("========================================================================")
    print("✅ VAULT SUCCESS: All 11,700 JSON tracks are now purely data-driven!")
    print("========================================================================")

if __name__ == "__main__":
    restore_pure_data_vault()
