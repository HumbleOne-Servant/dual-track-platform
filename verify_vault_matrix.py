# [File: verify_vault_matrix.py - Box 1 of 3: System Audit Initialization]
import os
import json

def verify_vault_matrix_compliance(vault_root_path):
    """
    Scans the local storage vault and verifies that files contain the mandatory
    data models required to populate the K-5, 6-8, and 9-12 interfaces.
    """
    print(f"========================================================================")
    print(f"🚀 STARTING SYSTEM MATRIX COMPLIANCE AUDIT FOR DUALTRACKLEARNING.ORG")
    print(f"Target Directory: {vault_root_path}")
    print(f"========================================================================")

    audit_summary = {"K5": {"passed": 0, "failed": 0}, "68": {"passed": 0, "failed": 0}, "912": {"passed": 0, "failed": 0}}
    
    if not os.path.exists(vault_root_path):
        print(f"🚨 Error: Directory vault path '{vault_root_path}' does not exist on this machine.")
        return

    for root, _, files in os.walk(vault_root_path):
        for file in files:
            if file.lower().endswith('.json'):
                file_path = os.path.join(root, file)
                normalized_path = file_path.lower()
# [File: verify_vault_matrix.py - Box 2 of 3: Matrix Validation Rules Engine]
                try:
                    with open(file_path, 'r', encoding='utf-8') as stream:
                        payload = json.load(stream)
                    
                    # 1. Evaluate Elementary (K-5) Requirements
                    if "k5_elementary" in normalized_path:
                        if "audio_instructions" in payload and "visual_assets" in payload:
                            audit_summary["K5"]["passed"] += 1
                        else:
                            audit_summary["K5"]["failed"] += 1
                            print(f"⚠️ K-5 Matrix Violation in: {file} (Missing audio or visual nodes)")
                            
                    # 2. Evaluate Middle School (6-8) Requirements
                    elif "68_middleschool" in normalized_path:
                        if "left_content_panel" in payload and "right_workspace_fields" in payload:
                            audit_summary["68"]["passed"] += 1
                        else:
                            audit_summary["68"]["failed"] += 1
                            print(f"⚠️ 6-8 Matrix Violation in: {file} (Missing split-screen content matrices)")
                            
                    # 3. Evaluate High School (9-12) Requirements
                    elif "912_highschool" in normalized_path:
                        if "grading_rubric" in payload or "essay_prompt" in payload:
                            audit_summary["912"]["passed"] += 1
                        else:
                            audit_summary["912"]["failed"] += 1
                            print(f"⚠️ 9-12 Matrix Violation in: {file} (Missing academic evaluation metrics)")
# [File: verify_vault_matrix.py - Box 3 of 3: Audit Summary Reporting]
                except Exception as error:
                    print(f"❌ Structural file error reading: {file} -> {error}")

    print("\n========================================================================")
    print("📋 FINAL VAULT COMPLIANCE METRIC REPORT")
    print("========================================================================")
    print(f"🧒 ELEMENTARY K-5  | Passed: {audit_summary['K5']['passed']} | Failed/Incomplete: {audit_summary['K5']['failed']}")
    print(f"🧑 MIDDLE SCHOOL 6-8| Passed: {audit_summary['68']['passed']} | Failed/Incomplete: {audit_summary['68']['failed']}")
    print(f"🎓 HIGH SCHOOL 9-12 | Passed: {audit_summary['912']['passed']} | Failed/Incomplete: {audit_summary['912']['failed']}")
    print("========================================================================")

if __name__ == "__main__":
    # Point this variable directly to your central backend directory location
    VAULT_LOCATION = r"C:\DualTrackLearning_Online\backend\vault"
    verify_vault_matrix_compliance(VAULT_LOCATION)
