#!/bin/bash

for f in *.m4a; do ffmpeg -i "$f" -vn "$(basename "$f" .mp4).mp3"; done

