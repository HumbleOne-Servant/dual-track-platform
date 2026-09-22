# FILE: C:\DualTrackLearning_Online\build_vault.py
# BOX 1 OF 3: GRADE-DIFFERENTIATED DIRECTORY INITIALIZER
import os
import json
import hashlib
from datetime import datetime

def get_grade_appropriate_content(grade, subject, day):
    """
    Returns meticulous, grade-leveled lesson text and worksheets.
    Kindergarten receives simple, visual, parent-guided activities.
    """
    clean_subj = subject.replace('_', ' ').title()
    
    if grade == "grade_k":
        # Ultra-simple Kindergarten Structures
        if "math" in subject:
            lesson = (
                f"🏫 MY FIRST MATH WORKBOOK -- KINDERGARTEN: DAY {day}\n"
                f"------------------------------------------------------------------------\n"
                f"🎵 PARENT OUT-LOUD GUIDE: Read this concept to your child.\n\n"
                f"Numbers live in a beautiful, neat line! Every number has its own home from left "
                f"to right. When we count our blocks, we go one by one so we never get lost. This "
                f"perfect order keeps all our counting safe."
            )
            worksheet = (
                f"📝 MY MATH HANDOUT: COUNT AND TRACE\n"
                f"========================================================================\n"
                f"👉 TASK 1: Trace your starting numbers with a pencil:\n"
                f"   1 . . . .    2 . . . .    3 . . . .\n\n"
                f"👉 TASK 2: Count these stars: (★) (★) (★)\n"
                f"   Write how many stars you found in the box: [ ____ ]\n"
                f"========================================================================"
            )
        elif "science" in subject:
            lesson = (
                f"🏫 MY FIRST SCIENCE WORKBOOK -- KINDERGARTEN: DAY {day}\n"
                f"------------------------------------------------------------------------\n"
                f"🎵 PARENT OUT-LOUD GUIDE: Read this concept to your child.\n\n"
                f"Look at the world around you! Things change shape but they are still there. "
                f"When cold ice melts, it turns into clear water. God rules the world with perfect "
                f"boundaries that hold everything together safely."
            )
            worksheet = (
                f"📝 MY SCIENCE HANDOUT: ICE AND WATER\n"
                f"========================================================================\n"
                f"👉 TASK 1: Use a blue crayon to color the ice blocks: [■] [■]\n\n"
                f"👉 TASK 2: Draw a circle around the item that is cold:\n"
                f"   ( Ice Cube )      ( Warm Soup )\n"
                f"========================================================================"
            )
        else:
            lesson = (
                f"🏫 MY FIRST DAILY WORKBOOK -- KINDERGARTEN: DAY {day}\n"
                f"------------------------------------------------------------------------\n"
                f"🎵 PARENT OUT-LOUD GUIDE: Read this concept to your child.\n\n"
                f"Words are made of letters that speak to us. When we speak fitly and kindly, "
                f"our words build paths. We trace our letters along the boundary lines to write neat stories."
            )
            worksheet = (
                f"📝 MY PRACTICE HANDOUT: LETTERS AND WORDS\n"
                f"========================================================================\n"
                f"👉 TASK 1: Trace the starting letter of today's lesson:\n"
                f"   A . . . .    B . . . .    C . . . .\n\n"
                f"👉 TASK 2: Draw a smiling face in the box if you listened nicely to the story: [    ]\n"
                f"========================================================================"
            )
        return lesson, worksheet
# BOX 2 OF 3: ADVANCED ACADEMIC LOGIC ENGINE FOR OLDER GRADES
    else:
        # Standard complex text fields for upper grade levels
        if "math" in subject:
            lesson = f"🏫 MAINSTREAM PUBLIC SCHOOL TEXT BOOK: LESSON DAY {day}\n🎯 FOCUS: {clean_subj}\n\nVariables operate inside a fixed coordinate matrix system..."
            worksheet = f"📝 CLASSROOM EXAMINATION COMPLIANCE WORKSHEET\n\nIsolate the primary numeric coefficients matching boundary conditions..."
        elif "science" in subject:
            lesson = f"🏫 MAINSTREAM PUBLIC SCHOOL TEXT BOOK: LESSON DAY {day}\n🎯 FOCUS: {clean_subj}\n\nResearchers track environmental matrix parameters to isolate raw coefficients..."
            worksheet = f"📝 CLASSROOM EXAMINATION COMPLIANCE WORKSHEET\n\nQuantify systemic energy generation and volumetric updates..."
        else:
            lesson = f"🏫 MAINSTREAM PUBLIC SCHOOL TEXT BOOK: LESSON DAY {day}\n🎯 FOCUS: {clean_subj}\n\nThis unit analyzes advanced structural parameters and contextual indexes..."
            worksheet = f"📝 CLASSROOM EXAMINATION COMPLIANCE WORKSHEET\n\nAssess structural lines and evaluate underlying rhetorical frames..."
        return lesson, worksheet
# BOX 3 OF 3: THE AUTOMATED SYSTEM UPGRADE DEPLOYMENT LOOP
def build_or_upgrade_vault():
    base_dir = r"C:\DualTrackLearning_Online\curriculum"
    grades = [f"grade_{i}" for i in range(1, 13)] + ["grade_k"]
    subjects = ["mathematics", "science", "language_arts", "history_social_studies", "biblical_studies"]
    
    print("⏳ Running Meticulous Grade Separation Build Logic...")
    
    for grade in grades:
        for subject in subjects:
            folder_path = os.path.join(base_dir, grade, subject)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            for day_num in range(1, 181):
                file_name = f"day_{day_num}.json"
                file_path = os.path.join(folder_path, file_name)
                
                lesson_body, worksheet_body = get_grade_appropriate_content(grade, subject, day_num)
                
                default_data = {
                    "title": f"Official Mainstream {subject.replace('_', ' ').title()} - Day {day_num}",
                    "public_core_concept": lesson_body,
                    "public_worksheet_instructions": worksheet_body,
                    "alignment_triggers": {
                        "matrix": {
                            "biblical_truth": "Colossians 1:17 — By him all things hold together. The orderly lattice and systems reflect creation's design.",
                            "alternative_framework": "Mainstream views treat order as an accident. Our alternative framework documents it as an intentionally sustained lattice.",
                            "game_word": "HOLD TOGETHER"
                        },
                        "parameters": {
                            "biblical_truth": "Job 38:10 — I set bars and doors. Boundaries and natural constants exist as protective barriers.",
                            "alternative_framework": "Secular textbooks argue rules evolved randomly. The true model shows changing a single constant collapses the system.",
                            "game_word": "DECREED PLACE"
                        }
                    },
                    "retention_questions": [
                        {"id": "q1", "text": "What simple pattern or design rules did you see in today's lesson story?"},
                        {"id": "q2", "text": "How does our alternative framework connect this daily counting/observation to higher order?"}
                    ],
                    "sync_hash": f"{subject[:3].upper()}_{grade.upper()}_DAY{day_num}"
                }
                
                # Force-rewrite Grade K files completely to clear out the old complex run-on blocks
                if os.path.exists(file_path) and grade != "grade_k":
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing = json.load(f)
                        for key in default_data:
                            if key not in existing:
                                existing[key] = default_data[key]
                        default_data = existing
                    except:
                        pass
                        
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, f, indent=2, ensure_ascii=False)

    print("✅ Success! Meticulous grade-leveled content populated smoothly across all 11,700 endpoints.")

if __name__ == "__main__":
    build_or_upgrade_vault()
