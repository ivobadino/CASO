from __future__ import annotations

import html.parser
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

from faster_whisper import WhisperModel


ROOT = Path(__file__).resolve().parents[1]
VIDEOS_DIR = ROOT / "videos"
TRANSCRIPTS_DIR = ROOT / "transcripciones"
MAP_DIR = ROOT / "mapa"

MODEL_NAME = "tiny"

VIDEOS = [
    {"class_no": 1, "title": "1 250320.mp4", "id": "1YzYRSJjOoXgdI2-csoQMUjKOXe6t6SCw", "folder": "principal"},
    {"class_no": 2, "title": "2 300320.mp4", "id": "1kOwT0Qcwku35fFV2L6DYuZ7GLjSq_f54", "folder": "principal"},
    {"class_no": 3, "title": "3 010420.mp4", "id": "1upty-I6nHk-ESWaGXIshmT-i3-U2b3ba", "folder": "principal"},
    {"class_no": 4, "title": "4 060420 - semaforos.mp4", "id": "1T-5r-IGgV7SMrwOBP_xXY9etLQRXSo2s", "folder": "principal"},
    {"class_no": 5, "title": "5 080420.mp4", "id": "1T_7_bnN7K6V8HwDq1fnMeCXxqrUcU3Uv", "folder": "principal"},
    {"class_no": 6, "title": "6 130420.mp4", "id": "1Ig7HMuWvqeCwQAcDfdORqcoJN8NykTr4", "folder": "principal"},
    {"class_no": 7, "title": "7 150420.mp4", "id": "10gm75LzA-_w2rBSNj9rC3fqlGJQu-S9e", "folder": "TP"},
    {"class_no": 8, "title": "8 200420.mp4", "id": "1zZ6ZP-khgijMfVsSpJRglQucbZ-nbwJ0", "folder": "principal"},
    {"class_no": 9, "title": "9 220420.mp4", "id": "12lYCziglEAWTN9Q3-zqIL9pXiilfgaiQ", "folder": "TP"},
    {"class_no": 10, "title": "10 240420.mp4", "id": "1AeitV1NVtIx76Rw2bzIUawM53ITJzi9G", "folder": "principal"},
    {"class_no": 11, "title": "11 270420.mp4", "id": "1TnspScMivD7Un_KOGFkVtZY9mhQuKZfM", "folder": "principal"},
    {"class_no": 12, "title": "12 290420 PT1.mp4", "id": "1cPpRzlAbpOZoEMQtxcsXEuirMDg0bBUe", "folder": "principal"},
    {"class_no": 13, "title": "13 290420 PT2.mp4", "id": "1FjmbupXZSpk4d6QKe61ImVpedpPlXoyg", "folder": "principal"},
    {"class_no": 14, "title": "14 040520.mp4", "id": "1vWEfuex1h76cV_vIkZT4KAyZTsZJW1YV", "folder": "principal"},
    {"class_no": 15, "title": "15 060520.mp4", "id": "1RuzLA42UOSeIt2ydcs__dUyb2990-2l0", "folder": "principal"},
    {"class_no": 16, "title": "16 130520.mp4", "id": "11MzlxQvaIKwAZ0fHIki2aRRkNdK7XLJl", "folder": "principal"},
    {"class_no": 17, "title": "17 180520.mp4", "id": "1db-lyLfz74MmJulM6bKoadJjWWCRei_r", "folder": "TP"},
    {"class_no": 18, "title": "18 200520.mp4", "id": "1rXjOwCzzvlxFqJwLLfOjKsnfMb9X5Vo6", "folder": "principal"},
    {"class_no": 19, "title": "19 270520.mp4", "id": "1KyUtM-dOF5NcsZJou32OWmsw_zc8VV9h", "folder": "principal"},
    {"class_no": 20, "title": "20 010620.mp4", "id": "1h3tph0dGMoCEx-Emdbd8B07HU7QKWgy-", "folder": "TP"},
    {"class_no": 21, "title": "21 030620.mp4", "id": "155xhzKHUcPYhZ-2QpThKDYvqG7B3Qhr7", "folder": "principal"},
    {"class_no": 22, "title": "22 080620.mp4", "id": "1ZfvSza7HmljbZeT5lSyM0e2oMdSJJpr7", "folder": "principal"},
    {"class_no": 23, "title": "23 170620.mp4", "id": "127NaJqK9u4E-EHv-1yn_J_N8HDf0SmH3", "folder": "TP"},
    {"class_no": 25, "title": "25 030720.mp4", "id": "1yJ3UgMIiP1EG4DIOJCgY4UdNTWeCadpE", "folder": "TP"},
    {"class_no": 26, "title": "26 060720.mp4", "id": "1Z5LchWpz9evqwlwF5uNvT6q1pAG6Mwm_", "folder": "TP"},
    {"class_no": 27, "title": "27 080720.mp4", "id": "1SKeOqHFP2GPxAuiDpr2ob--Dt2QPnxpy", "folder": "TP"},
]

