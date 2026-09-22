import os
import json
import zipfile
import urllib.request
import urllib.parse
import re
import xml.etree.ElementTree as ET
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = 8080
HTML_PATH = r"index.html"
DOCS_DIR = os.getcwd()

def parse_docx_text(file_path):
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
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if line.strip().startswith('URL='):
                    return line.strip().split('URL=', 1)[1].strip()
    except:
        pass
    return None
def scrape_online_curriculum(grade, subject, day):
    """Automatically queries public reference nodes to harvest and clean web lessons."""
    base_url = f"https://wikipedia.org{urllib.parse.quote(subject.replace(' ', '_'))}"
    if "math" in subject.lower():
        base_url = "https://wikipedia.orgElementary_mathematics"
    elif "science" in subject.lower():
        base_url = "https://wikipedia.orgOutline_of_science"

    print(f"[SCRAPER] Sourcing data over web: {base_url}")
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(base_url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        raw_p = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
        clean_paragraphs = []
        for p in raw_p:
            text = re.sub(r'<[^>]*>', '', p).strip()
            text = re.sub(r'\[\d+\]', '', text)
            if len(text) > 40 and not 'copyright' in text.lower():
                clean_paragraphs.append(text)
                
        mainstream_text = "\n\n".join(clean_paragraphs[1:4]) if len(clean_paragraphs) > 1 else f"Review core training standards for {subject} Day {day}."
        
        return {
            "grade": str(grade), "subject": str(subject), "day": str(day),
            "title": f"Web Module: {subject} — Day {day}",
            "objective": f"Dynamic online resource sync covering grade {grade} requirements.",
            "mainstream_body": mainstream_text,
            "biblical_body": f"Parallel tracking insights for {subject} unit study."
        }
    except Exception as e:
        print(f"[FALLBACK] Scraper timed out, using structural safety default: {str(e)}")
        return {
            "grade": str(grade), "subject": str(subject), "day": str(day),
            "title": f"{subject} — Lesson {day}",
            "objective": f"Review core frameworks inside {subject}.",
            "mainstream_body": f"Dynamic web module active. Open your local grade directory resources to review documents directly for day {day}.",
            "biblical_body": "Parallel forensic ledger tracking active."
        }
class DualLedgerAPIHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204); self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)
        path_clean = parsed_url.path.rstrip('/').lower()
        query_params = parse_qs(parsed_url.query)

        if path_clean == "" or path_clean == "/index.html":
            if not os.path.exists(HTML_PATH):
                self.send_response(404); self.end_headers(); return
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
            with open(HTML_PATH, "rb") as f: self.wfile.write(f.read())
            return

        elif parsed_url.path.startswith("/api/resources/"):
            rel_file_path = urllib.parse.unquote(parsed_url.path.replace("/api/resources/", ""))
            full_resource_path = os.path.normpath(os.path.join(DOCS_DIR, rel_file_path))
            if not full_resource_path.startswith(os.path.normpath(DOCS_DIR)) or not os.path.exists(full_resource_path):
                self.send_response(404); self.end_headers(); return
            self.send_response(200); self.send_header("Content-Type", "application/octet-stream"); self.end_headers()
            with open(full_resource_path, "rb") as f: self.wfile.write(f.read())
            return

        elif path_clean == "/api/curriculum":
            # FIXED: Unpack list items using index 0 to eliminate the .strip() list crash completely
            g_list = query_params.get('grade', ['K'])
            s_list = query_params.get('subject', ['Mathematics'])
            d_list = query_params.get('day', ['1'])
            
            grade_query = str(g_list[0]).strip() if g_list else "K"
            subject_query = str(s_list[0]).strip() if s_list else "Mathematics"
            day_query = str(d_list[0]).strip() if d_list else "1"

            grade_folder = f"Grade {grade_query}"
            target_dir = os.path.join(DOCS_DIR, grade_folder, subject_query)
            
            payload = {
                "grade": grade_query, "subject": subject_query, "day": day_query,
                "title": f"{subject_query} Module", "objective": f"Review daily targets for {subject_query}.",
                "mainstream_body": "", "biblical_body": "Parallel tracking context matrix operational.",
                "student_lessons": [], "student_worksheets": [], "teacher_guides": [], "powerpoints": [], "internet_links": []
            }

            folder_found_files = False
            if os.path.exists(target_dir):
                for file in os.listdir(target_dir):
                    file_lower = file.lower()
                    rel_path = os.path.relpath(os.path.join(target_dir, file), DOCS_DIR)
                    res_url = f"/api/resources/{urllib.parse.quote(rel_path)}"
                    file_meta = {"title": file, "url": res_url}
                    folder_found_files = True

                    if file_lower.endswith('.url'):
                        url_target = parse_url_link(os.path.join(target_dir, file))
                        if url_target: payload['internet_links'].append({"title": file.replace('.url',''), "url": url_target})
                    elif file_lower.endswith(('.ppt', '.pptx')):
                        payload['powerpoints'].append(file_meta)
                    elif file_lower.endswith('.docx'):
                        if any(k in file_lower for k in ['teacher', 'guide', 'key']):
                            payload['teacher_guides'].append(file_meta)
                        elif any(k in file_lower for k in ['worksheet', 'practice', 'quiz']):
                            payload['student_worksheets'].append(file_meta)
                        else:
                            payload['student_lessons'].append(file_meta)

                if payload['student_lessons']:
                    payload['student_lessons'].sort(key=lambda x: x['title'])
                    day_idx = (int(day_query) - 1) % len(payload['student_lessons'])
                    target_docx = os.path.normpath(os.path.join(DOCS_DIR, urllib.parse.unquote(payload['student_lessons'][day_idx]['url'].replace("/api/resources/", ""))))
                    extracted_text = parse_docx_text(target_docx)
                    if extracted_text: payload['mainstream_body'] = extracted_text
            if not folder_found_files or not payload['mainstream_body']:
                web_data = scrape_online_curriculum(grade_query, subject_query, day_query)
                payload['title'] = web_data['title']
                payload['objective'] = web_data['objective']
                payload['mainstream_body'] = web_data['mainstream_body']
                payload['biblical_body'] = web_data['biblical_body']

            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(json.dumps([payload]).encode('utf-8'))
            return
        else:
            self.send_response(404); self.end_headers()

if __name__ == "__main__":
    httpd = HTTPServer(('0.0.0.0', 8080), DualLedgerAPIHandler)
    print("Spreadsheet-Free Ingestion Engine Running Live...")
    try: httpd.serve_forever()
    except KeyboardInterrupt: httpd.server_close()
