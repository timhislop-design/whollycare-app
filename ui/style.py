"""
style.py — WhollyCare brand styles
Soft plum palette. inject() must be called on every page after st.set_page_config().
"""

import streamlit as st

DARK    = "#4A1A5C"   # deep plum
MID     = "#7A3A8C"   # mid plum
ACCENT  = "#A45AB0"   # accent plum
LIGHT   = "#C98AD4"   # light plum
BG      = "#F8F4FB"   # lavender cream
FOUND   = "#E87C2A"   # Found Money orange

BRAND_NAME   = "WhollyCare™"
BRAND_DOMAIN = "wholly-care.com"
TAGLINE      = "The personal care plan that pays you back."
PARENT_URL   = "https://sentir-solutions.com"


def inject():
    st.html(f"""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;1,9..144,300&family=Inter:wght@300;400;500;600&display=swap');

      :root {{
        --wc-dark:   {DARK};
        --wc-mid:    {MID};
        --wc-accent: {ACCENT};
        --wc-light:  {LIGHT};
        --wc-bg:     {BG};
        --wc-found:  {FOUND};
      }}

      [data-testid="stAppViewContainer"] > .main {{
        background: var(--wc-bg) !important;
      }}
      .block-container {{ padding-top: 0.5rem !important; }}
      [data-testid="stSidebarNav"] {{ display: none !important; }}
      header[data-testid="stHeader"] {{ display: none !important; }}

      .wc-card {{
        transition: transform 0.18s ease, box-shadow 0.18s ease !important;
      }}
      .wc-card:hover {{
        transform: translateY(-4px) !important;
        box-shadow: 0 14px 40px rgba(74,26,92,0.12) !important;
      }}

      .wc-tier-price {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--wc-dark);
        line-height: 1;
        margin: 0.5rem 0 0.25rem;
      }}

      .wc-tier-name {{
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: var(--wc-accent);
        margin-bottom: 0.25rem;
      }}

      .wc-stat {{
        background: #FFFFFF;
        border: 1px solid #DDD0E8;
        border-left: 3px solid var(--wc-found);
        padding: 1.25rem 1.5rem;
        border-radius: 6px;
      }}

      .wc-stat-num {{
        font-family: 'Fraunces', serif;
        font-size: 2.2rem;
        font-weight: 300;
        color: var(--wc-dark);
        line-height: 1;
      }}

      .wc-stat-label {{
        font-size: 0.82rem;
        color: #5C4870;
        margin-top: 0.3rem;
        line-height: 1.5;
      }}

      .wc-sincere {{
        display: inline-block;
        background: rgba(255,255,255,0.08);
        color: rgba(255,255,255,0.8);
        font-size: 0.72rem;
        font-weight: 500;
        padding: 4px 12px;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.12);
        margin: 2px;
      }}
    </style>
    """)


def page_header(title: str, subtitle: str = ""):
    sub_html = f"<p style='color:{LIGHT};font-size:0.95rem;margin-top:0.5rem;'>{subtitle}</p>" if subtitle else ""
    st.html(f"""
    <div style='background:linear-gradient(135deg,{DARK} 0%,{MID} 100%);
                padding:2.5rem 2rem 2rem;border-radius:12px;margin-bottom:1.5rem;'>
      <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
                color:{LIGHT};margin-bottom:0.5rem;'>WhollyCare™</p>
      <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:2rem;
                 color:#FFFFFF;margin:0;line-height:1.2;'>{title}</h1>
      {sub_html}
    </div>
    """)


def brand_nav():
    st.html(f"""
    <div style='display:flex;align-items:center;gap:10px;margin-bottom:16px;
                padding:10px 18px;background:#FFFFFF;
                border-radius:10px;border:1px solid #DDD0E8;'>
      <svg width="28" height="28" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 38 Q16 28 22 16 Q30 9 40 13 Q38 25 28 32 Q24 35 20 38Z"
              fill="{MID}" opacity="0.85"/>
        <line x1="20" y1="38" x2="31" y2="23" stroke="{ACCENT}" stroke-width="1.5"
              stroke-linecap="round" opacity="0.7"/>
        <path d="M12 30 Q9 25 12 20 Q15 25 12 30Z" fill="{LIGHT}" opacity="0.7"/>
        <circle cx="35" cy="10" r="2" fill="{ACCENT}" opacity="0.5"/>
      </svg>
      <span style='font-size:1rem;font-weight:700;color:{DARK};'>WhollyCare™</span>
      <span style='color:#D8C4E8;margin:0 4px;'>·</span>
      <span style='font-size:0.8rem;color:#666;'>a
        <a href="{PARENT_URL}" target="_blank"
           style="color:{MID};font-weight:600;text-decoration:none;">Sentir Solutions</a>® Company</span>
    </div>
    """)
