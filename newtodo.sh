#!/bin/sh
echo "tell application \"Things3\"
make new to do with properties {name:\"$1\",due date:date \"$2\",notes:\"$3\"}
end tell" | osascript
