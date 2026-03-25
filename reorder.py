import codecs
import re

with codecs.open("index.html", "r", "utf-8") as f:
    html = f.read()

body_start = html.find('<!-- Floating WhatsApp -->')
# Find the script tag containing the observer logic
body_end = html.find('<script>\n    // Intersection Observer')
if body_end == -1: body_end = html.find('<script>\r\n    // Intersection Observer')
if body_end == -1: body_end = html.rfind('<script>')

header = html[:body_start]
footer_scripts = html[body_end:]
body_content = html[body_start:body_end]

block_names = [
    "Floating WhatsApp",
    "HERO",
    "PROBLEMS",
    "SERVICES",
    "SYMPTOM CHECKER",
    "RESULTS BEFORE/AFTER",
    "SPECIALIST",
    "TRUST NUMBERS",
    "VIDEO SOCIAL PROOF",
    "HOW IT WORKS",
    "REVIEWS",
    "FORM + FOOTER"
]

blocks = {}
for i, name in enumerate(block_names):
    marker = f'<!-- {name} -->'
    start_idx = body_content.find(marker)
    if start_idx == -1: 
        blocks[name] = ""
        continue
    if i < len(block_names) - 1:
        next_idx = body_content.find(f'<!-- {block_names[i+1]} -->')
        if next_idx == -1: next_idx = len(body_content)
        blocks[name] = body_content[start_idx:next_idx]
    else:
        blocks[name] = body_content[start_idx:]

def apply_bg_safe(block, target_bg):
    if not block.strip(): return block
    
    m = re.search(r'<section([^>]*)class="([^"]*)"([^>]*)>', block)
    if not m:
        return block
    
    pre = m.group(1)
    cls = m.group(2)
    post = m.group(3)
    
    cls = re.sub(r'\bbg-(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d+\b', '', cls)
    cls = re.sub(r'\bfrom-[a-z]+-\d+\b', '', cls)
    cls = re.sub(r'\bto-[a-z]+-\d+\b', '', cls)
    cls = re.sub(r'\bvia-[a-z]+-\d+\b', '', cls)
    cls = cls.replace('bg-white', '').replace('bg-cream', '').replace('bg-gradient-to-br', '').replace('bg-gradient-to-b', '').replace('bg-gradient-to-r', '')
    
    cls = (cls + ' ' + target_bg).strip()
    cls = re.sub(r'\s+', ' ', cls)
    
    new_tag = f'<section{pre}class="{cls}"{post}>'
    return block[:m.start()] + new_tag + block[m.end():]

# Assemble pieces according to the user\'s requested order

# 1. Hero
hero = apply_bg_safe(blocks["HERO"], "bg-white")
hero = hero.replace('Диагностикаға жазылу', 'Тесттен өту')
hero = hero.replace('href="#form"', 'href="#checker"')

# 2. Checker (Moving symptom checker right after Hero)
checker = apply_bg_safe(blocks["SYMPTOM CHECKER"], "bg-slate-50")

# 3. Social Proof (Remove Video Proof if it\'s messing up flow? No, append it at the end of social proof. Actually let\'s just use the ones requested: Results + Reviews)
results = apply_bg_safe(blocks["RESULTS BEFORE/AFTER"], "bg-white")
reviews = apply_bg_safe(blocks["REVIEWS"], "bg-white")
social_proof = results + "\n" + reviews

# 4. Services (Compact grid)
services = apply_bg_safe(blocks["SERVICES"], "bg-slate-50")
services = services.replace('grid sm:grid-cols-2 lg:grid-cols-3', 'grid grid-cols-2 md:grid-cols-3')
services = services.replace('w-16 h-16', 'w-12 h-12 md:w-16 md:h-16')
services = services.replace('p-7', 'p-4 md:p-7')

# 5. Specialist
specialist = apply_bg_safe(blocks["SPECIALIST"], "bg-slate-50")

# 6. Process
process = apply_bg_safe(blocks["HOW IT WORKS"], "bg-white")

# 7. Form + Footer
form_footer = apply_bg_safe(blocks["FORM + FOOTER"], "bg-teal-50")

# Compile new DOM sequence (Discards PROBLEMS, TRUST NUMBERS, VIDEO SOCIAL PROOF entirely to keep layout focused as an app)
new_body = (
    blocks["Floating WhatsApp"] + "\n" +
    hero + "\n" +
    checker + "\n" +
    social_proof + "\n" +
    services + "\n" +
    specialist + "\n" +
    process + "\n" +
    form_footer
)

new_html = header + new_body + footer_scripts

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(new_html)

print("Reorder completed successfully.")
