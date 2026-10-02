from http.server import BaseHTTPRequestHandler, HTTPServer


class CurrencyService(BaseHTTPRequestHandler):

    def do_GET(self):

        amount = 8300
        usd = amount / 83

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        message = f"INR {amount} = USD {usd:.2f}"

        self.wfile.write(message.encode())


server = HTTPServer(("localhost", 8000), CurrencyService)

print("Currency Web Service Started")
print("Open: http://localhost:8000")

server.serve_forever()
