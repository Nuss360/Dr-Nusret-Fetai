#!/usr/bin/env python3
import re

with open('/sessions/zealous-trusting-euler/mnt/uploads/dr-fetai-optimiert.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File loaded: {len(content)} chars")

# ═══════════════════════════════════════════════════════
# NEW CSS — injected before </style>
# ═══════════════════════════════════════════════════════
new_css = """
/* ═══════════════════════════════════════════════════════════════
   ██████╗██╗███╗   ██╗███████╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗
  ██╔════╝██║████╗  ██║██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝
  ██║     ██║██╔██╗ ██║█████╗  ██╔████╔██║███████║   ██║   ██║██║
  ██║     ██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══██║   ██║   ██║██║
  ╚██████╗██║██║ ╚████║███████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗
   ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝
   CTA — Neuroscience × Cinema × Luxury — Weltbeste Button
   ═══════════════════════════════════════════════════════════════ */

/* ── WRAP ── */
.cin-wrap {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
  filter: drop-shadow(0 0 0px rgba(184,151,74,0));
  transition: filter .65s cubic-bezier(.16,1,.3,1);
  will-change: filter, transform;
}
.cin-wrap:hover {
  filter:
    drop-shadow(0 0 28px rgba(184,151,74,.24))
    drop-shadow(0 0 80px rgba(184,151,74,.1))
    drop-shadow(0 0 120px rgba(29,58,47,.14));
}

/* ── PARTICLE CANVAS (floats above button) ── */
.cin-canvas {
  position: absolute;
  bottom: calc(100% - 10px);
  left: 50%;
  transform: translateX(-50%);
  width: 220%;
  height: 100px;
  pointer-events: none;
  z-index: 20;
  opacity: 0;
  transition: opacity .5s ease;
}
.cin-wrap:hover .cin-canvas { opacity: 1; }

/* ── LIVE BADGE (above button) ── */
.cin-live {
  position: absolute;
  top: -11px; left: 50%;
  transform: translateX(-50%);
  display: flex; align-items: center; gap: .4rem;
  font-family: "Jost", sans-serif;
  font-size: .44rem; letter-spacing: .18em;
  text-transform: uppercase; font-weight: 700;
  padding: .22rem .78rem .22rem .55rem;
  border-radius: 20px; white-space: nowrap;
  z-index: 15; pointer-events: none;
  animation: cinLiveFloat 3.2s ease-in-out infinite;
  box-shadow:
    0 4px 18px rgba(184,151,74,.38),
    0 2px 8px rgba(14,11,8,.25),
    inset 0 1px 0 rgba(255,255,255,.2);
}
@keyframes cinLiveFloat {
  0%,100% { transform: translateX(-50%) translateY(0); }
  50%      { transform: translateX(-50%) translateY(-3.5px); }
}
.cin-live-dot {
  width: 5px; height: 5px; border-radius: 50%;
  animation: blink 1.4s infinite; flex-shrink: 0;
}

/* ── SURFACE ── */
.cin-surface {
  position: relative;
  overflow: hidden;
  display: flex; align-items: center; gap: 1.1rem;
  padding: 1.18rem 2.8rem;
  transition:
    box-shadow .55s cubic-bezier(.16,1,.3,1),
    transform .08s ease;
  will-change: box-shadow, transform;
}
.cin-wrap:active .cin-surface {
  transform: scale(.972) translateY(1px);
}

/* Scanline texture */
.cin-scan {
  position: absolute; inset: 0; pointer-events: none; z-index: 0;
  background-image: repeating-linear-gradient(
    0deg, transparent, transparent 3px,
    rgba(255,255,255,.014) 3px, rgba(255,255,255,.014) 6px
  );
}

/* Left gold edge accent */
.cin-edge {
  position: absolute; left: 0; top: 8%; bottom: 8%;
  width: 2px; z-index: 2;
  animation: cinEdgePulse 2.4s ease-in-out infinite;
}
@keyframes cinEdgePulse {
  0%,100% { opacity: .38; top: 14%; bottom: 14%; }
  50%      { opacity: .8;  top: 5%;  bottom: 5%;  }
}

/* Idle shimmer sweep */
.cin-sheen {
  position: absolute; top: 0; bottom: 0; left: -130%; width: 55%;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(255,255,255,.0) 25%,
    rgba(255,255,255,.09) 47%,
    rgba(184,151,74,.13) 50%,
    rgba(255,255,255,.0) 73%,
    transparent 100%
  );
  animation: cinSheen 5.5s ease-in-out 2s infinite;
  pointer-events: none; z-index: 1;
}
@keyframes cinSheen { 0% { left: -130%; } 100% { left: 220%; } }

/* Hover fill — diagonal reveal */
.cin-fill {
  position: absolute; inset: 0; z-index: 1;
  transform: translateX(-108%) skewX(-10deg);
  transition: transform .58s cubic-bezier(.16,1,.3,1);
}
.cin-wrap:hover .cin-fill { transform: translateX(0) skewX(0deg); }

/* Click flash */
.cin-flash {
  position: absolute; inset: 0; z-index: 6;
  opacity: 0; pointer-events: none;
  mix-blend-mode: screen;
  transition: opacity .06s ease;
  background: rgba(255,248,210,.95);
}
.cin-wrap:active .cin-flash { opacity: .5; }

/* Cursor proximity radial glow on surface */
.cin-surface::before {
  content: '';
  position: absolute; inset: 0; z-index: 0; pointer-events: none;
  background: radial-gradient(
    circle 90px at var(--bx,50%) var(--by,50%),
    rgba(184,151,74,.1) 0%, transparent 70%
  );
  opacity: 0; transition: opacity .3s ease;
}
.cin-wrap:hover .cin-surface::before { opacity: 1; }

/* ── TEXT ── */
.cin-text {
  position: relative; z-index: 3;
  font-family: "Jost", sans-serif;
  font-size: .62rem; letter-spacing: .4em; text-transform: uppercase;
  transition: color .45s ease, letter-spacing .5s cubic-bezier(.16,1,.3,1);
  white-space: nowrap; line-height: 1;
}

/* ── ARROW ── */
.cin-arrow {
  position: relative; z-index: 3;
  width: 30px; height: 30px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  transition: all .5s cubic-bezier(.16,1,.3,1);
}
.cin-arrow svg {
  width: 13px; height: 13px;
  transition: transform .45s cubic-bezier(.16,1,.3,1);
  display: block;
}
.cin-wrap:hover .cin-arrow { transform: translateX(4px); }
.cin-wrap:hover .cin-arrow svg { transform: translateX(1px); }
.cin-wrap:active .cin-arrow { transform: translateX(7px) scale(.86); }

/* ══ SAGE VARIANT (hero .btn-p) ══════════════════════════ */
.cin-sage .cin-surface {
  background: linear-gradient(148deg,
    #0c1c15 0%, var(--sage-dark) 30%, var(--sage) 65%, var(--sage-light) 100%);
  box-shadow:
    0 0 0 1px rgba(184,151,74,.32),
    0 0 22px rgba(184,151,74,.1),
    0 14px 42px rgba(14,11,8,.55),
    0 4px 12px rgba(14,11,8,.38),
    inset 0 1px 0 rgba(255,255,255,.07),
    inset 0 -1px 0 rgba(184,151,74,.1);
}
.cin-sage:hover .cin-surface {
  box-shadow:
    0 0 0 1.5px rgba(184,151,74,.6),
    0 0 32px rgba(184,151,74,.22),
    0 0 90px rgba(184,151,74,.08),
    0 22px 60px rgba(14,11,8,.62),
    0 4px 16px rgba(14,11,8,.42),
    inset 0 1px 0 rgba(255,255,255,.1),
    inset 0 -1px 0 rgba(184,151,74,.2);
}
.cin-sage .cin-fill {
  background: linear-gradient(135deg, #8d6e28 0%, var(--gold) 40%, #c8a055 65%, var(--gold-light) 100%);
}
.cin-sage .cin-edge {
  background: linear-gradient(to bottom, transparent, var(--gold), transparent);
}
.cin-sage .cin-text { color: var(--cream); }
.cin-sage:hover .cin-text { color: var(--dark); letter-spacing: .44em; }
.cin-sage .cin-arrow {
  background: rgba(184,151,74,.13);
  border: 1px solid rgba(184,151,74,.32);
  color: var(--gold);
}
.cin-sage:hover .cin-arrow {
  background: rgba(14,11,8,.16);
  border-color: rgba(14,11,8,.22);
  color: var(--dark);
}
.cin-sage .cin-live {
  background: var(--gold);
  color: var(--sage-dark);
}
.cin-sage .cin-live-dot { background: var(--sage-dark); }

/* ══ GOLD VARIANT (section .cta-main) ════════════════════ */
.cin-gold .cin-surface {
  background: linear-gradient(148deg,
    #5c4510 0%, #8a6520 35%, var(--gold) 65%, var(--gold-light) 100%);
  box-shadow:
    0 0 0 1px rgba(184,151,74,.58),
    0 0 24px rgba(184,151,74,.22),
    0 14px 42px rgba(14,11,8,.5),
    0 4px 12px rgba(14,11,8,.32),
    inset 0 1px 0 rgba(255,255,255,.18),
    inset 0 -1px 0 rgba(14,11,8,.12);
}
.cin-gold:hover .cin-surface {
  box-shadow:
    0 0 0 1.5px rgba(184,151,74,.78),
    0 0 40px rgba(184,151,74,.34),
    0 0 100px rgba(184,151,74,.12),
    0 22px 60px rgba(14,11,8,.55),
    0 4px 16px rgba(14,11,8,.38),
    inset 0 1px 0 rgba(255,255,255,.22),
    inset 0 -1px 0 rgba(14,11,8,.15);
}
.cin-gold .cin-fill {
  background: linear-gradient(135deg, #e8c87a 0%, var(--gold-light) 55%, #f0d899 100%);
}
.cin-gold .cin-edge {
  background: linear-gradient(to bottom, transparent, rgba(255,255,255,.4), transparent);
}
.cin-gold .cin-text { color: var(--dark); font-weight: 500; font-size: .65rem; }
.cin-gold:hover .cin-text { color: var(--dark); letter-spacing: .45em; }
.cin-gold .cin-arrow {
  background: rgba(14,11,8,.12);
  border: 1px solid rgba(14,11,8,.2);
  color: var(--dark);
}
.cin-gold:hover .cin-arrow {
  background: rgba(14,11,8,.18);
  border-color: rgba(14,11,8,.3);
  color: var(--dark);
}
.cin-gold .cin-live {
  background: var(--sage);
  color: var(--gold-light);
}
.cin-gold .cin-live-dot { background: var(--gold-light); }
"""

# ═══════════════════════════════════════════════════════
# NEW JS — injected before </body>
# ═══════════════════════════════════════════════════════
new_js = """
<!-- ═══════════════════════════════════════════════════════
     CINEMATIC CTA ENGINE — Neuroscience-driven interaction
     ═══════════════════════════════════════════════════════ -->
<script>
(function(){
'use strict';

/* Particle palette */
const P_COLS = [
  'rgba(184,151,74,',
  'rgba(212,181,118,',
  'rgba(247,244,239,',
  'rgba(200,160,85,',
];
const MAX_P = 24;

function enhanceBtn(el, variant, showLive) {
  /* Grab text before clearing */
  const orig = el.querySelector('span');
  const label = orig ? orig.textContent.trim() : el.textContent.trim();

  /* Reset host element */
  el.style.overflow    = 'visible';
  el.style.background  = 'none';
  el.style.padding     = '0';
  el.style.display     = 'inline-flex';
  el.style.position    = 'relative';
  el.style.border      = 'none';
  el.style.outline     = 'none';

  /* ── DOM STRUCTURE ── */
  const canvas  = document.createElement('canvas');
  canvas.className = 'cin-canvas';
  canvas.width  = 440; canvas.height = 100;

  const live = document.createElement('div');
  live.className = 'cin-live';
  live.innerHTML = '<span class="cin-live-dot"></span>Noch 3 Termine frei';

  /* Arrow SVG */
  const arrowSVG = `<svg viewBox="0 0 14 10" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0.5 5h13M9 1l4 4-4 4" stroke="currentColor" stroke-width="1.3"
      stroke-linecap="round" stroke-linejoin="round"/>
  </svg>`;

  const surface = document.createElement('div');
  surface.className = 'cin-surface';
  surface.innerHTML = `
    <div class="cin-scan"></div>
    <div class="cin-edge"></div>
    <div class="cin-sheen"></div>
    <div class="cin-fill"></div>
    <div class="cin-flash"></div>
    <span class="cin-text">${label}</span>
    <div class="cin-arrow">${arrowSVG}</div>
  `;

  const wrap = document.createElement('div');
  wrap.className = 'cin-wrap cin-' + variant;
  wrap.appendChild(canvas);
  if (showLive) wrap.appendChild(live);
  wrap.appendChild(surface);

  el.innerHTML = '';
  el.appendChild(wrap);

  /* ── PARTICLE ENGINE ── */
  const ctx   = canvas.getContext('2d');
  let   parts = [];
  let   raf   = null;
  let   alive = false;

  function spawn() {
    const col = P_COLS[Math.floor(Math.random() * P_COLS.length)];
    const cw  = canvas.width;
    parts.push({
      x   : cw * .15 + Math.random() * cw * .7,
      y   : canvas.height - 2,
      vx  : (Math.random() - .5) * .9,
      vy  : -(1.4 + Math.random() * 2.4),
      life: 1,
      dec : .014 + Math.random() * .018,
      r   : .9 + Math.random() * 2.1,
      col,
      wob : Math.random() * Math.PI * 2,
      ws  : .045 + Math.random() * .04,
    });
  }

  function tick() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (alive && parts.length < MAX_P && Math.random() < .48) spawn();

    parts = parts.filter(p => p.life > 0);
    parts.forEach(p => {
      p.wob += p.ws;
      p.x   += p.vx + Math.sin(p.wob) * .4;
      p.y   += p.vy;
      p.vy  *= .983;
      p.life -= p.dec;
      const a = Math.min(1, p.life * 2) * p.life;

      /* Core dot */
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r * Math.max(0, p.life), 0, Math.PI * 2);
      ctx.fillStyle = p.col + a + ')';
      ctx.fill();

      /* Soft halo */
      if (p.r > 1.3) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r * Math.max(0, p.life) * 2.8, 0, Math.PI * 2);
        ctx.fillStyle = p.col + (a * .12) + ')';
        ctx.fill();
      }
    });

    if (alive || parts.length > 0) raf = requestAnimationFrame(tick);
    else raf = null;
  }

  /* ── 3D TILT + MAGNETIC CURSOR ── */
  wrap.addEventListener('mousemove', function(e) {
    const r  = wrap.getBoundingClientRect();
    const cx = r.left + r.width  / 2;
    const cy = r.top  + r.height / 2;
    const dx = (e.clientX - cx) / (r.width  / 2);   /* -1 … +1 */
    const dy = (e.clientY - cy) / (r.height / 2);

    /* Perspective tilt (max 5° / 3.5°) */
    el.style.transform = `
      perspective(700px)
      rotateY(${dx * 5}deg)
      rotateX(${-dy * 3.5}deg)
      translateY(-2px)
    `;

    /* Radial glow position */
    const px = ((e.clientX - r.left) / r.width  * 100).toFixed(1) + '%';
    const py = ((e.clientY - r.top)  / r.height * 100).toFixed(1) + '%';
    surface.style.setProperty('--bx', px);
    surface.style.setProperty('--by', py);
  });

  wrap.addEventListener('mouseenter', function() {
    alive = true;
    if (!raf) tick();
  });

  wrap.addEventListener('mouseleave', function() {
    alive = false;
    el.style.transform = '';
    surface.style.removeProperty('--bx');
    surface.style.removeProperty('--by');
    /* Particles die out naturally */
    setTimeout(function() {
      if (!alive && parts.length === 0 && raf) {
        cancelAnimationFrame(raf); raf = null;
      }
    }, 1200);
  });

  /* ── CLICK FLASH + BURST ── */
  wrap.addEventListener('click', function() {
    const flash = surface.querySelector('.cin-flash');
    if (flash) {
      flash.style.opacity = '.5';
      for (let i = 0; i < 10; i++) spawn();
      setTimeout(function(){ flash.style.opacity = '0'; }, 160);
    }
  });
}

/* ── INIT ── */
function init() {
  document.querySelectorAll('a.btn-p').forEach(function(el) {
    enhanceBtn(el, 'sage', false);
  });
  document.querySelectorAll('a.cta-main').forEach(function(el) {
    enhanceBtn(el, 'gold', true);
  });
}

document.readyState === 'loading'
  ? document.addEventListener('DOMContentLoaded', init)
  : init();
})();
</script>
"""

# ── Apply patches ──
# 1. CSS before </style>  (first occurrence)
content = content.replace('</style>', new_css + '\n</style>', 1)

# 2. JS before </body>
content = content.replace('</body>', new_js + '\n</body>', 1)

with open('/sessions/zealous-trusting-euler/mnt/outputs/dr-fetai-cinematic-cta.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Done — {len(content):,} chars written to dr-fetai-cinematic-cta.html")
