
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
        // Mobile: simple vertical sequence
        pathD = `M ${points[0].x} ${points[0].y}`;
        for (let i = 1; i < points.length; i++) {
          pathD += ` L ${points[i].x} ${points[i].y}`;
        }
      } else {
        // Desktop: Row 1 (L-to-R) -> orthogonal curve down -> Row 2 (R-to-L)
        const pDev = points[2];
        const pQA = points[3];

        // Calculate right boundary based on the Development card's right edge
        const rectDev = cards[2].getBoundingClientRect();
        const devRight = rectDev.right - containerRect.left;

        const dx = 50; // Distance the line travels right of the cards
        const xRightLimit = devRight + dx;
        const R = 24; // Rounded corner radius

        pathD = `M ${points[0].x} ${points[0].y}`;
        pathD += ` L ${points[1].x} ${points[1].y}`;
        pathD += ` L ${pDev.x} ${pDev.y}`;

        // Draw horizontal segment out of Development, curve 90° down, straight down, curve 90° left, and horizontal into QA
        pathD += ` L ${xRightLimit - R} ${pDev.y}`;
        pathD += ` Q ${xRightLimit} ${pDev.y}, ${xRightLimit} ${pDev.y + R}`;
        pathD += ` L ${xRightLimit} ${pQA.y - R}`;
        pathD += ` Q ${xRightLimit} ${pQA.y}, ${xRightLimit - R} ${pQA.y}`;
        pathD += ` L ${pQA.x} ${pQA.y}`;

        pathD += ` L ${points[4].x} ${points[4].y}`;
        pathD += ` L ${points[5].x} ${points[5].y}`;

        // Place and orient arrowhead pointing left at the right edge of QA Testing
        if (arrow) {
          arrow.style.display = 'block';
          const rectQA = cards[3].getBoundingClientRect();
          const qaRight = rectQA.right - containerRect.left;
          const offset = 2; // small clearance from card edge
          const tipX = qaRight + offset;
          arrow.setAttribute('points', `${tipX},${pQA.y} ${tipX + 8},${pQA.y - 4} ${tipX + 8},${pQA.y + 4}`);
        }
      }

      path.setAttribute('d', pathD);

      // Apply motion path dynamically
      dots.forEach(dot => {
        if (dot) {
          dot.style.setProperty('offset-path', `path('${pathD}')`);
          dot.style.setProperty('-webkit-offset-path', `path('${pathD}')`);
        }
      });
    }

    // Run layout on load, resize, and font rendering
    window.addEventListener('DOMContentLoaded', updatePipeline);
    window.addEventListener('load', updatePipeline);
    window.addEventListener('resize', updatePipeline);
    if (document.fonts) {
      document.fonts.ready.then(updatePipeline);
    }

    // ── Card Glow Sync with Dot Animation ──
    (function () {
      // Approximate offset-distance (0–1) when dots arrive at each card centre
      var segments = [
        { id: 'card-req', at: 0.03 },
        { id: 'card-design', at: 0.18 },
        { id: 'card-dev', at: 0.35 },
        { id: 'card-qa', at: 0.62 },
        { id: 'card-dep', at: 0.79 },
        { id: 'card-live', at: 0.94 }
      ];
      var HALF = 0.065;          // each card glows for ±6.5% of cycle
      var activeId = null;
      var epoch = performance.now();

      // Re-sync at every animation iteration of the lead dot
      var dot1 = document.getElementById('dot-1');
      if (dot1) dot1.addEventListener('animationiteration', function () { epoch = performance.now(); });

      function tick(now) {
        var cycle = window.innerWidth <= 768 ? 7000 : 5500;
        var progress = ((now - epoch) % cycle) / cycle;
        if (progress < 0) progress += 1; // guard against negative modulo

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
              blocked = True;
              logMsg = "System override attack blocked. Source IP sandboxed.";
            } else if (checkPii.checked) {
              blocked = True;
              logMsg = "Database SSN keys masked and secure.";
            } else if (checkSafety.checked) {
              blocked = True;
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

    // ── FAQ Toggling Accordion ──
    

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

          // Switch active tabs
          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          // Switch active panels
          panels.forEach(p => p.classList.remove('active'));
          const targetPanel = document.getElementById(targetId);
          if (targetPanel) targetPanel.classList.add('active');

          // Change dynamic glow color blob
          if (glow && themeColors[theme]) {
            glow.style.background = themeColors[theme];
          }
        });
      });

      // --- SIMULATOR 1: Compiler Build Simulator ---
      const runBtn = document.getElementById('btn-run-compiler');
      const consoleOut = document.getElementById('ide-console');
      if (runBtn && consoleOut) {
        runBtn.addEventListener('click', () => {
          if (runBtn.classList.contains('building')) return;

          runBtn.classList.add('building');
          runBtn.innerHTML = `
            <svg class="spinner" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" style="animation: spin 1s linear infinite; margin-right: 6px;"><circle cx="12" cy="12" r="10" stroke-opacity="0.3"></circle><path d="M4 12a8 8 0 0 1 8-8"></path></svg>
            Building...
          `;

          consoleOut.innerHTML = `
            <p class="ide-line info">[info] Starting Globotech build optimizer v2.4...</p>
            <p class="ide-line">[build] bundling assets and routing system...</p>
          `;

          // Progress lines
          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[build] optimizing database schema & index graphs...</p>`;
          }, 600);

          setTimeout(() => {
            consoleOut.innerHTML += `<p class="ide-line">[build] generating static HTML shells (SSG)...</p>`;
          }, 1200);

          setTimeout(() => {
            consoleOut.innerHTML += `
              <p class="ide-line success">✓ Compiled successfully!</p>
              <p class="ide-line info">ℹ Lighthouse Score: 100/100 (Performance, SEO, A11y)</p>
              <p class="ide-line info">ℹ First Contentful Paint: 0.2s | Total bundle size: 48.2 KB</p>
            `;
            runBtn.classList.remove('building');
            runBtn.innerHTML = `
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              Run Build
            `;
          }, 1800);
        });
      }

      // --- SIMULATOR 2: Responsive Browser Resizer ---
      const browser = document.getElementById('resizable-browser');
      const resizerRange = document.getElementById('resizer-range');
      const respBtns = document.querySelectorAll('.resp-btn');

      if (browser && resizerRange) {
        // Sync range input with browser width
        resizerRange.addEventListener('input', (e) => {
          const pct = e.target.value;
          browser.style.width = `${pct}%`;

          // Remove active classes from buttons since user is dragging slider
          respBtns.forEach(btn => btn.classList.remove('active'));
        });

        // Sync preset buttons
        respBtns.forEach(btn => {
          btn.addEventListener('click', () => {
            const widthVal = btn.getAttribute('data-width');
            browser.style.width = widthVal;

            respBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Update slider value
            if (widthVal === '100%') resizerRange.value = 100;
            else if (widthVal === '70%') resizerRange.value = 70;
            else if (widthVal === '45%') resizerRange.value = 45;
          });
        });
      }

      // --- SIMULATOR 3: Modular CMS Builder ---
      const cmsChips = document.querySelectorAll('.cms-item-chip');
      const canvasContainer = document.getElementById('cms-canvas-container');
      const emptyState = document.getElementById('cms-empty-state');
      const clearBtn = document.getElementById('cms-clear');

      const blockTemplates = {
        hero: `<div class="cms-placed-block hero-block"><div>⚡ <strong>Hero Header</strong> (Globotech Section)</div><button class="cms-block-delete">&times;</button></div>`,
        text: `<div class="cms-placed-block text-block"><div>📝 <strong>Rich Content Block</strong> (frosted typography)</div><button class="cms-block-delete">&times;</button></div>`,
        gallery: `<div class="cms-placed-block gallery-block"><div>🖼️ <strong>Image Grid</strong> (responsive masonry)</div><button class="cms-block-delete">&times;</button></div>`,
        cta: `<div class="cms-placed-block cta-block"><div>🚀 <strong>Action Button</strong> (high-converting lead capture)</div><button class="cms-block-delete">&times;</button></div>`
      };

      if (canvasContainer && cmsChips) {
        cmsChips.forEach(chip => {
          chip.addEventListener('click', () => {
            const blockType = chip.getAttribute('data-block');

            // Hide empty state if visible
            if (emptyState) emptyState.style.display = 'none';

            // Insert block
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = blockTemplates[blockType];
            const newBlock = tempDiv.firstChild;
            canvasContainer.appendChild(newBlock);

            // Bind delete button
            newBlock.querySelector('.cms-block-delete').addEventListener('click', () => {
              newBlock.remove();
              if (canvasContainer.children.length === 0 && emptyState) {
                emptyState.style.display = 'flex';
              }
            });
          });
        });
      }

      if (clearBtn && canvasContainer && emptyState) {
        clearBtn.addEventListener('click', () => {
          const blocks = canvasContainer.querySelectorAll('.cms-placed-block');
          blocks.forEach(b => b.remove());
          emptyState.style.display = 'flex';
        });
      }

      // --- SIMULATOR 4: Ecommerce Transaction Checkout ---
      const payBtn = document.getElementById('btn-place-order');
      const visaCard = document.getElementById('ecom-visa-card');
      const receipt = document.getElementById('checkout-receipt');

      if (payBtn && visaCard && receipt) {
        payBtn.addEventListener('click', () => {
          if (payBtn.classList.contains('processing')) return;

          payBtn.classList.add('processing');
          payBtn.innerText = 'Processing Order...';

          // Animate transaction
          setTimeout(() => {
            // Slide card away
            visaCard.classList.add('paid');

            setTimeout(() => {
              visaCard.style.display = 'none';
              // Slide receipt in
              receipt.style.display = 'flex';
              payBtn.innerText = 'Order Placed!';
              payBtn.style.background = '#10b981';
            }, 600);
          }, 1200);
        });
      }
    })();

    // ── Tech Stack Tab Switching ──
    document.querySelectorAll('.tech-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-tab');

        // Update active tab button
        document.querySelectorAll('.tech-tab-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        // Update active tech grid
        document.querySelectorAll('.tech-grid').forEach(grid => grid.classList.remove('active'));
        const targetGrid = document.getElementById(targetId);
        if (targetGrid) {
          targetGrid.classList.add('active');
        }
      });
    });
  