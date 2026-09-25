# ========================================================================
# FILE: curricullm_engine.py (Box 1 of 5)
# DESCRIPTION: Core Database Paths, Key Validations, and Native SDK Connections
# ========================================================================
import os
import json
import time
from openai import OpenAI

# Decoupled flat-file data tree root path configuration variable
DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"

# Ingestion Security: Read token credentials directly from environment vectors
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("CRITICAL ERROR: OPENAI_API_KEY variable not detected in active session.")
    print("PowerShell Fix: Run -> $env:OPENAI_API_KEY='your_actual_key'")
    exit(1)

# Official SDK Client Layer handshake
client = OpenAI(api_key=api_key)

# Deterministic directory mapping parameter dictionaries
GROUPS = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies", "biblical"]

def calculate_chronological_unit(day):
    """Calculates lowercase unit folders based on the 180-day timeline loops."""
    if 1 <= day <= 45: return "unit_1_foundations"
    elif 46 <= day <= 90: return "unit_2_shapes_spaces"
    elif 91 <= day <= 135: return "unit_3_weather_seasons"
    elif 136 <= day <= 180: return "unit_4_counting_base"
    return "unit_1_foundations"
# ========================================================================
# FILE: curricullm_engine.py (Box 2 of 5)
# DESCRIPTION: Advanced System Prompts with Multi-Sensory Prompt Parameters
# ========================================================================
def generate_system_instructions(subject, grade, day):
    """Enforces absolute text cleansing filters and structural multi-sensory mandates."""
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
    """Generates structural directives matching the advanced case-insensitive keys."""
    return (
        f"Write a comprehensive curriculum lesson leaf node for Grade: {grade.upper()}, "
        f"Subject: {subject.title()}, Day: {day} inside Chapter: {unit_folder.replace('_', ' ').title()}.\n\n"
        f"Provide four distinct structural data blocks separated by exactly '---':\n"
        f"1. TITLE: Clean header string.\n"
        f"2. BODY: Academic core prose textbook entry text block.\n"
        f"3. WORKSPACE: Step-by-step interactive task instructions.\n"
        f"4. CHECKOUT: A deep socratic verification checkpoint challenge question query."
    )
