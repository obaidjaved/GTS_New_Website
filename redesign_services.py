import os
import re

WORKSPACE_DIR = r"d:\new-globotech-website-main"
SRC_DIR = os.path.join(WORKSPACE_DIR, "src")
SOURCE_PAGE_PATH = os.path.join(SRC_DIR, "Web-Dev", "web-development.html")

def extract_nav_html_block(content):
    start_idx = content.find('<div class="nav-wrap">')
    if start_idx == -1:
        start_idx = content.find('<div class="nav-wrap"')
    if start_idx == -1:
        return None
    
    idx = start_idx
    depth = 0
    while idx < len(content):
        if content[idx:idx+4] == '<div':
            depth += 1
            idx += 4
        elif content[idx:idx+5] == '</div':
            depth -= 1
            idx += 5
            if depth == 0:
                end_idx = content.find('>', idx)
                if end_idx != -1:
                    return (start_idx, end_idx + 1)
        else:
            idx += 1
    return None

def extract_footer_html_block(content):
    start_idx = content.find('<footer')
    if start_idx == -1:
        return None
    end_tag = '</footer>'
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        return None
    return (start_idx, end_idx + len(end_tag))

def find_nav_js_block(content):
    start_idx = content.find('<script>')
    if start_idx == -1:
        return None
    end_idx = content.find('</script>', start_idx)
    if end_idx == -1:
        return None
    return (start_idx + len('<script>'), end_idx)

def strip_active_classes(nav_html):
    nav_html = re.sub(r'\s*class="active"', '', nav_html)
    nav_html = re.sub(r'class="mega-item\s+active"', 'class="mega-item"', nav_html)
    nav_html = re.sub(r'class="active\s+mega-item"', 'class="mega-item"', nav_html)
    return nav_html


# ─────────────────────────────────────────────────────────────────────────────
# 1. AI SOLUTIONS PAGE DATA
# ─────────────────────────────────────────────────────────────────────────────

AI_HERO_HTML = """
  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <!-- LEFT SIDE -->
        <div>
          <div class="hero-eyebrow">
            <div class="hero-eyebrow-dot"></div>
            AI &amp; INTELLIGENT AUTOMATION
          </div>

          <h1 class="hero-h1">We Build <em>Autonomous. Intelligent.</em> Agents.</h1>

          <p class="hero-sub">Leverage cutting-edge LLMs, secure RAG databases, and agentic workflows to automate your operations and scale business productivity.</p>

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
              <div class="bm-url">ai.pipeline — globotechsolutions.com</div>
              <div class="bm-live"><div class="bm-live-dot"></div>LIVE</div>
            </div>

            <!-- Body -->
            <div class="bm-body">
              <div class="bm-header-row">
                <span class="bm-section-label">AI Build Pipeline</span>
                <span class="bm-cycle-badge" id="bm-cycle">Cycle 1</span>
              </div>

              <!-- Progress bar -->
              <div class="bm-progress-row">
                <div class="bm-progress-track">
                  <div class="bm-progress-fill" id="bm-fill"></div>
                </div>
                <span class="bm-pct" id="bm-pct">0%</span>
              </div>
              <div class="bm-status-msg" id="bm-status">Initializing AI environment...</div>

              <!-- Steps -->
              <div class="bm-steps">
                <div class="bm-step bm-pending" id="bm-s0">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Data Ingestion &amp; Cleaning</div>
                  <div class="bm-step-time" id="bm-t0"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s1">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Vector Embedding Pipeline</div>
                  <div class="bm-step-time" id="bm-t1"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s2">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">LLM Fine-Tuning &amp; RAG</div>
                  <div class="bm-step-time" id="bm-t2"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s3">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Agent Workflow Design</div>
                  <div class="bm-step-time" id="bm-t3"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s4">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Safety &amp; Guardrail Layer</div>
                  <div class="bm-step-time" id="bm-t4"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s5">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Live AI System Deploy</div>
                  <div class="bm-step-time" id="bm-t5"></div>
                </div>
              </div>

              <!-- Metrics footer -->
              <div class="bm-metrics">
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m0">—</span>
                  <span class="bm-metric-lbl">Accuracy</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m1">—</span>
                  <span class="bm-metric-lbl">Latency</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m2">—</span>
                  <span class="bm-metric-lbl">Uptime</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

AI_SHOWCASE_HTML = """
  <!-- PREMIUM FEATURE SHOWCASE -->
  <section class="showcase-section reveal">
    <div class="showcase-glow-blob blob-1" id="showcase-glow"></div>

    <div class="container">
      <div class="showcase-header">
        <p class="section-eyebrow">OUR SPECIALIZATION</p>
        <h2 class="section-h2">Intelligent AI Solutions</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We build enterprise AI agents, semantic search structures, and secure automation pipelines that integrate cleanly into your codebase.
        </p>
      </div>

      <div class="showcase-layout">
        <!-- Tab Navigation (Left Column) -->
        <div class="specialty-tabs">

          <!-- Tab 1: Cognitive Agent -->
          <div class="specialty-tab-btn active" data-tab="sim-custom" data-theme="purple">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Cognitive Agents</span>
                <span class="tab-badge">Self-Reflecting</span>
              </div>
              <p class="tab-desc">Design multi-agent workflows that plan, search, and self-correct to execute complex business tasks.</p>
            </div>
          </div>

          <!-- Tab 2: Vector Search / RAG -->
          <div class="specialty-tab-btn" data-tab="sim-responsive" data-theme="cyan">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Vector RAG Search</span>
                <span class="tab-badge">High Accuracy</span>
              </div>
              <p class="tab-desc">Retrieve real-time company knowledge securely using semantic embedding queries.</p>
            </div>
          </div>

          <!-- Tab 3: Tokenizer -->
          <div class="specialty-tab-btn" data-tab="sim-cms" data-theme="green">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <polygon points="12 2 2 22 12 17 22 22 12 2"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Tokenization Pipeline</span>
                <span class="tab-badge">Data Preparation</span>
              </div>
              <p class="tab-desc">Tokenize raw unstructured datasets and generate high-dimensional vectors instantly.</p>
            </div>
          </div>

          <!-- Tab 4: Security Shield -->
          <div class="specialty-tab-btn" data-tab="sim-ecom" data-theme="orange">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">PII &amp; Safety Shield</span>
                <span class="tab-badge">Hardened Guard</span>
              </div>
              <p class="tab-desc">Inject real-time protection shields to mask PII data and block prompt injection attacks.</p>
            </div>
          </div>

        </div>

        <!-- Interactive Console Display (Right Column) -->
        <div class="console-container">
          <div class="console-screen">

            <!-- Panel 1: LLM Agent Builder -->
            <div class="simulator-panel active" id="sim-custom">
              <div class="ide-mock">
                <div class="ide-header">
                  <div class="ide-dots">
                    <span class="term-dot term-dot-r"></span>
                    <span class="term-dot term-dot-y"></span>
                    <span class="term-dot term-dot-g"></span>
                  </div>
                  <button class="ide-btn-run" id="btn-run-compiler">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor">
                      <polygon points="5 3 19 12 5 21 5 3" />
                    </svg>
                    Run Agent
                  </button>
                </div>
                <div class="ide-body">
                  <div class="ide-code-lines" style="display: flex; flex-direction: column; gap: 8px;">
                    <span style="color: #6e6e73;">// Prompt Input:</span>
                    <input type="text" id="agent-prompt-input" value="Research competitors and summarize pricing" style="background:#1a1c23; border: 1px solid rgba(255,255,255,0.08); border-radius: 6px; padding: 8px 12px; color: #fff; font-family: monospace; font-size: 11px; outline: none; width: 100%;" />
                  </div>
                  <div class="ide-console-out" id="ide-console" style="margin-top: 12px; height: 110px; overflow-y: auto;">
                    <p class="ide-line info">Click "Run Agent" above to initiate cognitive reasoning cycle...</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 2: Vector Search / RAG -->
            <div class="simulator-panel" id="sim-responsive">
              <div class="responsive-panel-wrap">
                <div style="display: flex; gap: 12px; align-items: center; width: 100%;">
                  <input type="text" id="rag-query" value="How do we handle GDPR compliance?" style="flex: 1; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 8px; padding: 10px 14px; font-family: monospace; font-size: 12px; outline: none; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" />
                  <button id="btn-run-rag" class="ide-btn-run" style="padding: 10px 20px; border-radius: 8px; background: #33c5f3;">Search Vector</button>
                </div>
                <div class="responsive-viewport-container" style="height: 220px;">
                  <div class="responsive-canvas" style="width: 100%; height: 100%; border: none; padding: 16px; display: flex; flex-direction: column; gap: 8px;" id="rag-results-box">
                    <p style="font-size: 11px; color: #8e8e93; font-family: monospace; margin: auto;">Enter a search query to pull similarity matches from database indexes.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 3: Tokenizer Dashboard -->
            <div class="simulator-panel" id="sim-cms">
              <div class="cms-panel-wrap" style="grid-template-columns: 1fr; width: 100%;">
                <div style="display: flex; flex-direction: column; gap: 10px; width: 100%;">
                  <textarea id="tokenizer-input" style="height: 60px; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 8px; padding: 10px; font-family: monospace; font-size: 11px; outline: none; resize: none;">Globotech Solutions delivers high-performance custom AI integrations.</textarea>
                  <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 11px; font-weight: 700; color: #6e6e73;" id="token-stats">Tokens: 0 | Dimensions: 1536</span>
                    <button id="btn-tokenize" class="ide-btn-run" style="background:#10b981; padding: 6px 14px; border-radius: 6px;">Tokenize</button>
                  </div>
                </div>
                <div class="cms-canvas-wrap" style="min-height: 140px; padding: 12px; margin-top: 10px; background: #fafbfc;">
                  <div class="cms-canvas-body" id="token-chips-container" style="flex-direction: row; flex-wrap: wrap; align-content: flex-start; gap: 6px;">
                    <div class="cms-canvas-empty" style="margin-top: 20px;">Click Tokenize to run BPE parser.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 4: Security Sandbox Guard -->
            <div class="simulator-panel" id="sim-ecom">
              <div class="ecom-panel-wrap" style="grid-template-columns: 1.1fr 0.9fr; gap: 20px;">
                <div class="ecom-checkout-card" style="padding: 16px; gap: 12px;">
                  <h4 class="ecom-checkout-title" style="font-size: 12px; margin: 0; padding-bottom: 6px;">Security Sandbox Rulebook</h4>
                  <div style="display: flex; flex-direction: column; gap: 10px;">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">PII Masking Filter</span>
                      <input type="checkbox" id="guard-pii" checked style="width: 32px; height: 16px;" />
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">Injection Protection</span>
                      <input type="checkbox" id="guard-inject" checked style="width: 32px; height: 16px;" />
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">Safety Filter (Toxic)</span>
                      <input type="checkbox" id="guard-safety" checked style="width: 32px; height: 16px;" />
                    </div>
                  </div>
                  <button class="ecom-btn-pay" id="btn-run-threat-sim" style="background:#f59e0b; padding: 8px; border-radius: 8px; font-size: 11px;">Simulate Attack →</button>
                </div>
                <div class="ecom-graphics" style="display: flex; flex-direction: column; gap: 10px;">
                  <div class="payment-receipt" id="threat-receipt" style="display: flex; width: 100%; padding: 14px; background: #fff; border-radius: 12px; align-items: flex-start; min-height: 120px; box-sizing: border-box;">
                    <div class="receipt-check" id="threat-icon" style="margin-bottom: 0; width: 28px; height: 28px; font-size: 14px;">🛡️</div>
                    <div style="text-align: left; margin-left: 8px; flex: 1;">
                      <div class="receipt-title" id="threat-title" style="font-size: 11px; margin-bottom: 2px;">Shield Active</div>
                      <p class="receipt-desc" id="threat-desc" style="font-size: 10px;">Security gate monitoring inputs.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </section>
"""

AI_TECH_STACK_HTML = """
  <!-- TECH STACK SECTION -->
  <section class="tech-stack-section reveal">
    <div class="container">
      <div class="tech-stack-head">
        <p class="section-eyebrow">AI TECHNOLOGY STACK</p>
        <h2 class="section-h2">Advanced AI Stack We Use</h2>
        <p class="tech-stack-sub">
          We leverage cutting-edge foundation models, pipeline tools, and secure cloud clusters to develop custom AI systems.
        </p>
      </div>

      <div class="tech-tabs">
        <button class="tech-tab-btn active" data-tab="tech-frontend">Models &amp; Frameworks</button>
        <button class="tech-tab-btn" data-tab="tech-backend">Vector DBs &amp; Search</button>
        <button class="tech-tab-btn" data-tab="tech-database">DevOps &amp; Hosting</button>
      </div>

      <!-- Models & Frameworks -->
      <div class="tech-grid active" id="tech-frontend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <h3 class="tech-card-title">LangChain &amp; LlamaIndex</h3>
          <p class="tech-card-desc">Orchestrating agent workflows, structured prompts, state machines, and context data injection pipelines.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12h8M12 8v8"/></svg>
          </div>
          <h3 class="tech-card-title">OpenAI &amp; Anthropic APIs</h3>
          <p class="tech-card-desc">Powering agents with advanced models (GPT-4o, Claude 3.5 Sonnet) optimized for reasoning and structured JSON output.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
          </div>
          <h3 class="tech-card-title">Hugging Face &amp; Local LLMs</h3>
          <p class="tech-card-desc">Fine-tuning open-source models (Llama 3, Mistral) for offline database operation and specialized enterprise tasks.</p>
        </div>
      </div>

      <!-- Vector DBs -->
      <div class="tech-grid" id="tech-backend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>
          </div>
          <h3 class="tech-card-title">Pinecone &amp; Milvus</h3>
          <p class="tech-card-desc">Securing sub-millisecond similarity search retrievals across millions of high-dimensional vectors.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
          </div>
          <h3 class="tech-card-title">pgvector &amp; Redis</h3>
          <p class="tech-card-desc">Adding relational semantic capabilities directly into PostgreSQL alongside cache memories for query results.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </div>
          <h3 class="tech-card-title">Elastic Search &amp; Hybrid</h3>
          <p class="tech-card-desc">Combining classical keyword indexes with dense vector embeddings to maximize query mapping precision.</p>
        </div>
      </div>

      <!-- DevOps & Hosting -->
      <div class="tech-grid" id="tech-database">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>
          </div>
          <h3 class="tech-card-title">FastAPI &amp; Python serving</h3>
          <p class="tech-card-desc">Deploying scalable backend services in typed Python environments, optimized for asynchronous execution.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 22 22 2 22"></polygon></svg>
          </div>
          <h3 class="tech-card-title">Docker &amp; Kubernetes</h3>
          <p class="tech-card-desc">Containerizing model microservices to allow automated load balancing, cluster expansion, and failover protection.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <h3 class="tech-card-title">AWS &amp; Cloud GPUs</h3>
          <p class="tech-card-desc">Hosting custom models on robust instances with secure network endpoints and continuous accuracy monitoring.</p>
        </div>
      </div>
    </div>
  </section>
