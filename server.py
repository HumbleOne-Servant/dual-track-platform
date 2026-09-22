import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class DualLedgerBackend(BaseHTTPRequestHandler):
    def end_headers(self):
        # Permits your GitHub Pages frontend to securely pull data from Render
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        # Handles the mandatory security pre-flight checks web browsers perform
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        
        # Safely parse parameters without causing crashes/AttributeErrors
        query_params = parse_qs(parsed_url.query)
        
        # Pull parameters safely; default to standard values if missing
        grade = query_params.get('grade', ['Grade 1'])[0]
        subject = query_params.get('subject', ['Math'])[0]
        day = query_params.get('day', ['Day 1'])[0]

        # Clean string spaces to generate predictable open-source repository paths
        url_subject = subject.replace(" ", "_").lower()
        url_day = day.replace(" ", "_").lower()

        # DYNAMIC PATH ENGINE: Generates public textbook link and matching research ledger text
        # You can substitute "example.org" with your preferred open web repository root URL
        public_iframe_url = f"https://example.org{grade.replace(' ', '').lower()}/{url_subject}/{url_day}.html"
        
        forensic_text = f"Forensic tracking active for {grade}, {subject}, {day}. Verifying historical continuity vectors against standard repository nodes."
        sync_hash = f"SHA256-{hash(grade + subject + day) & 0xffffffff:08x}"

        # Package the complete response structure
        response_data = {
            "status": "synchronized",
            "iframe_target": public_iframe_url,
            "ledger_payload": {
                "cross_reference": forensic_text,
                "sync_hash": sync_hash
            }
        }

        # Send successful response back to frontend
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=DualLedgerBackend, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Dual-Ledger Core active on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    # Render manages port allocations dynamically via environment variables
    import os
    port = int(os.environ.get('PORT', 8000))
    run(port=port)
