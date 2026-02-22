#!/bin/bash
cd ~/successful-programmer-journey/02-software-engineering

count=$(find programming -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[)[0-9]+/\\1$count/" ~/successful-programmer-journey/README.md
count=$(find devops -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[[0-9]+, )[0-9]+/\\1$count/" ~/successful-programmer-journey/README.md
count=$(find cloud-infra -type f 2>/dev/null -exec cat {} + | wc -l | xargs); sed -i -E "s/((line|bar) \\[[0-9]+, [0-9]+, )[0-9]+/\\1$count/" ~/successful-programmer-journey/README.md
max=$(grep 'bar \[' ~/successful-programmer-journey/README.md | sed -E 's/.*bar \[(.*)\].*/\1/' | sed 's/, */\n/g' | sort -nr | head -n1); new_max=$((max + 1)); sed -i -E "s/(y-axis \"[^\"]*\" )[0-9]+ --> [0-9]+$/\10 --> $new_max/" ~/successful-programmer-journey/README.md