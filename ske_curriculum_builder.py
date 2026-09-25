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
                        "You are an elite educational game designer and curriculum developer. You output data strictly inside a single, raw, valid JSON object matching the requested schema. "
                        "Never write introductory remarks, formatting ticks, or markdown code fences. Keep layout variables precise and child-friendly."
                    )
                },
                {"role": "user", "content": prompt_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.5
        )
        # FIXED PROACTIVELY: Absolute explicit array index mapping to conform with modern SDKs
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"   [API Handshake Postponed] Delaying thread: {str(e)}")
        return None

def build_prompt_blueprint(group, grade, subject, unit, day):
    standards_focus = STANDARDS_VAULT.get(subject, {}).get(grade, "Age-appropriate national curriculum guidelines and logical ordering proofs.")
    
    if group == "k5":
        activity_instruction_rule = (
            "Write direct instructions for an elementary child. Tell them exactly what numbered crayon node (1, 2, or 3) "
            "to select from their palette box and which specific story object zone (Zone 1, Zone 2, or Zone 3) to fill to complete the visual count."
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
    
    CRITICAL ILLUSTRATOR INSTRUCTION: You must invent a completely unique real-world visual story scene for this specific lesson (e.g., apples on a tree, stars in a constellation, fish in a reef, or trucks on a highway). The lesson text, workbook instructions, and the vector shapes layout MUST perfectly match and describe this generated story scene. Every day must be a completely fresh visual world!
    
    You must output a single, raw valid JSON object with these exact keys:
    {{
        "grade_prefix": "{grade}",
        "layout_group": "{group.upper()}",
        "subject_track": "{subject}",
        "unit_folder": "{unit}",
        "day": {day},
        "lesson_title": "Grade {grade.upper()} {subject.replace('_', ' ').title()} - Day {day} (SKE Edition)",
        
        "lesson_body": "Write a 3-sentence textbook story introducing today's concept. You MUST explicitly name and weave your newly invented real-world objects and the three screen zones into the narrative.",
        "interactive_assignment": "Provide direct instructions telling the child exactly what action parameters or story object zones (Zone 1, Zone 2, or Zone 3) to choose or target to complete the milestone task.",
        "daily_assessment": "State a direct, short check-out problem question that tests ownership of this day's milestone.",
        
        "frontend_rendering_blueprint": {{
            "active_interaction_type": "{interaction_key}",
            "total_required_clicks_to_unlock": 3,
            "canvas_background_color": "Provide a unique, theme-appropriate custom pastel hex color code matching your story environment background mood",
            "vector_shapes_layout": [
                {{
                    "element_id": "canvasBgZone",
                    "svg_type": "rect",
                    "label_overlay_text": "Zone 1: Name the large environmental background area based on your story theme (e.g., 'The Green Meadow' or 'The Deep Space Field')"
                }},
                {{
                    "element_id": "canvasOvalZone",
                    "svg_type": "ellipse",
                    "label_overlay_text": "Zone 2: Name the primary container object based on your story theme (e.g., 'The Apple Basket' or 'The Rocket Ship Space')"
                }},
                {{
                    "element_id": "canvasCircleZone",
                    "svg_type": "circle",
                    "label_overlay_text": "Zone 3: Name the primary countable item constant based on your story theme (e.g., 'The Target Apple' or 'The Core Fuel Cell')"
                }}
            ],
            "computational_console_parameters": {{
                "console_objective_label": "GENERATE SET MATRIX: IDENTIFY AND VERIFY YOUR DAILY STORY VARIABLES",
                "premise_a_label": "Verify Story Target",
                "premise_b_label": "Lock Count Matrix",
                "console_success_message": "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE: ONE-TO-ONE LESSON SECURED",
                "console_audio_feedback_string": "Node verified"
            }}
        }},
        "worldview_track_matrices": {{
            "comparative_insight": "Provide a powerful 1-sentence analytical perspective showing absolute structural design or logical order constants matching this day's exact story theme.",
            "biblical_alignment": "Provide an explicit, highly relevant scriptural text quote and chapter verse that aligns perfectly with this specific day's structural or logical mechanic."
        }},
        "anti_repetition_remediation_branch": {{
            "remediation_threshold_score": 85,
            "remediation_body": "Completely rewrite the lesson concept using an entirely alternative, fresh real-world story analogy to break down stuck checkpoints.",
            "remediation_assignment": "Provide an alternative interactive task description matching the fresh remediation story.",
            "remediation_assessment": "An alternative short check-out verification question string."
        }}
    }}
    """

def run_mass_vault_generation(start_day=2, end_day=3):
    if not API_KEY:
        print("❌ ERROR: The environment variable 'OPENAI_API_KEY' is missing on this machine.")
        return
        
    print("========================================================================")
    print("🤖 LAUNCHING MULTI-GRADE GENERATIVE VISUAL STORY INGESTION ENGINE")
    print(f"Generating exactly {end_day - start_day + 1} days per subject across all grade brackets...")
    print("========================================================================")
    
    for group, grades in GROUPS_MAPPING.items():
        for grade in grades:
            for subject in SUBJECTS:
                for day_num in range(start_day, end_day + 1):
                    
                    unit = "unit_1_foundations"
                    folder_path = os.path.join(DATABASE_ROOT, group, grade, subject, unit)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    target_file = os.path.join(folder_path, f"day_{day_num}.json")
                    
                    print(f"🎨 Illustrating SKE Story Node: [{grade.upper()}] -> [{subject.upper()}] -> Day {day_num}")
                    prompt = build_prompt_blueprint(group, grade, subject, unit, day_num)
                    raw_json = call_openai_ske_model(prompt)
                    
                    if raw_json:
                        try:
                            parsed_data = json.loads(raw_json)
                            with open(target_file, 'w', encoding='utf-8') as f:
                                json.dump(parsed_data, f, indent=4, ensure_ascii=False)
                            print(f"   ✨ Day {day_num} Story Node Written Successfully.")
                        except Exception as parse_error:
                            print(f"   ❌ Formatting anomaly, skipping node: {str(parse_error)}")
                            
                    time.sleep(1.2) # Steady pipeline cadence control

if __name__ == "__main__":
    # CONSTRAINT LOCKED: Loops exactly 2 unique files (Day 2 and Day 3) for all grade brackets and subjects
    run_mass_vault_generation(start_day=2, end_day=3)