"""

AI_PROCESS_HTML = """
  <!-- DEVELOPMENT PROCESS SECTION -->
  <section class="process-section reveal">
    <div class="process-glow"></div>
    <div class="container">
      <div class="process-header">
        <p class="section-eyebrow">METHODOLOGY</p>
        <h2 class="section-h2">Our AI Build Process</h2>
        <p style="font-size: 16px; line-height: 1.7; color: rgba(255, 255, 255, 0.6); margin-top: 14px;">
          How we research, fine-tune, build, evaluate, and launch custom AI solutions secure for production.
        </p>
      </div>

      <div class="process-grid">
        <!-- Step 1 -->
        <div class="process-card">
          <span class="process-step">Phase 01</span>
          <h3 class="process-card-title">Discovery</h3>
          <p class="process-card-desc">We analyze company operations, map bottlenecks, audit source datasets, and verify AI feasibility metrics.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="process-card">
          <span class="process-step">Phase 02</span>
          <h3 class="process-card-title">RAG &amp; Prep</h3>
          <p class="process-card-desc">We chunk unstructured text logs, configure embedding algorithms, and setup semantic vector databases.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="process-card">
          <span class="process-step">Phase 03</span>
          <h3 class="process-card-title">Agent Build</h3>
          <p class="process-card-desc">We engineer cognitive agent state graphs, prompt routines, tool actions, and history contexts.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="process-card">
          <span class="process-step">Phase 04</span>
          <h3 class="process-card-title">Eval &amp; Safety</h3>
          <p class="process-card-desc">We validate outputs against custom test sets to calculate hallucination ratios and inject safety guards.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="process-card">
          <span class="process-step">Phase 05</span>
          <h3 class="process-card-title">API Integration</h3>
          <p class="process-card-desc">We launch secure microservices, hook up system API ports, and start continuous runtime monitoring.</p>
        </div>
      </div>
    </div>
  </section>
"""

AI_FEATURES_HTML = """
  <!-- WEB CAPABILITIES SECTION -->
  <section class="features-grid-section reveal">
    <div class="container">
      <div class="features-grid-head">
        <p class="section-eyebrow">BUILT FOR ACCURACY</p>
        <h2 class="section-h2">Core Capabilities in Every System</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We build AI solutions adhering to enterprise compliance, ensuring accuracy, privacy, and scale.
        </p>
      </div>

      <div class="features-grid">
        <!-- Feature 1 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
          </div>
          <h3 class="feature-grid-title">99% Accuracy Loops</h3>
          <p class="feature-grid-desc">Every cognitive agent utilizes self-reflection reasoning loops, executing validations and self-correcting prompt outputs to guarantee reliable operations.</p>
        </div>

        <!-- Feature 2 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          </div>
          <h3 class="feature-grid-title">PII Masking &amp; Safety</h3>
          <p class="feature-grid-desc">We build local ingestion proxies that automatically redact passwords, credit cards, SSNs, and emails before prompting public foundational models.</p>
        </div>

        <!-- Feature 3 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
          </div>
          <h3 class="feature-grid-title">Custom Tool integrations</h3>
          <p class="feature-grid-desc">Connect cognitive agents directly to your internal software, database queries, Slack groups, customer CRMs, and email gateways to automate work.</p>
        </div>
      </div>
    </div>
  </section>
"""

AI_WHY_CHOOSE_HTML = """
  <!-- WHY CHOOSE -->
  <section class="why-choose">
    <div class="container">
      <div class="why-choose-inner">
        <!-- LEFT SIDE -->
        <div class="why-choose-left">
          <div class="hero-eyebrow" style="margin-bottom: 14px;">
            <div class="hero-eyebrow-dot"></div>
            WHY CHOOSE GLOBOTECH
          </div>
          <h2 class="section-h2">Why GloboTech for <span>AI &amp; Automation Services in USA?</span></h2>
          <p class="why-choose-desc" style="margin-bottom: 20px;">Globotech Solutions delivers production-ready, business-first AI integrations. We focus on pragmatic, high-accuracy automation tools that connect cleanly to your software infrastructure and drive actual operational ROI.</p>
          <p class="why-choose-desc" style="margin-bottom: 0;">If you partner with Globotech, your company datasets remain completely private. We audit safety policies, optimize model latencies, prevent hallucinations, and build scalable clusters on secure cloud structures across the USA. Read more about our engineering ethics on our About page.</p>
        </div>
        <!-- RIGHT SIDE -->
        <div class="why-choose-right">
          <div class="why-choose-grid-glow"></div>
          <div class="why-choose-grid">
            <!-- Card 1 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                </div>
              </div>
              <div class="why-card-title">Pragmatic ROI</div>
              <div class="why-card-desc">We target high-value manual processes to automate, driving immediate time savings and lowering operation errors.</div>
            </div>
            <!-- Card 2 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
                </div>
              </div>
              <div class="why-card-title">100% Data Privacy</div>
              <div class="why-card-desc">Your enterprise secrets are safe. We setup local vectors and data guards so models never leak your datasets.</div>
            </div>
            <!-- Card 3 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
                </div>
              </div>
              <div class="why-card-title">Custom Fine-Tuning</div>
              <div class="why-card-desc">We fine-tune open-source models on your domain-specific codebooks, optimizing accuracy rates.</div>
            </div>
            <!-- Card 4 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>
                </div>
              </div>
              <div class="why-card-title">Continuous Monitoring</div>
              <div class="why-card-desc">We monitor agent outputs, analyze log traces, manage model upgrades, and ensure cluster health 24/7.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

