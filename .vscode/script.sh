#!/bin/bash
count=$(find python -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[)[0-9]+/\\1$count/" README.md
count=$(find docker -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[[0-9]+, )[0-9]+/\\1$count/" README.md
count=$(find 'fastapi' -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[[0-9]+, [0-9]+, )[0-9]+/\\1$count/" README.md
count=$(find 'pydantic' -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[[0-9]+, [0-9]+, [0-9]+, )[0-9]+/\\1$count/" README.md
max=$(grep 'bar \[' README.md | sed -E 's/.*bar \[(.*)\].*/\1/' | sed 's/, */\n/g' | sort -nr | head -n1); new_max=$((max + 1)); sed -i -E "s/(y-axis \"[^\"]*\" )[0-9]+ --> [0-9]+$/\10 --> $new_max/" README.md