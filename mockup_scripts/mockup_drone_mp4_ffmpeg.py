import subprocess

import subprocess

subprocess.run([
    "ffmpeg",
    "-re",
    "-stream_loop", "-1",
    "-i", "DJI_20260204155050_0004_S.MP4",

    "-vsync", "passthrough",

    "-c:v", "libx264",
    "-preset", "ultrafast",
    "-tune", "zerolatency",

    "-g", "60",
    "-keyint_min", "60",

    "-b:v", "4M",
    "-maxrate", "4M",
    "-bufsize", "8M",

    "-pix_fmt", "yuv420p",

    "-f", "flv",
    "rtmp://172.27.228.246/live/drone_01"
])