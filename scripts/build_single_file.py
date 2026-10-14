"""Build the portable ArenaHub.html using only the Python standard library."""
from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parent.parent
image = base64.b64encode((ROOT / "assets/arena-hero.webp").read_bytes()).decode("ascii")
css = (ROOT / "style.css").read_text(encoding="utf-8").replace("assets/arena-hero.webp", "data:image/webp;base64," + image)
html = (ROOT / "index.html").read_text(encoding="utf-8")
html = html.replace('<link rel="stylesheet" href="style.css">', "<style>" + css + "</style>")
html = html.replace('<script src="script.js"></script>', "<script>" + (ROOT / "script.js").read_text(encoding="utf-8") + "</script>")
(ROOT / "ArenaHub.html").write_text(html, encoding="utf-8")
print("Built ArenaHub.html")
