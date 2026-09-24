import os
import json

# Target folder path matching your dynamic index.html unit routing
TARGET_DIR = r"C:\DualTrackLearning_Online\pure_curriculum_vault\k5\gk\mathematics\unit_1_foundations"

def build_ske_sample_node():
    print("========================================================================")
    print("🚀 GENERATING SKE INFUSED CURRICULUM SAMPLE DATA...")
    print("========================================================================")
    
    # Secure directory creation paths
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # True SKE Structured Parameter Payload Map Layout
    ske_json_payload = {
        "grade_prefix": "gk",
        "layout_group": "K5",
        "subject_track": "mathematics",
        "unit_folder": "unit_1_foundations",
        "day": 1,
        "lesson_title": "Grade GK Mathematics - Day 1 (SKE Mastery Edition)",
        "lesson_body": "Welcome to your first day of mathematics. Today we explore the absolute structural consistency of numbers and layout sets. Look closely at the visual balance structures inside your workspace panel canvas grid.",
        "interactive_assignment": "SKE Algorithmic Puzzle: Drag and place the numeric coefficients cleanly across the canvas field grids to balance the space constants.",
        "daily_assessment": "How many units are required to balance a three-coefficient algebraic block? Please inputs your absolute validation gate integers below."
    }
    
    target_file = os.path.join(TARGET_DIR, "day_1.json")
    
    try:
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(ske_json_payload, f, indent=4, ensure_ascii=False)
        print(f"✅ SUCCESS: Created perfect SKE sample data node file at:\n   {target_file}")
    except Exception as e:
        print(f"❌ Failed to write file: {str(e)}")
    print("========================================================================")

if __name__ == "__main__":
    build_ske_sample_node()
