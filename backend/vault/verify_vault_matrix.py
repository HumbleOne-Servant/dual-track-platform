import os
import json
def verify_vault_matrix_compliance(vault_root_path):
    print("========================================================================")
    print("?? STARTING SYSTEM MATRIX COMPLIANCE AUDIT FOR DUALTRACKLEARNING.ORG")
    print(f"Target Directory: {vault_root_path}")
    print("========================================================================")
    audit_summary = {"K5": {"passed": 0, "failed": 0}, "68": {"passed": 0, "failed": 0}, "912": {"passed": 0, "failed": 0}}
    if not os.path.exists(vault_root_path):
        print(f"?? Error: Directory vault path '{vault_root_path}' does not exist on this machine.")
        return
    for root, _, files in os.walk(vault_root_path):
        for file in files:
            if file.lower().endswith('.json') and file.lower() != 'package.json':
                file_path = os.path.join(root, file)
                normalized_path = file_path.lower()
                try:
                    with open(file_path, 'r', encoding='utf-8') as stream:
                        payload = json.load(stream)
                    if "k5_elementary" in normalized_path:
                        if "audio_instructions" in payload and "visual_assets" in payload:
                            audit_summary["K5"]["passed"] += 1
                        else:
                            audit_summary["K5"]["failed"] += 1
                    elif "68_middleschool" in normalized_path:
                        if "left_content_panel" in payload and "right_workspace_fields" in payload:
                            audit_summary["68"]["passed"] += 1
                        else:
                            audit_summary["68"]["failed"] += 1
                    elif "912_highschool" in normalized_path:
                        if "grading_rubric" in payload or "essay_prompt" in payload:
                            audit_summary["912"]["passed"] += 1
                        else:
                            audit_summary["912"]["failed"] += 1
                except Exception as error:
                    print(f"? Structural file error reading: {file} -^> {error}")
    print("\n========================================================================")
    print("?? FINAL VAULT COMPLIANCE METRIC REPORT")
    print("========================================================================")
    print(f"?? ELEMENTARY K-5  | Passed: {audit_summary['K5']['passed']} | Failed/Incomplete: {audit_summary['K5']['failed']}")
    print(f"?? MIDDLE SCHOOL 6-8| Passed: {audit_summary['68']['passed']} | Failed/Incomplete: {audit_summary['68']['failed']}")
    print(f"?? HIGH SCHOOL 9-12 | Passed: {audit_summary['912']['passed']} | Failed/Incomplete: {audit_summary['912']['failed']}")
    print("========================================================================")
if __name__ == "__main__":
    VAULT_LOCATION = r"C:\DualTrackLearning_Online\backend\vault"
    verify_vault_matrix_compliance(VAULT_LOCATION)
