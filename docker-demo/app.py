
from http.server import BaseHTTPRequestHandler, HTTPServer


def response_for_path(path):
    if path == "/health":
        return 200, "OK"

    if path == "/":
        return 200, "Hello from Docker + GitHub Actions!"

    return 404, "Not found"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, message = response_for_path(self.path)

        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


def main():
    server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
    print("Server listening on port 8000", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
