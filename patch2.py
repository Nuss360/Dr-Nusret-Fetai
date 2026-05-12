#!/usr/bin/env python3

with open('/sessions/zealous-trusting-euler/mnt/outputs/dr-fetai-cinematic-cta.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. Switch to Web3Forms + add contact grid back ──────
old_form_action = '''          <!-- ACTION: Formspree endpoint — ersetze XXXXX mit deiner Formspree-ID -->
          <form id="lfFormEl" action="https://formspree.io/f/XXXXX" method="POST">
            <!-- Hidden fields für Formspree -->
            <input type="hidden" name="_subject" value="Neue Anfrage — Dr. Fetai Website">
            <input type="hidden" name="_language" value="de">'''

new_form_action = '''          <!-- ACTION: Web3Forms — ersetze XXXXX mit deinem Web3Forms Access Key -->
          <form id="lfFormEl" action="https://api.web3forms.com/submit" method="POST">
            <input type="hidden" name="access_key" value="XXXXX">
            <input type="hidden" name="subject" value="Neue Anfrage — Dr. Fetai Website">
            <input type="hidden" name="from_name" value="Dr. Fetai Website">
            <input type="hidden" name="redirect" value="false">'''

content = content.replace(old_form_action, new_form_action, 1)

# ── 2. Add contact grid back below form ─────────────────
old_note = '''      <p class="cta-note" style="margin-top:1.4rem">Oder direkt anrufen: 0211 / 158 76080</p>
    </div>'''

new_note = '''      <p class="cta-note" style="margin-top:1.4rem">Oder direkt anrufen: 0211 / 158 76080</p>
      <div class="contact-grid reveal" style="margin-top:1.2rem">
        <a href="tel:02111587608" class="cg"><div class="cg-icon">📞</div><div class="cg-label">Telefon</div><div class="cg-val">0211 / 158 76080</div></a>
        <a href="https://wa.me/4915259274323" target="_blank" class="cg"><div class="cg-icon">💬</div><div class="cg-label">WhatsApp</div><div class="cg-val">+49 1525 9274323</div></a>
        <a href="mailto:drfetai@mail.de" class="cg"><div class="cg-icon">✉</div><div class="cg-label">E-Mail</div><div class="cg-val">drfetai@mail.de</div></a>
        <a href="https://calendly.com/drfetai-mail" target="_blank" class="cg"><div class="cg-icon">📅</div><div class="cg-label">Online Termin</div><div class="cg-val">calendly.com/drfetai-mail</div></a>
      </div>
    </div>'''

content = content.replace(old_note, new_note, 1)

# ── 3. Mobile CTA — much bigger text ────────────────────
# sc-title (spacecraft mobile button)
content = content.replace(
    '.sc-title{\n  font-family:"Cormorant Garamond",serif;\n  font-size:1.22rem;font-weight:300;color:var(--cream);letter-spacing:.02em\n}',
    '.sc-title{\n  font-family:"Cormorant Garamond",serif;\n  font-size:1.55rem;font-weight:300;color:var(--cream);letter-spacing:.02em\n}'
)
# scta-book-main (sticky bar mobile)
content = content.replace(
    '.scta-book-main{font-size:.85rem;letter-spacing:.2em;text-transform:uppercase;font-weight:500;display:block}',
    '.scta-book-main{font-size:1.05rem;letter-spacing:.18em;text-transform:uppercase;font-weight:500;display:block}'
)
# mobile overrides
content = content.replace(
    '  .scta-book-main{font-size:.7rem;letter-spacing:.1em}',
    '  .scta-book-main{font-size:.95rem;letter-spacing:.1em}'
)
content = content.replace(
    '  .scta-book-main{font-size:.66rem}',
    '  .scta-book-main{font-size:.88rem}'
)

# ── 4. Update fetch handler for Web3Forms response ───────
old_handler = '''    .then(function(res){
      if(res.ok || res.error === undefined){'''
new_handler = '''    .then(function(res){
      if(res.success){'''
content = content.replace(old_handler, new_handler, 1)

with open('/sessions/zealous-trusting-euler/mnt/outputs/dr-fetai-cinematic-cta.html', 'w', encoding='utf-8') as f:
    f.write(content)

# verify
checks = {
  'Web3Forms':     'web3forms.com' in content,
  'Contact grid':  'cg-label' in content,
  'Mobile bigger': '1.55rem' in content or '1.05rem' in content,
}
for k,v in checks.items():
    print(f"{'✅' if v else '❌'} {k}")
print("Done")
