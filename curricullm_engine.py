import os
import json
import time
import re
from openai import OpenAI

DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("CRITICAL ERROR: OPENAI_API_KEY variable not detected in active session.")
    print("PowerShell Fix: Run -> $env:OPENAI_API_KEY='your_actual_key'")
    exit(1)

client = OpenAI(api_key=api_key)

GROUPS = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]

def calculate_chronological_unit(day):
    if 1 <= day <= 45: return "unit_1_foundations"
    elif 46 <= day <= 90: return "unit_2_shapes_spaces"
    elif 91 <= day <= 135: return "unit_3_weather_seasons"
    elif 136 <= day <= 180: return "unit_4_counting_base"
    return "unit_1_foundations"
def generate_system_instructions(subject, grade, day):
    base_prompt = (
        "You are an expert K-12 textbook author writing highly rigorous curriculum content.\n"
        "CLEANSING CORE FILTERS:\n"
        "1. Do NOT include markdown tags like '###', '**', or raw bullet list symbols.\n"
        "2. Banish timing markers like '(15 minutes)' or lesson planning meta-talk.\n"
        "3. Write completely pure, clean, highly informative prose text entries.\n"
        "4. Output text segments flatly with clean single-line spacing.\n\n"
        "DUAL-TRACK MULTI-SENSORY ENHANCEMENT MANDATE:\n"
        "You must tailor the lesson text to include explicit operational hooks for physics parameters, "
        "historical milestones, math proportions, or physical laws. You must also naturally weave in keywords "
        "from this look-up dictionary list to trigger right-panel alignments: "
        "'water', 'atoms', 'equations', 'inertia', 'stoichiometry', 'printing', 'migration', 'judah', 'babylon', 'covenant'.\n"
    )
    return base_prompt

def construct_user_instructions(grade, subject, day, unit_folder):
    return (
        f"Write a comprehensive curriculum lesson leaf node for Grade: {grade.upper()}, "
        f"Subject: {subject.title()}, Day: {day} inside Chapter: {unit_folder.replace('_', ' ').title()}.\n\n"
        f"Provide four distinct structural data blocks clearly labeled as follows:\n"
        f"TITLE: A short, clean lesson header.\n"
        f"BODY: Academic core prose textbook entry text block.\n"
        f"WORKSPACE: Step-by-step interactive student task instructions.\n"
        f"CHECKOUT: A deep socratic verification checkpoint challenge question query."
    )
