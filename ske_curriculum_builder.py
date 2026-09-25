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
        "g7": "Proportional Relationships, Rational Operations, Multi-Step Linear Equations.",
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
# Hardened SDK Data Parser: Native v1.0 Array Element Choice Extraction
def call_openai_ske_model(prompt_text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are an elite educational game designer and curriculum developer. You output data strictly inside a single, raw, valid JSON object matching the requested schema. "
                        "Never write introductory remarks, markdown code ticks (like ```json), or conversational footnotes. Keep parameters structurally perfect."
                    )
                },
                {"role": "user", "content": prompt_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        # FIXED PERMANENTLY: Enforced explicit choices[0] array index mapping configuration
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"   [API Handshake Postponed] Delaying thread: {str(e)}")
        return None
def build_prompt_blueprint(group, grade, subject, unit, day):
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, f"Advanced Grade {grade.upper()} standard curriculum milestones and logical ordering proofs.")
    
    if group == "k5":
        interaction_key = "tactile_svg_matrix"
        assignment_prompt = (
            "Write direct workbook instructions for an elementary child. Invent a completely unique real-world visual story scene "
            "(such as a colorful garden with butterflies, a coral reef with fish, or a space galaxy with rockets). Tell the child exactly what numbered palette crayon node to select "
            "and which specific story object zone (Zone 1, Zone 2, or Zone 3) to fill on their canvas chart to complete the visual count."
        )
        # CRITICAL HARDENING: Gives the AI rigid structural examples so it outputs real storytelling nouns, not code instructions
        blueprint_prompt = f"""
        "canvas_background_color": "#E0F2FE",
        "vector_shapes_layout": [
            {{
                "element_id": "canvasBgZone", 
                "svg_type": "rect", 
                "label_overlay_text": "Zone 1: [Invent a direct story setting noun here, do NOT use generic words like Name or Story. Example: 'The Colorful Garden Field']",
                "svg_path_data": "M 10 10 L 390 10 L 380 290 L 10 290 Z"
            }},
            {{
                "element_id": "canvasOvalZone", 
                "svg_type": "ellipse", 
                "label_overlay_text": "Zone 2: [Invent a direct container object noun here. Example: 'The Red Rose Petals']",
                "svg_path_data": "M 70 180 A 130 70 0 1 0 330 180 A 130 70 0 1 0 70 180 Z"
            }},
            {{
                "element_id": "canvasCircleZone", 
                "svg_type": "circle", 
                "label_overlay_text": "Zone 3: [Invent a direct countable target item noun here. Example: 'The Flapping Butterflies']",
                "svg_path_data": "M 170 70 A 30 30 0 1 0 230 70 A 30 30 0 1 0 170 70 Z"
            }}
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
        assignment_prompt = (
            f"Write rigorous analytical instructions for a Middle School student tackling {standards_focus}. Command them to evaluate "
            "the mathematical equation or data tracking chart, isolate the balanced sum constants step-by-step, and input the precise solution integer "
            "directly into the 'Isolate Unknown Token Variable (X)' console input text box to unblock the logic loops."
        )
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
        assignment_prompt = (
            f"Write advanced academic instructions for a High School student executing {standards_focus}. Command them to analyze "
            "the structural proof or thesis statement layout, formulate a multi-paragraph analytical summary evidence case study, and input "
            "their logical assertion validation strings directly into the Estonian Matrix Optimizer text arena."
        )
        blueprint_prompt = f"""
        "canvas_background_color": "#0F172A",
        "vector_shapes_layout": [],
        "computational_console_parameters": {{
            "console_objective_label": "RHETORICAL MATRIX OPTIMIZER: CONSTRUCT AND VALIDATE STRUCTURAL EVIDENCE CASE STUDY",
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
        print("❌ ERROR: The environment variable 'OPENAI_API_KEY' is missing on this machine.")
        return
        
    print("========================================================================")
    print("🤖 LAUNCHING UNIVERSAL ALL-GRADE GENERATIVE S-K-E INGESTION ENGINE")
    print(f"Generating exactly {end_day - start_day + 1} days per subject for ALL 13 Grade tracks...")
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
                    
                    print(f"⚙️ Formatting Age-Appropriate Node: [{grade.upper()}] -> [{subject.upper()}] -> Day {day_num}")
                    prompt = build_prompt_blueprint(group, grade, subject, unit, day_num)
                    raw_json = call_openai_ske_model(prompt)
                    
                    if raw_json:
                        try:
                            parsed_data = json.loads(raw_json)
                            with open(target_file, 'w', encoding='utf-8') as f:
                                json.dump(parsed_data, f, indent=4, ensure_ascii=False)
                            print(f"   ✨ Grade {grade.upper()} Day {day_num} Secured.")
                        except Exception as parse_error:
                            print(f"   ❌ Formatting anomaly, skipping node: {str(parse_error)}")
                            
                    time.sleep(1.2)

if __name__ == "__main__":
    run_mass_vault_generation(start_day=1, end_day=2)