AI_JS = """
    // ── Flow Animation Pipeline Layout & Motion Path Calculator ──
    function updatePipeline() {
      const container = document.getElementById('pipeline-container');
      const path = document.getElementById('pipeline-path');
      const arrow = document.getElementById('pipeline-arrow');
      const dots = [
        document.getElementById('dot-1'),
        document.getElementById('dot-2'),
        document.getElementById('dot-3')
      ];
      if (!container || !path) return;

      const containerRect = container.getBoundingClientRect();

      const cards = [
        document.getElementById('card-req'),
        document.getElementById('card-design'),
        document.getElementById('card-dev'),
        document.getElementById('card-qa'),
        document.getElementById('card-dep'),
        document.getElementById('card-live')
      ];

      if (cards.some(c => !c)) return;

      const points = cards.map(card => {
        const rect = card.getBoundingClientRect();
        return {
          x: rect.left - containerRect.left + rect.width / 2,
          y: rect.top - containerRect.top + rect.height / 2
        };
      });

      const isMobile = window.innerWidth <= 768;
      let pathD = '';

      if (isMobile) {
        if (arrow) arrow.style.display = 'none';
        pathD = "M " + points[0].x + " " + points[0].y;
        for (let i = 1; i < points.length; i++) {
          pathD += " L " + points[i].x + " " + points[i].y;
        }
      } else {
        const pDev = points[2];
        const pQA = points[3];

        const rectDev = cards[2].getBoundingClientRect();
        const devRight = rectDev.right - containerRect.left;

        const dx = 50;
        const xRightLimit = devRight + dx;
        const R = 24;

        pathD = "M " + points[0].x + " " + points[0].y;
        pathD += " L " + points[1].x + " " + points[1].y;
        pathD += " L " + pDev.x + " " + pDev.y;

        pathD += " L " + (xRightLimit - R) + " " + pDev.y;
        pathD += " Q " + xRightLimit + " " + pDev.y + ", " + xRightLimit + " " + (pDev.y + R);
        pathD += " L " + xRightLimit + " " + (pQA.y - R);
        pathD += " Q " + xRightLimit + " " + pQA.y + ", " + (xRightLimit - R) + " " + pQA.y;
        pathD += " L " + pQA.x + " " + pQA.y;

        pathD += " L " + points[4].x + " " + points[4].y;
        pathD += " L " + points[5].x + " " + points[5].y;

        if (arrow) {
          arrow.style.display = 'block';
          const rectQA = cards[3].getBoundingClientRect();
          const qaRight = rectQA.right - containerRect.left;
          const offset = 2;
          const tipX = qaRight + offset;
          arrow.setAttribute('points', tipX + "," + pQA.y + " " + (tipX + 8) + "," + (pQA.y - 4) + " " + (tipX + 8) + "," + (pQA.y + 4));
        }
      }

      path.setAttribute('d', pathD);

      dots.forEach(dot => {
        if (dot) {
          dot.style.setProperty('offset-path', "path('" + pathD + "')");
          dot.style.setProperty('-webkit-offset-path', "path('" + pathD + "')");
        }
      });
    }

    window.addEventListener('DOMContentLoaded', updatePipeline);
    window.addEventListener('load', updatePipeline);
    window.addEventListener('resize', updatePipeline);
    if (document.fonts) {
      document.fonts.ready.then(updatePipeline);
    }

    (function () {
      var segments = [
        { id: 'card-req', at: 0.03 },
        { id: 'card-design', at: 0.18 },
        { id: 'card-dev', at: 0.35 },
        { id: 'card-qa', at: 0.62 },
        { id: 'card-dep', at: 0.79 },
        { id: 'card-live', at: 0.94 }
      ];
      var HALF = 0.065;
      var activeId = null;
      var epoch = performance.now();

      var dot1 = document.getElementById('dot-1');
      if (dot1) dot1.addEventListener('animationiteration', function () { epoch = performance.now(); });

      function tick(now) {
        var cycle = window.innerWidth <= 768 ? 7000 : 5500;
        var progress = ((now - epoch) % cycle) / cycle;
        if (progress < 0) progress += 1;

        var newId = null;
        for (var i = 0; i < segments.length; i++) {
          if (progress >= segments[i].at - HALF && progress <= segments[i].at + HALF) {
            newId = segments[i].id;
            break;
          }
        }

        if (newId !== activeId) {
          if (activeId) { var prev = document.getElementById(activeId); if (prev) prev.classList.remove('fnode-active'); }
          if (newId) { var next = document.getElementById(newId); if (next) next.classList.add('fnode-active'); }
          activeId = newId;
        }
        requestAnimationFrame(tick);
      }

      window.addEventListener('load', function () { epoch = performance.now(); requestAnimationFrame(tick); });
    })();

    // ── Mega Menu ──
    (function () {
      const trigger = document.getElementById('nav-services-trigger');
      const menu = document.getElementById('mega-services');
      if (!trigger || !menu) return;
      let closeTimer;
      function openMenu() {
        clearTimeout(closeTimer);
        trigger.classList.add('open');
        menu.style.display = 'block';
        requestAnimationFrame(() => { menu.classList.add('visible'); });
      }
      function closeMenu() {
        closeTimer = setTimeout(() => {
          trigger.classList.remove('open');
          menu.classList.remove('visible');
          setTimeout(() => { if (!menu.classList.contains('visible')) menu.style.display = 'none'; }, 220);
        }, 120);
      }
      trigger.addEventListener('mouseenter', openMenu);
      trigger.addEventListener('mouseleave', closeMenu);
      menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
      menu.addEventListener('mouseleave', closeMenu);
    })();

    // ── Side Drawer Navigation ──
    (function () {
      const ham = document.querySelector('.nav-hamburger');
      const drawer = document.getElementById('nav-drawer');
      const overlay = document.getElementById('nav-drawer-overlay');
      const closeBtn = document.getElementById('nav-drawer-close');
      const svcToggle = document.getElementById('nav-drawer-services-toggle');
      const svcMenu = document.getElementById('nav-drawer-services');
      if (!ham || !drawer) return;
      function openDrawer() { drawer.classList.add('open'); overlay && overlay.classList.add('open'); document.body.style.overflow = 'hidden'; ham.setAttribute('aria-expanded', 'true'); }
      function closeDrawer() { drawer.classList.remove('open'); overlay && overlay.classList.remove('open'); document.body.style.overflow = ''; ham.setAttribute('aria-expanded', 'false'); }
      ham.addEventListener('click', (e) => { e.stopPropagation(); openDrawer(); });
      overlay && overlay.addEventListener('click', closeDrawer);
      closeBtn && closeBtn.addEventListener('click', closeDrawer);
      svcToggle && svcToggle.addEventListener('click', () => { svcToggle.classList.toggle('open'); svcMenu && svcMenu.classList.toggle('open'); });
      document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDrawer(); });
    })();

    // ── Scroll Reveal Observer ──
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    // ── Specialty Showcase Tabs and Simulator Engine ──
    (function () {
      const tabs = document.querySelectorAll('.specialty-tab-btn');
      const panels = document.querySelectorAll('.simulator-panel');
      const glow = document.getElementById('showcase-glow');

      const themeColors = {
        purple: '#8b5cf6',
        cyan: '#33c5f3',
        green: '#10b981',
        orange: '#f59e0b'
      };

      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          const targetId = tab.getAttribute('data-tab');
          const theme = tab.getAttribute('data-theme');

          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          panels.forEach(p => p.classList.remove('active'));
          const targetPanel = document.getElementById(targetId);
          if (targetPanel) targetPanel.classList.add('active');

          if (glow && themeColors[theme]) {
            glow.style.background = themeColors[theme];
          }
        });
      });

      // --- SIMULATOR 1: Cognitive Agent Builder ---
      const runBtn = document.getElementById('btn-run-compiler');
      const consoleOut = document.getElementById('ide-console');
      const promptInput = document.getElementById('agent-prompt-input');
      
      if (runBtn && consoleOut) {
        runBtn.addEventListener('click', () => {
          if (runBtn.classList.contains('building')) return;

          runBtn.classList.add('building');
          runBtn.innerHTML = `
            <svg class="spinner" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="animation: spin 1s linear infinite; margin-right: 6px;"><circle cx="12" cy="12" r="10" stroke-opacity="0.3"></circle><path d="M4 12a8 8 0 0 1 8-8"></path></svg>
            Running...
          `;

          const prompt = promptInput ? promptInput.value : "Research competitors";
          consoleOut.innerHTML = `
            <p class="ide-line info">[agent] Initiating reasoning graph for query: "${prompt}"</p>
            <p class="ide-line">[agent] Planner: task decomposed into 3 sequential nodes...</p>
          `;

          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[agent] SearchAgent: scanning web indexes and crawling documents...</p>`;
            consoleOut.scrollTop = consoleOut.scrollHeight;
          }, 500);

          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[agent] CodeAgent: parsing text chunks & summarizing tables...</p>`;
            consoleOut.scrollTop = consoleOut.scrollHeight;
          }, 1100);

          setTimeout(() => {
            consoleOut.innerHTML += `
              <p class="ide-line success">✓ Task Completed in 1.8s!</p>
              <p class="ide-line info">ℹ Self-Reflection Score: 0.98 (No errors or overrides detected)</p>
              <p class="ide-line info">ℹ Output: Competitor pricing mapped and saved to workspace</p>
            `;
            consoleOut.scrollTop = consoleOut.scrollHeight;
            runBtn.classList.remove('building');
            runBtn.innerHTML = `
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              Run Agent
            `;
          }, 1800);
        });
      }

      // --- SIMULATOR 2: Vector Similarity search ---
      const ragBtn = document.getElementById('btn-run-rag');
      const ragQuery = document.getElementById('rag-query');
      const ragResults = document.getElementById('rag-results-box');
      
      if (ragBtn && ragQuery && ragResults) {
        ragBtn.addEventListener('click', () => {
          if (ragBtn.classList.contains('building')) return;
          
          ragBtn.classList.add('building');
          ragBtn.innerText = "Searching...";
          
          ragResults.innerHTML = '<p style="font-size: 11px; color: #8e8e93; font-family: monospace; margin: auto;">Querying embedding database indexes...</p>';
          
          setTimeout(() => {
            const queryVal = ragQuery.value;
            ragResults.innerHTML = `
              <div style="font-family: monospace; font-size: 11px; display: flex; flex-direction: column; gap: 8px; width: 100%; height: 100%; text-align: left; overflow-y: auto;">
                <div style="color: #636d83; border-bottom: 1px solid rgba(0,0,0,0.05); padding-bottom: 4px;">Cosine distance computation PASS</div>
                <div style="display: flex; justify-content: space-between; background: rgba(51, 197, 243, 0.08); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #33c5f3;">
                  <span>📄 gdpr_compliance_policy.pdf</span>
                  <strong style="color: #33c5f3;">94.2% match</strong>
                </div>
                <div style="display: flex; justify-content: space-between; background: rgba(0,0,0,0.02); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #8e8e93;">
                  <span>📄 security_regulations_v2.docx</span>
                  <strong style="color: #6e6e73;">88.7% match</strong>
                </div>
                <div style="display: flex; justify-content: space-between; background: rgba(0,0,0,0.02); padding: 8px 10px; border-radius: 6px; border-left: 3px solid #8e8e93;">
                  <span>📄 internal_audit_report.txt</span>
                  <strong style="color: #6e6e73;">61.5% match</strong>
                </div>
              </div>
            `;
            ragBtn.classList.remove('building');
            ragBtn.innerText = "Search Vector";
          }, 800);
        });
      }

      // --- SIMULATOR 3: Tokenizer ---
      const tokenizeBtn = document.getElementById('btn-tokenize');
      const tokenizerInput = document.getElementById('tokenizer-input');
      const tokenChips = document.getElementById('token-chips-container');
      const tokenStats = document.getElementById('token-stats');
      
      if (tokenizeBtn && tokenizerInput && tokenChips && tokenStats) {
        tokenizeBtn.addEventListener('click', () => {
          const text = tokenizerInput.value;
          if (!text.strip) {
            text.strip = function() { return text.replace(/^\s+|\s+$/g, ''); };
          }
          if (text.strip() === "") return;
          
          tokenizeBtn.innerText = "Parsing...";
          tokenChips.innerHTML = "";
          
          setTimeout(() => {
            // Split by words/punctuation
            const tokens = text.split(/(\s+)/);
            let tokenCount = 0;
            
            tokens.forEach(tok => {
              if (tok.strip() === "") return;
              tokenCount++;
              const chip = document.createElement('div');
              chip.className = 'cms-placed-block';
              chip.style.padding = '4px 8px';
              chip.style.fontSize = '10px';
              chip.style.borderRadius = '4px';
              chip.style.margin = '0';
              chip.style.background = `rgba(${10 + (tokenCount * 45) % 200}, ${120 + (tokenCount * 25) % 100}, 243, 0.08)`;
              chip.style.border = '1px solid rgba(0,0,0,0.04)';
              chip.innerHTML = `<span style="font-family: monospace;">${tok}</span><span style="font-size: 8px; color: #8e8e93; margin-left: 4px;">#${1000 + tokenCount}</span>`;
              tokenChips.appendChild(chip);
            });
            
            tokenStats.innerText = `Tokens: ${tokenCount} | Char Count: ${text.length} | Dimensions: 1536`;
            tokenizeBtn.innerText = "Tokenize";
          }, 600);
        });
      }

      // --- SIMULATOR 4: Security Sandbox ---
      const runThreatBtn = document.getElementById('btn-run-threat-sim');
      const checkPii = document.getElementById('guard-pii');
      const checkInject = document.getElementById('guard-inject');
      const checkSafety = document.getElementById('guard-safety');
      const threatReceipt = document.getElementById('threat-receipt');
      const threatIcon = document.getElementById('threat-icon');
      const threatTitle = document.getElementById('threat-title');
      const threatDesc = document.getElementById('threat-desc');
      
      if (runThreatBtn && threatReceipt) {
        runThreatBtn.addEventListener('click', () => {
          if (runThreatBtn.classList.contains('processing')) return;
          
          runThreatBtn.classList.add('processing');
          runThreatBtn.innerText = "Simulating Attack...";
          
          threatReceipt.style.background = '#fff';
          threatIcon.innerText = "⏳";
          threatTitle.innerText = "Running Sandbox Audit...";
          threatDesc.innerText = "Executing vector prompts...";
          
          setTimeout(() => {
            let blocked = false;
            let logMsg = "";
            
            if (checkInject.checked) {
              blocked = true;
              logMsg = "System override attack blocked. Source IP sandboxed.";
            } else if (checkPii.checked) {
              blocked = true;
              logMsg = "Database SSN keys masked and secure.";
            } else if (checkSafety.checked) {
              blocked = true;
              logMsg = "Toxic output phrase filtered successfully.";
            }
            
            if (blocked) {
              threatReceipt.style.background = 'rgba(16, 185, 129, 0.06)';
              threatIcon.innerText = "✓";
              threatIcon.style.background = 'rgba(16, 185, 129, 0.1)';
              threatIcon.style.color = '#10b981';
              threatTitle.innerText = "Threat Blocked!";
              threatDesc.innerText = logMsg;
            } else {
              threatReceipt.style.background = 'rgba(239, 68, 68, 0.06)';
              threatIcon.innerText = "❌";
              threatIcon.style.background = 'rgba(239, 68, 68, 0.1)';
              threatIcon.style.color = '#ef4444';
              threatTitle.innerText = "Breach Detected!";
              threatDesc.innerText = "Warning: Prompt Injection executed successfully (system instructions leaked).";
            }
            
            runThreatBtn.classList.remove('processing');
            runThreatBtn.innerText = "Simulate Attack →";
          }, 1200);
        });
      }
    })();

    // ── Tech Stack Tab Switching ──
    document.querySelectorAll('.tech-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');

        document.querySelectorAll('.tech-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.tech-grid').forEach(grid => grid.classList.remove('active'));
        const targetGrid = document.getElementById(targetId);
        if (targetGrid) {
          targetGrid.classList.add('active');
        }
      });
    });
"""

# ─────────────────────────────────────────────────────────────────────────────
# 2. E-COMMERCE SOLUTIONS PAGE DATA
# ─────────────────────────────────────────────────────────────────────────────

