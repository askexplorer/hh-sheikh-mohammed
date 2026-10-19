#!/bin/bash
# Double-click to preview the page with the video playing inside it.
# (YouTube only plays embedded videos on pages served over http, not on files opened straight from disk.)
cd "$(dirname "$0")"
PORT=8765
echo "Preview running. Close this window to stop it."
( sleep 1; open "http://localhost:$PORT/dist/preview/en.html" ) &
python3 -m http.server $PORT
