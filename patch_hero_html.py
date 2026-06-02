"""
Patch redesign_services.py:
  Replace AI_HERO_HTML, ECOM_HERO_HTML, MKT_HERO_HTML
  with the new Build Monitor style hero sections.
"""

import re

BUILD_MONITOR_TEMPLATE = '''  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <!-- LEFT SIDE -->
        <div>
          <div class="hero-eyebrow">
            <div class="hero-eyebrow-dot"></div>
            {EYEBROW}
          </div>

          <h1 class="hero-h1">{H1}</h1>

          <p class="hero-sub">{SUB}</p>

          <div class="hero-btns">
            <a href="#cta" class="hero-btn-primary">Start a Project &rarr;</a>
            <a href="../Home/homepage.html#cases" class="hero-btn-secondary">View our work &darr;</a>
          </div>
        </div>

        <!-- RIGHT SIDE: BUILD MONITOR -->
        <div class="dev-flow" id="pipeline-container">
          <div class="build-monitor" id="build-monitor">
            <!-- MacOS chrome bar -->
            <div class="bm-chrome">
              <div class="bm-dots"><span></span><span></span><span></span></div>
              <div class="bm-url">{URL}</div>
              <div class="bm-live"><div class="bm-live-dot"></div>LIVE</div>
            </div>

            <!-- Body -->
            <div class="bm-body">
              <div class="bm-header-row">
                <span class="bm-section-label">{PIPELINE_LABEL}</span>
                <span class="bm-cycle-badge" id="bm-cycle">Cycle 1</span>
              </div>

              <!-- Progress bar -->
              <div class="bm-progress-row">
                <div class="bm-progress-track">
                  <div class="bm-progress-fill" id="bm-fill"></div>
                </div>
                <span class="bm-pct" id="bm-pct">0%</span>
              </div>
              <div class="bm-status-msg" id="bm-status">{INIT_MSG}</div>

              <!-- Steps -->
              <div class="bm-steps">
{STEPS}
              </div>

              <!-- Metrics footer -->
              <div class="bm-metrics">
{METRICS}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

def make_step(idx, label):
    return f'''                <div class="bm-step bm-pending" id="bm-s{idx}">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">{label}</div>
                  <div class="bm-step-time" id="bm-t{idx}"></div>
                </div>'''

def make_metric(idx, val, label):
    return f'''                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m{idx}">{val}</span>
                  <span class="bm-metric-lbl">{label}</span>
                </div>'''

# ── AI Solutions ──────────────────────────────────────────────────────────────
AI_STEPS = [
    "Data Ingestion &amp; Cleaning",
    "Vector Embedding Pipeline",
    "LLM Fine-Tuning &amp; RAG",
    "Agent Workflow Design",
    "Safety &amp; Guardrail Layer",
    "Live AI System Deploy",
]
AI_METRICS = [
    ("—", "Accuracy"),
    ("—", "Latency"),
    ("—", "Uptime"),
]

AI_HERO = BUILD_MONITOR_TEMPLATE.format(
    EYEBROW="AI &amp; INTELLIGENT AUTOMATION",
    H1='We Build <em>Autonomous. Intelligent.</em> Agents.',
    SUB="Leverage cutting-edge LLMs, secure RAG databases, and agentic workflows to automate your operations and scale business productivity.",
    URL="ai.pipeline — globotechsolutions.com",
    PIPELINE_LABEL="AI Build Pipeline",
    INIT_MSG="Initializing AI environment...",
    STEPS="\n".join(make_step(i, l) for i, l in enumerate(AI_STEPS)),
    METRICS="\n".join(make_metric(i, v, l) for i, (v, l) in enumerate(AI_METRICS)),
)

# ── E-Commerce ────────────────────────────────────────────────────────────────
ECOM_STEPS = [
    "Operational Audit &amp; Scoping",
    "Storefront Design &amp; UX",
    "Cart &amp; Checkout Engineering",
    "Third-Party API Integrations",
    "Payment QA &amp; Security",
    "Live Storefront Launch",
]
ECOM_METRICS = [
    ("—", "Conversion"),
    ("—", "Load Time"),
    ("—", "Uptime"),
]

ECOM_HERO = BUILD_MONITOR_TEMPLATE.format(
    EYEBROW="E-COMMERCE DEVELOPMENT",
    H1='We Build <em>Scalable. Profitable.</em> Stores.',
    SUB="From custom Shopify builds to headless commerce — we engineer end-to-end storefronts that convert visitors into loyal customers.",
    URL="store.pipeline — globotechsolutions.com",
    PIPELINE_LABEL="Store Build Pipeline",
    INIT_MSG="Initializing store environment...",
    STEPS="\n".join(make_step(i, l) for i, l in enumerate(ECOM_STEPS)),
    METRICS="\n".join(make_metric(i, v, l) for i, (v, l) in enumerate(ECOM_METRICS)),
)

# ── Digital Marketing ─────────────────────────────────────────────────────────
MKT_STEPS = [
    "Audience Research &amp; ICP",
    "SEO &amp; Content Strategy",
    "Paid Media Campaign Setup",
    "Creative &amp; Ad Copy",
    "Analytics &amp; Tracking",
    "Live Campaign Launch",
]
MKT_METRICS = [
    ("—", "ROAS"),
    ("—", "CTR"),
    ("—", "CPA"),
]

MKT_HERO = BUILD_MONITOR_TEMPLATE.format(
    EYEBROW="DIGITAL MARKETING &amp; GROWTH",
    H1='We Run <em>Data-Driven. High-ROI.</em> Campaigns.',
    SUB="From SEO to paid acquisition — we design growth engines that attract qualified leads, reduce CAC, and maximise return on ad spend.",
    URL="campaign.pipeline — globotechsolutions.com",
    PIPELINE_LABEL="Campaign Pipeline",
    INIT_MSG="Initializing campaign environment...",
    STEPS="\n".join(make_step(i, l) for i, l in enumerate(MKT_STEPS)),
    METRICS="\n".join(make_metric(i, v, l) for i, (v, l) in enumerate(MKT_METRICS)),
)

# ── Patch file ─────────────────────────────────────────────────────────────────
with open("redesign_services.py", "r", encoding="utf-8") as f:
    src = f.read()

def replace_constant(src, const_name, new_value):
    # Match:  CONST_NAME = """..."""  (multiline, non-greedy)
    pattern = re.compile(
        rf'({re.escape(const_name)}\s*=\s*""").*?(""")',
        re.DOTALL
    )
    replacement = rf'\g<1>{new_value}\g<2>'
    result, n = pattern.subn(replacement, src, count=1)
    if n == 0:
        print(f"  WARNING: {const_name} not found — skipped")
    else:
        print(f"  Patched {const_name} OK")
    return result

src = replace_constant(src, "AI_HERO_HTML", "\n" + AI_HERO + "\n")
src = replace_constant(src, "ECOM_HERO_HTML", "\n" + ECOM_HERO + "\n")
src = replace_constant(src, "MKT_HERO_HTML", "\n" + MKT_HERO + "\n")

with open("redesign_services.py", "w", encoding="utf-8") as f:
    f.write(src)

print("redesign_services.py patched successfully.")
