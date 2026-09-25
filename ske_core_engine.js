let audioClickCount = 0; 
let activeCrayonColor = "#2ECC71";
let coloredZonesTrackingSet = new Set();
let consoleSuccessStringData = "⚡ CIRCUIT STATUS VERIFIES NODE ACTIVE";
let consoleAudioFeedbackString = "Circuit status verifies node active.";
let targetClicksToUnlock = 3;

const PORTAL_GRADES_MAP = {
    "k5": ["gk", "g1", "g2", "g3", "g4", "g5"],
    "68": ["g6", "g7", "g8"],
    "912": ["g9", "g10", "g11", "g12"]
};

function enforceWorkspaceLockState() {
    audioClickCount = 0;
    coloredZonesTrackingSet.clear(); 
    const shield = document.getElementById("lockShieldWrapper");
    const notice = document.getElementById("audioLockNoticeBox");
    const statusLine = document.getElementById("circuitStatusTextLine");
    const pNodeA = document.getElementById("premiseNodeA");
    const pNodeB = document.getElementById("premiseNodeB");
    
    if (document.getElementById("middleSchoolExpressionBox")) document.getElementById("middleSchoolExpressionBox").value = "";
    if (statusLine) { statusLine.style.color = "#64748B"; statusLine.innerText = "Circuit Logic Status: Awaiting S-K-E validation parameters..."; }
    if (pNodeA) { pNodeA.style.borderColor = "#475569"; pNodeA.style.color = "#64748B"; pNodeA.style.backgroundColor = "#1E293B"; pNodeA.innerText = "[Premise A Node]"; }
    if (pNodeB) { pNodeB.style.borderColor = "#475569"; pNodeB.style.color = "#64748B"; pNodeB.style.backgroundColor = "#1E293B"; pNodeB.innerText = "[Premise B Node]"; }
    if (shield) shield.classList.add("workspace-locked");
    if (notice) {
        notice.style.backgroundColor = "#FEF2F2"; notice.style.borderColor = "#FCA5A5"; notice.style.color = "#EF4444";
        notice.innerHTML = "⚠️ ATTENTION: You must click the 'Read Out Loud' button TWICE before this worksheet unlocks.";
    }
}

function adaptPortalStyleBrackets() {
    const group = document.getElementById("portalGroupSelect").value;
    const subGradeSelector = document.getElementById("gradePrefixSelect");
    if ('speechSynthesis' in window) { window.speechSynthesis.cancel(); }

    subGradeSelector.innerHTML = "";
    PORTAL_GRADES_MAP[group].forEach((g, idx) => {
        subGradeSelector.innerHTML += `<option value="${g}" ${idx === 0 ? "selected" : ""}>Grade ${g.toUpperCase()}</option>`;
    });

    const elView = document.getElementById("elementaryWorkspaceView");
    const msView = document.getElementById("middleSchoolWorkspaceView");
    const hsView = document.getElementById("highSchoolWorkspaceView");
    const consolePanel = document.getElementById("nativeComputationalCircuitConsole");

    if (group === "k5") {
        document.documentElement.style.setProperty('--bar-gradient', 'linear-gradient(135deg, #E96B8B, #F9A86C)');
        elView.style.display = "block"; msView.style.display = "none"; hsView.style.display = "none";
    } else if (group === "68") {
        document.documentElement.style.setProperty('--bar-gradient', 'linear-gradient(135deg, #2563EB, #1D4ED8)');
        elView.style.display = "none"; msView.style.display = "block"; hsView.style.display = "none";
    } else {
        document.documentElement.style.setProperty('--bar-gradient', 'linear-gradient(135deg, #0F172A, #1E293B)');
        elView.style.display = "none"; msView.style.display = "none"; hsView.style.display = "block";
    }
    if (consolePanel) consolePanel.style.display = "block";
    enforceWorkspaceLockState();
    loadLiveDatabaseFile();
}

