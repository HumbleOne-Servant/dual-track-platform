import os
import json
import time
from openai import OpenAI

DATABASE_ROOT = r"C:\DualTrackLearning_Online\pure_curriculum_vault"
API_KEY = os.environ.get("OPENAI_API_KEY")

GROUPS_MAPPING = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
}
SUBJECTS = [
    "mathematics", 
    "science", 
    "language_arts", 
    "historical_studies"
]

STANDARDS_VAULT = {
    "mathematics": {
        "gk": "One-to-One Correspondence, Cardinality, Counting up to 20, Basic Geometric Shapes.",
        "g1": "Addition and Subtraction within 20, Place Value Systems, Measuring Lengths.",
        "g2": "Place Value Foundations to 1000, Multi-Digit Addition, Linear Measurement Plots.",
        "g3": "Multiplication and Division Concepts, Fraction Numerators, Area Calculation Layouts.",
        "g4": "Fraction Equivalence, Multi-Digit Arithmetic Circuits, Angle Rotation Measures.",
        "g5": "Fractions Multi-Tier Operations, Coordinate Grid Cartesian Planes, Volume Constants.",
        "g6": "Ratios and Rates, Division of Fractions, Rational Numbers, Algebraic Expressions.",
        "g7": "Proportional Relationships, Ratios, Rational Number Operations, Expressions and Equations.",
        "g8": "Radicals and Integer Exponents, Linear Functions, Pythagorean Theorem, Volume Profiles.",
        "g9": "Quadratic Functions, Linear Systems, Structural Modeling Functions, Matrix Transformations.",
        "g10": "Coordinate Geometry Proofs, Trigonometric Ratio Constants, Circle Theorem Layouts.",
        "g11": "Exponential and Logarithmic Vectors, Polynomial Remainder Rules, Conic Section Constants.",
        "g12": "Calculus Derivatives, Integral Optimization, Limits Convergence, Transcendental Equations."
    },
    "science": {
        "gk": "Physical properties of elements, Animal survival tracking, Weather patterns and seasons.",
        "g1": "Light and Sound wave properties, Observable patterns in space, Plant structural traits.",
        "g2": "Ecosystem biodiversity variables, Matter state transformations, Earth surface event dynamics.",
        "g3": "Force and Motion interaction loops, Inheritance patterns, Environmental adaptation tracks.",
        "g4": "Energy transfer mechanisms, Wave configuration matrices, Fossil rock layer logs.",
        "g5": "Matter particle models, Gravitational space vectors, Global water cycle dynamics.",
        "g6": "Geological rock cycles, Solar system balance tracking, Climate feedback mechanism models.",
        "g7": "Cell Structures and Functions, Earth and Space Cycles, Kinetic vs Potential Energy Waves.",
        "g8": "Atomic molecular models, Chemical reaction constants, Genes and natural selection paths.",
        "g9": "Mendelian genetics, Carbon cycle ecosystems, Tectonic plate mechanics, Energy vectors.",
        "g10": "Newtonian motion acceleration vectors, Circuit resistance pathways, Wave interference laws.",
        "g11": "Chemical Bonding Vectors, Stoichiometric Kinetics, Thermodynamics Laws, Ideal Gas Constants.",
        "g12": "Nuclear decay milestones, Quantum electron states, Organic molecular configurations."
    }
}
ART_BLUEPRINT_VAULT = {
    1: {
        "theme": "magical_forest",
        "bg_color": "#ECFDF5",
        "bg_path": "M 0 0 L 400 0 L 400 300 L 0 300 Z",
        "container_path": "M 50,220 C 100,180 300,180 350,220 C 320,260 80,260 50,220 Z",
        "target_path": "M 200,60 C 180,40 150,60 170,90 C 190,110 210,110 230,90 C 250,60 220,40 200,60 Z",
        "bg_label": "Zone 1: The Magical Forest Field",
        "container_label": "Zone 2: The Forest Stream Pond",
        "target_label": "Zone 3: The Targeted Hidden Counting Leaf"
    },
    2: {
        "theme": "butterfly_garden",
        "bg_color": "#FFFDF2",
        "bg_path": "M 10 10 L 390 10 L 390 290 L 10 290 Z",
        "container_path": "M 200,130 Q 110,150 110,230 Q 200,270 290,230 Q 290,150 200,130 Z",
        "target_path": "M 180,50 C 160,30 160,80 180,70 C 200,80 200,30 180,50 Z",
        "bg_label": "Zone 1: The Sunny Garden Field",
        "container_label": "Zone 2: The Butterfly Flower Patch",
        "target_label": "Zone 3: The Flapping Counting Butterfly"
    }
}
def call_openai_ske_model(prompt_text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert curriculum writer. You output content strictly inside valid JSON objects matching the user blueprint."},
                {"role": "user", "content": prompt_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"   [API Handshake Postponed] Delaying thread: {str(e)}")
        return None
def build_prompt_blueprint(group, grade, subject, unit, day):
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, f"Advanced Grade {grade.upper()} milestones.")
    art_meta = ART_BLUEPRINT_VAULT.get(day, ART_BLUEPRINT_VAULT[1])
    
    if group == "k5":
        interaction_key = "tactile_svg_matrix"
        assignment_prompt = f"Imagine you are exploring an interactive lesson centered around {art_meta['theme'].replace('_', ' ')}. Write clear, child-friendly instructions telling the student exactly what action palette crayon number node to pick to select their element tool, and command them to color {art_meta['bg_label']}, {art_meta['container_label']}, and {art_meta['target_label']} to verify the final concept count value."
        blueprint_prompt = f"""
        "canvas_background_color": "{art_meta['bg_color']}",
        "vector_shapes_layout": [
            {{"element_id": "canvasBgZone", "svg_type": "path", "label_overlay_text": "{art_meta['bg_label']}", "svg_path_data": "{art_meta['bg_path']}"}},
            {{"element_id": "canvasOvalZone", "svg_type": "path", "label_overlay_text": "{art_meta['container_label']}", "svg_path_data": "{art_meta['container_path']}"}},
            {{"element_id": "canvasCircleZone", "svg_type": "path", "label_overlay_text": "{art_meta['target_label']}", "svg_path_data": "{art_meta['target_path']}"}}
        ],
        "computational_console_parameters": {{
            "console_objective_label": "GENERATE SET MATRIX: VERIFY YOUR DAILY STORY VARIABLES",
            "premise_a_label": "Verify Story Target",
            "premise_b_label": "Lock Count Matrix",
            "console_success_message": "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE: CONCEPT DAY {day} SECURED",
            "console_audio_feedback_string": "Node verified"
        }}
        """
    elif group == "68":
        interaction_key = "algebraic_balancer_grid"
        assignment_prompt = f"Write clear instructions directing a Middle School student to calculate the balanced system constant for this specific Day {day} equation, and type their isolated variable directly into the variable box."
        blueprint_prompt = f"""
        "canvas_background_color": "#FAFBFD",
        "vector_shapes_layout": [],
        "computational_console_parameters": {{
            "console_objective_label": "ALGEBRAIC BALANCER: COMPUTE AND ISOLATE VARIABLE TARGET CONSTANTS",
            "premise_a_label": "Isolate Balance X",
            "premise_b_label": "Compute Ratio Constant",
            "console_success_message": "⚡ CIRCUIT STATUS VERIFIES VARIABLE X SECURED: EQUATION Day {day} BALANCED",
            "console_audio_feedback_string": "Node verified"
        }}
        """
    else:
        interaction_key = "thesis_optimizer_console"
        assignment_prompt = f"Write advanced instructions commanding a High School student to review the layout statements and input an evidentiary proof summary into the matrix analyzer text arena."
        blueprint_prompt = f"""
        "canvas_background_color": "#0F172A",
        "vector_shapes_layout": [],
        "computational_console_parameters": {{
            "console_objective_label": "RHETORICAL MATRIX OPTIMIZER: CONSTRUCT EVIDENCE CASE STUDY",
            "premise_a_label": "Validate Assertion Case",
            "premise_b_label": "Lock Logic Constants",
            "console_success_message": "⚡ CIRCUIT STATUS VERIFIES ARCHITECTURE SECURED: THESIS PROOF Day {day} OPERATIONAL",
            "console_audio_feedback_string": "Node verified"
        }}
        """
    return f"""
    Generate an unbendable, production-ready S-K-E data node for Grade {grade.upper()}, Subject Track: {subject}, Day {day}.
    Active Academic Standard Focus Milestone: {standards_focus}
    
    You must output a single, raw valid JSON object with these exact keys:
    {{
        "grade_prefix": "{grade}",
        "layout_group": "{group.upper()}",
        "subject_track": "{subject}",
        "unit_folder": "{unit}",
        "day": {day},
        "lesson_title": "Grade {grade.upper()} {subject.replace('_', ' ').title()} - Day {day} (SKE Edition)",
        "lesson_body": "Write a 3-sentence, deeply educational textbook text block introducing the day's standard milestone. Make the vocabulary and complexity strictly appropriate for Grade {grade.upper()}.",
        "interactive_assignment": "{assignment_prompt}",
        "daily_assessment": "State a direct, short check-out problem question that tests ownership of this specific day's milestone.",
        
        "frontend_rendering_blueprint": {{
            "active_interaction_type": "{interaction_key}",
            "total_required_clicks_to_unlock": 3,
            {blueprint_prompt}
        }},
        "worldview_track_matrices": {{
            "comparative_insight": "Provide a powerful, grade-appropriate 1-sentence analytical perspective showing absolute structural design or logical order constants matching this lesson's exact theme.",
            "biblical_alignment": "Provide an explicit, highly relevant scriptural text quote and chapter verse that aligns perfectly with this specific day's structural or logical mechanic."
        }},
        "anti_repetition_remediation_branch": {{
            "remediation_threshold_score": 85,
            "remediation_body": "Completely rewrite the lesson concept using an entirely alternative, fresh concrete visual analogy appropriate for Grade {grade.upper()}.",
            "remediation_assignment": "Provide an alternative interactive task description matching the fresh remediation story.",
            "remediation_assessment": "An alternative short check-out verification question string."
        }}
    }}
    """