ECOM_HERO_HTML = """
  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <!-- LEFT SIDE -->
        <div>
          <div class="hero-eyebrow">
            <div class="hero-eyebrow-dot"></div>
            E-COMMERCE DEVELOPMENT
          </div>

          <h1 class="hero-h1">We Build <em>Scalable. Profitable.</em> Stores.</h1>

          <p class="hero-sub">From custom Shopify builds to headless commerce — we engineer end-to-end storefronts that convert visitors into loyal customers.</p>

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
              <div class="bm-url">store.pipeline — globotechsolutions.com</div>
              <div class="bm-live"><div class="bm-live-dot"></div>LIVE</div>
            </div>

            <!-- Body -->
            <div class="bm-body">
              <div class="bm-header-row">
                <span class="bm-section-label">Store Build Pipeline</span>
                <span class="bm-cycle-badge" id="bm-cycle">Cycle 1</span>
              </div>

              <!-- Progress bar -->
              <div class="bm-progress-row">
                <div class="bm-progress-track">
                  <div class="bm-progress-fill" id="bm-fill"></div>
                </div>
                <span class="bm-pct" id="bm-pct">0%</span>
              </div>
              <div class="bm-status-msg" id="bm-status">Initializing store environment...</div>

              <!-- Steps -->
              <div class="bm-steps">
                <div class="bm-step bm-pending" id="bm-s0">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Operational Audit &amp; Scoping</div>
                  <div class="bm-step-time" id="bm-t0"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s1">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Storefront Design &amp; UX</div>
                  <div class="bm-step-time" id="bm-t1"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s2">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Cart &amp; Checkout Engineering</div>
                  <div class="bm-step-time" id="bm-t2"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s3">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Third-Party API Integrations</div>
                  <div class="bm-step-time" id="bm-t3"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s4">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Payment QA &amp; Security</div>
                  <div class="bm-step-time" id="bm-t4"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s5">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Live Storefront Launch</div>
                  <div class="bm-step-time" id="bm-t5"></div>
                </div>
              </div>

              <!-- Metrics footer -->
              <div class="bm-metrics">
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m0">—</span>
                  <span class="bm-metric-lbl">Conversion</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m1">—</span>
                  <span class="bm-metric-lbl">Load Time</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m2">—</span>
                  <span class="bm-metric-lbl">Uptime</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

ECOM_SHOWCASE_HTML = """
  <!-- PREMIUM FEATURE SHOWCASE -->
  <section class="showcase-section reveal">
    <div class="showcase-glow-blob blob-1" id="showcase-glow"></div>

    <div class="container">
      <div class="showcase-header">
        <p class="section-eyebrow">OUR SPECIALIZATION</p>
        <h2 class="section-h2">Headless E-Commerce Solutions</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We build secure transactional environments, automatic warehouse inventory bridges, and multi-currency localized checkouts.
        </p>
      </div>

      <div class="showcase-layout">
        <!-- Tab Navigation (Left Column) -->
        <div class="specialty-tabs">

          <!-- Tab 1: Checkout -->
          <div class="specialty-tab-btn active" data-tab="sim-ecom" data-theme="purple">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /><line x1="3" y1="6" x2="21" y2="6" /><path d="M16 10a4 4 0 0 1-8 0" />
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Checkout Funnel</span>
                <span class="tab-badge">Instant Pay</span>
              </div>
              <p class="tab-desc">Provide seamless checkout experiences with secure 3D-secure card authentication and zero latency.</p>
            </div>
          </div>

          <!-- Tab 2: Inventory Sync -->
          <div class="specialty-tab-btn" data-tab="sim-custom" data-theme="cyan">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Stock Sync Monitor</span>
                <span class="tab-badge">Omnichannel</span>
              </div>
              <p class="tab-desc">Automatically synchronize stock levels across warehouse databases, ERP systems, and retail platforms.</p>
            </div>
          </div>

          <!-- Tab 3: Promo Coupon -->
          <div class="specialty-tab-btn" data-tab="sim-cms" data-theme="green">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Coupon Promo Engine</span>
                <span class="tab-badge">Drives AOV</span>
              </div>
              <p class="tab-desc">Calculate discounts, bulk pricing, and localized VAT rates instantly during checkout.</p>
            </div>
          </div>

          <!-- Tab 4: Multi-Currency -->
          <div class="specialty-tab-btn" data-tab="sim-responsive" data-theme="orange">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Localized Pricing</span>
                <span class="tab-badge">Global Reach</span>
              </div>
              <p class="tab-desc">Instantly update product pricing and shipping rules relative to localized visitor countries.</p>
            </div>
          </div>

        </div>

        <!-- Interactive Console Display (Right Column) -->
        <div class="console-container">
          <div class="console-screen">

            <!-- Panel 1: Checkout Transaction -->
            <div class="simulator-panel active" id="sim-ecom">
              <div class="ecom-panel-wrap">
                <div class="ecom-checkout-card">
                  <h4 class="ecom-checkout-title">Express Checkout</h4>
                  <div class="ecom-checkout-item">
                    <div class="ecom-item-thumb">👟</div>
                    <div class="ecom-item-meta">
                      <div class="ecom-item-name">Flyknit Racer Pro</div>
                      <div class="ecom-item-qty">Qty: 1</div>
                    </div>
                    <div class="ecom-item-price">$180.00</div>
                  </div>
                  <div class="ecom-checkout-total">
                    <span class="ecom-total-label">Total Amount</span>
                    <span class="ecom-total-price" id="checkout-total-val">$180.00</span>
                  </div>
                  <button class="ecom-btn-pay" id="btn-place-order">Place Order →</button>
                </div>
                <div class="ecom-graphics">
                  <!-- Tilt card -->
                  <div class="interactive-card" id="ecom-visa-card">
                    <div class="card-chip"></div>
                    <div class="card-number">•••• •••• •••• 9024</div>
                    <div class="card-footer">
                      <span class="card-holder">GLOBO DTC</span>
                      <div class="card-vendor"></div>
                    </div>
                  </div>
                  <!-- Success receipt -->
                  <div class="payment-receipt" id="checkout-receipt">
                    <div class="receipt-check">✓</div>
                    <div class="receipt-title">Order Confirmed!</div>
                    <p class="receipt-desc">Thank you for your purchase. Receipt sent to customer@dtc.io</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 2: Inventory Sync -->
            <div class="simulator-panel" id="sim-custom">
              <div class="ide-mock">
                <div class="ide-header">
                  <div class="ide-dots">
                    <span class="term-dot term-dot-r"></span>
                    <span class="term-dot term-dot-y"></span>
                    <span class="term-dot term-dot-g"></span>
                  </div>
                  <button class="ide-btn-run" id="btn-run-compiler" style="background: #33c5f3;">
                    Trigger Sync
                  </button>
                </div>
                <div class="ide-body">
                  <div style="display: flex; gap: 10px; margin-bottom: 12px; align-items: center;">
                    <span style="color: #6e6e73; font-size: 11px;">Target Product:</span>
                    <select id="sync-product-selector" style="background:#1a1c23; border: 1px solid rgba(255,255,255,0.08); border-radius: 4px; padding: 4px 8px; color: #fff; font-family: monospace; font-size: 11px; outline: none;">
                      <option value="Flyknit Racer Pro">Flyknit Racer Pro</option>
                      <option value="Vision Pro DevKit">Vision Pro DevKit</option>
                    </select>
                  </div>
                  <div class="ide-console-out" id="ide-console" style="height: 110px; overflow-y: auto;">
                    <p class="ide-line info">Click "Trigger Sync" above to run inventory check across channels...</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 3: Promo Coupon -->
            <div class="simulator-panel" id="sim-cms">
              <div class="cms-panel-wrap" style="grid-template-columns: 1fr; width: 100%;">
                <div style="display: flex; gap: 12px; align-items: center; width: 100%;">
                  <input type="text" id="promo-code-input" value="GLOBOTECH20" placeholder="Enter coupon code..." style="flex: 1; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 8px; padding: 10px; font-family: monospace; font-size: 12px; outline: none; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" />
                  <button id="btn-apply-promo" class="ide-btn-run" style="background:#10b981; padding: 10px 20px; border-radius: 8px;">Apply Code</button>
                </div>
                <div class="cms-canvas-wrap" style="min-height: 140px; padding: 16px; margin-top: 10px; background: #fafbfc; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                  <div style="width: 100%; max-width: 280px; font-family: monospace; font-size: 11px; display: flex; flex-direction: column; gap: 6px;" id="promo-receipt-box">
                    <div style="display:flex; justify-content: space-between;"><span>Subtotal:</span><span>$180.00</span></div>
                    <div style="display:flex; justify-content: space-between; color: #8e8e93;" id="promo-discount-line"><span>Discount (0%):</span><span>-$0.00</span></div>
                    <div style="display:flex; justify-content: space-between; border-top: 1px dashed rgba(0,0,0,0.08); padding-top: 6px; font-weight: 700; font-size: 12px;"><span>Grand Total:</span><span id="promo-grand-total">$180.00</span></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 4: Localized pricing -->
            <div class="simulator-panel" id="sim-responsive">
              <div class="responsive-panel-wrap">
                <div class="responsive-controls" style="gap: 6px;">
                  <button class="resp-btn active" data-currency="USD">🇺🇸 USD ($)</button>
                  <button class="resp-btn" data-currency="EUR">🇪🇺 EUR (€)</button>
                  <button class="resp-btn" data-currency="GBP">🇬🇧 GBP (£)</button>
                  <button class="resp-btn" data-currency="JPY">🇯🇵 JPY (¥)</button>
                </div>
                <div class="responsive-viewport-container" style="height: 220px; background: #fff; border: 1px solid rgba(0,0,0,0.04); box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
                  <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;">
                    <span style="font-size: 38px;">👟</span>
                    <h4 style="font-family: var(--fh); font-size: 16px; font-weight: 800; color: #1d1d1f; margin: 0;">Flyknit Racer Pro</h4>
                    <div style="font-family: monospace; font-size: 20px; font-weight: 800; color: #10b981;" id="currency-price-tag">$180.00</div>
                    <p style="font-size: 10px; color: #8e8e93;" id="currency-shipping-rule">Free shipping across USA</p>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </section>
"""

ECOM_TECH_STACK_HTML = """
  <!-- TECH STACK SECTION -->
  <section class="tech-stack-section reveal">
    <div class="container">
      <div class="tech-stack-head">
        <p class="section-eyebrow">E-COMMERCE TECHNOLOGY STACK</p>
        <h2 class="section-h2">Storefront Technology We Use</h2>
        <p class="tech-stack-sub">
          We leverage modern headless frontends, SaaS commerce platforms, and secure transaction gateways to build fast online stores.
        </p>
      </div>

      <div class="tech-tabs">
        <button class="tech-tab-btn active" data-tab="tech-frontend">Headless Frontends</button>
        <button class="tech-tab-btn" data-tab="tech-backend">Commerce Platforms</button>
        <button class="tech-tab-btn" data-tab="tech-database">Integrations &amp; Shipping</button>
      </div>

      <!-- Frontends -->
      <div class="tech-grid active" id="tech-frontend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line></svg>
          </div>
          <h3 class="tech-card-title">Next.js Commerce</h3>
          <p class="tech-card-desc">Developing blazing-fast React storefronts utilizing static generation, incremental rebuilds, and edge route rendering.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon></svg>
          </div>
          <h3 class="tech-card-title">Shopify Hydrogen</h3>
          <p class="tech-card-desc">Building sub-second headless Shopify storefronts powered by specialized React components and oxygen edge hostings.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path></svg>
          </div>
          <h3 class="tech-card-title">Tailwind CSS</h3>
          <p class="tech-card-desc">Accelerating checkout page designs and layout configurations with utility-first CSS styling frameworks.</p>
        </div>
      </div>

      <!-- Platforms -->
      <div class="tech-grid" id="tech-backend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /></svg>
          </div>
          <h3 class="tech-card-title">Shopify Custom</h3>
          <p class="tech-card-desc">Writing custom templates, schema sections, and private applications utilizing the GraphQL Admin APIs.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10z"/></svg>
          </div>
          <h3 class="tech-card-title">WooCommerce &amp; WP</h3>
          <p class="tech-card-desc">Developing relational WordPress shop extensions and localized payment gateway connectors optimized for scale.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
          </div>
          <h3 class="tech-card-title">MedusaJS &amp; Custom</h3>
          <p class="tech-card-desc">Architecting custom, open-source Node.js headless commerce engines supporting unique subscription rules.</p>
        </div>
      </div>

      <!-- Shipping -->
      <div class="tech-grid" id="tech-database">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
          </div>
          <h3 class="tech-card-title">Stripe &amp; PayPal APIs</h3>
          <p class="tech-card-desc">Integrating transactional token checkouts, subscription processors, and 3D Secure verification cards.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
          </div>
          <h3 class="tech-card-title">ERP &amp; Inventory Bridges</h3>
          <p class="tech-card-desc">Syncing warehouse count logs dynamically with storefront catalogs to prevent overselling risks.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <h3 class="tech-card-title">Logistics &amp; Shipping</h3>
          <p class="tech-card-desc">Hooking up automated shipping labels, tracking updates, and return portals via ShipStation or custom APIs.</p>
        </div>
      </div>
    </div>
  </section>
"""

ECOM_PROCESS_HTML = """
  <!-- DEVELOPMENT PROCESS SECTION -->
  <section class="process-section reveal">
    <div class="process-glow"></div>
    <div class="container">
      <div class="process-header">
        <p class="section-eyebrow">METHODOLOGY</p>
        <h2 class="section-h2">Our E-Com Build Process</h2>
        <p style="font-size: 16px; line-height: 1.7; color: rgba(255, 255, 255, 0.6); margin-top: 14px;">
          How we map catalogs, draft responsive stores, sync ERP inventories, and launch custom checkouts.
        </p>
      </div>

      <div class="process-grid">
        <!-- Step 1 -->
        <div class="process-card">
          <span class="process-step">Phase 01</span>
          <h3 class="process-card-title">Audit &amp; Scope</h3>
          <p class="process-card-desc">We audit product catalogs, analyze checkout funnels, review warehouse databases, and draft API scopes.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="process-card">
          <span class="process-step">Phase 02</span>
          <h3 class="process-card-title">UI/UX Design</h3>
          <p class="process-card-desc">We draft storefront interfaces, optimize product detail pages, and build simple checkout wireframes.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="process-card">
          <span class="process-step">Phase 03</span>
          <h3 class="process-card-title">Storefront Build</h3>
          <p class="process-card-desc">Engineers build fast Next.js React templates or custom Shopify Liquid pages optimized for mobile load speeds.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="process-card">
          <span class="process-step">Phase 04</span>
          <h3 class="process-card-title">Integrations</h3>
          <p class="process-card-desc">We bridge secure payment processors, sync ERP shipping logs, and hook up automated stock updates.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="process-card">
          <span class="process-step">Phase 05</span>
          <h3 class="process-card-title">Speed &amp; Launch</h3>
          <p class="process-card-desc">We load test transactional gateways, run speed index checks, and launch your optimized storefront globally.</p>
        </div>
      </div>
    </div>
  </section>
"""

ECOM_FEATURES_HTML = """
  <!-- WEB CAPABILITIES SECTION -->
  <section class="features-grid-section reveal">
    <div class="container">
      <div class="features-grid-head">
        <p class="section-eyebrow">BUILT FOR RETAIL SCALE</p>
        <h2 class="section-h2">Core Capabilities in Every Store</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We construct storefronts targeting speed, high conversion yields, and stable operational synchronization.
        </p>
      </div>

      <div class="features-grid">
        <!-- Feature 1 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line></svg>
          </div>
          <h3 class="feature-grid-title">0.2s Storefront Speeds</h3>
          <p class="feature-grid-desc">Every storefront is optimized to yield 99+ Lighthouse speed scores, using statically pre-rendered content and edge caches to rank higher on search engines.</p>
        </div>

        <!-- Feature 2 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /></svg>
          </div>
          <h3 class="feature-grid-title">Zero Checkout Drops</h3>
          <p class="feature-grid-desc">Minimizing abandoned carts by stripping input fields, bridging mobile express wallets (Apple/Google Pay), and rendering instant checkout transitions.</p>
        </div>

        <!-- Feature 3 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
          </div>
          <h3 class="feature-grid-title">Omnichannel Sync</h3>
          <p class="feature-grid-desc">Bidirectional webhook pipelines update stock counts automatically between ERP, Shopify, Amazon, and warehouse locations in under 500ms.</p>
        </div>
      </div>
    </div>
  </section>
"""

ECOM_WHY_CHOOSE_HTML = """
  <!-- WHY CHOOSE -->
  <section class="why-choose">
    <div class="container">
      <div class="why-choose-inner">
        <!-- LEFT SIDE -->
        <div class="why-choose-left">
          <div class="hero-eyebrow" style="margin-bottom: 14px;">
            <div class="hero-eyebrow-dot"></div>
            WHY CHOOSE GLOBOTECH
          </div>
          <h2 class="section-h2">Why GloboTech for <span>E-Commerce Services in USA?</span></h2>
          <p class="why-choose-desc" style="margin-bottom: 20px;">Globotech Solutions offers high-performance e-commerce development that scales. We combine fast React page architectures with robust SaaS inventory connectors to ensure your store is fast and converts visitors into sales.</p>
          <p class="why-choose-desc" style="margin-bottom: 0;">We have helped retail companies across the USA modernize their storefront layouts and bridge logistics channels cleanly. We guarantee 99.9% storefront uptime, secure payment transactions, and direct developer communication. Please read about our past projects on our case studies page.</p>
        </div>
        <!-- RIGHT SIDE -->
        <div class="why-choose-right">
          <div class="why-choose-grid-glow"></div>
          <div class="why-choose-grid">
            <!-- Card 1 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect></svg>
                </div>
              </div>
              <div class="why-card-title">99.99% Uptime</div>
              <div class="why-card-desc">We build headless pages served via edge hosts, guaranteeing your store never drops offline during ad spikes.</div>
            </div>
            <!-- Card 2 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z" /></svg>
                </div>
              </div>
              <div class="why-card-title">Conversion UX</div>
              <div class="why-card-desc">We craft beautiful storefront wireframes designed to optimize average order values and reduce drops.</div>
            </div>
            <!-- Card 3 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
                </div>
              </div>
              <div class="why-card-title">Seamless ERP Sync</div>
              <div class="why-card-desc">We bridge ERP warehouses and sales platforms cleanly, matching stock logs across channels.</div>
            </div>
            <!-- Card 4 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg>
                </div>
              </div>
              <div class="why-card-title">Post-Launch Support</div>
              <div class="why-card-desc">We stay with you to audit security configurations, test discount engines, and expand catalogs.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

