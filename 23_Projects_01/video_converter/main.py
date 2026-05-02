# video_to_gif.py

from moviepy.editor import VideoFileClip
import os

def convert_video_to_gif(
    input_path: str,
    output_path: str = "output.gif",
    start_time: int = 0,
    end_time: int = None,
    width: int = 480,
    fps: int = 10
):
    # Check if input file exists
    if not os.path.isfile(input_path):
        print("❌ Error: Input file not found.")
        return

    print("🔄 Loading video...")
    clip = VideoFileClip(input_path)

    # Trim the clip if end_time is specified
    if end_time:
        clip = clip.subclip(start_time, end_time)
    elif start_time > 0:
        clip = clip.subclip(start_time)

    # Resize the clip
    if width:
        clip = clip.resize(width=width)

    print("🎞️ Converting to GIF...")
    clip.write_gif(output_path, fps=fps, loop=0)

    print(f"✅ GIF saved as: {output_path}")

# ========== Run Script ==========

if __name__ == "__main__":
    print("🎥 Video to GIF Converter")

    input_video = input("Enter video path (e.g., sample.mp4): ").strip()
    output_gif = input("Enter output GIF name (e.g., mygif.gif): ").strip() or "output.gif"

    try:
        start = int(input("Start time (in seconds): ").strip())
    except:
        start = 0

    try:
        end = input("End time (in seconds, press Enter to skip): ").strip()
        end = int(end) if end else None
    except:
        end = None

    try:
        width = input("GIF width (default 480, press Enter to skip): ").strip()
        width = int(width) if width else 480
    except:
        width = 480

    convert_video_to_gif(
        input_path=input_video,
        output_path=output_gif,
        start_time=start,
        end_time=end,
        width=width,
        fps=10
    )
