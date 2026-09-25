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

SUBJECTS = ["mathematics", "science", "language_arts", "historical_studies"]

STANDARDS_VAULT = {
    "mathematics": {
        "gk": "One-to-One Correspondence, Cardinality, Counting up to 20, Basic Geometric Shapes.",
        "g1": "Addition and Subtraction within 20, Place Value Systems, Measuring Lengths.",
        "g7": "Proportional Relationships, Ratios, Rational Number Operations, Expressions and Equations."
    },
    "science": {
        "gk": "Physical properties of elements, Animal survival tracking, Weather patterns and seasons.",
        "g1": "Light and Sound wave properties, Observable patterns in space, Plant structural traits."
    }
}

def call_openai_ske_model(prompt_text):
    client = OpenAI(api_key=API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are an expert curriculum writer and digital game interaction designer. You output data strictly inside a single, raw, valid JSON object matching the user's schema blueprint format. "
                        "Never write introductory remarks, markdown formatting ticks (like ```json), or explanatory footnotes. Keep content engaging, standard-aligned, and deeply educational."
                    )
                },
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
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, "Age-appropriate national curriculum guidelines and logical ordering proofs.")
    
    if group == "k5":
        activity_instruction_rule = (
            "Write direct instructions for an elementary child. Tell them exactly what numbered crayon node (1, 2, or 3) "
            "to select from their palette box and which graphic chart canvas zone (Zone 1, Zone 2, or Zone 3) to fill to verify the count."
        )
        interaction_key = "tactile_svg_matrix"
    elif group == "68":
        activity_instruction_rule = (
            "Write clear instructions for a Middle School student. Command them to analyze the textbook equation or science data tracking line, "
            "formulate the balanced sum step-by-step, and input the precise solution integer directly into the 'Isolate Unknown Token Variable (X)' console input box."
        )
        interaction_key = "algebraic_balancer_grid"
    else:
        activity_instruction_rule = (
            "Write advanced academic instructions for a High School student. Command them to analyze the thesis layout statements "
            "and input a multi-paragraph analytical summary evidence proof directly into the Estonian Matrix Optimizer text arena."
        )
        interaction_key = "thesis_optimizer_console"

    return f"""
    Generate an unbendable, production-ready S-K-E data node for Grade {grade.upper()}, Subject Track: {subject}, Day {day}.
    Target Academic Standard Focus Milestone: {standards_focus}
    
    CRITICAL DIRECTION: Every individual calendar day must be uniquely and distinctly designed. Do not repeat the visual layouts, shape labels, or analogies used in previous days. The interactive assignment MUST explicitly command the student how to manipulate the specific geometric zones or input consoles generated in the rendering blueprint below.
    
    You must output a single, raw valid JSON object with these exact keys:
    {{
        "grade_prefix": "{grade}",
        "layout_group": "{group.upper()}",
        "subject_track": "{subject}",
        "unit_folder": "{unit}",
        "day": {day},
        "lesson_title": "Grade {grade.upper()} {subject.replace('_', ' ').title()} - Day {day} (SKE Edition)",
        "lesson_body": "Write 3 sentences of precise, direct textbook prose teaching the day's specific standard milestone. For K-5, explicitly name and describe the unique visual shape zones (Zone 1, Zone 2, Zone 3) generated in the rendering blueprint below.",
        "interactive_assignment": "{activity_instruction_rule}",
        "daily_assessment": "State the short evaluation question or check-out problem that verifies complete ownership of this day's concept.",
        
        "frontend_rendering_blueprint": {{
            "active_interaction_type": "{interaction_key}",
            "total_required_clicks_to_unlock": 3,
            "canvas_background_color": "#FAFBFD",
            "vector_shapes_layout": [
                {{
                    "element_id": "canvasBgZone",
                    "svg_type": "rect",
                    "label_overlay_text": "Zone 1: Field Area focus parameter for day {day}",
                    "target_matching_palette_number": 1
                }},
                {{
                    "element_id": "canvasOvalZone",
                    "svg_type": "ellipse",
                    "label_overlay_text": "Zone 2: Set Container mapping parameter for day {day}",
                    "target_matching_palette_number": 1
                }},
                {{
                    "element_id": "canvasCircleZone",
                    "svg_type": "circle",
                    "label_overlay_text": "Zone 3: Core Value marker unit for day {day}",
                    "target_matching_palette_number": 1
                }}
            ],
            "computational_console_parameters": {{
                "premise_a_label": "Verify Entry Checkpoint {day}",
                "premise_b_label": "Lock Verification Matrix {day}",
                "console_success_message": "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE: CONCEPT DAY {day} SECURED",
                "console_audio_feedback_string": "Circuit status verifies node active. Concept day {day} secured."
            }}
        }},
        "worldview_track_matrices": {{
            "comparative_insight": "Provide a powerful 1-sentence analytical perspective showing absolute structural design or logical order constants matching this day's exact milestone.",
            "biblical_alignment": "Provide an explicit, highly relevant scriptural text quote and chapter verse that aligns perfectly with this specific day's structural or logical mechanic."
        }},
        "anti_repetition_remediation_branch": {{
            "remediation_threshold_score": 85,
            "remediation_body": "Completely rewrite the day's core concept explanation using an entirely alternative, fresh concrete visual analogy to break down stuck checkpoints.",
            "remediation_assignment": "Provide an alternative interactive task description matching the fresh analogy.",
            "remediation_assessment": "An alternative short check-out verification question string."
        }}
    }}
    """

def run_mass_vault_generation(start_day=2, end_day=5):
    if not API_KEY:
        print("❌ ERROR: The environment variable 'OPENAI_API_KEY' is missing on this machine.")
        return
        
    print("========================================================================")
    print("🤖 STARTING AUTOMATED BATCH VAULT INGESTION LOOP (UPGRADED SKE SCHEMAS)")
    print(f"Targeting Days: {start_day} to {end_day} across Grade Tracks")
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
                    
                    # FORCE OVERWRITE OLD TEST FILES: Wipes out simple legacy data nodes
                    print(f"📝 Writing Upgraded SKE Matrix: Grade {grade.upper()} -> {subject.title()} -> Day {day_num}")
                    prompt = build_prompt_blueprint(group, grade, subject, unit, day_num)
                    raw_json = call_openai_ske_model(prompt)
                    
                    if raw_json:
                        try:
                            parsed_data = json.loads(raw_json)
                            with open(target_file, 'w', encoding='utf-8') as f:
                                json.dump(parsed_data, f, indent=4, ensure_ascii=False)
                            print(f"   ✅ Upgraded Node Written Successfully.")
                        except Exception as parse_error:
                            print(f"   ❌ Syntax mismatch caught, skipping file: {str(parse_error)}")
                            
                    time.sleep(1.2)

if __name__ == "__main__":
    # Runs the upgraded generator loop for Days 2 through 5 to overwrite them with true SKE parameters
    run_mass_vault_generation(start_day=2, end_day=5)
