import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS and caching headers for smooth PDF/Image rendering
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    url = f"http://localhost:{PORT}"
    print("=" * 60)
    print(f"  WRATH OF YASH (YUVV) - Test Paper Web Platform")
    print(f"  Local Server: {url}")
    print(f"  Opening browser automatically...")
    print("=" * 60)
    
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Note: Could not auto-open browser: {e}")

    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server listening on port {PORT}. Press Ctrl+C to stop.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")
            sys.exit(0)

if __name__ == "__main__":
    run_server()
