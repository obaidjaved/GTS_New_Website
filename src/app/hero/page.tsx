import React from 'react';

export default function HeroPage() {
  return (
    <>
      <style dangerouslySetInnerHTML={{
        __html: `
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800;900&family=Inter:wght@400;500;600&display=swap');

        .hero-container {
          font-family: 'Inter', -apple-system, sans-serif;
          background: #F5F5F7;
          min-height: 100vh;
          padding: 40px 24px 80px;
        }

        .hero-container * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        .hero-container .page-label{
          text-align:center;
          font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
          color:#9ca3af;margin-bottom:32px;
        }

        /* ── HERO ── */
        .hero-container .hero{
          max-width:1100px;
          margin:0 auto;
          background:#ffffff;
          border-radius:32px;
          overflow:hidden;
          box-shadow:0 4px 24px rgba(0,0,0,0.06),0 24px 80px rgba(0,0,0,0.08);
          position:relative;
          min-height:560px;
          display:flex;align-items:center;
          padding:72px 72px;
        }

        /* Mesh background */
        .hero-container .hero::before{
          content:'';position:absolute;inset:0;
          background:
            radial-gradient(ellipse 55% 75% at 90% 35%, rgba(51,197,243,0.11) 0%,transparent 65%),
            radial-gradient(ellipse 35% 45% at 10% 85%, rgba(16,185,129,0.06) 0%,transparent 55%),
            radial-gradient(ellipse 30% 40% at 75% 90%, rgba(139,92,246,0.06) 0%,transparent 55%);
          pointer-events:none;
        }

        .hero-container .hero-grid{
          position:relative;z-index:1;
          display:grid;
          grid-template-columns:1fr 1fr;
          grid-template-rows:auto auto;
          gap:0 56px;
          align-items:start;
          width:100%;
        }

        /* Full-width heading row spans both columns */
        .hero-container .hero-heading-full{
          grid-column: 1 / -1;
          margin-bottom:0;
        }

        /* Left content bottom */
        .hero-container .hero-left{
          grid-column: 1;
        }

        /* Right flow stays in its column, row 2 only */
        .hero-container .hero-right{
          grid-column: 2;
          grid-row: 2;
          display:flex;
          align-items:center;
          justify-content:center;
          margin-top:45px;
        }

        /* ── LEFT ── */
        .hero-container .eyebrow{
          display:inline-flex;align-items:center;gap:8px;
          font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
          color:#33c5f3;margin-bottom:24px;
        }
        .hero-container .eyebrow-dot{width:6px;height:6px;border-radius:50%;background:#33c5f3;animation:blink 2s ease infinite;}
        @keyframes blink{0%,100%{opacity:1;}50%{opacity:.3;}}

        .hero-container h1{
          font-family:'Plus Jakarta Sans',sans-serif;
          font-size:clamp(32px,3.8vw,52px);
          font-weight:900;
          letter-spacing:-.045em;
          line-height:1.08;
          color:#1d1d1f;
          margin-bottom:0;
        }
        .hero-container h1 em{
          font-style:normal;
          background:linear-gradient(110deg,#33c5f3 0%,#8b5cf6 100%);
          -webkit-background-clip:text;
          -webkit-text-fill-color:transparent;
          background-clip:text;
        }
        /* "Businesses" standalone heading — seamless continuation of h1 */
        .hero-container .h1-businesses{
          font-family:'Plus Jakarta Sans',sans-serif;
          font-size:clamp(32px,3.8vw,52px);
          font-weight:900;
          letter-spacing:-.045em;
          line-height:1.08;
          color:#1d1d1f;
          margin-top:0;
          margin-bottom:22px;
        }

        .hero-container .sub{
          font-size:16px;line-height:1.7;
          color:#6e6e73;
          max-width:380px;
          margin-bottom:36px;
        }

        .hero-container .ctas{display:flex;gap:12px;align-items:center;margin-bottom:44px;}
        .hero-container .btn-primary{
          background:#1d1d1f;color:#fff;
          font-family:'Plus Jakarta Sans',sans-serif;
          font-size:15px;font-weight:700;letter-spacing:-.01em;
          padding:15px 30px;border-radius:100px;
          white-space:nowrap;
          box-shadow:0 4px 16px rgba(0,0,0,0.15);
          transition:transform .2s ease,box-shadow .2s ease;
          cursor:default;
        }
        .hero-container .btn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 24px rgba(0,0,0,0.2);}
        .hero-container .btn-secondary{
          font-size:15px;font-weight:600;color:#6e6e73;
          padding:15px 20px;
          cursor:default;
          display:flex;align-items:center;gap:6px;
        }
        .hero-container .btn-secondary::after{content:'→';opacity:.5;}

        /* Trust bar */
        .hero-container .trust{
          display:flex;gap:32px;
          padding-top:24px;
          border-top:1px solid rgba(0,0,0,0.07);
          margin-bottom:20px;
        }
        .hero-container .trust-item .n{
          font-family:'Plus Jakarta Sans',sans-serif;
          font-size:26px;font-weight:900;letter-spacing:-.04em;
          color:#1d1d1f;line-height:1;
        }
        .hero-container .trust-item .n span{color:#33c5f3;}
        .hero-container .trust-item .l{font-size:12px;color:#9ca3af;font-weight:500;margin-top:4px;}

        /* Trusted By */
        .hero-container .trusted-by{
          display:flex;
          flex-direction:column;
          gap:10px;
        }
        .hero-container .trusted-by-label{
          font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
          color:#c0c0c8;
        }
        .hero-container .trusted-by-logos{
          display:flex;
          align-items:center;
          gap:20px;
        }
        .hero-container .trusted-by-logos img{
          height:28px;
          width:auto;
          object-fit:contain;
          opacity:0.55;
          filter:grayscale(1);
          transition:opacity .2s ease,filter .2s ease;
        }
        .hero-container .trusted-by-logos img:hover{
          opacity:0.85;
          filter:grayscale(0);
        }

        /* ── RIGHT: FLOW DIAGRAM ── */
        .hero-container .flow{
          display:flex;
          align-items:center;
          justify-content:center;
          gap:0;
          width:100%;
        }

        /* Input/Output columns */
        .hero-container .flow-col{
          display:flex;flex-direction:column;
          gap:12px;
          flex:1;
          min-width:0;
        }

        .hero-container .fnode{
          background:rgba(255,255,255,0.82);
          backdrop-filter:blur(16px) saturate(160%);
          -webkit-backdrop-filter:blur(16px) saturate(160%);
          border:1px solid rgba(255,255,255,0.95);
          border-radius:14px;
          padding:12px 14px;
          box-shadow:0 1px 4px rgba(0,0,0,0.04),0 4px 16px rgba(0,0,0,0.05);
          display:flex;align-items:center;gap:10px;
          transition:transform .3s ease,box-shadow .3s ease;
        }
        .hero-container .fnode:hover{transform:translateX(-3px);box-shadow:0 2px 8px rgba(0,0,0,0.06),0 8px 24px rgba(0,0,0,0.08);}
        .hero-container .fnode-right:hover{transform:translateX(3px);}

        .hero-container .fnode-icon{
          width:34px;height:34px;border-radius:10px;
          display:flex;align-items:center;justify-content:center;
          font-size:15px;flex-shrink:0;
        }
        .hero-container .fnode-text .name{
          font-family:'Plus Jakarta Sans',sans-serif;
          font-size:13px;font-weight:700;color:#1d1d1f;
          line-height:1.2;margin-bottom:2px;
        }
        .hero-container .fnode-text .detail{font-size:11px;color:#9ca3af;}

        /* Output nodes — no border accent, same as input nodes */
        .hero-container .fnode-out{
          border-left: none;
        }

        /* ── CONNECTOR ── */
        .hero-container .connector{
          width:52px;flex-shrink:0;
          display:flex;flex-direction:column;
          align-items:center;justify-content:center;
          gap:8px;
          position:relative;
        }
        .hero-container .conn-line{
          position:absolute;
          left:0;right:0;top:50%;
          height:1px;
          transform:translateY(-50%);
        }
        .hero-container .conn-line-left{background:linear-gradient(90deg,rgba(51,197,243,0.08),rgba(51,197,243,0.35));}
        .hero-container .conn-line-right{background:linear-gradient(90deg,rgba(51,197,243,0.35),rgba(51,197,243,0.08));}

        /* Animated flow dots */
        .hero-container .fdot{
          position:absolute;
          top:50%;transform:translateY(-50%);
          width:6px;height:6px;border-radius:50%;
          background:#33c5f3;
          box-shadow:0 0 6px rgba(51,197,243,0.6);
          animation:flowR 1.8s linear infinite;
          opacity:0;
        }
        .hero-container .fdot:nth-child(2){animation-delay:.6s;}
        .hero-container .fdot:nth-child(3){animation-delay:1.2s;}
        @keyframes flowR{
          0%{left:0%;opacity:0;}
          10%{opacity:1;}
          90%{opacity:1;}
          100%{left:100%;opacity:0;}
        }
        .hero-container .fdot-rev{animation-name:flowL;}
        @keyframes flowL{
          0%{right:0%;left:auto;opacity:0;}
          10%{opacity:1;}
          90%{opacity:1;}
          100%{right:100%;left:auto;opacity:0;}
        }

        /* ── ENGINE HUB ── */
        .hero-container .engine{
          flex-shrink:0;
          display:flex;
          align-items:center;
          justify-content:center;
          position:relative;
          width:148px;height:148px;
        }

        /* Pulse rings */
        .hero-container .pulse-ring{
          position:absolute;
          border-radius:50%;
          border:1.5px solid rgba(51,197,243,0.2);
          animation:pulseRing 3.2s ease-out infinite;
        }
        .hero-container .pulse-ring:nth-child(1){width:148px;height:148px;animation-delay:0s;}
        .hero-container .pulse-ring:nth-child(2){width:148px;height:148px;animation-delay:1.06s;}
        .hero-container .pulse-ring:nth-child(3){width:148px;height:148px;animation-delay:2.12s;}
        @keyframes pulseRing{
          0%{transform:scale(1);opacity:.45;}
          100%{transform:scale(1.75);opacity:0;}
        }

        /* Engine circle */
        .hero-container .engine-circle{
          position:absolute;
          width:112px;height:112px;border-radius:50%;
          background:#ffffff;
          border:1.5px solid rgba(51,197,243,0.2);
          box-shadow:
            0 0 0 8px rgba(51,197,243,0.05),
            0 4px 24px rgba(51,197,243,0.14),
            0 12px 48px rgba(0,0,0,0.07),
            inset 0 1px 0 rgba(255,255,255,1);
          display:flex;align-items:center;justify-content:center;
        }

        /* Rotating ring */
        .hero-container .engine-ring-svg{
          position:absolute;
          width:132px;height:132px;
          animation:spinRing 14s linear infinite;
        }
        @keyframes spinRing{from{transform:rotate(0deg);}to{transform:rotate(360deg);}}

        /* Emblem — use mix-blend-mode so gradients render correctly on white */
        .hero-container .emblem{
          width:72px;height:72px;
          display:flex;align-items:center;justify-content:center;
          position:relative;z-index:1;
          background:#fff;
          border-radius:50%;
        }
        .hero-container .emblem img{
          width:100%;height:100%;
          object-fit:contain;
          filter:drop-shadow(0 2px 8px rgba(51,197,243,0.25));
        }
      `}} />
      <div className="hero-container">
        <p className="page-label">Hero Banner — Option B Refined · Globotech emblem in engine</p>

        <div className="hero">
          {/* HERO GRID */}
          <div className="hero-grid">

            {/* FULL-WIDTH HEADING — spans both columns, sits above flow diagram */}
            <div className="hero-heading-full">
              <div className="eyebrow"><span className="eyebrow-dot"></span>Software Studio — Web · Mobile · AI</div>
              <h1>Custom <em>AI Development, Automation</em><br /><em>& Full-Stack Solutions</em> for Ambitious</h1>
            </div>

            {/* LEFT BOTTOM — "Businesses" + sub + CTAs + trust */}
            <div className="hero-left">
              <div className="h1-businesses">Businesses</div>
              <p className="sub">From discovery to post-launch — Globotech designs, builds, and owns your entire product in-house. No outsourcing. No surprises.</p>
              <div className="ctas">
                <div className="btn-primary">Start a Project →</div>
                <div className="btn-secondary">See our work</div>
              </div>
              <div className="trust">
                <div className="trust-item"><div className="n">200<span>+</span></div><div className="l">Projects delivered</div></div>
                <div className="trust-item"><div className="n">98<span>%</span></div><div className="l">Client retention</div></div>
                <div className="trust-item"><div className="n">5.0<span>★</span></div><div className="l">Clutch rating</div></div>
              </div>
              <div className="trusted-by">
                <div className="trusted-by-label">Trusted by</div>
                <div className="trusted-by-logos">
                  <img src="/assets/logos/Venturous.png" alt="Venturous" />
                  <img src="/assets/logos/Throne_1.avif" alt="Throne" />
                </div>
              </div>
            </div>

            {/* RIGHT FLOW DIAGRAM — spans rows 1 & 2 */}
            <div className="hero-right">
              <div className="flow">

                {/* INPUT NODES */}
                <div className="flow-col">
                  <div className="fnode">
                    <div className="fnode-icon" style={{ background: 'rgba(99,102,241,0.1)' }}>💡</div>
                    <div className="fnode-text">
                      <div className="name">Your Idea</div>
                      <div className="detail">Vision & goals</div>
                    </div>
                  </div>
                  <div className="fnode">
                    <div className="fnode-icon" style={{ background: 'rgba(51,197,243,0.1)' }}>📋</div>
                    <div className="fnode-text">
                      <div className="name">Requirements</div>
                      <div className="detail">Scope locked</div>
                    </div>
                  </div>
                  <div className="fnode">
                    <div className="fnode-icon" style={{ background: 'rgba(16,185,129,0.1)' }}>🎨</div>
                    <div className="fnode-text">
                      <div className="name">Design Brief</div>
                      <div className="detail">Brand & UX</div>
                    </div>
                  </div>
                </div>

                {/* LEFT CONNECTOR */}
                <div className="connector">
                  <div className="conn-line conn-line-left"></div>
                  <div className="fdot" style={{ animationDelay: '0s' }}></div>
                  <div className="fdot" style={{ animationDelay: '.6s' }}></div>
                  <div className="fdot" style={{ animationDelay: '1.2s' }}></div>
                </div>

                {/* ENGINE HUB */}
                <div className="engine">
                  <div className="pulse-ring"></div>
                  <div className="pulse-ring"></div>
                  <div className="pulse-ring"></div>

                  {/* Rotating dashed ring */}
                  <svg className="engine-ring-svg" viewBox="0 0 106 106" fill="none">
                    <circle cx="53" cy="53" r="50" stroke="#33c5f3" strokeWidth="1.2"
                      strokeDasharray="5 4" strokeLinecap="round" />
                  </svg>

                  {/* Solid circle with emblem */}
                  <div className="engine-circle">
                    <div className="emblem">
                      <img src="/assets/emblem.svg" alt="Globotech" />
                    </div>
                  </div>
                </div>

                {/* RIGHT CONNECTOR */}
                <div className="connector">
                  <div className="conn-line conn-line-right"></div>
                  <div className="fdot fdot-rev" style={{ animationDelay: '.3s' }}></div>
                  <div className="fdot fdot-rev" style={{ animationDelay: '.9s' }}></div>
                  <div className="fdot fdot-rev" style={{ animationDelay: '1.5s' }}></div>
                </div>

                {/* OUTPUT NODES */}
                <div className="flow-col">
                  <div className="fnode fnode-right fnode-out web">
                    <div className="fnode-icon" style={{ background: 'rgba(99,102,241,0.1)' }}>🌐</div>
                    <div className="fnode-text">
                      <div className="name">Web Product</div>
                      <div className="detail">Shipped & live</div>
                    </div>
                  </div>
                  <div className="fnode fnode-right fnode-out mob">
                    <div className="fnode-icon" style={{ background: 'rgba(51,197,243,0.1)' }}>📱</div>
                    <div className="fnode-text">
                      <div className="name">Mobile App</div>
                      <div className="detail">iOS + Android</div>
                    </div>
                  </div>
                  <div className="fnode fnode-right fnode-out ai">
                    <div className="fnode-icon" style={{ background: 'rgba(139,92,246,0.1)' }}>🤖</div>
                    <div className="fnode-text">
                      <div className="name">AI Feature</div>
                      <div className="detail">Production-ready</div>
                    </div>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