ECOM_JS = """
    // ── Flow Animation Pipeline Layout & Motion Path Calculator ──
    function updatePipeline() {
      const container = document.getElementById('pipeline-container');
      const path = document.getElementById('pipeline-path');
      const arrow = document.getElementById('pipeline-arrow');
      const dots = [
        document.getElementById('dot-1'),
        document.getElementById('dot-2'),
        document.getElementById('dot-3')
      ];
      if (!container || !path) return;

      const containerRect = container.getBoundingClientRect();

      const cards = [
        document.getElementById('card-req'),
        document.getElementById('card-design'),
        document.getElementById('card-dev'),
        document.getElementById('card-qa'),
        document.getElementById('card-dep'),
        document.getElementById('card-live')
      ];

      if (cards.some(c => !c)) return;

      const points = cards.map(card => {
        const rect = card.getBoundingClientRect();
        return {
          x: rect.left - containerRect.left + rect.width / 2,
          y: rect.top - containerRect.top + rect.height / 2
        };
      });

      const isMobile = window.innerWidth <= 768;
      let pathD = '';

      if (isMobile) {
        if (arrow) arrow.style.display = 'none';
        pathD = "M " + points[0].x + " " + points[0].y;
        for (let i = 1; i < points.length; i++) {
          pathD += " L " + points[i].x + " " + points[i].y;
        }
      } else {
        const pDev = points[2];
        const pQA = points[3];

        const rectDev = cards[2].getBoundingClientRect();
        const devRight = rectDev.right - containerRect.left;

        const dx = 50;
        const xRightLimit = devRight + dx;
        const R = 24;

        pathD = "M " + points[0].x + " " + points[0].y;
        pathD += " L " + points[1].x + " " + points[1].y;
        pathD += " L " + pDev.x + " " + pDev.y;

        pathD += " L " + (xRightLimit - R) + " " + pDev.y;
        pathD += " Q " + xRightLimit + " " + pDev.y + ", " + xRightLimit + " " + (pDev.y + R);
        pathD += " L " + xRightLimit + " " + (pQA.y - R);
        pathD += " Q " + xRightLimit + " " + pQA.y + ", " + (xRightLimit - R) + " " + pQA.y;
        pathD += " L " + pQA.x + " " + pQA.y;

        pathD += " L " + points[4].x + " " + points[4].y;
        pathD += " L " + points[5].x + " " + points[5].y;

        if (arrow) {
          arrow.style.display = 'block';
          const rectQA = cards[3].getBoundingClientRect();
          const qaRight = rectQA.right - containerRect.left;
          const offset = 2;
          const tipX = qaRight + offset;
          arrow.setAttribute('points', tipX + "," + pQA.y + " " + (tipX + 8) + "," + (pQA.y - 4) + " " + (tipX + 8) + "," + (pQA.y + 4));
        }
      }

      path.setAttribute('d', pathD);

      dots.forEach(dot => {
        if (dot) {
          dot.style.setProperty('offset-path', "path('" + pathD + "')");
          dot.style.setProperty('-webkit-offset-path', "path('" + pathD + "')");
        }
      });
    }

    window.addEventListener('DOMContentLoaded', updatePipeline);
    window.addEventListener('load', updatePipeline);
    window.addEventListener('resize', updatePipeline);
    if (document.fonts) {
      document.fonts.ready.then(updatePipeline);
    }

    (function () {
      var segments = [
        { id: 'card-req', at: 0.03 },
        { id: 'card-design', at: 0.18 },
        { id: 'card-dev', at: 0.35 },
        { id: 'card-qa', at: 0.62 },
        { id: 'card-dep', at: 0.79 },
        { id: 'card-live', at: 0.94 }
      ];
      var HALF = 0.065;
      var activeId = null;
      var epoch = performance.now();

      var dot1 = document.getElementById('dot-1');
      if (dot1) dot1.addEventListener('animationiteration', function () { epoch = performance.now(); });

      function tick(now) {
        var cycle = window.innerWidth <= 768 ? 7000 : 5500;
        var progress = ((now - epoch) % cycle) / cycle;
        if (progress < 0) progress += 1;

        var newId = null;
        for (var i = 0; i < segments.length; i++) {
          if (progress >= segments[i].at - HALF && progress <= segments[i].at + HALF) {
            newId = segments[i].id;
            break;
          }
        }

        if (newId !== activeId) {
          if (activeId) { var prev = document.getElementById(activeId); if (prev) prev.classList.remove('fnode-active'); }
          if (newId) { var next = document.getElementById(newId); if (next) next.classList.add('fnode-active'); }
          activeId = newId;
        }
        requestAnimationFrame(tick);
      }

      window.addEventListener('load', function () { epoch = performance.now(); requestAnimationFrame(tick); });
    })();

    // ── Mega Menu ──
    (function () {
      const trigger = document.getElementById('nav-services-trigger');
      const menu = document.getElementById('mega-services');
      if (!trigger || !menu) return;
      let closeTimer;
      function openMenu() {
        clearTimeout(closeTimer);
        trigger.classList.add('open');
        menu.style.display = 'block';
        requestAnimationFrame(() => { menu.classList.add('visible'); });
      }
      function closeMenu() {
        closeTimer = setTimeout(() => {
          trigger.classList.remove('open');
          menu.classList.remove('visible');
          setTimeout(() => { if (!menu.classList.contains('visible')) menu.style.display = 'none'; }, 220);
        }, 120);
      }
      trigger.addEventListener('mouseenter', openMenu);
      trigger.addEventListener('mouseleave', closeMenu);
      menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
      menu.addEventListener('mouseleave', closeMenu);
    })();

    // ── Side Drawer Navigation ──
    (function () {
      const ham = document.querySelector('.nav-hamburger');
      const drawer = document.getElementById('nav-drawer');
      const overlay = document.getElementById('nav-drawer-overlay');
      const closeBtn = document.getElementById('nav-drawer-close');
      const svcToggle = document.getElementById('nav-drawer-services-toggle');
      const svcMenu = document.getElementById('nav-drawer-services');
      if (!ham || !drawer) return;
      function openDrawer() { drawer.classList.add('open'); overlay && overlay.classList.add('open'); document.body.style.overflow = 'hidden'; ham.setAttribute('aria-expanded', 'true'); }
      function closeDrawer() { drawer.classList.remove('open'); overlay && overlay.classList.remove('open'); document.body.style.overflow = ''; ham.setAttribute('aria-expanded', 'false'); }
      ham.addEventListener('click', (e) => { e.stopPropagation(); openDrawer(); });
      overlay && overlay.addEventListener('click', closeDrawer);
      closeBtn && closeBtn.addEventListener('click', closeDrawer);
      svcToggle && svcToggle.addEventListener('click', () => { svcToggle.classList.toggle('open'); svcMenu && svcMenu.classList.toggle('open'); });
      document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDrawer(); });
    })();

    // ── Scroll Reveal Observer ──
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    // ── Specialty Showcase Tabs and Simulator Engine ──
    (function () {
      const tabs = document.querySelectorAll('.specialty-tab-btn');
      const panels = document.querySelectorAll('.simulator-panel');
      const glow = document.getElementById('showcase-glow');

      const themeColors = {
        purple: '#8b5cf6',
        cyan: '#33c5f3',
        green: '#10b981',
        orange: '#f59e0b'
      };

      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          const targetId = tab.getAttribute('data-tab');
          const theme = tab.getAttribute('data-theme');

          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          panels.forEach(p => p.classList.remove('active'));
          const targetPanel = document.getElementById(targetId);
          if (targetPanel) targetPanel.classList.add('active');

          if (glow && themeColors[theme]) {
            glow.style.background = themeColors[theme];
          }
        });
      });

      // --- SIMULATOR 1: Checkout Transaction ---
      const payBtn = document.getElementById('btn-place-order');
      const visaCard = document.getElementById('ecom-visa-card');
      const receipt = document.getElementById('checkout-receipt');

      if (payBtn && visaCard && receipt) {
        payBtn.addEventListener('click', () => {
          if (payBtn.classList.contains('processing')) return;

          payBtn.classList.add('processing');
          payBtn.innerText = 'Processing Order...';

          setTimeout(() => {
            visaCard.classList.add('paid');
            setTimeout(() => {
              visaCard.style.display = 'none';
              receipt.style.display = 'flex';
              payBtn.innerText = 'Order Placed!';
              payBtn.style.background = '#10b981';
            }, 600);
          }, 1200);
        });
      }

      // --- SIMULATOR 2: Inventory Sync Monitor ---
      const runBtn = document.getElementById('btn-run-compiler');
      const consoleOut = document.getElementById('ide-console');
      const productSelect = document.getElementById('sync-product-selector');
      
      if (runBtn && consoleOut && productSelect) {
        runBtn.addEventListener('click', () => {
          if (runBtn.classList.contains('building')) return;

          runBtn.classList.add('building');
          runBtn.innerText = "Syncing...";

          const prod = productSelect.value;
          consoleOut.innerHTML = `
            <p class="ide-line info">[sync] Triggering stock query for "${prod}"...</p>
            <p class="ide-line">[sync] Querying ERP backend database (Stock: 142)...</p>
          `;

          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[sync] Sending webhook update to Shopify admin ports... PASS</p>`;
          }, 500);

          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[sync] Updating Amazon storefront catalog index... PASS</p>`;
          }, 1000);

          setTimeout(() => {
            consoleOut.innerHTML += `
              <p class="ide-line success">✓ Inventory fully synced across all channels!</p>
              <p class="ide-line info">ℹ Sync execution duration: 0.38s</p>
            `;
            runBtn.classList.remove('building');
            runBtn.innerText = "Trigger Sync";
          }, 1500);
        });
      }

      // --- SIMULATOR 3: Promo Coupon engine ---
      const applyPromoBtn = document.getElementById('btn-apply-promo');
      const promoInput = document.getElementById('promo-code-input');
      const discountLine = document.getElementById('promo-discount-line');
      const grandTotal = document.getElementById('promo-grand-total');
      
      if (applyPromoBtn && promoInput && discountLine && grandTotal) {
        applyPromoBtn.addEventListener('click', () => {
          const code = promoInput.value.replace(/^\s+|\s+$/g, '').toUpperCase();
          
          if (code === "GLOBOTECH20") {
            applyPromoBtn.innerText = "Applying...";
            setTimeout(() => {
              discountLine.innerHTML = "<span>Discount (20%):</span><span>-$36.00</span>";
              discountLine.style.color = "#10b981";
              grandTotal.innerText = "$144.00";
              applyPromoBtn.innerText = "Code Applied!";
              applyPromoBtn.style.background = "#10b981";
            }, 600);
          } else if (code === "FREESHIP") {
            applyPromoBtn.innerText = "Applying...";
            setTimeout(() => {
              discountLine.innerHTML = "<span>Shipping Coupon:</span><span>-$10.00</span>";
              discountLine.style.color = "#10b981";
              grandTotal.innerText = "$170.00";
              applyPromoBtn.innerText = "Code Applied!";
              applyPromoBtn.style.background = "#10b981";
            }, 600);
          } else {
            promoInput.value = "INVALID CODE";
            setTimeout(() => { promoInput.value = ""; }, 1000);
          }
        });
      }

      // --- SIMULATOR 4: Multi-currency converter preset ---
      const respBtns = document.querySelectorAll('.resp-btn');
      const priceTag = document.getElementById('currency-price-tag');
      const shipRule = document.getElementById('currency-shipping-rule');
      
      const currencyPrices = {
        USD: { price: "$180.00", ship: "Free shipping across USA" },
        EUR: { price: "€168.00", ship: "VAT included. International shipping €15" },
        GBP: { price: "£142.00", ship: "Duty free delivery across UK" },
        JPY: { price: "¥26,500", ship: "Custom shipping calculated at port" }
      };

      if (respBtns && priceTag && shipRule) {
        respBtns.forEach(btn => {
          btn.addEventListener('click', () => {
            const cur = btn.getAttribute('data-currency');
            respBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            if (currencyPrices[cur]) {
              priceTag.innerText = currencyPrices[cur].price;
              shipRule.innerText = currencyPrices[cur].ship;
            }
          });
        });
      }
    })();

    // ── Tech Stack Tab Switching ──
    document.querySelectorAll('.tech-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');

        document.querySelectorAll('.tech-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.tech-grid').forEach(grid => grid.classList.remove('active'));
        const targetGrid = document.getElementById(targetId);
        if (targetGrid) {
          targetGrid.classList.add('active');
        }
      });
    });
"""

# ─────────────────────────────────────────────────────────────────────────────
# 3. DIGITAL MARKETING PAGE DATA
# ─────────────────────────────────────────────────────────────────────────────

