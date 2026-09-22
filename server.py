import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class DualLedgerBackend(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        # Pull selected properties or fallback smoothly to defaults
        grade = query_params.get('grade', ['Grade 5'])[0]
        subject = query_params.get('subject', ['Mathematics'])[0]
        day = query_params.get('day', ['Day 1'])[0]

        # CALCULATIVE CONTENT GENERATOR ENGINE
        # This replaces the missing spreadsheet, building lesson text automatically
        if "math" in subject.lower():
            title = "Fractions on a Number Line"
            description = "Represent fractions on a number line from 0 to 1."
            concept = "A fraction shows part of a whole."
            bullet1 = "The bottom number is the denominator — it tells how many equal parts the whole is cut into."
            bullet2 = "The top number is the numerator — it tells how many parts you have."
            bullet3 = "1/4 means one part out of four; 3/4 means three parts out of four."
            cross_ref = "Mark 6:41 — Jesus broke five loaves and gave them to all; the bread was divided among many."
        elif "science" in subject.lower():
            title = "Introduction to Ecosystems"
            description = "Explore how living organisms interact with their environments."
            concept = "Ecosystems balance living and non-living elements."
            bullet1 = "Biotic factors include plants, animals, and micro-organisms."
            bullet2 = "Abiotic factors include sunlight, water, air, and mineral soils."
            bullet3 = "Energy transfers upward from primary producers to apex consumers."
            cross_ref = "Genesis 1:25 — And God made the beast of the earth after his kind, and cattle after their kind."
        elif "history" in subject.lower() or "social" in subject.lower():
            title = "Ancient Civilizations Exploration"
            description = "Analyze the growth and structure of ancient river valley cultures."
            concept = "Rivers provided critical resources for early urban settlements."
            bullet1 = "The Nile, Tigris, and Euphrates provided rich soil for early farming."
            bullet2 = "Written codes, like Hammurabi's Code, established formal societal rules."
            bullet3 = "Irrigation systems required collaborative community organization."
            cross_ref = "Proverbs 22:28 — Remove not the ancient landmark, which thy fathers have set."
        elif "language" in subject.lower():
            title = "Analyzing Structural Elements of Text"
            description = "Identify the differences between main themes and supporting details."
            concept = "Clear composition relies on cohesive arguments."
            bullet1 = "The topic sentence states the central argument of a paragraph."
            bullet2 = "Supporting evidence validates claims through data or narrative examples."
            bullet3 = "Transitions ensure readability between distinct conceptual frameworks."
            cross_ref = "John 1:1 — In the beginning was the Word, and the Word was with God."
        else:
            title = f"{subject} Core Study"
            description = f"Overview reading curriculum for {grade} study modules."
            concept = "Continuous systematic learning expands core comprehension parameters."
            bullet1 = "Review modern reference resources for standard historical timelines."
            bullet2 = "Complete corresponding activity worksheets to reinforce knowledge checkpoints."
            bullet3 = "Maintain consistent daily progress tracking throughout the year."
            cross_ref = "Psalm 119:105 — Thy word is a lamp unto my feet, and a light unto my path."

        # Package the HTML curriculum structure cleanly to send directly into the left side viewport frame
        html_content = f"""
        <div style="padding: 20px; font-family: -apple-system, sans-serif; background-color: #ffffff; color: #1f2937;">
            <div style="display: inline-block; background-color: #f3f4f6; color: #4b5563; font-size: 11px; font-weight: 700; padding: 4px 8px; border-radius: 4px; text-transform: uppercase; margin-bottom: 12px;">{grade} &nbsp;&bull;&nbsp; {subject} &nbsp;&bull;&nbsp; {day}</div>
            <h2 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 700; color: #111827;">{title}</h2>
            <p style="margin: 0 0 20px 0; font-size: 14px; color: #6b7280;">🎯 {description}</p>
            <div style="border-left: 3px solid #e5e7eb; padding-left: 12px; margin-bottom: 20px; font-style: italic; color: #4b5563;">{concept}</div>
            <ul style="margin: 0 0 20px 0; padding-left: 20px; line-height: 1.6; font-size: 14px; color: #374151;">
                <li style="margin-bottom: 8px;">{bullet1}</li>
                <li style="margin-bottom: 8px;">{bullet2}</li>
                <li style="margin-bottom: 0;">{bullet3}</li>
            </ul>
        </div>
        """

        sync_hash = f"NS8xLUZyYW{hash(grade + subject + day) & 0xffff:04x}WN8"

        response_payload = {
            "status": "synchronized",
            "iframe_target": html_content,
            "ledger_payload": {
                "cross_reference": cross_ref,
                "sync_hash": sync_hash
            }
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_payload).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=DualLedgerBackend, port=8000):
    import os
    port = int(os.environ.get('PORT', port))
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server executing on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
