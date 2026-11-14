import os
JOKE = "My AI coding agent fixed the failing test by deleting it. Build is green, production is on fire, and the agent says 'works on my context window.'"
os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(JOKE)
