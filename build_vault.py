# FILE: C:\DualTrackLearning_Online\build_vault.py
# BOX 1 OF 3: CORE BACKEND DATA ENGINE STRUCTURING FACTORY
import os
import json

def build_or_upgrade_vault():
    base_dir = r"C:\DualTrackLearning_Online\curriculum"
    grades = [f"grade_{i}" for i in range(1, 13)] + ["grade_k"]
    subjects = ["mathematics", "science", "language_arts", "history_social_studies", "biblical_studies"]
    
    print("⏳ Initialization started: Structuring synchronized dual-track data architecture...")
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        
    for grade in grades:
        for subject in subjects:
            folder_path = os.path.join(base_dir, grade, subject)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                
            for day_num in range(1, 181):
                file_name = f"day_{day_num}.json"
                file_path = os.path.join(folder_path, file_name)
                
                # Public school data sits primarily on the left, with alignment tags feeding the interface
                default_data = {
                    "title": f"Public School {subject.replace('_', ' ').title()} Lesson - Day {day_num}",
                    "public_core_concept": "This public school unit introduces standard coordinate tracking, spatial measurement, and the foundational parameters governing local structural matrix formulas.",
                    "public_worksheet_instructions": "Complete the calculation segments. Map out the standard values below and run your verification algorithms.",
                    "alignment_triggers": {
                        "matrix": {
                            "biblical_truth": "Colossians 1:17 — He is before all things, and by him all things hold together. The matrix grid reflects the universal order holding creation intact.",
                            "alternative_framework": "Mainstream models treat the grid as an empty secular coordinate system. Our alternative framework proves the grid is a physical, designed lattice constructed on permanent divine laws.",
                            "game_word": "HOLD TOGETHER"
                        },
                        "parameters": {
                            "biblical_truth": "Job 38:10 — When I broke up for it my decreed place, and set bars and doors. All natural systems operate inside strict, design-centric boundaries.",
                            "alternative_framework": "Secular science claims parameters evolved randomly. The true model shows that breaking a fundamental parameter collapses the mathematical integrity of the system.",
                            "game_word": "DECREED PLACE"
                        }
                    },
                    "retention_questions": [
                        {"id": "q1", "text": "What biblical principles are active inside the public school concept text highlighted on the left?"},
                        {"id": "q2", "text": "How does our alternative framework unify these mainstream school facts with universal design?"}
                    ],
                    "sync_hash": f"{subject[:3].upper()}_{grade.upper()}_DAY{day_num}"
                }
                
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing = json.load(f)
                        for key in default_data:
                            if key not in existing:
                                existing[key] = default_data[key]
                        default_data = existing
                    except:
                        pass
                        
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(default_data, indent=2, f, ensure_ascii=False)

    print("✅ Success! All 11,700 curriculum nodes contain parallel framework targets.")

if __name__ == "__main__":
    build_or_upgrade_vault()