CLASS_24 = {
    "class_no": 24,
    "title": "24.txt",
    "source": "https://www.youtube.com/watch?v=RaeHF1l6oCo&list=WL&index=38&t=8414s",
}


class FormParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.action = None
        self.params = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "form" and data.get("id") == "download-form":
            self.action = data.get("action")
        if tag == "input" and data.get("name"):
            self.params[data["name"]] = data.get("value", "")


def download_file(file_id: str, dest: Path) -> None:
    if dest.exists() and dest.stat().st_size > 1_000_000:
        print(f"skip download: {dest.name}", flush=True)
        return

    warning_url = f"https://drive.google.com/uc?export=download&id={urllib.parse.quote(file_id)}"
    with urllib.request.urlopen(warning_url, timeout=60) as response:
        first = response.read()
        content_type = response.headers.get("content-type", "")

    if "text/html" in content_type.lower() and b"download-form" in first:
        parser = FormParser()
        parser.feed(first.decode("utf-8", errors="replace"))
        if not parser.action:
            raise RuntimeError(f"Could not find Drive confirmation form for {file_id}")
        url = parser.action + "?" + urllib.parse.urlencode(parser.params)
    else:
        dest.write_bytes(first)
        return

    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(url, timeout=120) as response, tmp.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
    tmp.replace(dest)
    print(f"downloaded: {dest.name} ({dest.stat().st_size} bytes)", flush=True)


def transcribe_video(model: WhisperModel, video_path: Path, transcript_path: Path) -> None:
    if transcript_path.exists() and transcript_path.stat().st_size > 200:
        existing = transcript_path.read_text(encoding="utf-8", errors="replace")
        duration_match = re.search(r"^# duration: ([0-9.]+)", existing, re.MULTILINE)
        segment_matches = list(re.finditer(r"\[[0-9.]+ --> ([0-9.]+)\]", existing))
        if duration_match and segment_matches:
            duration = float(duration_match.group(1))
            last_end = float(segment_matches[-1].group(1))
            if last_end >= duration - 120:
                print(f"skip transcript: {transcript_path.name}", flush=True)
                return
            print(f"redo partial transcript: {transcript_path.name}", flush=True)
    segments, info = model.transcribe(
        str(video_path),
        language="es",
        beam_size=1,
        vad_filter=True,
    )
    with transcript_path.open("w", encoding="utf-8") as f:
        print(f"# {video_path.name}", file=f)
        print(f"# duration: {info.duration}", file=f)
        print(file=f)
        for segment in segments:
            text = re.sub(r"\s+", " ", segment.text.strip())
            print(f"[{segment.start:08.2f} --> {segment.end:08.2f}] {text}", file=f)
            f.flush()
    print(f"transcribed: {transcript_path.name}", flush=True)


def main() -> int:
    VIDEOS_DIR.mkdir(exist_ok=True)
    TRANSCRIPTS_DIR.mkdir(exist_ok=True)
    MAP_DIR.mkdir(exist_ok=True)

    model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")
    inventory_path = MAP_DIR / "inventario_videos_drive.json"
    inventory_path.write_text(json.dumps({"videos": VIDEOS, "class_24": CLASS_24}, indent=2, ensure_ascii=False), encoding="utf-8")

    for video in sorted(VIDEOS, key=lambda item: item["class_no"]):
        video_path = VIDEOS_DIR / video["title"]
        transcript_path = TRANSCRIPTS_DIR / f"clase{video['class_no']:02d}.txt"
        print(f"== Clase {video['class_no']:02d}: {video['title']} ==", flush=True)
        download_file(video["id"], video_path)
        transcribe_video(model, video_path, transcript_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