MKT_HERO_HTML = """
  <!-- HERO -->
  <section class="hero">
    <div class="container">
      <div class="hero-inner">
        <!-- LEFT SIDE -->
        <div>
          <div class="hero-eyebrow">
            <div class="hero-eyebrow-dot"></div>
            DIGITAL MARKETING &amp; GROWTH
          </div>

          <h1 class="hero-h1">We Run <em>Data-Driven. High-ROI.</em> Campaigns.</h1>

          <p class="hero-sub">From SEO to paid acquisition — we design growth engines that attract qualified leads, reduce CAC, and maximise return on ad spend.</p>

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
              <div class="bm-url">campaign.pipeline — globotechsolutions.com</div>
              <div class="bm-live"><div class="bm-live-dot"></div>LIVE</div>
            </div>

            <!-- Body -->
            <div class="bm-body">
              <div class="bm-header-row">
                <span class="bm-section-label">Campaign Pipeline</span>
                <span class="bm-cycle-badge" id="bm-cycle">Cycle 1</span>
              </div>

              <!-- Progress bar -->
              <div class="bm-progress-row">
                <div class="bm-progress-track">
                  <div class="bm-progress-fill" id="bm-fill"></div>
                </div>
                <span class="bm-pct" id="bm-pct">0%</span>
              </div>
              <div class="bm-status-msg" id="bm-status">Initializing campaign environment...</div>

              <!-- Steps -->
              <div class="bm-steps">
                <div class="bm-step bm-pending" id="bm-s0">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Audience Research &amp; ICP</div>
                  <div class="bm-step-time" id="bm-t0"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s1">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">SEO &amp; Content Strategy</div>
                  <div class="bm-step-time" id="bm-t1"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s2">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Paid Media Campaign Setup</div>
                  <div class="bm-step-time" id="bm-t2"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s3">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Creative &amp; Ad Copy</div>
                  <div class="bm-step-time" id="bm-t3"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s4">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Analytics &amp; Tracking</div>
                  <div class="bm-step-time" id="bm-t4"></div>
                </div>
                <div class="bm-step bm-pending" id="bm-s5">
                  <div class="bm-step-ico"><div class="bm-step-ico-circle"></div></div>
                  <div class="bm-step-label">Live Campaign Launch</div>
                  <div class="bm-step-time" id="bm-t5"></div>
                </div>
              </div>

              <!-- Metrics footer -->
              <div class="bm-metrics">
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m0">—</span>
                  <span class="bm-metric-lbl">ROAS</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m1">—</span>
                  <span class="bm-metric-lbl">CTR</span>
                </div>
                <div class="bm-metric">
                  <span class="bm-metric-val" id="bm-m2">—</span>
                  <span class="bm-metric-lbl">CPA</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

"""

MKT_SHOWCASE_HTML = """
  <!-- PREMIUM FEATURE SHOWCASE -->
  <section class="showcase-section reveal">
    <div class="showcase-glow-blob blob-1" id="showcase-glow"></div>

    <div class="container">
      <div class="showcase-header">
        <p class="section-eyebrow">OUR SPECIALIZATION</p>
        <h2 class="section-h2">Growth Engineering Solutions</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We leverage technical SEO configurations, conversion funnel split-testing, and dynamic budget CPC algorithms.
        </p>
      </div>

      <div class="showcase-layout">
        <!-- Tab Navigation (Left Column) -->
        <div class="specialty-tabs">

          <!-- Tab 1: SEO Audit -->
          <div class="specialty-tab-btn active" data-tab="sim-responsive" data-theme="purple">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Search Auditor</span>
                <span class="tab-badge">SEO Audit</span>
              </div>
              <p class="tab-desc">Analyze metadata mappings, crawling indexes, and site speed dials instantly.</p>
            </div>
          </div>

          <!-- Tab 2: CPC Simulator -->
          <div class="specialty-tab-btn" data-tab="sim-custom" data-theme="cyan">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Ad Bid Simulator</span>
                <span class="tab-badge">Maximize ROI</span>
              </div>
              <p class="tab-desc">Forecast impressions, CPC curves, and projected customer acquisition costs (CAC).</p>
            </div>
          </div>

          <!-- Tab 3: A/B Split Test -->
          <div class="specialty-tab-btn" data-tab="sim-cms" data-theme="green">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Split Tester</span>
                <span class="tab-badge">CRO Engine</span>
              </div>
              <p class="tab-desc">A/B test copy variations to engineer higher conversion rates.</p>
            </div>
          </div>

          <!-- Tab 4: Funnel Leak -->
          <div class="specialty-tab-btn" data-tab="sim-ecom" data-theme="orange">
            <div class="tab-icon-wrap">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"/>
              </svg>
            </div>
            <div class="tab-info">
              <div class="tab-info-header">
                <span class="tab-title">Funnel Leak Analyzer</span>
                <span class="tab-badge">Funnel CRO</span>
              </div>
              <p class="tab-desc">Identify friction points in user flows to minimize checkout drop-offs.</p>
            </div>
          </div>

        </div>

        <!-- Interactive Console Display (Right Column) -->
        <div class="console-container">
          <div class="console-screen">

            <!-- Panel 1: SEO Audit Analyzer -->
            <div class="simulator-panel active" id="sim-responsive">
              <div class="responsive-panel-wrap">
                <div style="display: flex; gap: 12px; align-items: center; width: 100%;">
                  <input type="text" id="seo-url" value="globotechsolutions.com" style="flex: 1; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 8px; padding: 10px 14px; font-family: monospace; font-size: 12px; outline: none; box-shadow: 0 2px 8px rgba(0,0,0,0.02);" />
                  <button id="btn-run-seo" class="ide-btn-run" style="padding: 10px 20px; border-radius: 8px; background: #8b5cf6;">Analyze Site</button>
                </div>
                <div class="responsive-viewport-container" style="height: 220px; padding: 16px;">
                  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; width: 100%; height: 100%; align-content: center;" id="seo-dial-box">
                    <div style="text-align: center;">
                      <div class="receipt-check" id="dial-perf" style="margin: 0 auto 8px; background: #fafbfc; border: 2px solid rgba(0,0,0,0.05); color: #8e8e93; font-weight:800;">0</div>
                      <span style="font-size: 9px; font-weight:700; color: #6e6e73;">Performance</span>
                    </div>
                    <div style="text-align: center;">
                      <div class="receipt-check" id="dial-seo" style="margin: 0 auto 8px; background: #fafbfc; border: 2px solid rgba(0,0,0,0.05); color: #8e8e93; font-weight:800;">0</div>
                      <span style="font-size: 9px; font-weight:700; color: #6e6e73;">Search SEO</span>
                    </div>
                    <div style="text-align: center;">
                      <div class="receipt-check" id="dial-a11y" style="margin: 0 auto 8px; background: #fafbfc; border: 2px solid rgba(0,0,0,0.05); color: #8e8e93; font-weight:800;">0</div>
                      <span style="font-size: 9px; font-weight:700; color: #6e6e73;">Accessibility</span>
                    </div>
                    <div style="text-align: center;">
                      <div class="receipt-check" id="dial-best" style="margin: 0 auto 8px; background: #fafbfc; border: 2px solid rgba(0,0,0,0.05); color: #8e8e93; font-weight:800;">0</div>
                      <span style="font-size: 9px; font-weight:700; color: #6e6e73;">Best Practice</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 2: CPC Bid Simulator -->
            <div class="simulator-panel" id="sim-custom">
              <div class="ide-mock" style="max-width: 100%;">
                <div class="ide-header">
                  <div class="ide-dots">
                    <span class="term-dot term-dot-r"></span>
                    <span class="term-dot term-dot-y"></span>
                    <span class="term-dot term-dot-g"></span>
                  </div>
                  <span style="font-size: 10px; color: #8e8e93; font-family: monospace;" id="cpc-roi-tag">Projected ROI: 0%</span>
                </div>
                <div class="ide-body" style="padding: 16px; min-height: 180px;">
                  <div style="display: flex; flex-direction: column; gap: 8px;">
                    <div style="display: flex; justify-content: space-between; font-size: 11px;">
                      <label style="color: #abb2bf;">Monthly Ad Budget:</label>
                      <strong style="color: #33c5f3;" id="cpc-budget-val">$5,000</strong>
                    </div>
                    <input type="range" min="1000" max="50000" step="1000" value="5000" class="resizer-slider" id="cpc-range" style="width: 100%; margin: 8px 0;" />
                  </div>
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 14px; border-top: 1px dashed rgba(255,255,255,0.08); padding-top: 12px; font-size: 11px; font-family: monospace;">
                    <div>
                      <p style="color: #636d83; margin: 0 0 4px;">Clicks: <strong style="color: #fff;" id="cpc-clicks">0</strong></p>
                      <p style="color: #636d83; margin: 0;">Avg CPC: <strong style="color: #fff;" id="cpc-rate">$0.00</strong></p>
                    </div>
                    <div>
                      <p style="color: #636d83; margin: 0 0 4px;">Conversions: <strong style="color: #fff;" id="cpc-converts">0</strong></p>
                      <p style="color: #636d83; margin: 0;">Proj. Revenue: <strong style="color: #10b981;" id="cpc-revenue">$0</strong></p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 3: A/B Split Copy Tester -->
            <div class="simulator-panel" id="sim-cms">
              <div class="cms-panel-wrap" style="grid-template-columns: 1fr; width: 100%;">
                <div style="display: flex; flex-direction: column; gap: 8px; width: 100%;">
                  <div style="display: flex; gap: 10px;">
                    <div style="flex:1;">
                      <label style="font-size: 10px; font-weight:700; color: #8e8e93;">Variant A Copy</label>
                      <input type="text" id="ab-variant-a" value="Build digital products" style="width: 100%; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 11px;" />
                    </div>
                    <div style="flex:1;">
                      <label style="font-size: 10px; font-weight:700; color: #8e8e93;">Variant B Copy</label>
                      <input type="text" id="ab-variant-b" value="We build fast, scalable products." style="width: 100%; background: #fff; border: 1px solid rgba(0,0,0,0.08); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 11px;" />
                    </div>
                  </div>
                  <button id="btn-run-ab" class="ide-btn-run" style="background:#10b981; padding: 8px; width: 100%; border-radius: 8px;">Run Split Test</button>
                </div>
                <div class="cms-canvas-wrap" style="min-height: 120px; padding: 12px; margin-top: 10px; background: #fafbfc; display: flex; flex-direction: column; justify-content: center;">
                  <div style="width: 100%; font-family: monospace; font-size: 11px; display: flex; flex-direction: column; gap: 8px;" id="ab-results-box">
                    <p style="color: #8e8e93; text-align: center; margin: 0;">Click "Run Split Test" to compute conversion index lift.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Panel 4: Conversion Funnel Optimizer -->
            <div class="simulator-panel" id="sim-ecom">
              <div class="ecom-panel-wrap" style="grid-template-columns: 1.15fr 0.85fr; gap: 20px;">
                <div class="ecom-checkout-card" style="padding: 16px; gap: 12px;">
                  <h4 class="ecom-checkout-title" style="font-size: 12px; margin: 0; padding-bottom: 6px;">Funnel Leak Optimizer</h4>
                  <div style="display: flex; flex-direction: column; gap: 10px;">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">Schema Markup</span>
                      <input type="checkbox" id="funnel-opt-schema" checked style="width: 32px; height: 16px;" />
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">Edge Page Speed</span>
                      <input type="checkbox" id="funnel-opt-speed" checked style="width: 32px; height: 16px;" />
                    </div>
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                      <span style="font-size: 11px; font-weight: 700; color: #3a3a3c;">Checkout Wallets</span>
                      <input type="checkbox" id="funnel-opt-wallets" checked style="width: 32px; height: 16px;" />
                    </div>
                  </div>
                  <button class="ecom-btn-pay" id="btn-run-funnel" style="background:#f59e0b; padding: 8px; border-radius: 8px; font-size: 11px;">Update Funnel Metrics</button>
                </div>
                <div class="ecom-graphics" style="display: flex; flex-direction: column; gap: 10px; width: 100%;">
                  <div class="payment-receipt" style="display: flex; flex-direction: column; width: 100%; padding: 12px; background: #fff; border-radius: 12px; box-sizing: border-box; font-family: monospace; font-size: 10px; text-align: left; gap: 6px;">
                    <div style="display:flex; justify-content: space-between;"><span>1. Traffic:</span><span id="funnel-step-1">10,000 visitors</span></div>
                    <div style="display:flex; justify-content: space-between;"><span>2. Leads:</span><span id="funnel-step-2">1,500 clicks</span></div>
                    <div style="display:flex; justify-content: space-between; border-bottom: 1px dashed rgba(0,0,0,0.08); padding-bottom: 4px;"><span>3. Checkout:</span><span id="funnel-step-3">220 actions</span></div>
                    <div style="display:flex; justify-content: space-between; font-weight: 700;"><span>Yield Yield:</span><span id="funnel-step-yield">2.2%</span></div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
  </section>
"""