<!-- FILE: C:\DualTrackLearning_Online\index.html -->
<!-- BOX 2 OF 3: FRONTEND USER INTERFACE AND SCREEN CANVAS LAYOUT -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dual-Track Learning Platform</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f0f3f8; color: #222; }
        .control-panel { background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.08); margin-bottom: 20px; display: flex; gap: 15px; }
        select, button { padding: 10px; border-radius: 4px; border: 1px solid #bbb; font-size: 14px; }
        button { background-color: #0d6efd; color: white; cursor: pointer; border: none; font-weight: bold; }
        button:hover { background-color: #0b5ed7; }
        .canvas-container { display: flex; gap: 20px; min-height: 550px; }
        .track-panel { flex: 1; background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; }
        .panel-header { border-bottom: 3px solid #0d6efd; padding-bottom: 10px; margin-top: 0; color: #1e293b; }
        .public-lesson-box { background-color: #f8fafc; padding: 15px; border-radius: 6px; border-left: 4px solid #64748b; margin-bottom: 15px; }
        .highlight-trigger { background-color: #fde047; border-bottom: 2px dashed #eab308; cursor: pointer; padding: 0 4px; font-weight: bold; border-radius: 2px; }
        .highlight-trigger:hover { background-color: #fef08a; }
        
        /* Interactive Alignment Portal Box */
        .alignment-portal { background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%); border: 2px solid #3b82f6; padding: 20px; border-radius: 8px; margin-top: 20px; display: none; }
        .portal-section { margin-bottom: 12px; font-size: 15px; }
        .portal-title { font-weight: bold; color: #1e40af; margin-bottom: 3px; text-transform: uppercase; font-size: 12px; tracking: 1px; }
        
        /* Gamified Muscle-Memory Element */
        .game-box { background: #fff; border: 1px solid #bfdbfe; padding: 12px; border-radius: 6px; margin-top: 10px; display: flex; align-items: center; gap: 10px; }
        .game-input { padding: 6px; border: 2px solid #3b82f6; border-radius: 4px; outline: none; font-weight: bold; font-size: 14px; text-transform: uppercase; }
        .game-status { font-weight: bold; font-size: 14px; }
        
        .student-textbox { width: 100%; box-sizing: border-box; padding: 10px; border-radius: 4px; border: 1px solid #94a3b8; margin-top: 5px; font-size: 14px; }
        .status-footer { display: flex; justify-content: space-between; align-items: center; background: #e2e8f0; padding: 15px; border-radius: 6px; margin-top: 20px; }
    </style>
</head>
<body>

    <div class="control-panel">
        <select id="grade-dropdown"><option value="grade_5">Grade 5</option><option value="grade_6">Grade 6</option></select>
        <select id="subject-dropdown">
            <option value="mathematics">Mathematics</option>
            <option value="science">Science</option>
            <option value="language_arts">Language Arts</option>
            <option value="history_social_studies">History / Social Studies</option>
            <option value="biblical_studies">Biblical Studies</option>
        </select>
        <select id="day-dropdown"><option value="day_1">Day 1</option><option value="day_2">Day 2</option></select>
        <button onclick="loadCurriculumDay()">Open Selected Lesson</button>
    </div>

    <div class="canvas-container">
        <!-- LEFT PANEL: MAINSTREAM PUBLIC SCHOOL CURRICULUM & INTERACTIVE WORKSHEETS -->
        <div class="track-panel" id="left-track">
            <div>
                <h2 class="panel-header">🏫 Left Side: Public School Core Lesson & Handout</h2>
                <h3 id="lesson-title" style="margin-top:10px; color:#334155;"></h3>
                
                <div class="public-lesson-box">
                    <strong>📖 Core Concept Framework:</strong>
                    <p id="public-core-content">Select a grade and subject, then click open to build the interactive canvas channels...</p>
                </div>
                
                <div style="background: #fff; padding: 15px; border: 1px dashed #94a3b8; border-radius: 6px;">
                    <strong>📋 Public Curriculum Worksheet Generation Frame</strong>
                    <p id="public-worksheet-instructions" style="font-size:14px; color:#475569;"></p>
                    <textarea id="left-public-worksheet-input" class="student-textbox" rows="4" placeholder="Type answers matching standard school requirements here..."></textarea>
                </div>
            </div>
        </div>

        <!-- RIGHT PANEL: UNIFIED ALIGNMENT FRAMEWORK, GAMES & YEAR-END ARCHIVE LOGGER -->
        <div class="track-panel" id="right-track">
            <div>
                <h2 class="panel-header">🛡️ Right Side: Truth Alignment Portal & Game Check</h2>
                
                <div id="portal-instructions" style="color: #64748b; font-style: italic; text-align: center; margin-top: 40px;">
                    Click any yellow highlighted keyword on the left school panel to reveal the underlying biblical principles, alternative frameworks, and unlock muscle-memory tracking.
                </div>

                <!-- Hidden until triggered by keyword click -->
                <div id="alignment-portal-display" class="alignment-portal">
                    <h3 style="margin-top:0; color:#1d4ed8; border-bottom:1px solid #bfdbfe; padding-bottom:5px;">🔗 Dynamic Alignment Connection</h3>
                    
                    <div class="portal-section">
                        <div class="portal-title">✝️ Biblical Principle & Truth Comparison</div>
                        <div id="portal-bible-text"></div>
                    </div>
                    
                    <div class="portal-section">
                        <div class="portal-title">🔬 Uploaded Alternative Design Framework</div>
                        <div id="portal-alternative-text"></div>
                    </div>
                    
                    <div class="portal-section">
                        <div class="portal-title">🕹️ Muscle Memory Lock: Type the matching core truth phrase</div>
                        <div class="game-box">
                            <input type="text" id="game-typing-input" class="game-input" placeholder="Type target phrase...">
                            <span id="game-target-phrase" style="font-weight:bold; color:#475569; font-size:13px;"></span>
                            <span id="game-validation-status" class="game-status"></span>
                        </div>
                    </div>
                </div>

                <div id="retention-questions-block" style="margin-top:25px; display:none;">
                    <h3 style="color:#1e293b; margin-bottom:5px;">🧠 Retention Verification Answers</h3>
                    <div id="questions-container"></div>
                </div>
            </div>

            <div class="status-footer">
                <label style="font-weight: bold; cursor: pointer; font-size:14px;">
                    <input type="checkbox" id="mark-complete-toggle"> 🔒 Lock Responses & Save to Private Evaluation Drive
                </label>
                <div id="save-status-indicator" style="font-weight: bold; color: #16a34a; font-size:13px;"></div>
            </div>
        </div>
    </div>
// FILE: C:\DualTrackLearning_Online\app.js
// BOX 3 OF 3: INTERACTIVE DROP-LOAD ENGINE AND COMPILATION LOGGER
let activeLessonData = null;
let currentTargetGameWord = "";

async function loadCurriculumDay() {
    const grade = document.getElementById('grade-dropdown').value;
    const subject = document.getElementById('subject-dropdown').value;
    const day = document.getElementById('day-dropdown').value;
    
    // Reset window layout states
    document.getElementById('alignment-portal-display').style.display = 'none';
    document.getElementById('retention-questions-block').style.display = 'none';
    document.getElementById('portal-instructions').style.display = 'block';
    document.getElementById('save-status-indicator').innerText = '';
    document.getElementById('mark-complete-toggle').checked = false;
    document.getElementById('game-typing-input').value = "";
    document.getElementById('game-validation-status').innerText = "";
    
    const targetUrl = `curriculum/${grade}/${subject}/${day}.json`;
    
    try {
        const response = await fetch(targetUrl);
        if (!response.ok) throw new Error("File path mismatch.");
        
        activeLessonData = await response.json();
        renderPublicToBiblicalInterface(activeLessonData);
        loadSavedDatabaseMetrics(grade, subject, day);
    } catch (err) {
        document.getElementById('public-core-content').innerText = `❌ Pathway Mismatch: Unable to resolve file target at ${targetUrl}`;
    }
}

function renderPublicToBiblicalInterface(data) {
    document.getElementById('lesson-title').innerText = data.title;
    document.getElementById('public-worksheet-instructions').innerText = data.public_worksheet_instructions;
    
    let publicText = data.public_core_concept;
    
    // Parse left public text strings to inject highlighted interactive click words
    if (data.alignment_triggers) {
        for (const word in data.alignment_triggers) {
            const regex = new RegExp(`\\b(${word})\\b`, 'gi');
            publicText = publicText.replace(regex, `<span class="highlight-trigger" onclick="activateAlignmentPortal('${word}')">$1</span>`);
        }
    }
    document.getElementById('public-core-content').innerHTML = publicText;
    
    // Assemble right panel retention review text blocks
    let questionsHtml = "";
    data.retention_questions.forEach((q, index) => {
        questionsHtml += `
            <div style="margin-top:12px;">
                <label style="font-size:14px; font-weight:bold; color:#334155;">[Verification ${index+1}] ${q.text}</label>
                <textarea id="retention-ans-${q.id}" class="student-textbox" rows="2" placeholder="Type summary conclusions here..."></textarea>
            </div>
        `;
    });
    document.getElementById('questions-container').innerHTML = questionsHtml;
}

function activateAlignmentPortal(word) {
    if (!activeLessonData || !activeLessonData.alignment_triggers[word]) return;
    
    const triggerNode = activeLessonData.alignment_triggers[word];
    document.getElementById('portal-instructions').style.display = 'none';
    document.getElementById('alignment-portal-display').style.display = 'block';
    document.getElementById('retention-questions-block').style.display = 'block';
    
    document.getElementById('portal-bible-text').innerText = triggerNode.biblical_truth;
    document.getElementById('portal-alternative-text').innerText = triggerNode.alternative_framework;
    
    // Set up the muscle memory gamified typing challenge
    currentTargetGameWord = triggerNode.game_word.toUpperCase();
    document.getElementById('game-target-phrase').innerText = `(Type: "${currentTargetGameWord}")`;
    const inputField = document.getElementById('game-typing-input');
    inputField.value = "";
    inputField.focus();
    document.getElementById('game-validation-status').innerText = "⏳ Awaiting Match";
    document.getElementById('game-validation-status').style.color = "#a16207";
}

// Game check event tracking keyboard interactions for instant muscle memory success loop
document.getElementById('game-typing-input').addEventListener('input', function(e) {
    const value = e.target.value.toUpperCase();
    const statusLabel = document.getElementById('game-validation-status');
    
    if (value === currentTargetGameWord) {
        statusLabel.innerText = "🎯 MATCH LOCKED!";
        statusLabel.style.color = "#16a34a";
    } else {
        statusLabel.innerText = "⏳ Typing...";
        statusLabel.style.color = "#a16207";
    }
});

function getStorageRecordKey(grade, subject, day) {
    return `dualtrack_vault_${grade}_${subject}_${day}`;
}

function loadSavedDatabaseMetrics(grade, subject, day) {
    const key = getStorageRecordKey(grade, subject, day);
    const saved = localStorage.getItem(key);
    
    if (saved) {
        const record = JSON.parse(saved);
        const worksheetInput = document.getElementById('left-public-worksheet-input');
        if (worksheetInput && record.public_worksheet_text) worksheetInput.value = record.public_worksheet_text;
        
        if (activeLessonData && activeLessonData.retention_questions) {
            activeLessonData.retention_questions.forEach(q => {
                const textInput = document.getElementById(`retention-ans-${q.id}`);
                if (textInput && record.retention_answers[q.id]) textInput.value = record.retention_answers[q.id];
            });
        }
        
        if (record.is_finalized) {
            document.getElementById('mark-complete-toggle').checked = true;
            setLockState(true);
            document.getElementById('save-status-indicator').innerText = "🔒 Finalized & Logged to Year-End Private Drive File";
        }
    } else {
        setLockState(false);
    }
}

document.getElementById('mark-complete-toggle').addEventListener('change', function(e) {
    const grade = document.getElementById('grade-dropdown').value;
    const subject = document.getElementById('subject-dropdown').value;
    const day = document.getElementById('day-dropdown').value;
    const key = getStorageRecordKey(grade, subject, day);
    
    if (e.target.checked) {
        const retAnswers = {};
        if (activeLessonData && activeLessonData.retention_questions) {
            activeLessonData.retention_questions.forEach(q => {
                const el = document.getElementById(`retention-ans-${q.id}`);
                if (el) retAnswers[q.id] = el.value;
            });
        }
        
        const masterReportRecord = {
            timestamp: new Date().toISOString(),
            grade: grade,
            subject: subject,
            day: day,
            hash: activeLessonData ? activeLessonData.sync_hash : "EMPTY",
            public_worksheet_text: document.getElementById('left-public-worksheet-input').value,
            retention_answers: retAnswers,
            is_finalized: true
        };
        
        localStorage.setItem(key, JSON.stringify(masterReportRecord));
        
        // Year-end compiler append
        let archiveDrive = localStorage.getItem("PRIVATE_EVALUATION_DRIVE_BACKUP");
        let archiveList = archiveDrive ? JSON.parse(archiveDrive) : [];
        archiveList = archiveList.filter(item => !(item.grade === grade && item.subject === subject && item.day === day));
        archiveList.push(masterReportRecord);
        localStorage.setItem("PRIVATE_EVALUATION_DRIVE_BACKUP", JSON.stringify(archiveList));
        
        setLockState(true);
        document.getElementById('save-status-indicator').innerText = "🔒 Finalized & Logged to Year-End Private Drive File";
    } else {
        setLockState(false);
        localStorage.removeItem(key);
        document.getElementById('save-status-indicator').innerText = "🔓 Form Unlocked";
    }
});

function setLockState(lock) {
    const ws = document.getElementById('left-public-worksheet-input');
    if (ws) ws.disabled = lock;
    if (activeLessonData && activeLessonData.retention_questions) {
        activeLessonData.retention_questions.forEach(q => {
            const el = document.getElementById(`retention-ans-${q.id}`);
            if (el) el.disabled = lock;
        });
    }
}
