import os
from pydub import AudioSegment

# Specify the path to ffmpeg and ffprobe
AudioSegment.converter = "/usr/local/bin/ffmpeg"
AudioSegment.ffprobe   = "/usr/local/bin/ffprobe"

VOICE_MEMOS_DIR = os.path.expanduser("~/Library/Application Support/com.apple.voicememos/Recordings/")
PROCESSED_FILES = set()

def convert_to_mp3(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="mp3")

def process_new_recordings():
    global PROCESSED_FILES
    for filename in os.listdir(VOICE_MEMOS_DIR):
        if filename.endswith(".m4a") and filename not in PROCESSED_FILES:
            input_path = os.path.join(VOICE_MEMOS_DIR, filename)
            output_path = os.path.join(VOICE_MEMOS_DIR, filename.replace(".m4a", ".mp3"))
            convert_to_mp3(input_path, output_path)
            PROCESSED_FILES.add(filename)
            print(f"Converted {filename} to MP3 format.")

if __name__ == "__main__":
    process_new_recordings()
