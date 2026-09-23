# [File: server.py - Box 1 of 2: API Setup & Routing Logic]
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import urllib.parse

class DualTrackServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        # Allow cross-origin access so your frontend frame interacts smoothly
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        """Handles fetching lesson configurations from the file vault based on user track parameters."""
        parsed_url = urllib.parse.urlparse(self.path)
        
        if parsed_url.path == '/api/get_lesson':
            query_params = urllib.parse.parse_qs(parsed_url.query)
            grade = query_params.get('grade', ['6-8'])[0].upper()
            day = query_params.get('day', ['1'])[0]
            subject = query_params.get('subject', ['science'])[0].lower()
            
            vault_base = r"C:\DualTrackLearning_Online\backend\vault"
            
            # Map the grade track parameter to the correct isolated disk directory folder
            if grade == "K-5":
                folder = "K5_elementary"
            elif grade == "6-8":
                folder = "68_middleschool"
            else:
                folder = "912_highschool"
                
            target_file_name = f"{subject}_day_{day}.json"
            full_file_path = os.path.join(vault_base, folder, target_file_name)
# [File: server.py - Box 2 of 2: File Fetch Stream & Server Main Entry]
            if os.path.exists(full_file_path):
                try:
                    with open(full_file_path, 'r', encoding='utf-8') as file_stream:
                        lesson_data = json.load(file_stream)
                    self._set_headers(200)
                    self.wfile.write(json.dumps(lesson_data).encode('utf-8'))
                except Exception as err:
                    self._set_headers(500)
                    self.wfile.write(json.dumps({"error": f"Internal database error: {str(err)}"}).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": f"Lesson file not found at locus path: {full_file_path}"}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Unknown backend endpoint API connection route."}).encode('utf-8'))

def run_backend_engine(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DualTrackServerHandler)
    print(f"🚀 Dual-Track Server engine online and listening on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping background server cleanly.")
        httpd.server_close()

if __name__ == '__main__':
    run_backend_engine()