function loadLiveDatabaseFile() {
    const group = document.getElementById("portalGroupSelect").value;
    const grade = document.getElementById("gradePrefixSelect").value;
    const subject = document.getElementById("subjectTrackSelect").value;
    const day = parseInt(document.getElementById("daySelect").value) || 1;

    let unit = "unit_1_foundations";
    if (day > 45 && day <= 90) unit = "unit_2_shapes_spaces";
    else if (day > 90 && day <= 135) unit = "unit_3_weather_seasons";
    else if (day > 135) unit = "unit_4_counting_base";

    fetch(`pure_curriculum_vault/${group}/${grade}/${subject}/${unit}/day_${day}.json`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("lessonTitleLabel").innerText = data.lesson_title || `Day ${day} Lesson`;
            let displayTarget = (group === "k5") ? document.getElementById("elProseBodyContainer") : (group === "68") ? document.getElementById("msProseBodyContainer") : document.getElementById("hsProseBodyContainer");
            
            if (displayTarget) displayTarget.innerHTML = (data.lesson_body || "").replace(/###/g, "").replace(/\*\*/g, "");
            document.getElementById("assignmentDirectionsLabel").innerHTML = `🎯 <strong>Instructions:</strong> ${data.interactive_assignment || 'Complete goals.'}`;
            document.getElementById("lessonGuideContent").innerHTML = `📄 <strong>Summary:</strong> ${data.daily_assessment || 'Verify check.'}`;
            
            if (data.worldview_track_matrices) {
                document.getElementById("comparativeContextLabel").innerText = data.worldview_track_matrices.comparative_insight || "";
                document.getElementById("biblicalAlignmentLabel").innerText = data.worldview_track_matrices.biblical_alignment || "";
            }

            const canvasStage = document.getElementById("dynamicVectorStageNode");
            if (canvasStage && data.frontend_rendering_blueprint && data.frontend_rendering_blueprint.vector_shapes_layout) {
                canvasStage.innerHTML = "";
                targetClicksToUnlock = data.frontend_rendering_blueprint.total_required_clicks_to_unlock || 3;
                document.getElementById("chameleonCanvasStage").style.backgroundColor = data.frontend_rendering_blueprint.canvas_background_color || "#F1F5F9";

                data.frontend_rendering_blueprint.vector_shapes_layout.forEach(shape => {
                    let newEl = document.createElementNS("http://w3.org", shape.svg_type || "path");
                    newEl.setAttribute("id", shape.element_id);
                    newEl.setAttribute("fill", "#E2E8F0");
                    newEl.setAttribute("stroke", "#94A3B8");
                    newEl.setAttribute("stroke-width", "2");
                    newEl.setAttribute("style", "cursor: pointer; transition: fill 0.2s;");
                    if (shape.svg_path_data) newEl.setAttribute("d", shape.svg_path_data);
                    canvasStage.appendChild(newEl);
                });

                const layouts = data.frontend_rendering_blueprint.vector_shapes_layout;
                if (layouts && layouts[0] && document.getElementById("lblZone1")) document.getElementById("lblZone1").innerText = layouts[0].label_overlay_text;
                if (layouts && layouts[1] && document.getElementById("lblZone2")) document.getElementById("lblZone2").innerText = layouts[1].label_overlay_text;
                if (layouts && layouts[2] && document.getElementById("lblZone3")) document.getElementById("lblZone3").innerText = layouts[2].label_overlay_text;
            }

            if (data.frontend_rendering_blueprint && data.frontend_rendering_blueprint.computational_console_parameters) {
                const params = data.frontend_rendering_blueprint.computational_console_parameters;
                if (params.premise_a_label) document.getElementById("premiseNodeA").innerText = `[${params.premise_a_label}]`;
                if (params.premise_b_label) document.getElementById("premiseNodeB").innerText = `[${params.premise_b_label}]`;
                consoleSuccessStringData = params.console_success_message || "⚡ NODE ACTIVE";
                consoleAudioFeedbackString = params.console_audio_feedback_string || "Verified";
                if (params.console_objective_label) document.getElementById("consoleHeaderObjective").innerText = `💻 OBJECTIVE: ${params.console_objective_label}`;
            }
        }).catch(err => console.log("Missing path file.", err.message));
}

