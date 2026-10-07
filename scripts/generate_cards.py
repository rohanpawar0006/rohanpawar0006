#!/usr/bin/env python3
"""
Title Sequence Profile Asset Generator
Converts fonts (Bebas Neue, Inter, JetBrains Mono) directly into vector SVG paths.
Produces self-contained, pixel-perfect SVGs with no external CSS or web font dependencies.
Palette:
  Background: near-black #0A0A0A (cards #121212, hairline borders #262626)
  Text: warm off-white #F2EDE4, muted text #8A857C
  Single Accent: ember orange #E8643A
"""

import os
import sys
import base64
import matplotlib.font_manager as fm
from matplotlib.textpath import TextPath
from matplotlib.path import Path

FONTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fonts'))
ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets'))
SCREENSHOTS_DIR = os.path.join(ASSETS_DIR, 'screenshots')

DISPLAY_FONT = os.path.join(FONTS_DIR, 'BebasNeue.ttf')
SANS_FONT = os.path.join(FONTS_DIR, 'Inter.ttf')
MONO_FONT = os.path.join(FONTS_DIR, 'JetBrainsMono.ttf')

def text_to_svg_path(text, font_path, size, x=0, y=0):
    """Bake text string into an SVG path d string using exact font outlines."""
    prop = fm.FontProperties(fname=os.path.abspath(font_path), size=size)
    tp = TextPath((0, 0), text, prop=prop)
    cmds = []
    i = 0
    verts = tp.vertices
    codes = tp.codes
    if codes is None:
        return ""
    while i < len(codes):
        code = codes[i]
        if code == Path.MOVETO:
            cmds.append(f"M {verts[i][0] + x:.2f} {-verts[i][1] + y:.2f}")
            i += 1
        elif code == Path.LINETO:
            cmds.append(f"L {verts[i][0] + x:.2f} {-verts[i][1] + y:.2f}")
            i += 1
        elif code == Path.CURVE3:
            cmds.append(f"Q {verts[i][0] + x:.2f} {-verts[i][1] + y:.2f} {verts[i+1][0] + x:.2f} {-verts[i+1][1] + y:.2f}")
            i += 2
        elif code == Path.CURVE4:
            cmds.append(f"C {verts[i][0] + x:.2f} {-verts[i][1] + y:.2f} {verts[i+1][0] + x:.2f} {-verts[i+1][1] + y:.2f} {verts[i+2][0] + x:.2f} {-verts[i+2][1] + y:.2f}")
            i += 3
        elif code == Path.CLOSEPOLY:
            cmds.append("Z")
            i += 1
        else:
            i += 1
    return " ".join(cmds)

def get_text_width(text, font_path, size):
    prop = fm.FontProperties(fname=os.path.abspath(font_path), size=size)
    tp = TextPath((0, 0), text, prop=prop)
    if len(tp.vertices) == 0:
        return 0
    return tp.vertices[:, 0].max() - tp.vertices[:, 0].min()

