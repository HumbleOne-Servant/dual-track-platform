import os
import json

# Setup local folder architecture targets
VAULT_DIR = "curriculum"
GRADES = ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
SUBJECTS = ["mathematics", "science", "language_arts", "history_social_studies", "biblical_studies"]

print("⚡ Starting Upgraded Progressive Curriculum Content Engine...")

def get_lesson_content(grade, subject, day_num):
    # FIXED RULE TIER BOUNDARIES (K-5 Elementary, 6-8 Middle, 9-12 High School)
    if grade in ["K", "1", "2", "3", "4", "5"]:
        tier = "Elementary"
    elif grade in ["6", "7", "8"]:
        tier = "Middle"
    else:
        tier = "High"

    # Cyclical curriculum modules that shift vocabulary and topics dynamically per day
    math_topics = ["Operations", "Fractions", "Algebraic Geometry", "Ratios", "Data Distributions", "Calculus Limits", "Linear Systems", "Coordinate Scaling"]
    sci_topics = ["Matter Properties", "Eco Energy", "Genetics Map", "Kinematics", "Chemical Bonds", "Thermodynamics", "Tectonic Plates", "Cell Mitosis"]
    ela_topics = ["Phonics Grammar", "Textual Theme", "Rhetorical Style", "Narrative Depth", "Syntax Blending", "Analytical Research", "Poetic Form"]
    hist_topics = ["Civic Mapping", "River Valleys", "Macroeconomics", "Industrial Growth", "Global Treaties", "Feudal Structures", "Colonization"]
    bib_topics = ["Faith Parables", "Near East Topography", "Hermeneutics Logic", "Covenant Law", "Epistolary Context", "Prophetic Metaphor"]

    if subject == "mathematics":
        topic = math_topics[day_num % len(math_topics)]
        calc_level = (day_num // 20) + 1
        title = f"{tier} {topic} Analysis: Level {calc_level}"
        desc = f"Investigating the foundational properties of {topic.lower()} framework lines down to level milestone block {day_num}."
        concept = "Mathematical progression coordinates balance numerical inputs across multi-tier matrices."
        bullets = [
            f"Execute operational calculations isolating variable units under block parameter {day_num * 3}.",
            "Map the scalar values across a Cartesian number line boundary system cleanly.",
            f"Formulate deductive summary balances evaluating structural precision limits for milestone {day_num}."
        ]
        ref = f"Job 38:{(day_num % 40) + 1} — Who hath laid the measures thereof, if thou knowest?"
        hash_pre = "MATH_"
    elif subject == "science":
        topic = sci_topics[day_num % len(sci_topics)]
        calc_phase = (day_num // 25) + 1
        title = f"{tier} {topic} Explorations: Phase {calc_phase}"
        desc = f"Analyzing molecular and environmental properties governing {topic.lower()} systems on calendar node {day_num}."
        concept = "Natural physical properties transition predictably while preserving core structural balances."
        bullets = [
            f"Isolate organic variables inside the system matrix to observe structural modifications at node {day_num}.",
            "Quantify chemical and heat energy outputs matching thermodynamic milestone rules.",
            "Formulate complete experimental balance sheets logging reaction vector changes."
        ]
        ref = f"Genesis 1:{(day_num % 31) + 1} — And God made the firmament, and divided the waters."
        hash_pre = "SCI_"
    elif subject == "language_arts":
        topic = ela_topics[day_num % len(ela_topics)]
        calc_stage = (day_num // 30) + 1
        title = f"{tier} {topic} Masterclass: Stage {calc_stage}"
        desc = f"Deconstructing complex text configurations and structural syntax patterns inside chapter unit {day_num}."
        concept = "Sophisticated compositional frameworks utilize structural organization lines to deliver cohesive parameters."
        bullets = [
            f"Identify supporting thesis statements across targeted informational reading inputs on day {day_num}.",
            "Deconstruct rhetorical framing models to isolate conceptual argumentative lines.",
            "Draft persuasive analytical commentary integrating advanced sentence style transitions."
        ]
        ref = f"Proverbs 25:{(day_num % 25) + 1} — A word fitly spoken is like apples of gold."
        hash_pre = "ELA_"
    elif subject == "history_social_studies":
        topic = hist_topics[day_num % len(hist_topics)]
        calc_epoch = (day_num // 15) + 1
        title = f"{tier} World Legacy: Epoch {calc_epoch} ({topic})"
        desc = f"Reviewing critical geopolitical transformations and macroeconomic infrastructure adjustments during era milestone {day_num}."
        concept = "Historical community structural profiles develop in direct alignment with natural resource routes."
        bullets = [
            f"Trace structural adjustments in municipal legislative guidelines during developmental phase {day_num}.",
            "Map industrial and monetary trade distribution networks across regional border segments.",
            "Evaluate individual leadership initiatives balancing public safety requirements."
        ]
        ref = f"Romans 13:{(day_num % 14) + 1} — Render therefore to all their dues: tribute to whom tribute is due."
        hash_pre = "HIST_"
    else:
        topic = bib_topics[day_num % len(bib_topics)]
        title = f"{tier} Biblical Theology Contextual Study: Lesson {day_num}"
        desc = f"Deconstructing chronological text translations and covenantal tracking logic maps for unit segment {day_num}."
        concept = "Scriptural hermeneutics demands rigorous syntax verification matching original historical frameworks."
        bullets = [
            f"Examine original semantic root metrics to isolate contextual ideological parameters for section {day_num}.",
            "Cross-reference geographic and topological indicators across historical narrative charts.",
            "Apply systematic structural analysis rules to evaluate epistolary logic progression rows."
        ]
        ref = f"2 Timothy 2:{(day_num % 20) + 1} — Study to shew thyself approved unto God."
        hash_pre = "BIB_"

    sync_hash = f"{hash_pre}{day_num:03d}G{grade.upper()}WN8"
    return { "title": title, "description": desc, "concept": concept, "bullets": bullets, "cross_reference": ref, "sync_hash": sync_hash }

# Loop and build files on local disk
count = 0
for grade in GRADES:
    for subject in SUBJECTS:
        folder_path = os.path.join(VAULT_DIR, f"grade_{grade.lower()}", subject)
        os.makedirs(folder_path, exist_ok=True)
        
        for day_num in range(1, 181):
            file_name = f"day_{day_num}.json"
            full_file_path = os.path.join(folder_path, file_name)
            
            lesson_payload = get_lesson_content(grade, subject, day_num)
            
            with open(full_file_path, "w", encoding="utf-8") as json_file:
                json.dump(lesson_payload, json_file, indent=2, ensure_ascii=False)
            
            count += 1

print(f"🎉 Success! Generated {count} dynamic, grade-tiered curriculum files inside your dedicated storage vault.")