function colorWorksheetSegment(targetNode) {
    if (targetNode && (targetNode.id === 'canvasBgZone' || targetNode.id === 'canvasOvalZone' || targetNode.id === 'canvasCircleZone')) {
        targetNode.setAttribute('fill', activeCrayonColor);
        coloredZonesTrackingSet.add(targetNode.id);
        const statusLine = document.getElementById("circuitStatusTextLine");
        if (coloredZonesTrackingSet.size < targetClicksToUnlock) {
            if (statusLine) statusLine.innerHTML = `⚡ EVALUATION ACTIVE: [${coloredZonesTrackingSet.size} of ${targetClicksToUnlock} mapped]`;
        } else {
            triggerTerminalSuccessGate();
        }
    }
}

function evaluateMiddleSchoolAnswer(val) { if (val.trim().length > 0) triggerTerminalSuccessGate(); }
function evaluateHighSchoolAnswer(val) { if (val.trim().length > 5) triggerTerminalSuccessGate(); }

function triggerTerminalSuccessGate() {
    const statusLine = document.getElementById("circuitStatusTextLine");
    const pNodeA = document.getElementById("premiseNodeA");
    const pNodeB = document.getElementById("premiseNodeB");
    if (pNodeA && pNodeB && statusLine) {
        pNodeA.style.borderColor = "#10B981"; pNodeA.style.color = "#10B981"; pNodeA.style.backgroundColor = "rgba(16, 185, 129, 0.15)";
        pNodeB.style.borderColor = "#A855F7"; pNodeB.style.color = "#A855F7"; pNodeB.style.backgroundColor = "rgba(168, 85, 247, 0.15)";
        statusLine.style.color = "#38BDF8"; statusLine.style.fontWeight = "bold";
        statusLine.innerHTML = consoleSuccessStringData;
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const utter = new SpeechSynthesisUtterance(consoleAudioFeedbackString);
            utter.rate = 0.95; window.speechSynthesis.speak(utter);
        }
    }
}

function triggerVoiceReader() {
    if ('speechSynthesis' in window) { window.speechSynthesis.cancel(); } else { return; }
let stringData = (audioClickCount === 0) ? document.getElementById('lessonGuideContent').innerText : document.getElementById('assignmentDirectionsLabel').innerText;const shield = document.getElementById("lockShieldWrapper");const notice = document.getElementById("audioLockNoticeBox");stringData = stringData.replace(/📄/g, "").replace(/Summary:/gi, "").replace(/Instructions:/gi, "").replace(/🎯/g, "").replace(/⚡/g, "").trim();if (audioClickCount === 0) {audioClickCount = 1;if (notice) { notice.style.backgroundColor = "#FEF3C7"; notice.style.borderColor = "#FCD34D"; notice.style.color = "#D97706"; notice.innerHTML = "⚡ STEP 1 COMPLETE. Click once more to unlock!"; }} else {audioClickCount = 2;if (shield) shield.classList.remove("workspace-locked");if (notice) { notice.style.backgroundColor = "#D1FAE5"; notice.style.borderColor = "#A7F3D0"; notice.style.color = "#059669"; notice.innerHTML = "✅ WORKSHEET UNLOCKED."; }}const utter = new SpeechSynthesisUtterance(stringData);utter.rate = 0.95; window.speechSynthesis.speak(utter);}function pickCrayonColor(el, hex) { activeCrayonColor = hex; document.querySelectorAll('.crayon-option').forEach(c => c.style.borderColor='transparent'); el.style.borderColor='#1E293B'; }function initializeGlobal180DayTimeline() {const daySelect = document.getElementById("daySelect");if (!daySelect) return;daySelect.innerHTML = "";for (let d = 1; d <= 180; d++) { daySelect.innerHTML += <option value="${d}">🗓️ Course Day ${d}</option>; }adaptPortalStyleBrackets();}window.onload = initializeGlobal180DayTimeline;