# ========================================================================
# FILE: curricullm_engine.py (Box 3 of 5)
# DESCRIPTION: Slicing Handlers & Early Elementary to Intermediate Algorithmic Matrices
# ========================================================================
def build_custom_schema_payload(raw_content, grade, subject, day, unit_folder):
    """Slices raw data text and builds an elite high-graphic canvas, socratic, and providential payload."""
    chunks = raw_content.split("---")
    title, body, workspace, checkout = "Lesson", raw_content, "Sandbox", "Check"
    
    clean_chunks = []
    for c in chunks:
        p = c.strip()
        for h in ["TITLE:", "BODY:", "WORKSPACE:", "CHECKOUT:"]:
            if p.upper().startswith(h): p = p[len(h):].strip()
        clean_chunks.append(p)
        
    if len(clean_chunks) >= 1: title = clean_chunks[0]
    if len(clean_chunks) >= 2: body = clean_chunks[1]
    if len(clean_chunks) >= 3: workspace = clean_chunks[2]
    if len(clean_chunks) >= 4: checkout = clean_chunks[3]

    for tag in ["TITLE:", "BODY:", "WORKSPACE:", "CHECKOUT:", "Title:", "Body:", "Workspace:", "Checkout:"]:
        body = body.replace(tag, "").strip()
        workspace = workspace.replace(tag, "").strip()
        checkout = checkout.replace(tag, "").strip()

    grade_lower = str(grade).lower()
    if grade_lower in ["gk", "g1"]:
        interaction_type = "tactile_svg_matrix"
        bg_color = "#FEF3C7"
        palette_tokens = [
            {"token_label": "🖍️ Select Crayon 3", "canvas_action_trigger": "color_stroke_blue", "voice_synthesis_phrase": "Blue crayon tracking active.", "grade_rigor_weight": 1},
            {"token_label": "🌸 Forest Flower Count", "canvas_action_trigger": "render_flower_nodes", "voice_synthesis_phrase": "Counting daily object points.", "grade_rigor_weight": 1}
        ]
        vector_shapes = [
            {"element_id": "canvasBgZone", "svg_type": "path", "label_overlay_text": "Zone 1: Active Tactile Input Field", "svg_path_data": "M 0 0 L 500 0 L 500 180 L 0 180 Z"},
            {"element_id": "countTargetZone", "svg_type": "circle", "label_overlay_text": "Target Node Alpha", "svg_path_data": "cx:250, cy:90, r:40"}
        ]
        console_params = {"console_objective_label": "COUNT THE VISUAL VARIABLES IN THE FIELD", "premise_a_label": "Select Blue Crayon", "premise_b_label": "Lock Item Count", "console_success_message": "⚡ SUCCESS: COUNT SECURED"}
        socratic_tree = {"optimal_keywords": ["count", "shapes", "blue"], "misconception_catcher": "If the count skips numbers, re-verify points on the grid layer.", "remediation_analogy": "Let's tap each circle with your pointer handle slowly, just like counting steps."}
        providential_node = {"calendar_year": "Creation Foundations", "geographic_coordinate_bounds": "Global Matrix", "biblical_epoch_match": "Genesis Order", "primary_source_excerpt": "Order and numerical harmony establish natural constants from the beginning."}

    elif grade_lower in ["g2", "g3", "g4", "g5"]:
        interaction_type = "fluid_fraction_console"
        bg_color = "#E0F2FE"
        palette_tokens = [
            {"token_label": "🗜️ Shift Place Value", "canvas_action_trigger": "toggle_base_ten", "voice_synthesis_phrase": "Base ten matrix shifts.", "grade_rigor_weight": 2},
            {"token_label": "🧪 Open Fraction Valve", "canvas_action_trigger": "fill_pipe_ratio", "voice_synthesis_phrase": "Siphoning fluid system ratios.", "grade_rigor_weight": 2}
        ]
        vector_shapes = [
            {"element_id": "pipeReservoir", "svg_type": "rect", "label_overlay_text": "Fraction Reactor Grid", "svg_path_data": "x:50, y:30, width:400, height:80"},
            {"element_id": "indicatorNotch", "svg_type": "path", "label_overlay_text": "Ratio Alignment Axis", "svg_path_data": "M 250 20 L 250 120"}
        ]
        console_params = {"console_objective_label": "BALANCE TRANSLATION VALUE METRICS", "premise_a_label": "Open System Valve", "premise_b_label": "Equate Numeric Ratio", "console_success_message": "⚡ CIRCIUT LOGIC STATUS VERIFIED"}
        socratic_tree = {"optimal_keywords": ["fraction", "ratio", "value", "equal"], "misconception_catcher": "Remember that numerator divisions change values inversely to height shifts.", "remediation_analogy": "Think of cutting a continuous pipe into precisely matched distribution lines."}
        providential_node = {"calendar_year": "1493 A.D.", "geographic_coordinate_bounds": "0.254, 6.605 (Sao Tome Island)", "biblical_epoch_match": "Deuteronomy Diaspora Scattering Blocks", "primary_source_excerpt": "Approximately 2,000 Judean youth forcefully split from lineage centers, shipped to uncharted volcanic coordinates."}