def build_custom_schema_payload(raw_content, grade, subject, day, unit_folder):
    # BULLETPROOF REGE ZONE EXTRACTOR: Captures content sectors directly to completely block leaks
    title_match = re.search(r"TITLE:\s*(.*?)(?=BODY:|WORKSPACE:|CHECKOUT:|$)", raw_content, re.IGNORECASE | re.DOTALL)
    body_match = re.search(r"BODY:\s*(.*?)(?=WORKSPACE:|CHECKOUT:|TITLE:|$)", raw_content, re.IGNORECASE | re.DOTALL)
    workspace_match = re.search(r"WORKSPACE:\s*(.*?)(?=CHECKOUT:|TITLE:|BODY:|$)", raw_content, re.IGNORECASE | re.DOTALL)
    checkout_match = re.search(r"CHECKOUT:\s*(.*?)(?=TITLE:|BODY:|WORKSPACE:|$)", raw_content, re.IGNORECASE | re.DOTALL)

    title = title_match.group(1).strip() if title_match else "Lesson Concept"
    body = body_match.group(1).strip() if body_match else raw_content
    workspace = workspace_match.group(1).strip() if workspace_match else "Complete active playground assignment."
    checkout = checkout_match.group(1).strip() if checkout_match else "Answer verification challenge question."

    # Strip out any residual numbering prefixes or header titles from text blocks
    for clean_pat in [r"^(\d+\.\s*)", r"TITLE:", r"BODY:", r"WORKSPACE:", r"CHECKOUT:"]:
        title = re.sub(clean_pat, "", title, flags=re.IGNORECASE).strip()
        body = re.sub(clean_pat, "", body, flags=re.IGNORECASE).strip()
        workspace = re.sub(clean_pat, "", workspace, flags=re.IGNORECASE).strip()
        checkout = re.sub(clean_pat, "", checkout, flags=re.IGNORECASE).strip()

    grade_lower = str(grade).lower()
    if grade_lower in ["gk", "g1"]:
        interaction_type = "Hands-On Activity Lab"
        bg_color = "#FEF3C7"
        palette_tokens = [
            {"token_label": "🖍️ Use Blue Marker", "canvas_action_trigger": "color_stroke_blue", "voice_synthesis_phrase": "Blue color selected.", "grade_rigor_weight": 1},
            {"token_label": "🌸 Object Counter", "canvas_action_trigger": "render_flower_nodes", "voice_synthesis_phrase": "Counting active screen items.", "grade_rigor_weight": 1}
        ]
        vector_shapes = [
            {"element_id": "canvasBgZone", "svg_type": "path", "label_overlay_text": "Activity Area: Interactive Playground Field", "svg_path_data": "M 0 0 L 500 0 L 500 180 L 0 180 Z"},
            {"element_id": "countTargetZone", "svg_type": "circle", "label_overlay_text": "Target Object Node", "svg_path_data": "cx:250, cy:90, r:40"}
        ]
        console_params = {"console_objective_label": "COUNT THE OBJECTS DISPLAYED IN THE PLAYGROUND", "premise_a_label": "Select Blue Marker", "premise_b_label": "Submit Item Count", "console_success_message": "⚡ WORKSPACE VERIFIED: MATH TARGET MET"}
        socratic_tree = {"optimal_keywords": ["count", "shapes", "blue"], "misconception_catcher": "If your count skips numbers, review the screen items slowly.", "remediation_analogy": "Let's touch each object one by one with your pointer, just like climbing steps."}
        providential_node = {"calendar_year": "Creation Foundations", "geographic_coordinate_bounds": "Global Coordinates", "biblical_epoch_match": "Genesis Order", "primary_source_excerpt": "Order, symmetry, and numerical harmony establish natural constants from the beginning."}
    elif grade_lower in ["g2", "g3", "g4", "g5"]:
        interaction_type = "Visual Concept Lab"
        bg_color = "#E0F2FE"
        palette_tokens = [
            {"token_label": "🗜️ Shift Place Value", "canvas_action_trigger": "toggle_base_ten", "voice_synthesis_phrase": "Base ten positions shifting.", "grade_rigor_weight": 2},
            {"token_label": "🧪 Measure Proportion", "canvas_action_trigger": "fill_pipe_ratio", "voice_synthesis_phrase": "Measuring fraction values.", "grade_rigor_weight": 2}
        ]
        vector_shapes = [
            {"element_id": "pipeReservoir", "svg_type": "rect", "label_overlay_text": "Fraction Visualization Grid", "svg_path_data": "x:50, y:30, width:400, height:80"},
            {"element_id": "indicatorNotch", "svg_type": "path", "label_overlay_text": "Proportion Alignment Mark", "svg_path_data": "M 250 20 L 250 120"}
        ]
        console_params = {"console_objective_label": "BALANCE AND COMPARE FRACTIONAL VALUES", "premise_a_label": "Adjust Liquid Valve", "premise_b_label": "Submit Numeric Ratio", "console_success_message": "⚡ EQUATION BALANCE STATUS: VERIFIED"}
        socratic_tree = {"optimal_keywords": ["fraction", "ratio", "value", "equal"], "misconception_catcher": "Remember that larger denominators split the area into smaller pieces.", "remediation_analogy": "Think of cutting a long block into perfectly matched sections to share evenly."}
        providential_node = {"calendar_year": "1493 A.D.", "geographic_coordinate_bounds": "0.254, 6.605 (Sao Tome Island)", "biblical_epoch_match": "Deuteronomy Diaspora Realities", "primary_source_excerpt": "Approximately 2,000 Judean children forcefully separated from community centers, transported to charting coordinates."}

    elif grade_lower in ["g6", "g7", "g8"]:
        interaction_type = "Interactive Modeling Studio"
        bg_color = "#ECFDF5"
        palette_tokens = [
            {"token_label": "减 Plot Data Variable", "canvas_action_trigger": "update_linear_slope", "voice_synthesis_phrase": "Coordinate point locked.", "grade_rigor_weight": 3},
            {"token_label": "📡 Isolate Outliers", "canvas_action_trigger": "isolate_outlier", "voice_synthesis_phrase": "Scanning data outliers.", "grade_rigor_weight": 3}
        ]
        vector_shapes = [
            {"element_id": "xAxisInertia", "svg_type": "line", "label_overlay_text": "Horizontal Time Data Axis", "svg_path_data": "x1:30, y1:150, x2:470, y2:150"},
            {"element_id": "yAxisMass", "svg_type": "line", "label_overlay_text": "Vertical Variable Measurement Axis", "svg_path_data": "x1:50, y1:10, x2:50, y2:170"}
        ]
        console_params = {"console_objective_label": "ALIGN COORDINATE EQUATION DATA RATIOS", "premise_a_label": "Adjust X Coordinate", "premise_b_label": "Isolate Data Outliers", "console_success_message": "⚡ DATA STUDIO MODEFICATION: STABLE"}
        socratic_tree = {"optimal_keywords": ["linear", "slope", "inertia", "outlier", "variable"], "misconception_catcher": "Data outliers shouldn't be ignored; they reveal important boundary conditions.", "remediation_analogy": "Imagine a seesaw where moving your seat instantly changes the balance point for both sides."}
        providential_node = {"calendar_year": "539 B.C.", "geographic_coordinate_bounds": "32.536, 44.421 (Ancient Babylon)", "biblical_epoch_match": "Jeremiah Historical Timeline Node", "primary_source_excerpt": "Geopolitical strategy shift where Cyrus redirects waterway channels, creating an unexpected structural approach path."}

    else:
        interaction_type = "Advanced Analytical Workspace"
        bg_color = "#F0F3FF"
        palette_tokens = [
            {"token_label": "计 Compute System Matrix", "canvas_action_trigger": "solve_linear_system", "voice_synthesis_phrase": "Executing linear transformation matrices.", "grade_rigor_weight": 4},
            {"token_label": "线 Modulate Economic Index", "canvas_action_trigger": "adjust_macro_slider", "voice_synthesis_phrase": "Adjusting baseline metric indexing variables.", "grade_rigor_weight": 4}
        ]
        vector_shapes = [
            {"element_id": "matrixGridA", "svg_type": "rect", "label_overlay_text": "Equation Optimization Field 1", "svg_path_data": "x:40, y:20, width:180, height:120"},
            {"element_id": "matrixGridB", "svg_type": "rect", "label_overlay_text": "System Boundary Variable Matrix 2", "svg_path_data": "x:280, y:20, width:180, height:120"}
        ]
        console_params = {"console_objective_label": "OPTIMIZE TRANSFORMATION GRID MATRIX VALUES", "premise_a_label": "Compute Inverse Matrix", "premise_b_label": "Verify Policy Threshold", "console_success_message": "⚡ ANALYSIS COMPLETE: 100% MASTERY VERIFIED"}
        socratic_tree = {"optimal_keywords": ["matrix", "transformation", "stoichiometry", "inflation", "macroeconomic", "rhetorical"], "misconception_catcher": "A determinant of zero means there is no unique solution; your grid values must have clear boundary conditions.", "remediation_analogy": "Like adjusting a camera lens along two focal planes at the same time to bring a blurry picture into sharp focus."}
        providential_node = {"calendar_year": "1492 A.D.", "geographic_coordinate_bounds": "-3.749, 40.416 (Iberian Peninsula)", "biblical_epoch_match": "Alhambra Displacement Impact Networks", "primary_source_excerpt": "The convergence of local expulsion policies with breakthrough oceanic navigation mapping maps out a distinct providential timeline."}

    def resolve_group_id(gk):
        for grp, lst in GROUPS.items():
            if gk in lst: return grp
        return "k5"

    return {
        "grade_prefix": str(grade).lower(),
        "layout_group": str(resolve_group_id(grade)).upper(),
        "subject_track": str(subject).lower(),
        "unit_folder": str(unit_folder).lower(),
        "day": int(day),
        "lesson_title": str(title),
        "lesson_body": str(body),
        "interactive_assignment": str(workspace),
        "daily_assessment": str(checkout),
        "interactive_learning_module": {
            "active_interaction_type": str(interaction_type),
            "canvas_background_color": str(bg_color),
            "vector_shapes_layout": vector_shapes,
            "computational_console_parameters": console_params
        },
        "historical_connections": providential_node,
        "guided_learning_coaching": socratic_tree,
        "learning_tool_buttons": palette_tokens
    }