MKT_TECH_STACK_HTML = """
  <!-- TECH STACK SECTION -->
  <section class="tech-stack-section reveal">
    <div class="container">
      <div class="tech-stack-head">
        <p class="section-eyebrow">DIGITAL MARKETING STACK</p>
        <h2 class="section-h2">Growth Tools We Use</h2>
        <p class="tech-stack-sub">
          We leverage advanced conversion tools, tracking pixels, schema systems, and ad network architectures to scale budgets.
        </p>
      </div>

      <div class="tech-tabs">
        <button class="tech-tab-btn active" data-tab="tech-frontend">Analytics &amp; Tracking</button>
        <button class="tech-tab-btn" data-tab="tech-backend">SEO &amp; Crawling</button>
        <button class="tech-tab-btn" data-tab="tech-database">PPC Ad Networks</button>
      </div>

      <!-- Tracking -->
      <div class="tech-grid active" id="tech-frontend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg>
          </div>
          <h3 class="tech-card-title">Google Analytics 4</h3>
          <p class="tech-card-desc">Hooking up granular user flow analytics, tracking audience pathways, and mapping checkout funnel loops.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
          </div>
          <h3 class="tech-card-title">Conversions API</h3>
          <p class="tech-card-desc">Bypassing third-party cookie blocking by sending purchase conversions directly server-to-server to Facebook / Meta.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3 class="tech-card-title">Hotjar Heatmaps</h3>
          <p class="tech-card-desc">Recording scroll pathways, identifying form leaks, and analyzing dynamic visual session recordings.</p>
        </div>
      </div>

      <!-- SEO -->
      <div class="tech-grid" id="tech-backend">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10z"/></svg>
          </div>
          <h3 class="tech-card-title">Schema &amp; JSON-LD</h3>
          <p class="tech-card-desc">Injecting structured data graphs into your site code, boosting search engine rich result cards.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
          </div>
          <h3 class="tech-card-title">Search Console</h3>
          <p class="tech-card-desc">Monitoring search index exclusions, verifying XML maps, and analyzing impressions by keyword.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </div>
          <h3 class="tech-card-title">Ahrefs &amp; Semrush</h3>
          <p class="tech-card-desc">Mapping keyword competition gaps, auditing backlink structures, and auditing technical search crawl limits.</p>
        </div>
      </div>

      <!-- Networks -->
      <div class="tech-grid" id="tech-database">
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l19-9-9 19-2-8-8-2z" /></svg>
          </div>
          <h3 class="tech-card-title">Google Ads (PMax)</h3>
          <p class="tech-card-desc">Deploying search ads and performance max campaigns matching transactional intent query parameters.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line></svg>
          </div>
          <h3 class="tech-card-title">Meta Ads (FB/IG)</h3>
          <p class="tech-card-desc">Orchestrating demographic ad splits, targeting conversion values, and tracking catalog sales metrics.</p>
        </div>
        <div class="tech-card">
          <div class="tech-icon-container" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
          </div>
          <h3 class="tech-card-title">LinkedIn Campaign</h3>
          <p class="tech-card-desc">Targeting exact corporate profiles, firmographic records, and engineering B2B funnel leads.</p>
        </div>
      </div>
    </div>
  </section>
"""

MKT_PROCESS_HTML = """
  <!-- DEVELOPMENT PROCESS SECTION -->
  <section class="process-section reveal">
    <div class="process-glow"></div>
    <div class="container">
      <div class="process-header">
        <p class="section-eyebrow">METHODOLOGY</p>
        <h2 class="section-h2">Our Growth Process</h2>
        <p style="font-size: 16px; line-height: 1.7; color: rgba(255, 255, 255, 0.6); margin-top: 14px;">
          How we map targets, build search parameters, launch campaign ads, test layout splits, and scale.
        </p>
      </div>

      <div class="process-grid">
        <!-- Step 1 -->
        <div class="process-card">
          <span class="process-step">Phase 01</span>
          <h3 class="process-card-title">Target Mapping</h3>
          <p class="process-card-desc">We outline competitor ad spends, verify search query volumes, and audit website tracking pixels.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="process-card">
          <span class="process-step">Phase 02</span>
          <h3 class="process-card-title">SEO Audit</h3>
          <p class="process-card-desc">We clean meta schema formats, optimize page load speeds, and verify search index mappings.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="process-card">
          <span class="process-step">Phase 03</span>
          <h3 class="process-card-title">PPC Launch</h3>
          <p class="process-card-desc">We draft high-converting ad variants, target customer intent query groups, and start search network bids.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="process-card">
          <span class="process-step">Phase 04</span>
          <h3 class="process-card-title">A/B Testing</h3>
          <p class="process-card-desc">We run conversion split tests on landing page headings, visual buttons, and cart checkout fields.</p>
          <div class="process-arrow">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </div>
        </div>

        <!-- Step 5 -->
        <div class="process-card">
          <span class="process-step">Phase 05</span>
          <h3 class="process-card-title">Scale &amp; Optimize</h3>
          <p class="process-card-desc">We scale successful ad sets, optimize cost-per-click values, and continuously scale search rankings.</p>
        </div>
      </div>
    </div>
  </section>
"""

MKT_FEATURES_HTML = """
  <!-- WEB CAPABILITIES SECTION -->
  <section class="features-grid-section reveal">
    <div class="container">
      <div class="features-grid-head">
        <p class="section-eyebrow">BUILT FOR SCALABLE ACQUISITION</p>
        <h2 class="section-h2">Core Capabilities in Every Campaign</h2>
        <p style="font-size: 16px; line-height: 1.7; color: var(--text-2); margin-top: 14px;">
          We engineer campaign architecture focused on data visibility, lower CAC, and high search relevance.
        </p>
      </div>

      <div class="features-grid">
        <!-- Feature 1 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(16, 185, 129, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg>
          </div>
          <h3 class="feature-grid-title">100% Data Visibility</h3>
          <p class="feature-grid-desc">We configure secure conversions APIs and UTM trackers, guaranteeing your dashboard displays accurate return-on-ad-spend (ROAS).</p>
        </div>

        <!-- Feature 2 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(51, 197, 243, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
          </div>
          <h3 class="feature-grid-title">Automated Bidding Filters</h3>
          <p class="feature-grid-desc">Deploy automated bid adjustments based on customer purchase triggers to maximize ad returns while preventing budget waste.</p>
        </div>

        <!-- Feature 3 -->
        <div class="feature-grid-card">
          <div class="feature-grid-icon" style="background: rgba(139, 92, 246, 0.08);">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </div>
          <h3 class="feature-grid-title">Search Relevance Schema</h3>
          <p class="feature-grid-desc">Deploy JSON-LD schemas and clean semantic tags, ensuring Google and Bing crawlers index your pages for valuable keywords.</p>
        </div>
      </div>
    </div>
  </section>
"""

