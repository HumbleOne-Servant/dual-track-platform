import os
import csv
import json
import zipfile
import urllib.parse
import xml.etree.ElementTree as ET
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8080
CSV_PATH = r"C:\DualLedgerPlatform\curriculum_source.csv"
HTML_PATH = r"C:\DualLedgerPlatform\index.html"
DOCS_DIR = r"C:\DualLedgerPlatform"

def parse_docx_text(file_path):
    """Safely extracts clean paragraph blocks from Microsoft Word XML nodes."""
    if not os.path.exists(file_path):
        return ""
    try:
        with zipfile.ZipFile(file_path) as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            ns = {'w': 'http://openxmlformats.org'}
            paragraphs = []
            for para in root.findall('.//w:p', ns):
                text_nodes = para.findall('.//w:t', ns)
                text_pieces = [node.text for node in text_nodes if node.text]
                if text_pieces:
                    paragraphs.append("".join(text_pieces))
            return "\n\n".join(paragraphs).strip()
    except:
        return ""

def parse_url_link(file_path):
    """Reads a standard Windows internet shortcut file and pulls the target URL."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip().startswith('URL='):
                    return line.strip().split('URL=', 1)[1].strip()
    except:
        pass
    return None
class DualLedgerAPIHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path_clean = parsed_url.path.rstrip('/').lower()
        query_params = parse_qs(parsed_url.query)

        # Serve Dashboard Frame Panel File Natively
        if path_clean == "" or path_clean == "/index.html":
            if not os.path.exists(HTML_PATH):
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            with open(HTML_PATH, "rb") as f:
                self.wfile.write(f.read())
            return

        # Serve PowerPoint Decks and Word Documents without corrupting files
        elif parsed_url.path.startswith("/api/resources/"):
            relative_file_path = urllib.parse.unquote(parsed_url.path.replace("/api/resources/", ""))
            full_resource_path = os.path.normpath(os.path.join(DOCS_DIR, relative_file_path))
            
            if not full_resource_path.startswith(os.path.normpath(DOCS_DIR)) or not os.path.exists(full_resource_path):
                self.send_response(404)
                self.end_headers()
                return

            self.send_response(200)
            self.send_header("Content-Type", "application/octet-stream")
            self.send_header("Content-Disposition", f"attachment; filename=\"{os.path.basename(full_resource_path)}\"")
            self.end_headers()
            with open(full_resource_path, "rb") as f:
                self.wfile.write(f.read())
            return
        # Centralized REST API Query Mapping Database Conduit
        elif path_clean == "/api/curriculum":
            grade_list = query_params.get('grade', [None])
            subject_list = query_params.get('subject', [None])
            
            grade_query = grade_list[0] if grade_list and grade_list[0] else None
            subject_query = subject_list[0] if subject_list and subject_list[0] else None

            filtered_records = []
            for row in CURRICULUM_DATA:
                if grade_query and str(row.get('grade', '')).strip().lower() != str(grade_query).strip().lower():
                    continue
                if subject_query and str(row.get('subject', '')).strip().lower() != str(subject_query).strip().lower():
                    continue
                
                # Setup structure payload dictionary containers
                payload = row.copy()
                payload['student_lessons'] = []
                payload['student_worksheets'] = []
                payload['teacher_guides'] = []
                payload['powerpoints'] = []
                payload['internet_links'] = []
                
                # Keep database row text as an explicit safety net fallback
                payload['mainstream_body'] = row.get('mainstream_body', row.get('objective', ''))

                # Scan local subject folders to classify files using the Structural Dictionary
                grade_folder = f"Grade {str(row.get('grade', '')).strip()}"
                target_dir = os.path.join(DOCS_DIR, grade_folder, str(row.get('subject', '')).strip())
                
                if os.path.exists(target_dir):
                    for file in os.listdir(target_dir):
                        file_lower = file.lower()
                        rel_path = os.path.relpath(os.path.join(target_dir, file), DOCS_DIR)
                        resource_url = f"/api/resources/{urllib.parse.quote(rel_path)}"
                        
                        # STRUCTURAL DICTIONARY MANIFEST MAPPING RULES:
                        # Rule A: Parse Internet Configuration Links
                        if file_lower.endswith('.url'):
                            url_target = parse_url_link(os.path.join(target_dir, file))
                            if url_target:
                                payload['internet_links'].append({"title": file.replace('.url', ''), "url": url_target})
                        # Rule B: Map PowerPoint Interaction Decks
                        elif file_lower.endswith(('.ppt', '.pptx')):
                            payload['powerpoints'].append({"title": file, "url": resource_url})
                        # Rule C: Separate Teacher Materials from Student Content
                        elif file_lower.endswith('.docx'):
                            file_meta = {"title": file, "url": resource_url}
                            
                            if 'teacher' in file_lower or 'guide' in file_lower or 'key' in file_lower:
                                payload['teacher_guides'].append(file_meta)
                            elif 'worksheet' in file_lower or 'practice' in file_lower or 'quiz' in file_lower or 'drill' in file_lower:
                                payload['student_worksheets'].append(file_meta)
                            else:
                                payload['student_lessons'].append(file_meta)

                    # Dynamic Assignment Resolver: Match files to active Day tracker safely
                    if payload['student_lessons']:
                        payload['student_lessons'].sort(key=lambda x: x['title'])
                        day_index = (int(row.get('day', '1')) - 1) % len(payload['student_lessons'])
                        target_docx_path = os.path.normpath(os.path.join(DOCS_DIR, urllib.parse.unquote(payload['student_lessons'][day_index]['url'].replace("/api/resources/", ""))))
                        
                        extracted_lesson_text = parse_docx_text(target_docx_path)
                        if extracted_lesson_text:
                            payload['mainstream_body'] = extracted_lesson_text

                filtered_records.append(payload)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(filtered_records).encode('utf-8'))
            return

        else:
            self.send_response(404)
            self.end_headers()
def load_master_ledger():
    records = []
    if not os.path.exists(CSV_PATH):
        print(f"[CRITICAL MATRIX ERROR] File not found at: {CSV_PATH}")
        return records
    try:
        with open(CSV_PATH, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(dict(row))
        print(f"[SUCCESS Engine Status] Synchronized {len(records)} matrix records securely.")
    except Exception as e:
        print(f"[FAILURE Lifecycle Process] Operational file breakdown: {str(e)}")
    return records

if __name__ == "__main__":
    CURRICULUM_DATA = load_master_ledger()
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, DualLedgerAPIHandler)
    print(f"\n=======================================================")
    print(f"Structure-Aware Media Processing Stream Active on Port: {PORT}")
    print(f"Target Front-End Panel URL: http://localhost:8080/index.html")
    print(f"=======================================================\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down file stream engine handles.")
        httpd.server_close()