def pipeline_batch_execution(target_days=None):
    if target_days is None:
        target_days = [1, 46, 91, 136]
        
    print(f"Executing deep multi-sensory database architecture sync inside: {DATABASE_ROOT}")
    
    for group_folder, grade_keys in GROUPS.items():
        for grade in grade_keys:
            for subject in SUBJECTS:
                for day in target_days:
                    unit_folder = calculate_chronological_unit(day)
                    target_dir = os.path.join(DATABASE_ROOT, group_folder.lower(), grade.lower(), subject.lower(), unit_folder.lower())
                    os.makedirs(target_dir, exist_ok=True)
                    
                    target_file = os.path.join(target_dir, f"day_{day}.json")
                    
                    if os.path.exists(target_file):
                        try:
                            os.remove(target_file)
                        except Exception as e:
                            print(f"File handle clear issue on day {day}: {str(e)}")
                            
                    print(f"Streaming advanced multi-sensory variables for: {grade.upper()} {subject.title()} (Day {day})...")
                    
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": generate_system_instructions(subject, grade, day)},
                                {"role": "user", "content": construct_user_instructions(grade, subject, day, unit_folder)}
                            ],
                            temperature=0.7
                        )
                        
                        raw_stream = response.choices[0].message.content.strip()
                        json_payload = build_custom_schema_payload(raw_stream, grade, subject, day, unit_folder)
                        
                        with open(target_file, "w", encoding="utf-8") as out_file:
                            json.dump(json_payload, out_file, indent=4, ensure_ascii=False)
                            
                        time.sleep(2.0)
                        
                    except Exception as loop_error:
                        print(f"Ingestion bottleneck bypassed on day {day}: {str(loop_error)}")
                        time.sleep(3.0)

if __name__ == "__main__":
    pipeline_batch_execution()
    print("\nLocal Flat-File Vault database multi-sensory matrices synchronized successfully.")