def generate_hero_svg():
    """Generate 1200x520 Hero Title Card SVG."""
    width, height = 1200, 520

    # Bake typography into paths
    header_meta = text_to_svg_path("PROD. 2026 // TITLE SEQUENCE // ACT I", MONO_FONT, 13, 60, 65)
    timecode_meta = text_to_svg_path("TC 00:01:24:08", MONO_FONT, 13, 1020, 65)

    name_path = text_to_svg_path("ROHAN PAWAR", DISPLAY_FONT, 140, 60, 240)
    
    positioning_path = text_to_svg_path(
        "I build AI systems from first principles: retrieval, vision and the pipelines around them.",
        SANS_FONT, 20.5, 60, 345
    )

    label_row_1 = text_to_svg_path("AI / ML ENGINEER IN THE MAKING", MONO_FONT, 13.5, 60, 420)
    label_sep = text_to_svg_path("—", MONO_FONT, 13.5, 345, 420)
    label_row_2 = text_to_svg_path("RAG  ·  COMPUTER VISION  ·  DATA PIPELINES", MONO_FONT, 13.5, 375, 420)

    grad_degree = text_to_svg_path("FINAL-YEAR B.E. (AI/ML & DS) // SVCE '27", MONO_FONT, 12, 60, 465)
    intern_status = text_to_svg_path("OPEN TO INTERNSHIPS", MONO_FONT, 12, 975, 465)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <!-- Cinematic Vignette & Grain simulation -->
    <radialGradient id="vignette" cx="50%" cy="50%" r="70%">
      <stop offset="40%" stop-color="#121212" stop-opacity="0" />
      <stop offset="100%" stop-color="#050505" stop-opacity="0.8" />
    </radialGradient>
    <linearGradient id="ember-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E8643A" />
      <stop offset="60%" stop-color="#E8643A" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#E8643A" stop-opacity="0.1" />
    </linearGradient>
  </defs>

  <!-- Solid Dark Frame (#0A0A0A) - Consistent in Light/Dark Mode -->
  <rect width="{width}" height="{height}" rx="14" fill="#0A0A0A" />
  <rect width="{width}" height="{height}" rx="14" fill="url(#vignette)" />
  <rect width="{width}" height="{height}" rx="14" fill="none" stroke="#262626" stroke-width="1.2" />

  <!-- Top Metadata Bar -->
  <path d="{header_meta}" fill="#8A857C" />
  <path d="{timecode_meta}" fill="#8A857C" />
  <line x1="60" y1="85" x2="1140" y2="85" stroke="#1A1A1A" stroke-width="1" />

  <!-- Hero Name in Vectorized Bebas Neue -->
  <path d="{name_path}" fill="#F2EDE4" />

  <!-- Ember Accent Rule with One Subtle Slow Animation -->
  <line x1="60" y1="285" x2="1140" y2="285" stroke="url(#ember-glow)" stroke-width="1.8" stroke-dasharray="1080" stroke-dashoffset="1080">
    <animate attributeName="stroke-dashoffset" from="1080" to="0" dur="2.4s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1.0" />
  </line>

  <!-- Ember Accent Indicator Dot -->
  <circle cx="64" cy="285" r="3" fill="#E8643A">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="3s" repeatCount="indefinite" />
  </circle>

  <!-- Positioning Line in Vectorized Inter -->
  <path d="{positioning_path}" fill="#F2EDE4" />

  <!-- Mono Label Row -->
  <path d="{label_row_1}" fill="#E8643A" />
  <path d="{label_sep}" fill="#8A857C" />
  <path d="{label_row_2}" fill="#8A857C" />

  <!-- Bottom Details Rule -->
  <line x1="60" y1="440" x2="1140" y2="440" stroke="#1A1A1A" stroke-width="1" />
  <path d="{grad_degree}" fill="#8A857C" />
  <circle cx="960" cy="461" r="3.5" fill="#E8643A" />
  <path d="{intern_status}" fill="#E8643A" />
</svg>"""
    return svg

def generate_vaultmind_card():
    """Generate 1200x620 VaultMind-RAG poster card SVG."""
    width, height = 1200, 620

    # Typography paths
    scene_label = text_to_svg_path("SCENE 01 // PRODUCTION RETRIEVAL", MONO_FONT, 12.5, 60, 65)
    title_path = text_to_svg_path("VAULTMIND-RAG", DISPLAY_FONT, 64, 60, 135)
    
    pitch_path = text_to_svg_path(
        "Custom RAG assistant for Obsidian vaults, built without LangChain or LlamaIndex on purpose.",
        SANS_FONT, 16, 60, 180
    )

    # Bullet mechanics
    b1_label = text_to_svg_path("DETERMINISTIC PIPELINE", MONO_FONT, 11, 80, 225)
    b1_body = text_to_svg_path("Sanitise notes (strip frontmatter/wikilinks) -> sliding chunker (~1200 chars, 200 overlap)", SANS_FONT, 13.5, 80, 248)

    b2_label = text_to_svg_path("LOCAL DENSE EMBEDDINGS", MONO_FONT, 11, 80, 290)
    b2_body = text_to_svg_path("sentence-transformers all-MiniLM-L6-v2 running locally -> ChromaDB vector store", SANS_FONT, 13.5, 80, 313)

    b3_label = text_to_svg_path("STRICT GROUNDING & REFUSAL", MONO_FONT, 11, 80, 355)
    b3_body = text_to_svg_path("Cosine similarity threshold fallback -> Gemini Flash with source note citations", SANS_FONT, 13.5, 80, 378)

    tags_label = text_to_svg_path("TECH STACK", MONO_FONT, 11, 60, 440)
    tags_body = text_to_svg_path("Python  ·  sentence-transformers  ·  ChromaDB  ·  Gemini Flash  ·  Streamlit", MONO_FONT, 13.5, 60, 468)

    metric_label = text_to_svg_path("VERIFIED CORPUS & METRIC SLOT", MONO_FONT, 11, 60, 520)
    metric_body = text_to_svg_path("Ships with 18-note sample vault  ·  [ADD REAL NUMBER: retrieval latency ms / indexing time]", MONO_FONT, 13, 60, 548)

    action_hint = text_to_svg_path("VIEW SOURCE REPO ->", MONO_FONT, 12, 60, 588)

    # Movie still label
    still_meta = text_to_svg_path("FRAME 01 // OBSIDIAN-DARK STREAMLIT UI", MONO_FONT, 11, 670, 75)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#262626" />
      <stop offset="50%" stop-color="#333333" />
      <stop offset="100%" stop-color="#1A1A1A" />
    </linearGradient>
    <clipPath id="still-clip">
      <rect x="660" y="90" width="480" height="480" rx="8" />
    </clipPath>
  </defs>

  <!-- Card Background #121212, hairline border #262626 -->
  <rect width="{width}" height="{height}" rx="12" fill="#121212" />
  <rect width="{width}" height="{height}" rx="12" fill="none" stroke="url(#card-border)" stroke-width="1.2" />

  <!-- LEFT SECTION: Narrative & Architecture -->
  <path d="{scene_label}" fill="#E8643A" />
  <path d="{title_path}" fill="#F2EDE4" />
  <path d="{pitch_path}" fill="#8A857C" />

  <!-- Hairline divider -->
  <line x1="60" y1="198" x2="620" y2="198" stroke="#1F1F1F" stroke-width="1" />

  <!-- Bullets with ember line tick -->
  <line x1="64" y1="215" x2="64" y2="250" stroke="#E8643A" stroke-width="2" />
  <path d="{b1_label}" fill="#E8643A" />
  <path d="{b1_body}" fill="#F2EDE4" />

  <line x1="64" y1="280" x2="64" y2="315" stroke="#E8643A" stroke-width="2" />
  <path d="{b2_label}" fill="#E8643A" />
  <path d="{b2_body}" fill="#F2EDE4" />

  <line x1="64" y1="345" x2="64" y2="380" stroke="#E8643A" stroke-width="2" />
  <path d="{b3_label}" fill="#E8643A" />
  <path d="{b3_body}" fill="#F2EDE4" />

  <!-- Tech tags as simple clean text -->
  <path d="{tags_label}" fill="#8A857C" />
  <path d="{tags_body}" fill="#F2EDE4" />

  <!-- Metric slot -->
  <path d="{metric_label}" fill="#8A857C" />
  <path d="{metric_body}" fill="#E8643A" />

  <path d="{action_hint}" fill="#F2EDE4" />

  <!-- RIGHT SECTION: Movie Still / App Screenshot Frame -->
  <path d="{still_meta}" fill="#8A857C" />

  <!-- Movie still frame container -->
  <rect x="660" y="90" width="480" height="480" rx="8" fill="#0A0A0A" stroke="#262626" stroke-width="1" />

  <g clip-path="url(#still-clip)">
    <!-- App UI Mockup Still -->
    <!-- Window Titlebar -->
    <rect x="660" y="90" width="480" height="36" fill="#171717" />
    <circle cx="682" cy="108" r="4.5" fill="#333333" />
    <circle cx="698" cy="108" r="4.5" fill="#333333" />
    <circle cx="714" cy="108" r="4.5" fill="#333333" />
    <line x1="660" y1="126" x2="1140" y2="126" stroke="#262626" stroke-width="1" />

    <!-- Sidebar in UI -->
    <rect x="660" y="126" width="140" height="444" fill="#0F0F0F" stroke="#262626" stroke-width="1" />
    <rect x="675" y="145" width="110" height="18" rx="3" fill="#1C1C1C" />
    <text x="682" y="158" fill="#8A857C" font-family="monospace" font-size="9">OBSIDIAN VAULT</text>
    <text x="675" y="185" fill="#666666" font-family="monospace" font-size="8.5">Index: 18 notes</text>
    <text x="675" y="205" fill="#666666" font-family="monospace" font-size="8.5">Chunks: 74</text>
    <text x="675" y="225" fill="#E8643A" font-family="monospace" font-size="8.5">Threshold: 0.68</text>

    <!-- Main Chat Feed -->
    <rect x="815" y="145" width="310" height="46" rx="6" fill="#171717" stroke="#262626" stroke-width="1" />
    <text x="828" y="165" fill="#8A857C" font-family="monospace" font-size="8.5">&gt; user query</text>
    <text x="828" y="180" fill="#F2EDE4" font-family="sans-serif" font-size="9.5">How does Raft handle leader crashes in our notes?</text>

    <!-- Pipeline Retrieval Badge -->
    <rect x="815" y="202" width="220" height="20" rx="3" fill="#1F1511" stroke="#E8643A" stroke-width="0.8" />
    <text x="825" y="215" fill="#E8643A" font-family="monospace" font-size="8">✓ CHROMA COSINE SIM: 0.812 (PASSED)</text>

    <!-- Response Block -->
    <rect x="815" y="232" width="310" height="190" rx="6" fill="#141414" stroke="#262626" stroke-width="1" />
    <text x="828" y="255" fill="#8A857C" font-family="monospace" font-size="8.5">GROUNDED SYNTHESIS (GEMINI FLASH):</text>
    
    <text x="828" y="280" fill="#F2EDE4" font-family="sans-serif" font-size="10">From [[consensus-protocols.md#failover]]:</text>
    <text x="828" y="304" fill="#8A857C" font-family="sans-serif" font-size="9.5">1. Followers transition to Candidate upon election</text>
    <text x="828" y="322" fill="#8A857C" font-family="sans-serif" font-size="9.5">   timeout (randomized 150-300ms window).</text>
    <text x="828" y="344" fill="#8A857C" font-family="sans-serif" font-size="9.5">2. Term counter increments; votes requested.</text>

    <line x1="828" y1="365" x2="1110" y2="365" stroke="#222222" stroke-width="1" />
    <text x="828" y="388" fill="#E8643A" font-family="monospace" font-size="8.5">SOURCE CITATION: [[consensus-protocols.md]]</text>
    <text x="828" y="405" fill="#666666" font-family="monospace" font-size="8">Grounding check: strict threshold fallback active</text>

    <!-- Film still metadata footer -->
    <rect x="815" y="435" width="310" height="30" rx="4" fill="#111111" />
    <text x="825" y="454" fill="#8A857C" font-family="monospace" font-size="8.5">TAKE: PROD_RAG_V1 // STREAMLIT ENGINE</text>
  </g>
</svg>"""
    return svg

def generate_signbridge_card():
    """Generate 1200x620 SignBridge AI poster card SVG."""
    width, height = 1200, 620

    # Typography paths
    scene_label = text_to_svg_path("SCENE 02 // COMPUTER VISION & MULTIMODAL", MONO_FONT, 12.5, 60, 65)
    title_path = text_to_svg_path("SIGNBRIDGE AI", DISPLAY_FONT, 64, 60, 135)
    
    sub_pitch = text_to_svg_path("Bridging Signs and Speech", MONO_FONT, 14, 450, 130)

    pitch_path = text_to_svg_path(
        "Real-time bidirectional Indian Sign Language communication platform.",
        SANS_FONT, 16, 60, 180
    )

    # Bullet mechanics
    b1_label = text_to_svg_path("SIGN -> TEXT / SPEECH", MONO_FONT, 11, 80, 225)
    b1_body = text_to_svg_path("MediaPipe hand mesh -> PyTorch Bi-LSTM (16 ISL words) + 36-class alphabet/digit classifier", SANS_FONT, 13.5, 80, 248)

    b2_label = text_to_svg_path("SPEECH / TEXT -> SIGN PLAYBACK", MONO_FONT, 11, 80, 290)
    b2_body = text_to_svg_path("Spoken voice parsed into animated sign sequences for two-way conversation mode", SANS_FONT, 13.5, 80, 313)

    b3_label = text_to_svg_path("FULL ACCESSIBILITY SUITE", MONO_FONT, 11, 80, 355)
    b3_body = text_to_svg_path("Interactive ISL dictionary + gamified practice mode for non-signers to learn", SANS_FONT, 13.5, 80, 378)

    tags_label = text_to_svg_path("TECH STACK", MONO_FONT, 11, 60, 440)
    tags_body = text_to_svg_path("PyTorch  ·  MediaPipe  ·  Bi-LSTM  ·  React + Vite  ·  Render  ·  Vercel", MONO_FONT, 13.5, 60, 468)

    metric_label = text_to_svg_path("VERIFIED CORPUS & METRIC SLOT", MONO_FONT, 11, 60, 520)
    metric_body = text_to_svg_path("16 Dynamic ISL Words  ·  36 Static Classes  ·  [ADD REAL NUMBER: inference FPS / latency ms]", MONO_FONT, 13, 60, 548)

    action_hint = text_to_svg_path("VIEW SOURCE REPO & LIVE DEMO ->", MONO_FONT, 12, 60, 588)

    # Movie still label
    still_meta = text_to_svg_path("FRAME 02 // REAL-TIME LANDMARK INFERENCE", MONO_FONT, 11, 670, 75)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
  <defs>
    <linearGradient id="sb-card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#262626" />
      <stop offset="50%" stop-color="#333333" />
      <stop offset="100%" stop-color="#1A1A1A" />
    </linearGradient>
    <clipPath id="sb-still-clip">
      <rect x="660" y="90" width="480" height="480" rx="8" />
    </clipPath>
  </defs>

  <!-- Card Background #121212, hairline border #262626 -->
  <rect width="{width}" height="{height}" rx="12" fill="#121212" />
  <rect width="{width}" height="{height}" rx="12" fill="none" stroke="url(#sb-card-border)" stroke-width="1.2" />

  <!-- LEFT SECTION: Narrative & Architecture -->
  <path d="{scene_label}" fill="#E8643A" />
  <path d="{title_path}" fill="#F2EDE4" />
  <path d="{sub_pitch}" fill="#E8643A" />
  <path d="{pitch_path}" fill="#8A857C" />

  <!-- Hairline divider -->
  <line x1="60" y1="198" x2="620" y2="198" stroke="#1F1F1F" stroke-width="1" />

  <!-- Bullets with ember line tick -->
  <line x1="64" y1="215" x2="64" y2="250" stroke="#E8643A" stroke-width="2" />
  <path d="{b1_label}" fill="#E8643A" />
  <path d="{b1_body}" fill="#F2EDE4" />

  <line x1="64" y1="280" x2="64" y2="315" stroke="#E8643A" stroke-width="2" />
  <path d="{b2_label}" fill="#E8643A" />
  <path d="{b2_body}" fill="#F2EDE4" />

  <line x1="64" y1="345" x2="64" y2="380" stroke="#E8643A" stroke-width="2" />
  <path d="{b3_label}" fill="#E8643A" />
  <path d="{b3_body}" fill="#F2EDE4" />

  <!-- Tech tags as simple clean text -->
  <path d="{tags_label}" fill="#8A857C" />
  <path d="{tags_body}" fill="#F2EDE4" />

  <!-- Metric slot -->
  <path d="{metric_label}" fill="#8A857C" />
  <path d="{metric_body}" fill="#E8643A" />

  <path d="{action_hint}" fill="#F2EDE4" />

  <!-- RIGHT SECTION: Movie Still / App Screenshot Frame -->
  <path d="{still_meta}" fill="#8A857C" />

  <!-- Movie still frame container -->
  <rect x="660" y="90" width="480" height="480" rx="8" fill="#0A0A0A" stroke="#262626" stroke-width="1" />

  <g clip-path="url(#sb-still-clip)">
    <!-- Window Titlebar -->
    <rect x="660" y="90" width="480" height="36" fill="#171717" />
    <circle cx="682" cy="108" r="4.5" fill="#333333" />
    <circle cx="698" cy="108" r="4.5" fill="#333333" />
    <circle cx="714" cy="108" r="4.5" fill="#333333" />
    <text x="730" y="112" fill="#8A857C" font-family="monospace" font-size="9.5">SIGNBRIDGE // LIVE CAMERA INFERENCE</text>
    <line x1="660" y1="126" x2="1140" y2="126" stroke="#262626" stroke-width="1" />

    <!-- Simulated Camera Viewport -->
    <rect x="680" y="145" width="440" height="230" rx="6" fill="#080808" stroke="#1F1F1F" stroke-width="1" />

    <!-- Landmark Mesh Outline -->
    <path d="M 900 320 L 900 240 L 860 190 M 900 240 L 900 160 M 900 240 L 945 180 M 900 240 L 980 215" stroke="#E8643A" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.9" />
    <circle cx="900" cy="320" r="7" fill="#E8643A" />
    <circle cx="900" cy="240" r="5" fill="#F2EDE4" />
    <circle cx="860" cy="190" r="5" fill="#F2EDE4" />
    <circle cx="900" cy="160" r="5" fill="#F2EDE4" />
    <circle cx="945" cy="180" r="5" fill="#F2EDE4" />
    <circle cx="980" cy="215" r="5" fill="#F2EDE4" />

    <!-- Camera HUD Tags -->
    <rect x="695" y="160" width="96" height="22" rx="3" fill="#171717" fill-opacity="0.9" />
    <circle cx="706" cy="171" r="3" fill="#E8643A" />
    <text x="716" y="175" fill="#F2EDE4" font-family="monospace" font-size="8.5">LIVE TRACK</text>

    <!-- Two-Way Live Prediction Card -->
    <rect x="680" y="390" width="440" height="60" rx="6" fill="#141414" stroke="#262626" stroke-width="1" />
    <text x="696" y="412" fill="#E8643A" font-family="monospace" font-size="9">ISL GESTURE CLASSIFIED:</text>
    <text x="696" y="434" fill="#F2EDE4" font-family="sans-serif" font-size="14" font-weight="bold">"Namaste / Hello"  ->  [Synthetic Voice Output]</text>

    <!-- Bottom Dialogue Mode Bar -->
    <rect x="680" y="465" width="440" height="35" rx="4" fill="#0F0F0F" stroke="#1A1A1A" stroke-width="1" />
    <text x="696" y="487" fill="#8A857C" font-family="monospace" font-size="9">MODE: TWO-WAY CONVERSATION (SPEECH &lt;=&gt; SIGN)</text>
  </g>
</svg>"""
    return svg

def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    print("Generating Hero Title Card (assets/hero.svg)...")
    hero_svg = generate_hero_svg()
    with open(os.path.join(ASSETS_DIR, 'hero.svg'), 'w', encoding='utf-8') as f:
        f.write(hero_svg)

    print("Generating VaultMind Card (assets/card-vaultmind.svg)...")
    vm_svg = generate_vaultmind_card()
    with open(os.path.join(ASSETS_DIR, 'card-vaultmind.svg'), 'w', encoding='utf-8') as f:
        f.write(vm_svg)

    print("Generating SignBridge Card (assets/card-signbridge.svg)...")
    sb_svg = generate_signbridge_card()
    with open(os.path.join(ASSETS_DIR, 'card-signbridge.svg'), 'w', encoding='utf-8') as f:
        f.write(sb_svg)

    print("All SVGs successfully generated with baked vector font paths.")

if __name__ == '__main__':
    main()