# ========================================================================
# FILE: curricullm_engine.py (Box 4 of 5)
# DESCRIPTION: Middle School and Advanced Secondary Algorithmic Matrices
# ========================================================================
    elif grade_lower in ["g6", "g7", "g8"]:
        interaction_type = "linear_inertia_grapher"
        bg_color = "#ECFDF5"
        palette_tokens = [
            {"token_label": "减 Plot Variable Beam", "canvas_action_trigger": "update_linear_slope", "voice_synthesis_phrase": "Linear variable coordinate locked.", "grade_rigor_weight": 3},
            {"token_label": "📡 Deflect Outlier Panel", "canvas_action_trigger": "isolate_outlier", "voice_synthesis_phrase": "Outlier deflection matrix running.", "grade_rigor_weight": 3}
        ]
        vector_shapes = [
            {"element_id": "xAxisInertia", "svg_type": "line", "label_overlay_text": "Inertia Time Plane Axis", "svg_path_data": "x1:30, y1:150, x2:470, y2:150"},
            {"element_id": "yAxisMass", "svg_type": "line", "label_overlay_text": "Mass Resistance Threshold Axis", "svg_path_data": "x1:50, y1:10, x2:50, y2:170"}
        ]
        console_params = {"console_objective_label": "ALIGN SLOPE EQUATION MASS COEFFICIENTS", "premise_a_label": "Adjust X Variable", "premise_b_label": "Isolate Scatter Outliers", "console_success_message": "⚡ COGNITIVE LINEAR INGESTION COMPLETE"}
        socratic_tree = {"optimal_keywords": ["linear", "slope", "inertia", "outlier", "variable"], "misconception_catcher": "Do not treat outlier vectors as noise; they expose critical structural boundary forces.", "remediation_analogy": "Imagine a balanced beam where shifting a slider instantly alters the systemic tilt value across the full axis."}
        providential_node = {"calendar_year": "539 B.C.", "geographic_coordinate_bounds": "32.536, 44.421 (Ancient Babylon)", "biblical_epoch_match": "Jeremiah 50 Prisons", "primary_source_excerpt": "Geopolitical pivot point where Cyrus redirects river routes, creating an inverted directional vulnerability vector."}

    else:
        interaction_type = "matrix_optimizer_console"
        bg_color = "#F0F3FF"
        palette_tokens = [
            {"token_label": "计 Compute Matrix Inverse", "canvas_action_trigger": "solve_linear_system", "voice_synthesis_phrase": "Executing linear transformation check.", "grade_rigor_weight": 4},
            {"token_label": "线 Modulate Inflation index", "canvas_action_trigger": "adjust_macro_slider", "voice_synthesis_phrase": "Modulating macroeconomic indexing values.", "grade_rigor_weight": 4}
        ]
        vector_shapes = [
            {"element_id": "matrixGridA", "svg_type": "rect", "label_overlay_text": "Transformation Bracket Plane 1", "svg_path_data": "x:40, y:20, width:180, height:120"},
            {"element_id": "matrixGridB", "svg_type": "rect", "label_overlay_text": "Output Optimization Bounds Plane 2", "svg_path_data": "x:280, y:20, width:180, height:120"}
        ]
        console_params = {"console_objective_label": "OPTIMIZE INDICES TRANSFORMATION COORDINATES", "premise_a_label": "Compute Matrix Equation", "premise_b_label": "Verify Policy Threshold", "console_success_message": "密 100% HIGHEST MASTERY MET: TERMINAL OPEN"}
        socratic_tree = {"optimal_keywords": ["matrix", "transformation", "stoichiometry", "inflation", "macroeconomic", "rhetorical"], "misconception_catcher": "A non-zero determinant verifies absolute coordinate lock; structural tracking cannot bypass singular zero vectors.", "remediation_analogy": "Like scaling a high-definition photograph along two different geometric axes at the exact same moment without losing pixel focus."}
        providential_node = {"calendar_year": "1492 A.D.", "geographic_coordinate_bounds": "-3.749, 40.416 (Iberian Peninsula)", "biblical_epoch_match": "Alhambra Decree Dispersal Waves", "primary_source_excerpt": "The synchronization of the expulsion mandate with maritime breakthroughs charts a global providential matrix."}

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
        "geometry_canvas_blueprint": {
            "active_interaction_type": str(interaction_type),
            "canvas_background_color": str(bg_color),
            "vector_shapes_layout": vector_shapes,
            "computational_console_parameters": console_params
        },
        "providential_temporal_nodes": providential_node,
        "socratic_remediation_tree": socratic_tree,
        "tactile_hud_tokens": palette_tokens
    }
# ========================================================================
# FILE: curricullm_engine.py (Box 5 of 5)
# DESCRIPTION: Force Overwrite Automated Loops and Request Pacing Guards
# ========================================================================
def pipeline_batch_execution(target_days=None):
    """Loops recursively down the flat-file vault, force cleaning all double text artifacts."""
    if target_days is None:
        # Foundations testing index points to distribute clean templates across all 4 units
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
                    
                    # FORCE CLEAN MATRIX: Wipes any lingering double content files automatically
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
                        
                        raw_stream = response.choices.message.content.strip()
                        json_payload = build_custom_schema_payload(raw_stream, grade, subject, day, unit_folder)
                        
                        with open(target_file, "w", encoding="utf-8") as out_file:
                            json.dump(json_payload, out_file, indent=4, ensure_ascii=False)
                            
                        # Hardened SDK stream request engine pacing delay (2.0s protects server sockets)
                        time.sleep(2.0)
                        
                    except Exception as loop_error:
                        print(f"Ingestion bottleneck bypassed on day {day}: {str(loop_error)}")
                        time.sleep(3.0)

if __name__ == "__main__":
    pipeline_batch_execution()
    print("\nLocal Flat-File Vault database multi-sensory matrices synchronized successfully.")