def run_mass_vault_generation(start_day=1, end_day=2):
    if not API_KEY:
        print("❌ ERROR: OpenAI API key missing.")
        return
    print("========================================================================")
    print("🤖 LAUNCHING PATH VECTOR GENERATIVE INGESTION ENGINE")
    print("========================================================================")
    for group, grades in GROUPS_MAPPING.items():
        for grade in grades:
            for subject in SUBJECTS:
                for day_num in range(start_day, end_day + 1):
                    unit = "unit_1_foundations"
                    if day_num > 45 and day_num <= 90: unit = "unit_2_shapes_spaces"
                    elif day_num > 90 and day_num <= 135: unit = "unit_3_weather_seasons"
                    elif day_num > 135: unit = "unit_4_counting_base"
                    
                    folder_path = os.path.join(DATABASE_ROOT, group, grade, subject, unit)
                    os.makedirs(folder_path, exist_ok=True)
                    target_file = os.path.join(folder_path, f"day_{day_num}.json")
                    
                    print(f"🎨 Injecting Graphic Vector Artwork: [{grade.upper()}] -> [{subject.upper()}] -> Day {day_num}")
                    prompt = build_prompt_blueprint(group, grade, subject, unit, day_num)
                    raw_json = call_openai_ske_model(prompt)
                    if raw_json:
                        try:
                            parsed_data = json.loads(raw_json)
                            with open(target_file, 'w', encoding='utf-8') as f:
                                json.dump(parsed_data, f, indent=4, ensure_ascii=False)
                            print(f"   ✅ Upgraded Node Written Successfully.")
                        except Exception as parse_error:
                            print(f"   ❌ Formatting anomaly, skipping node: {str(parse_error)}")
                    time.sleep(1.2)

if __name__ == "__main__":
    run_mass_vault_generation(start_day=1, end_day=2)