MKT_WHY_CHOOSE_HTML = """
  <!-- WHY CHOOSE -->
  <section class="why-choose">
    <div class="container">
      <div class="why-choose-inner">
        <!-- LEFT SIDE -->
        <div class="why-choose-left">
          <div class="hero-eyebrow" style="margin-bottom: 14px;">
            <div class="hero-eyebrow-dot"></div>
            WHY CHOOSE GLOBOTECH
          </div>
          <h2 class="section-h2">Why GloboTech for <span>Digital Marketing &amp; SEO in USA?</span></h2>
          <p class="why-choose-desc" style="margin-bottom: 20px;">Globotech Solutions delivers marketing as an engineering pipeline rather than creative guesswork. We combine page layout adjustments, accurate conversion APIs, and structured meta tags to lower acquisition costs.</p>
          <p class="why-choose-desc" style="margin-bottom: 0;">We have helped companies across the USA audit ad spends, improve keyword rankings, and build clear reporting pipelines. We are committed to absolute data visibility, regular split testing, and continuous optimization. Learn more about our values on our About page.</p>
        </div>
        <!-- RIGHT SIDE -->
        <div class="why-choose-right">
          <div class="why-choose-grid-glow"></div>
          <div class="why-choose-grid">
            <!-- Card 1 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6l4 2"/></svg>
                </div>
              </div>
              <div class="why-card-title">100% Visibility</div>
              <div class="why-card-desc">We bridge Conversions APIs and Google Analytics 4, ensuring you track conversions with accuracy.</div>
            </div>
            <!-- Card 2 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"></path><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"></path></svg>
                </div>
              </div>
              <div class="why-card-title">Conversion Focus</div>
              <div class="why-card-desc">We optimize landing page speed, CTA visual accents, and checkout loops to boost your store conversion.</div>
            </div>
            <!-- Card 3 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                </div>
              </div>
              <div class="why-card-title">Structured Data</div>
              <div class="why-card-desc">We deploy structured schema JSONs so search robots index your sites and boost click-throughs.</div>
            </div>
            <!-- Card 4 -->
            <div class="why-card">
              <div class="why-card-icon-container">
                <div class="why-card-icon-bg">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#33c5f3" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 22 12 17 22 22 12 2"/></svg>
                </div>
              </div>
              <div class="why-card-title">Continuous Optimization</div>
              <div class="why-card-desc">We execute daily campaign tracking, monitor bidding scripts, and test copy split metrics continuously.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

MKT_JS = """
    // ── Flow Animation Pipeline Layout & Motion Path Calculator ──
    function updatePipeline() {
      const container = document.getElementById('pipeline-container');
      const path = document.getElementById('pipeline-path');
      const arrow = document.getElementById('pipeline-arrow');
      const dots = [
        document.getElementById('dot-1'),
        document.getElementById('dot-2'),
        document.getElementById('dot-3')
      ];
      if (!container || !path) return;

      const containerRect = container.getBoundingClientRect();

      const cards = [
        document.getElementById('card-req'),
        document.getElementById('card-design'),
        document.getElementById('card-dev'),
        document.getElementById('card-qa'),
        document.getElementById('card-dep'),
        document.getElementById('card-live')
      ];

      if (cards.some(c => !c)) return;

      const points = cards.map(card => {
        const rect = card.getBoundingClientRect();
        return {
          x: rect.left - containerRect.left + rect.width / 2,
          y: rect.top - containerRect.top + rect.height / 2
        };
      });

      const isMobile = window.innerWidth <= 768;
      let pathD = '';

      if (isMobile) {
        if (arrow) arrow.style.display = 'none';
        pathD = "M " + points[0].x + " " + points[0].y;
        for (let i = 1; i < points.length; i++) {
          pathD += " L " + points[i].x + " " + points[i].y;
        }
      } else {
        const pDev = points[2];
        const pQA = points[3];

        const rectDev = cards[2].getBoundingClientRect();
        const devRight = rectDev.right - containerRect.left;

        const dx = 50;
        const xRightLimit = devRight + dx;
        const R = 24;

        pathD = "M " + points[0].x + " " + points[0].y;
        pathD += " L " + points[1].x + " " + points[1].y;
        pathD += " L " + pDev.x + " " + pDev.y;

        pathD += " L " + (xRightLimit - R) + " " + pDev.y;
        pathD += " Q " + xRightLimit + " " + pDev.y + ", " + xRightLimit + " " + (pDev.y + R);
        pathD += " L " + xRightLimit + " " + (pQA.y - R);
        pathD += " Q " + xRightLimit + " " + pQA.y + ", " + (xRightLimit - R) + " " + pQA.y;
        pathD += " L " + pQA.x + " " + pQA.y;

        pathD += " L " + points[4].x + " " + points[4].y;
        pathD += " L " + points[5].x + " " + points[5].y;

        if (arrow) {
          arrow.style.display = 'block';
          const rectQA = cards[3].getBoundingClientRect();
          const qaRight = rectQA.right - containerRect.left;
          const offset = 2;
          const tipX = qaRight + offset;
          arrow.setAttribute('points', tipX + "," + pQA.y + " " + (tipX + 8) + "," + (pQA.y - 4) + " " + (tipX + 8) + "," + (pQA.y + 4));
        }
      }

      path.setAttribute('d', pathD);

      dots.forEach(dot => {
        if (dot) {
          dot.style.setProperty('offset-path', "path('" + pathD + "')");
          dot.style.setProperty('-webkit-offset-path', "path('" + pathD + "')");
        }
      });
    }

    window.addEventListener('DOMContentLoaded', updatePipeline);
    window.addEventListener('load', updatePipeline);
    window.addEventListener('resize', updatePipeline);
    if (document.fonts) {
      document.fonts.ready.then(updatePipeline);
    }

    (function () {
      var segments = [
        { id: 'card-req', at: 0.03 },
        { id: 'card-design', at: 0.18 },
        { id: 'card-dev', at: 0.35 },
        { id: 'card-qa', at: 0.62 },
        { id: 'card-dep', at: 0.79 },
        { id: 'card-live', at: 0.94 }
      ];
      var HALF = 0.065;
      var activeId = null;
      var epoch = performance.now();

      var dot1 = document.getElementById('dot-1');
      if (dot1) dot1.addEventListener('animationiteration', function () { epoch = performance.now(); });

      function tick(now) {
        var cycle = window.innerWidth <= 768 ? 7000 : 5500;
        var progress = ((now - epoch) % cycle) / cycle;
        if (progress < 0) progress += 1;

        var newId = null;
        for (var i = 0; i < segments.length; i++) {
          if (progress >= segments[i].at - HALF && progress <= segments[i].at + HALF) {
            newId = segments[i].id;
            break;
          }
        }

        if (newId !== activeId) {
          if (activeId) { var prev = document.getElementById(activeId); if (prev) prev.classList.remove('fnode-active'); }
          if (newId) { var next = document.getElementById(newId); if (next) next.classList.add('fnode-active'); }
          activeId = newId;
        }
        requestAnimationFrame(tick);
      }

      window.addEventListener('load', function () { epoch = performance.now(); requestAnimationFrame(tick); });
    })();

    // ── Mega Menu ──
    (function () {
      const trigger = document.getElementById('nav-services-trigger');
      const menu = document.getElementById('mega-services');
      if (!trigger || !menu) return;
      let closeTimer;
      function openMenu() {
        clearTimeout(closeTimer);
        trigger.classList.add('open');
        menu.style.display = 'block';
        requestAnimationFrame(() => { menu.classList.add('visible'); });
      }
      function closeMenu() {
        closeTimer = setTimeout(() => {
          trigger.classList.remove('open');
          menu.classList.remove('visible');
          setTimeout(() => { if (!menu.classList.contains('visible')) menu.style.display = 'none'; }, 220);
        }, 120);
      }
      trigger.addEventListener('mouseenter', openMenu);
      trigger.addEventListener('mouseleave', closeMenu);
      menu.addEventListener('mouseenter', () => clearTimeout(closeTimer));
      menu.addEventListener('mouseleave', closeMenu);
    })();

    // ── Side Drawer Navigation ──
    (function () {
      const ham = document.querySelector('.nav-hamburger');
      const drawer = document.getElementById('nav-drawer');
      const overlay = document.getElementById('nav-drawer-overlay');
      const closeBtn = document.getElementById('nav-drawer-close');
      const svcToggle = document.getElementById('nav-drawer-services-toggle');
      const svcMenu = document.getElementById('nav-drawer-services');
      if (!ham || !drawer) return;
      function openDrawer() { drawer.classList.add('open'); overlay && overlay.classList.add('open'); document.body.style.overflow = 'hidden'; ham.setAttribute('aria-expanded', 'true'); }
      function closeDrawer() { drawer.classList.remove('open'); overlay && overlay.classList.remove('open'); document.body.style.overflow = ''; ham.setAttribute('aria-expanded', 'false'); }
      ham.addEventListener('click', (e) => { e.stopPropagation(); openDrawer(); });
      overlay && overlay.addEventListener('click', closeDrawer);
      closeBtn && closeBtn.addEventListener('click', closeDrawer);
      svcToggle && svcToggle.addEventListener('click', () => { svcToggle.classList.toggle('open'); svcMenu && svcMenu.classList.toggle('open'); });
      document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDrawer(); });
    })();

    // ── Scroll Reveal Observer ──
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));

    // ── Specialty Showcase Tabs and Simulator Engine ──
    (function () {
      const tabs = document.querySelectorAll('.specialty-tab-btn');
      const panels = document.querySelectorAll('.simulator-panel');
      const glow = document.getElementById('showcase-glow');

      const themeColors = {
        purple: '#8b5cf6',
        cyan: '#33c5f3',
        green: '#10b981',
        orange: '#f59e0b'
      };

      tabs.forEach(tab => {
        tab.addEventListener('click', () => {
          const targetId = tab.getAttribute('data-tab');
          const theme = tab.getAttribute('data-theme');

          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          panels.forEach(p => p.classList.remove('active'));
          const targetPanel = document.getElementById(targetId);
          if (targetPanel) targetPanel.classList.add('active');

          if (glow && themeColors[theme]) {
            glow.style.background = themeColors[theme];
          }
        });
      });

      // --- SIMULATOR 1: SEO Auditor ---
      const runSeoBtn = document.getElementById('btn-run-seo');
      const seoUrlInput = document.getElementById('seo-url');
      const dialPerf = document.getElementById('dial-perf');
      const dialSeo = document.getElementById('dial-seo');
      const dialA11y = document.getElementById('dial-a11y');
      const dialBest = document.getElementById('dial-best');
      
      if (runSeoBtn && seoUrlInput && dialPerf) {
        runSeoBtn.addEventListener('click', () => {
          if (runSeoBtn.classList.contains('building')) return;
          
          runSeoBtn.classList.add('building');
          runSeoBtn.innerText = "Analyzing...";
          
          // Reset dials
          [dialPerf, dialSeo, dialA11y, dialBest].forEach(d => {
            d.innerText = "0";
            d.style.background = "#fafbfc";
            d.style.color = "#8e8e93";
            d.style.borderColor = "rgba(0,0,0,0.05)";
          });
          
          setTimeout(() => {
            // Animate dials
            const targetScores = [98, 100, 95, 100];
            const dials = [dialPerf, dialSeo, dialA11y, dialBest];
            
            dials.forEach((dial, idx) => {
              setTimeout(() => {
                dial.innerText = targetScores[idx];
                dial.style.background = "rgba(16, 185, 129, 0.08)";
                dial.style.color = "#10b981";
                dial.style.borderColor = "#10b981";
              }, 150 * idx);
            });
            
            runSeoBtn.classList.remove('building');
            runSeoBtn.innerText = "Analyze Site";
          }, 1000);
        });
      }

      // --- SIMULATOR 2: CPC Bid Simulator ---
      const cpcRange = document.getElementById('cpc-range');
      const budgetVal = document.getElementById('cpc-budget-val');
      const roiTag = document.getElementById('cpc-roi-tag');
      const cpcClicks = document.getElementById('cpc-clicks');
      const cpcRate = document.getElementById('cpc-rate');
      const cpcConverts = document.getElementById('cpc-converts');
      const cpcRevenue = document.getElementById('cpc-revenue');
      
      if (cpcRange && budgetVal) {
        cpcRange.addEventListener('input', (e) => {
          const val = parseInt(e.target.value, 10);
          budgetVal.innerText = "$" + val.toLocaleString();
          
          // Calculations based on budget
          const rate = 1.25 - (val / 100000); // larger budget, slightly lower cpc due to volume
          const clicks = Math.round(val / rate);
          const cr = 0.024; // 2.4% conversion rate
          const converts = Math.round(clicks * cr);
          const aov = 150; // $150 average order value
          const revenue = converts * aov;
          const roi = Math.round(((revenue - val) / val) * 100);
          
          cpcClicks.innerText = clicks.toLocaleString();
          cpcRate.innerText = "$" + rate.toFixed(2);
          cpcConverts.innerText = converts.toLocaleString();
          cpcRevenue.innerText = "$" + revenue.toLocaleString();
          roiTag.innerText = `Projected ROI: ${roi}%`;
        });
        
        // Trigger initial input event
        cpcRange.dispatchEvent(new Event('input'));
      }

      // --- SIMULATOR 3: A/B headline Split Tester ---
      const runAbBtn = document.getElementById('btn-run-ab');
      const inputA = document.getElementById('ab-variant-a');
      const inputB = document.getElementById('ab-variant-b');
      const abResults = document.getElementById('ab-results-box');
      
      if (runAbBtn && abResults) {
        runAbBtn.addEventListener('click', () => {
          if (runAbBtn.classList.contains('building')) return;
          
          runAbBtn.classList.add('building');
          runAbBtn.innerText = "Running Test Sprints...";
          abResults.innerHTML = '<p style="color: #8e8e93; text-align: center; margin: 0;">Generating search user click maps...</p>';
          
          setTimeout(() => {
            const valA = inputA.value;
            const valB = inputB.value;
            
            abResults.innerHTML = `
              <div style="display:flex; flex-direction:column; gap:6px;">
                <div style="display:flex; justify-content:space-between; background:rgba(0,0,0,0.02); padding:6px 10px; border-radius:4px;">
                  <span>A: "${valA}"</span>
                  <strong style="color: #6e6e73;">1.4% CTR</strong>
                </div>
                <div style="display:flex; justify-content:space-between; background:rgba(16, 185, 129, 0.08); padding:6px 10px; border-radius:4px; border-left:3px solid #10b981;">
                  <span>B: "${valB}"</span>
                  <strong style="color: #10b981;">2.8% CTR</strong>
                </div>
                <div style="font-size: 10px; color:#10b981; margin-top:2px;">✓ Variant B achieved 100% CTR conversion lift with 99.8% statistical confidence.</div>
              </div>
            `;
            
            runAbBtn.classList.remove('building');
            runAbBtn.innerText = "Run Split Test";
          }, 1200);
        });
      }

      // --- SIMULATOR 4: Funnel Leak Analyzer ---
      const runFunnelBtn = document.getElementById('btn-run-funnel');
      const optSchema = document.getElementById('funnel-opt-schema');
      const optSpeed = document.getElementById('funnel-opt-speed');
      const optWallets = document.getElementById('funnel-opt-wallets');
      const step1 = document.getElementById('funnel-step-1');
      const step2 = document.getElementById('funnel-step-2');
      const step3 = document.getElementById('funnel-step-3');
      const stepYield = document.getElementById('funnel-step-yield');
      
      if (runFunnelBtn && step1) {
        runFunnelBtn.addEventListener('click', () => {
          runFunnelBtn.innerText = "Updating...";
          
          setTimeout(() => {
            let traff = 10000;
            let leads = 1500;
            let checkouts = 220;
            
            if (optSchema.checked) {
              traff = 14500; // SEO Schema drives more traffic
            }
            if (optSpeed.checked) {
              leads = Math.round(traff * 0.22); // Fast loading keeps leads
            } else {
              leads = Math.round(traff * 0.15);
            }
            if (optWallets.checked) {
              checkouts = Math.round(leads * 0.24); // Instant wallets boost checkout conversion
            } else {
              checkouts = Math.round(leads * 0.14);
            }
            
            const y = ((checkouts / traff) * 100).toFixed(1);
            
            step1.innerText = traff.toLocaleString() + " visitors";
            step2.innerText = leads.toLocaleString() + " clicks";
            step3.innerText = checkouts.toLocaleString() + " actions";
            stepYield.innerText = y + "%";
            
            runFunnelBtn.innerText = "Update Funnel Metrics";
          }, 800);
        });
      }
    })();

    // ── Tech Stack Tab Switching ──
    document.querySelectorAll('.tech-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');

        document.querySelectorAll('.tech-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        document.querySelectorAll('.tech-grid').forEach(grid => grid.classList.remove('active'));
        const targetGrid = document.getElementById(targetId);
        if (targetGrid) {
          targetGrid.classList.add('active');
        }
      });
    });
"""

# ─────────────────────────────────────────────────────────────────────────────
# 4. REDESIGN PROCESS EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def redesign_page(filename, title, hero_html, showcase_html, tech_html, process_html, features_html, choose_html, custom_js):
    filepath = os.path.join(SRC_DIR, filename)
    if not os.path.exists(filepath):
        print(f"File {filepath} not found. Skipping.")
        return
        
    print(f"Redesigning {filename}...")
    
    # 1. Read base clean template (web-development.html has the updated styles and nav wrappers)
    with open(SOURCE_PAGE_PATH, 'r', encoding='utf-8') as f:
        base = f.read()
        
    # 2. Extract wrapper segments from base
    nav_html_range = extract_nav_html_block(base)
    footer_html_range = extract_footer_html_block(base)
    
    if not nav_html_range or not footer_html_range:
        print("ERROR: Nav/Footer wrappers not found in source of truth template!")
        return
        
    header_wrapper = base[:nav_html_range[0]]
    middle_nav_wrapper = base[nav_html_range[1]:footer_html_range[0]]
    footer_wrapper = base[footer_html_range[1]:]
    
    # Update title in header_wrapper
    header_wrapper = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', header_wrapper)
    
    # Standardize links back to root paths
    nav_html_tmpl = base[nav_html_range[0]:nav_html_range[1]]
    footer_html_tmpl = base[footer_html_range[0]:footer_html_range[1]]
    
    # Construct page middle content
    middle_body = f"{hero_html}\n{showcase_html}\n{tech_html}\n{process_html}\n{features_html}\n{choose_html}"
    
    # Assemble raw document
    doc = f"{header_wrapper}{nav_html_tmpl}{middle_body}{footer_html_tmpl}{footer_wrapper}"
    
    # Replace custom JS script at bottom
    js_range = find_nav_js_block(doc)
    if js_range:
        doc = doc[:js_range[0]] + custom_js + doc[js_range[1]:]
        
    # Apply dynamic active states for navigation links on this page
    doc = strip_active_classes(doc)
    
    # Services main nav link is active
    doc = doc.replace('href="../Services/services.html"', 'href="../Services/services.html" class="active"')
    
    # Sub-page links active
    if "ai-solutions" in filename:
        doc = doc.replace('class="mega-item" href="../ai-solutions/ai-solutions.html"', 'class="mega-item active" href="../ai-solutions/ai-solutions.html"')
        doc = doc.replace('href="../ai-solutions/ai-solutions.html">AI Solutions</a>', 'href="../ai-solutions/ai-solutions.html" class="active">AI Solutions</a>')
    elif "e-commerce-solutions" in filename:
        doc = doc.replace('class="mega-item" href="../e-commerce-solutions/e-commerce-solutions.html"', 'class="mega-item active" href="../e-commerce-solutions/e-commerce-solutions.html"')
        doc = doc.replace('href="../e-commerce-solutions/e-commerce-solutions.html">E-Commerce Solutions</a>', 'href="../e-commerce-solutions/e-commerce-solutions.html" class="active">E-Commerce Solutions</a>')
    elif "digital-marketing" in filename:
        doc = doc.replace('class="mega-item" href="../digital-marketing/digital-marketing.html"', 'class="mega-item active" href="../digital-marketing/digital-marketing.html"')
        doc = doc.replace('href="../digital-marketing/digital-marketing.html">Digital Marketing</a>', 'href="../digital-marketing/digital-marketing.html" class="active">Digital Marketing</a>')
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(doc)
        
    print(f"Successfully redesigned {filename}!")

def main():
    # 1. Redesign AI Solutions
    redesign_page(
        filename="ai-solutions/ai-solutions.html",
        title="AI Solutions & Intelligent Automation — Globotech Solutions",
        hero_html=AI_HERO_HTML,
        showcase_html=AI_SHOWCASE_HTML,
        tech_html=AI_TECH_STACK_HTML,
        process_html=AI_PROCESS_HTML,
        features_html=AI_FEATURES_HTML,
        choose_html=AI_WHY_CHOOSE_HTML,
        custom_js=AI_JS
    )
    
    # 2. Redesign E-Commerce Solutions
    redesign_page(
        filename="e-commerce-solutions/e-commerce-solutions.html",
        title="Custom E-Commerce Storefronts & Integrations — Globotech Solutions",
        hero_html=ECOM_HERO_HTML,
        showcase_html=ECOM_SHOWCASE_HTML,
        tech_html=ECOM_TECH_STACK_HTML,
        process_html=ECOM_PROCESS_HTML,
        features_html=ECOM_FEATURES_HTML,
        choose_html=ECOM_WHY_CHOOSE_HTML,
        custom_js=ECOM_JS
    )
    
    # 3. Redesign Digital Marketing
    redesign_page(
        filename="digital-marketing/digital-marketing.html",
        title="Digital Marketing, SEO, & Conversion Rate Optimization — Globotech Solutions",
        hero_html=MKT_HERO_HTML,
        showcase_html=MKT_SHOWCASE_HTML,
        tech_html=MKT_TECH_STACK_HTML,
        process_html=MKT_PROCESS_HTML,
        features_html=MKT_FEATURES_HTML,
        choose_html=MKT_WHY_CHOOSE_HTML,
        custom_js=MKT_JS
    )

if __name__ == "__main__":
    main()
