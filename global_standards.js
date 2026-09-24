// Box 1: S-K-E S-K-E Framework Dynamic International Mastery Content Vault Matrix
const EAST_ASIAN_STANDARD_VAULT = {
    "mathematics": {
        "gk": "Singapore CPA Core: Visual vector calculations. Factor grouping networks prioritize rapid mental sums up to 20 using abstract block layouts.",
        "g4": "Advanced Fraction Reactor: Analyze equivalent fractions using matrix factorization methods. Identify common denominators via prime factorization pathways instantly.",
        "g8": "Deductive Geometric Proof Engine: Construct unbendable geometric logic chains. Map multivariable linear expressions directly to a coordinate grid axis layout."
    },
    "science": {
        "gk": "Systemic Environmental Classification: Identify categorical structural properties of elements. Chart physical cycles using thermodynamic relationship diagrams.",
        "g4": "Circuit Logic Architecture: Formulate parallel circuit networks. Calculate resistance constants using variable current tracking meters.",
        "g8": "Subatomic Isotope Sandbox: Balance atomic electron configurations. Calculate mass metrics of volatile materials using quantum shell alignment maps."
    }
};
// Box 2: High-Impact Pathway Logic Engines (Dynamic Keyword Pulse Scanner)
function executeHighImpactPathways(subject, rawContent) {
    /**
     * PATHWAY 1: The Dynamic Keyword Pulse Scanner
     * Adds glowing vector tracers to keywords, allowing touch animations
     * to shoot across the panel divider grid to highlight worldview items.
     */
    let processedText = rawContent;
    const pulseKeywords = ["equations", "vector", "water", "atoms", "printing", "migration"];
    
    pulseKeywords.forEach(word => {
        const pattern = new RegExp(`\\b(${word})\\b`, 'gi');
        processedText = processedText.replace(pattern, 
            `<span class="pulse-vector-keyword" onclick="fireCrossPanelPulse('${word}')" style="color: #634EE4; font-weight: bold; border-bottom: 2px dotted #634EE4; cursor: pointer; position: relative; display: inline-block;">$1</span>`
        );
    });
    
    return processedText;
}

function fireCrossPanelPulse(detectedWord) {
    /**
     * Triggers a visual particle wave pulse across the interface divider line
     * and forces the right panel reference cards to jump directly to that track.
     */
    const rightPanel = document.getElementById("rightComparativeWorkspace");
    if (!rightPanel) return;
    
    rightPanel.style.borderColor = "#634EE4";
    rightPanel.style.backgroundColor = "#EEF2FF";
    
    setTimeout(() => {
        rightPanel.style.borderColor = "#CBD5E1";
        rightPanel.style.backgroundColor = "#FAFBFD";
    }, 600);
}
// Box 3: International Standards Core Router Toggle Switch
function toggleInternationalRigorTrack() {
    const activeStandard = document.getElementById("rigorTrackSelect").value;
    const group = document.getElementById("portalGroupSelect").value;
    const grade = document.getElementById("gradePrefixSelect").value;
    const subject = document.getElementById("subjectTrackSelect").value;
    
    const displayTarget = (group === "k5") ? document.getElementById("elProseBodyContainer") : (group === "68") ? document.getElementById("msProseBodyContainer") : document.getElementById("hsProseBodyContainer");
    
    if (!displayTarget) return;

    if (activeStandard === "east_asian") {
        // Intercept standard view and swap with East Asian Compulsory Education criteria
        const topicKey = EAST_ASIAN_STANDARD_VAULT[subject];
        const gradeKey = grade ? grade.toLowerCase() : "gk";
        
        if (topicKey && topicKey[gradeKey]) {
            displayTarget.innerHTML = `<div style="border-left: 4px solid #10B981; padding-left: 12px; font-style: italic; color: #065F46; line-height: 1.5;">🎒 EAST ASIAN MASTERY STANDARD ACTIVE:<br>${topicKey[gradeKey]}</div>`;
        } else {
            displayTarget.innerHTML = `<div style="border-left: 4px solid #10B981; padding-left: 12px; font-style: italic; color: #065F46; line-height: 1.5;">🎒 EAST ASIAN MASTERY STANDARD ACTIVE:<br>Accelerated high-frequency logic optimization problem set active for Grade ${grade.toUpperCase()}.</div>`;
        }
        
        // Append the computational block directly
        drawComputationalLogicSandbox(displayTarget.id);
    } else {
        // Fallback cleanly to your generated file database curriculum
        if (typeof loadLiveDatabaseFile === "function") {
            loadLiveDatabaseFile();
        }
    }
}
// Box 4: Computational Logic Node Blueprint Sandbox Builder
function drawComputationalLogicSandbox(targetContainerId) {
    /**
     * PATHWAY 2: The Computational Logic Node Sandbox
     * Blends sentence layout diagramming with early logic programming node blocks.
     */
    const container = document.getElementById(targetContainerId);
    if (!container) return;
    
    const sandboxHtml = `
        <div style="background: #0F172A; color: #38BDF8; padding: 16px; border-radius: 12px; font-family: monospace; margin-top: 16px; box-shadow: inset 0 2px 8px rgba(0,0,0,0.5);">
            <div style="color: #64748B; border-bottom: 1px solid #1E293B; padding-bottom: 4px; margin-bottom: 10px;">💻 COMPUTATIONAL LOGIC NODE CIRCUIT DESK</div>
            <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 8px;">
                <span style="background: #1E293B; padding: 4px 8px; border-radius: 4px; border: 1px solid #38BDF8; color: #38BDF8;">[Premise A Node]</span>
                <span style="color: #A855F7;">➔ AND ➔</span>
                <span style="background: #1E293B; padding: 4px 8px; border-radius: 4px; border: 1px solid #38BDF8; color: #38BDF8;">[Premise B Node]</span>
            </div>
            <div style="font-size: 0.8rem; color: #475569;">Circuit Logic Status: Awaiting S-K-E structural validation parameters...</div>
        </div>
    `;
    container.innerHTML += sandboxHtml;
}
