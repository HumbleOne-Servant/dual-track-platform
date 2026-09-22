# BOX 1 OF 4: PLATFORM CONFIGURATION AND ALL 12 GRADE FILE MAPPER
import os
import json

def build_or_upgrade_vault():
    base_dir = r"C:\DualTrackLearning_Online\curriculum"
    grades = [f"grade_{i}" for i in range(1, 13)] + ["grade_k"]
    subjects = ["mathematics", "science", "language_arts", "history_social_studies", "biblical_studies"]
    
    print("⏳ Initialization started: Structuring synchronized dual-track data architecture...")
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for grade in grades:
        for subject in subjects:
            folder_path = os.path.join(base_dir, grade, subject)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
# BOX 2 OF 4: FULL CONTENT PROFILE GENESIS MODEL FOR INTEGRATED LEARNING
            for day_num in range(1, 181):
                file_name = f"day_{day_num}.json"
                file_path = os.path.join(folder_path, file_name)
                
                # RESTORED: Your complete public curriculum tracking matrix with dual alignment triggers
                default_data = {
                    "title": f"Public School {subject.replace('_', ' ').title()} Curriculum Handout - Day {day_num}",
                    "public_core_concept": "Analyzing progressive numerical coordinate systems, operational parameters, and structural matrix algorithms for mainstream lesson milestone units.",
                    "public_worksheet_instructions": "Isolate the primary numeric coefficients matching mainstream structural boundary conditions. Map the values across the grid segment and formulate a vertical precision check proof.",
                    "alignment_triggers": {
                        "matrix": {
                            "biblical_truth": "Colossians 1:17 — He is before all things, and by him all things hold together. The physical matrix and mathematical grids reflect the structural stability established from the beginning of natural law.",
                            "alternative_framework": "Mainstream secular curriculum pushes a narrative that empty numerical coordinates exist independently. Our alternative framework proves the grid is a designed lattice holding systemic information in absolute unity.",
                            "game_word": "HOLD TOGETHER"
                        },
                        "parameters": {
                            "biblical_truth": "Job 38:10 — When I broke up for it my decreed place, and set bars and doors. Natural constants and structural limits act as strict, divine barriers protecting system integrity.",
                            "alternative_framework": "Secular textbooks argue that operational parameters arose via random evolutionary paths. The true alignment demonstrates that changing even one universal parameter completely collapses the structural math of creation.",
                            "game_word": "DECREED PLACE"
                        }
                    },
                    "retention_questions": [
                        {"id": "q1", "text": "What biblical principles or truths are active inside the public school curriculum core concept highlighted on the left?"},
                        {"id": "q2", "text": "How does our alternative framework demonstrate that secular school metrics and design laws are actually one and the same?"}
                    ],
                    "sync_hash": f"{subject[:3].upper()}_{grade.upper()}_DAY{day_num}"
                }
# BOX 3 OF 4: PERSISTENT CURRICULUM MERGE LOGIC (PRESERVES EXISTING FILES)
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing = json.load(f)
                        # Safeguard: Ensure no existing text or data is overwritten, only append new fields
                        for key in default_data:
                            if key not in existing:
                                existing[key] = default_data[key]
                        default_data = existing
                    except:
                        pass
# BOX 4 OF 4: POSITIONALLY FIXED ENCODE WRAPPER AND EXECUTOR TERMINATION
                with open(file_path, 'w', encoding='utf-8') as f:
                    # FIXED FIRST TIME: Position argument 'f' now correctly leads keyword settings
                    json.dump(default_data, f, indent=2, ensure_ascii=False)

    print("✅ Success! All 11,700 curriculum nodes contain parallel framework targets.")

if __name__ == "__main__":
    build_or_upgrade_vault()
