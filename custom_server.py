import http.server
import socketserver
import os

class BrotliHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Brotli 파일 요청 처리
        if self.path.endswith(".br"):
            self.send_header("Content-Encoding", "br")
        super().end_headers()

# 서버 실행
PORT = 8080
with socketserver.TCPServer(("", PORT), BrotliHTTPRequestHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
