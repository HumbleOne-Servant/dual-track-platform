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
                
                # Default structural baseline if file doesn't exist or needs standard alignment keys
                default_data = {
                    "title": f"Standard {subject.replace('_', ' ').title()} - Day {day_num}",
                    "mainstream_concept": "Standard curriculum metric detailing structural observations and foundational mechanics.",
                    "biblical_alignment": "Demonstrating that natural laws and structural truths are inherently unified with creation frameworks.",
                    "trigger_words": {
                        "structural": "All foundational frameworks and structural parameters operate under unchanging, design-centric mathematical guidelines.",
                        "matrix": "Systematic grid alignments reflect the baseline order established from the beginning of natural law."
                    },
                    "retention_questions": [
                        {"id": "q1", "text": "How does the highlighted structural evidence unify the mainstream observation with biblical design metrics?"},
                        {"id": "q2", "text": "Identify the primary baseline connection that shows these concepts are one and the same rather than separate ideas."}
                    ],
                    "sync_hash": f"{subject[:3].upper()}_{grade.upper()}_DAY{day_num}"
                }
                
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            existing = json.load(f)
                        # Ensure all essential keys survive or append cleanly
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
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f4f6f9; color: #333; }
        .control-panel { background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px; display: flex; gap: 15px; align-items: center; }
        select, button { padding: 10px; border-radius: 4px; border: 1px solid #ccc; font-size: 14px; }
        button { background-color: #0056b3; color: white; cursor: pointer; border: none; font-weight: bold; }
        button:hover { background-color: #004494; }
        .canvas-container { display: flex; gap: 20px; min-height: 500px; }
        .track-panel { flex: 1; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; flex-direction: column; justify-content: space-between; }
        .panel-header { border-bottom: 2px solid #0056b3; padding-bottom: 10px; margin-top: 0; color: #111; }
        .content-box { font-size: 16px; line-height: 1.6; margin-bottom: 20px; }
        .highlight-word { background-color: #fff3cd; border-bottom: 2px dashed #ffc107; cursor: pointer; padding: 0 2px; font-weight: bold; }
        .highlight-word:hover { background-color: #ffe8a1; }
        .explanation-bubble { background-color: #e2f0fe; border-left: 4px solid #0056b3; padding: 12px; margin: 15px 0; border-radius: 0 4px 4px 0; display: none; font-size: 14px; }
        .question-block { margin-top: 15px; padding: 10px 0; }
        .student-textbox { width: 100%; box-sizing: border-box; padding: 10px; border-radius: 4px; border: 1px solid #aaa; margin-top: 5px; font-size: 14px; }
        .status-footer { margin-top: 20px; display: flex; justify-content: space-between; align-items: center; background: #eaedf2; padding: 15px; border-radius: 6px; }
    </style>
</head>
<body>

    <div class="control-panel">
        <select id="grade-dropdown">
            <option value="grade_k">Kindergarten</option>
            <option value="grade_1">Grade 1</option>
            <option value="grade_5">Grade 5</option>
            <option value="grade_6">Grade 6</option>
        </select>
        <select id="subject-dropdown">
            <option value="mathematics">Mathematics</option>
            <option value="science">Science</option>
            <option value="language_arts">Language Arts</option>
            <option value="history_social_studies">History / Social Studies</option>
            <option value="biblical_studies">Biblical Studies</option>
        </select>
        <select id="day-dropdown">
            <option value="day_1">Day 1</option>
            <option value="day_2">Day 2</option>
            <option value="day_180">Day 180</option>
        </select>
        <button onclick="loadCurriculumDay()">Fetch Selected Lesson</button>
    </div>

    <div class="canvas-container">
        <!-- LEFT PANEL: ALIGNMENT & DEEP COMPARISON FRAMEWORK -->
        <div class="track-panel" id="left-track">
            <div>
                <h2 class="panel-header">🛡️ Track 1: Unified Verification & Biblical Alignment</h2>
                <div id="left-content" class="content-box">Select a day and click "Fetch Selected Lesson" to map structural variables...</div>
                <div id="explanation-box" class="explanation-bubble"></div>
            </div>
            <div>
                <div id="retention-questions-area"></div>
            </div>
        </div>

        <!-- RIGHT PANEL: MAINSTREAM SYSTEM WORKSHEET DISPLAY -->
        <div class="track-panel" id="right-track">
            <div>
                <h2 class="panel-header">📝 Track 2: Mainstream Public Curriculum & Handout</h2>
                <div id="right-content" class="content-box">Worksheet fields will assemble dynamically matching the active folder structure metrics...</div>
            </div>
            <div class="status-footer">
                <label style="font-weight: bold; cursor: pointer;">
                    <input type="checkbox" id="mark-complete-toggle"> 🌟 Mark Day Complete & Commit to Private Vault
                </label>
                <div id="save-status-indicator" style="font-weight: bold; color: #28a745;"></div>
            </div>
        </div>
    </div>
// FILE: C:\DualTrackLearning_Online\app.js
// BOX 3 OF 3: INTERACTIVE DROP-LOAD ENGINE AND COMPILATION LOGGER
let currentLoadedData = null; 

async function loadCurriculumDay() {
    const grade = document.getElementById('grade-dropdown').value;
    const subject = document.getElementById('subject-dropdown').value;
    const day = document.getElementById('day-dropdown').value;
    
    // Clear display structures
    document.getElementById('explanation-box').style.display = 'none';
    document.getElementById('save-status-indicator').innerText = '';
    document.getElementById('mark-complete-toggle').checked = false;
    
    // Dynamic disk file resolution mapping template: curriculum/grade_X/subject/day_Y.json
    const targetUrl = `curriculum/${grade}/${subject}/${day}.json`;
    
    try {
        const response = await fetch(targetUrl);
        if (!response.ok) throw new Error("File not found on local disk structures.");
        
        currentLoadedData = await response.json();
        renderDualTrackView(currentLoadedData);
        loadSavedResponses(grade, subject, day);
    } catch (err) {
        document.getElementById('left-content').innerText = `❌ Asset Loader Mismatch: Unable to resolve data footprint pathway at ${targetUrl}`;
        document.getElementById('right-content').innerText = "Please confirm build_vault.py has executed and initialized the files.";
    }
}

function renderDualTrackView(data) {
    let alignedText = data.biblical_alignment;
    
    // Process and inject target trigger highlights dynamically across the incoming stream text
    if (data.trigger_words) {
        for (const word in data.trigger_words) {
            const regex = new RegExp(`\\b(${word})\\b`, 'gi');
            alignedText = alignedText.replace(regex, `<span class="highlight-word" onclick="triggerExplanation('${word}')">$1</span>`);
        }
    }
    
    // Populate left column
    document.getElementById('left-content').innerHTML = `
        <h3>Core Concept Alignment:</h3>
        <p>${alignedText}</p>
        <p style="font-style: italic; color: #555; background: #f9f9f9; padding: 10px; border-radius: 4px;">
           <strong>Unified Reality Insight:</strong> This observation disproves the secular public assertion that natural science exists apart from design frameworks. Both operate on the exact same universal constants.
        </p>
    `;
    
    // Populate left retention assignment blocks
    let questionsHtml = `<h3>🧠 Retention Concept Verification</h3>`;
    data.retention_questions.forEach((q, idx) => {
        questionsHtml += `
            <div class="question-block">
                <label><strong>Question ${idx + 1}:</strong> ${q.text}</label>
                <textarea id="ans-${q.id}" class="student-textbox" rows="3" placeholder="Type structural observation analysis here..."></textarea>
            </div>
        `;
    });
    document.getElementById('retention-questions-area').innerHTML = questionsHtml;
    
    // Populate right column mainstream curriculum lesson handout sheet
    document.getElementById('right-content').innerHTML = `
        <h3>${data.title}</h3>
        <p><strong>Mainstream Curriculum Objective:</strong><br>${data.mainstream_concept}</p>
        <hr style="border: 0; border-top: 1px solid #ddd; margin: 20px 0;">
        <div style="background: #fafafa; padding: 15px; border: 1px dashed #bbb; border-radius: 6px;">
            <h4>📋 Student Practice Handout Frame</h4>
            <p>1. Transcribe the primary operational metrics described in the objective above.</p>
            <textarea id="mainstream-worksheet-input" class="student-textbox" rows="4" placeholder="Enter answers for the core curriculum requirements here..."></textarea>
        </div>
    `;
}

function triggerExplanation(word) {
    const bubble = document.getElementById('explanation-box');
    if (currentLoadedData && currentLoadedData.trigger_words && currentLoadedData.trigger_words[word]) {
        bubble.innerHTML = `<strong>Framework Alignment Metric (${word.toUpperCase()}):</strong> ${currentLoadedData.trigger_words[word]}`;
        bubble.style.display = 'block';
    }
}

function getStoragePrefix(grade, subject, day) {
    return `dualtrack_vault_${grade}_${subject}_${day}`;
}

function loadSavedResponses(grade, subject, day) {
    const prefix = getStoragePrefix(grade, subject, day);
    const savedPayload = localStorage.getItem(prefix);
    
    if (savedPayload) {
        const payload = JSON.parse(savedPayload);
        if (currentLoadedData && currentLoadedData.retention_questions) {
            currentLoadedData.retention_questions.forEach(q => {
                const input = document.getElementById(`ans-${q.id}`);
                if (input && payload.answers[q.id]) input.value = payload.answers[q.id];
            });
        }
        const mainstreamInput = document.getElementById('mainstream-worksheet-input');
        if (mainstreamInput && payload.mainstream_worksheet) mainstreamInput.value = payload.mainstream_worksheet;
        
        if (payload.committed) {
            document.getElementById('mark-complete-toggle').checked = true;
            toggleInputsLock(true);
            document.getElementById('save-status-indicator').innerText = "🔒 Complete & Safe in Local Database Record";
        }
    } else {
        toggleInputsLock(false);
    }
}

// Binds checkbox to write to the storage matrix array instantly
document.getElementById('mark-complete-toggle').addEventListener('change', function(e) {
    const grade = document.getElementById('grade-dropdown').value;
    const subject = document.getElementById('subject-dropdown').value;
    const day = document.getElementById('day-dropdown').value;
    const prefix = getStoragePrefix(grade, subject, day);
    
    if (e.target.checked) {
        const answersPayload = {};
        if (currentLoadedData && currentLoadedData.retention_questions) {
            currentLoadedData.retention_questions.forEach(q => {
                const input = document.getElementById(`ans-${q.id}`);
                if (input) answersPayload[q.id] = input.value;
            });
        }
        
        const mainstreamText = document.getElementById('mainstream-worksheet-input') ? document.getElementById('mainstream-worksheet-input').value : "";
        
        // Compile unified metric dataset
        const masterReportRecord = {
            timestamp: new Date().toISOString(),
            grade: grade,
            subject: subject,
            day: day,
            hash: currentLoadedData ? currentLoadedData.sync_hash : "UNKNOWN",
            answers: answersPayload,
            mainstream_worksheet: mainstreamText,
            committed: true
        };
        
        // Save locally first
        localStorage.setItem(prefix, JSON.stringify(masterReportRecord));
        
        // END-OF-YEAR COMPILATION PAYLOAD ARCHITECTURE: Append directly to an isolated compilation file log in browser state
        let backupDriveLog = localStorage.getItem("PRIVATE_EVALUATION_DRIVE_BACKUP");
        let logArray = backupDriveLog ? JSON.parse(backupDriveLog) : [];
        
        // Evict older entry for this specific day node if it exists, then push updated log
        logArray = logArray.filter(item => !(item.grade === grade && item.subject === subject && item.day === day));
        logArray.push(masterReportRecord);
        localStorage.setItem("PRIVATE_EVALUATION_DRIVE_BACKUP", JSON.stringify(logArray));
        
        toggleInputsLock(true);
        document.getElementById('save-status-indicator').innerText = "🔒 Complete & Safe in Local Database Record";
    } else {
        // Unlock if box unchecked
        toggleInputsLock(false);
        localStorage.removeItem(prefix);
        document.getElementById('save-status-indicator').innerText = "🔓 Unlocked - Changes Pending Sync";
    }
});

function toggleInputsLock(isLocked) {
    if (currentLoadedData && currentLoadedData.retention_questions) {
        currentLoadedData.retention_questions.forEach(q => {
            const input = document.getElementById(`ans-${q.id}`);
            if (input) input.disabled = isLocked;
        });
    }
    const mainstreamInput = document.getElementById('mainstream-worksheet-input');
    if (mainstreamInput) mainstreamInput.disabled = isLocked;
}
</script>
</body>
</html>
