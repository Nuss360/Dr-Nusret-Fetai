#!/usr/bin/env python3

with open('/sessions/zealous-trusting-euler/mnt/outputs/dr-fetai-cinematic-cta.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── 1. BIGGER CTA TEXT ──────────────────────────────────
# Patch cin-text font-size for both variants
content = content.replace(
    '.cin-text {\n  position: relative; z-index: 3;\n  font-family: "Jost", sans-serif;\n  font-size: .62rem; letter-spacing: .4em; text-transform: uppercase;\n  transition: color .45s ease, letter-spacing .5s cubic-bezier(.16,1,.3,1);\n  white-space: nowrap; line-height: 1;\n}',
    '.cin-text {\n  position: relative; z-index: 3;\n  font-family: "Jost", sans-serif;\n  font-size: .85rem; letter-spacing: .32em; text-transform: uppercase;\n  transition: color .45s ease, letter-spacing .5s cubic-bezier(.16,1,.3,1);\n  white-space: nowrap; line-height: 1;\n}'
)
content = content.replace(
    '.cin-gold .cin-text { color: var(--dark); font-weight: 500; font-size: .65rem; }',
    '.cin-gold .cin-text { color: var(--dark); font-weight: 500; font-size: .88rem; }'
)

# ── 2. FORM CSS ─────────────────────────────────────────
form_css = """
/* ═══════════════════════════════════════════
   ANFRAGE-FORMULAR — Luxury Lead Form
   ═══════════════════════════════════════════ */
.lf-wrap{
  background:rgba(247,244,239,.04);
  border:1px solid rgba(184,151,74,.18);
  border-top:2px solid var(--gold);
  padding:3rem 3rem 2.8rem;
  position:relative;
  overflow:hidden;
}
.lf-wrap::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 80% 0%,rgba(184,151,74,.07),transparent 55%);
  pointer-events:none;
}
.lf-badge{
  font-size:.58rem;letter-spacing:.35em;text-transform:uppercase;
  color:var(--gold);display:flex;align-items:center;gap:.7rem;
  margin-bottom:1.6rem;
}
.lf-badge::before{content:'';width:18px;height:1px;background:var(--gold)}
.lf-title{
  font-family:'Cormorant Garamond',serif;font-size:1.9rem;font-weight:300;
  color:var(--cream);line-height:1.1;margin-bottom:.5rem;
}
.lf-title em{font-style:italic;color:var(--gold-light)}
.lf-sub{
  font-size:.72rem;color:rgba(247,244,239,.42);
  letter-spacing:.06em;margin-bottom:2.2rem;line-height:1.7;
}
.lf-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-bottom:1px}
.lf-field{position:relative}
.lf-field label{
  display:block;font-size:.52rem;letter-spacing:.28em;text-transform:uppercase;
  color:rgba(184,151,74,.62);margin-bottom:.5rem;font-family:'Jost',sans-serif;
}
.lf-field input,
.lf-field select{
  width:100%;background:rgba(247,244,239,.05);
  border:none;border-bottom:1px solid rgba(184,151,74,.2);
  color:var(--cream);font-family:'Jost',sans-serif;font-size:.82rem;font-weight:300;
  padding:.85rem 1rem .85rem 0;outline:none;
  transition:border-color .3s,background .3s;
  appearance:none;-webkit-appearance:none;
  letter-spacing:.04em;
}
.lf-field input::placeholder{color:rgba(247,244,239,.22);font-size:.78rem}
.lf-field input:focus,
.lf-field select:focus{
  border-bottom-color:var(--gold);
  background:rgba(184,151,74,.04);
}
.lf-field select option{background:#152b22;color:var(--cream)}
.lf-field-full{grid-column:1/-1}
/* Erreichbarkeit pills */
.lf-pills{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:.3rem}
.lf-pill{
  position:relative;
}
.lf-pill input[type=checkbox]{position:absolute;opacity:0;width:0;height:0}
.lf-pill label{
  display:block;font-size:.55rem;letter-spacing:.18em;text-transform:uppercase;
  color:rgba(247,244,239,.45);border:1px solid rgba(184,151,74,.18);
  padding:.38rem .9rem;cursor:pointer;
  transition:all .25s;font-family:'Jost',sans-serif;
  margin:0;
}
.lf-pill input:checked + label{
  background:rgba(184,151,74,.15);
  border-color:rgba(184,151,74,.5);
  color:var(--gold-light);
}
.lf-pill label:hover{border-color:rgba(184,151,74,.35);color:rgba(247,244,239,.7)}
/* Success state */
.lf-success{
  display:none;text-align:center;padding:2rem 1rem;
}
.lf-success-icon{font-size:2rem;margin-bottom:1rem}
.lf-success h4{
  font-family:'Cormorant Garamond',serif;font-size:1.6rem;font-weight:300;
  color:var(--cream);margin-bottom:.6rem;
}
.lf-success p{font-size:.78rem;color:rgba(247,244,239,.5);line-height:1.8}
/* Submit btn */
.lf-submit{
  width:100%;margin-top:1px;
  background:linear-gradient(135deg,var(--gold) 0%,var(--gold-light) 100%);
  border:none;color:var(--dark);
  font-family:'Jost',sans-serif;font-size:.82rem;letter-spacing:.28em;
  text-transform:uppercase;font-weight:600;
  padding:1.15rem 2rem;cursor:pointer;
  position:relative;overflow:hidden;
  transition:filter .3s,transform .1s;
}
.lf-submit:hover{filter:brightness(1.08)}
.lf-submit:active{transform:scale(.98)}
.lf-submit::after{
  content:'';position:absolute;top:0;bottom:0;left:-110%;width:55%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);
  animation:lfShimmer 3.5s ease-in-out 1s infinite;
}
@keyframes lfShimmer{0%{left:-110%}100%{left:200%}}
.lf-note{
  font-size:.58rem;color:rgba(247,244,239,.22);
  text-align:center;margin-top:1.2rem;letter-spacing:.08em;line-height:1.7;
}
@media(max-width:600px){
  .lf-grid{grid-template-columns:1fr}
  .lf-wrap{padding:2rem 1.5rem}
}
"""

# ── 3. FORM HTML (replaces old contact-grid in CTA section) ──
old_cta_right = '''    <div>
      <p class="cta-sub reveal">30 Minuten · Kein Verkaufsdruck · Nur ehrliche Analyse<br>Body Art Surgery Institute · Immermannstraße 10, Etage 2 · 40210 Düsseldorf</p>
      <a href="https://calendly.com/drfetai-mail" target="_blank" class="cta-main reveal"><span>Termin online buchen →</span></a>
      <p class="cta-note">Oder direkt anrufen: 0211 / 158 76080</p>
      <div class="contact-grid reveal">
        <a href="tel:02111587608" class="cg"><div class="cg-icon">📞</div><div class="cg-label">Telefon</div><div class="cg-val">0211 / 158 76080</div></a>
        <a href="https://wa.me/4915259274323" target="_blank" class="cg"><div class="cg-icon">💬</div><div class="cg-label">WhatsApp</div><div class="cg-val">+49 1525 9274323</div></a>
        <a href="mailto:drfetai@mail.de" class="cg"><div class="cg-icon">✉</div><div class="cg-label">E-Mail</div><div class="cg-val">drfetai@mail.de</div></a>
        <a href="https://calendly.com/drfetai-mail" target="_blank" class="cg"><div class="cg-icon">📅</div><div class="cg-label">Online Termin</div><div class="cg-val">calendly.com/drfetai-mail</div></a>
      </div>
    </div>'''

new_cta_right = '''    <div>
      <!-- ══ ANFRAGE-FORMULAR ══ -->
      <div class="lf-wrap reveal">
        <div id="lfForm">
          <div class="lf-badge">Kostenlos · Unverbindlich · 24h Antwort</div>
          <div class="lf-title">Deine Anfrage an<br><em>Dr. Fetai</em></div>
          <p class="lf-sub">Füll kurz aus — wir melden uns innerhalb von 24 Stunden.</p>

          <!-- ACTION: Formspree endpoint — ersetze XXXXX mit deiner Formspree-ID -->
          <form id="lfFormEl" action="https://formspree.io/f/XXXXX" method="POST">
            <!-- Hidden fields für Formspree -->
            <input type="hidden" name="_subject" value="Neue Anfrage — Dr. Fetai Website">
            <input type="hidden" name="_language" value="de">

            <div class="lf-grid">
              <!-- Name -->
              <div class="lf-field">
                <label>Vorname &amp; Nachname *</label>
                <input type="text" name="name" placeholder="z.B. Laura Müller" required>
              </div>
              <!-- Telefon -->
              <div class="lf-field">
                <label>Telefonnummer *</label>
                <input type="tel" name="telefon" placeholder="z.B. 0170 123 456 7" required>
              </div>
              <!-- Wunschbehandlung -->
              <div class="lf-field lf-field-full">
                <label>Gewünschte Behandlung</label>
                <select name="behandlung">
                  <option value="" disabled selected>Bitte wählen…</option>
                  <option>Hyaluron Filler</option>
                  <option>Botulinum (Botox)</option>
                  <option>PRP Eigenbluttherapie</option>
                  <option>Fadenlifting</option>
                  <option>Liposuktion / Bodysculpting</option>
                  <option>Brust-OP</option>
                  <option>Nasenkorrektur</option>
                  <option>Kombinationsbehandlung</option>
                  <option>Erstberatung (noch unentschieden)</option>
                </select>
              </div>
              <!-- Erreichbarkeit -->
              <div class="lf-field lf-field-full">
                <label>Ich bin erreichbar</label>
                <div class="lf-pills">
                  <div class="lf-pill"><input type="checkbox" name="erreichbar" id="er1" value="Morgens (8–12)"><label for="er1">Morgens 8–12</label></div>
                  <div class="lf-pill"><input type="checkbox" name="erreichbar" id="er2" value="Mittags (12–15)"><label for="er2">Mittags 12–15</label></div>
                  <div class="lf-pill"><input type="checkbox" name="erreichbar" id="er3" value="Nachmittags (15–18)"><label for="er3">Nachmittags 15–18</label></div>
                  <div class="lf-pill"><input type="checkbox" name="erreichbar" id="er4" value="Abends (18–20)"><label for="er4">Abends 18–20</label></div>
                  <div class="lf-pill"><input type="checkbox" name="erreichbar" id="er5" value="WhatsApp jederzeit"><label for="er5">WhatsApp jederzeit</label></div>
                </div>
              </div>
            </div>

            <button type="submit" class="lf-submit">Anfrage jetzt absenden →</button>
            <p class="lf-note">🔒 Deine Daten werden vertraulich behandelt und nicht weitergegeben.<br>DSGVO-konform · Kein Spam · Nur Dr. Fetais Team liest mit.</p>
          </form>

          <!-- Success Message -->
          <div class="lf-success" id="lfSuccess">
            <div class="lf-success-icon">✦</div>
            <h4>Vielen Dank,<br>deine Anfrage ist angekommen.</h4>
            <p>Dr. Fetais Team meldet sich<br>innerhalb von 24 Stunden bei dir.</p>
          </div>
        </div>
      </div>

      <p class="cta-note" style="margin-top:1.4rem">Oder direkt anrufen: 0211 / 158 76080</p>
    </div>'''

# ── 4. FORM JS ──────────────────────────────────────────
form_js = """
<!-- FORM SUBMIT HANDLER -->
<script>
(function(){
  var form = document.getElementById('lfFormEl');
  var success = document.getElementById('lfSuccess');
  if(!form) return;

  form.addEventListener('submit', function(e){
    e.preventDefault();
    var btn = form.querySelector('.lf-submit');
    btn.textContent = 'Wird gesendet…';
    btn.disabled = true;

    var data = new FormData(form);
    fetch(form.action, {
      method:'POST',
      body: data,
      headers:{ 'Accept':'application/json' }
    })
    .then(function(r){ return r.json(); })
    .then(function(res){
      if(res.ok || res.error === undefined){
        form.style.display = 'none';
        success.style.display = 'block';
        // Facebook Pixel event
        if(typeof fbq !== 'undefined') fbq('track','Lead');
      } else {
        btn.textContent = 'Fehler — bitte erneut versuchen';
        btn.disabled = false;
      }
    })
    .catch(function(){
      btn.textContent = 'Fehler — bitte erneut versuchen';
      btn.disabled = false;
    });
  });
})();
</script>
"""

# Apply all patches
content = content.replace('</style>', form_css + '\n</style>', 1)
content = content.replace(old_cta_right, new_cta_right, 1)
content = content.replace('</body>', form_js + '\n</body>', 1)

with open('/sessions/zealous-trusting-euler/mnt/outputs/dr-fetai-cinematic-cta.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
ok_form  = 'lfFormEl' in content
ok_big   = '.85rem' in content
ok_css   = 'lf-wrap' in content
print(f"Form injected:   {ok_form}")
print(f"Bigger CTA text: {ok_big}")
print(f"Form CSS:        {ok_css}")
print("✅ Done")
