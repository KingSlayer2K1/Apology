import json
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


HOST = "0.0.0.0"
PORT = 8000
BASE_DIR = Path(__file__).resolve().parent
INDEX_FILE = BASE_DIR / "index.html"
RESPONSES_FILE = BASE_DIR / "responses.json"


def load_existing_responses():
  if not RESPONSES_FILE.exists():
    return []
  try:
    with RESPONSES_FILE.open("r", encoding="utf-8") as f:
      data = json.load(f)
      if isinstance(data, list):
        return data
  except (json.JSONDecodeError, OSError):
    pass
  return []


def save_response(entry):
  all_entries = load_existing_responses()
  all_entries.append(entry)
  with RESPONSES_FILE.open("w", encoding="utf-8") as f:
    json.dump(all_entries, f, indent=2, ensure_ascii=False)


class GiftRequestHandler(BaseHTTPRequestHandler):
  def _send_json(self, payload, status=200):
    body = json.dumps(payload).encode("utf-8")
    self.send_response(status)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def _send_html(self, html_text, status=200):
    body = html_text.encode("utf-8")
    self.send_response(status)
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def do_GET(self):
    if self.path in ("/", "/index.html"):
      try:
        html = INDEX_FILE.read_text(encoding="utf-8")
        self._send_html(html)
      except OSError:
        self._send_html("<h1>index.html not found.</h1>", status=500)
      return

    if self.path == "/latest-plan":
      entries = load_existing_responses()
      if not entries:
        self._send_json({"ok": True, "latest": None}, status=200)
      else:
        self._send_json({"ok": True, "latest": entries[-1]}, status=200)
      return

    self._send_json({"error": "Not found"}, status=404)

  def do_POST(self):
    if self.path != "/submit":
      self._send_json({"error": "Not found"}, status=404)
      return

    try:
      length = int(self.headers.get("Content-Length", "0"))
      raw = self.rfile.read(length)
      payload = json.loads(raw.decode("utf-8"))
    except (ValueError, json.JSONDecodeError, UnicodeDecodeError):
      self._send_json({"ok": False, "error": "Invalid JSON body"}, status=400)
      return

    picks = payload.get("picks", [])
    suggested_gift = str(payload.get("suggestedGift", "")).strip()
    suggested_description = str(payload.get("suggestedDescription", "")).strip()
    starter_plan = payload.get("starterPlan", [])
    final_wish = str(payload.get("finalWish", "")).strip()
    skipped = bool(payload.get("skippedWishInput", False))

    entry = {
      "timestamp_utc": datetime.now(timezone.utc).isoformat(),
      "picks": picks if isinstance(picks, list) else [],
      "suggestedGift": suggested_gift,
      "suggestedDescription": suggested_description,
      "starterPlan": starter_plan if isinstance(starter_plan, list) else [],
      "finalWish": final_wish,
      "skippedWishInput": skipped,
    }

    try:
      save_response(entry)
    except OSError:
      self._send_json({"ok": False, "error": "Failed to save response"}, status=500)
      return

    self._send_json({"ok": True, "message": "Saved with love."}, status=200)

  def log_message(self, format, *args):
    return


if __name__ == "__main__":
  server = HTTPServer((HOST, PORT), GiftRequestHandler)
  print(f"Server running at http://127.0.0.1:{PORT}")
  print("Press Ctrl+C to stop.")
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    pass
  finally:
    server.server_close()
