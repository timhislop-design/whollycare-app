"""
Home.py — WhollyCare Landing Page
Run with:  streamlit run Home.py
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyCare — Personal Care, Honestly Priced",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()
style.brand_nav()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='position:relative;overflow:hidden;
            background:linear-gradient(140deg,#2E0A3D 0%,#4A1A5C 55%,#7A3A8C 100%);
            border-radius:18px;padding:54px 52px 50px;margin-bottom:20px;'>

  <!-- Decorative leaf/droplet, right side -->
  <svg style='position:absolute;right:60px;top:50%;transform:translateY(-55%);
              opacity:0.10;pointer-events:none;'
       width="200" height="200" viewBox="0 0 48 48" fill="none"
       xmlns="http://www.w3.org/2000/svg">
    <path d="M18 42 Q12 28 20 12 Q32 4 44 10 Q42 26 30 36 Q24 40 18 42Z" fill="white"/>
    <path d="M10 34 Q6 28 10 22 Q14 28 10 34Z" fill="white" opacity="0.6"/>
  </svg>

  <!-- Badge -->
  <div style='display:inline-flex;align-items:center;gap:7px;
              background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.18);
              border-radius:20px;padding:5px 14px;margin-bottom:20px;'>
    <span style='width:7px;height:7px;background:#A45AB0;border-radius:50%;
                 display:inline-block;'></span>
    <span style='font-size:0.72rem;font-weight:600;letter-spacing:0.1em;
                 text-transform:uppercase;color:rgba(255,255,255,0.85);'>
      Personal care intelligence &nbsp;·&nbsp; Ingredient-aware savings
    </span>
  </div>

  <!-- Headline -->
  <h1 style='font-family:Fraunces,serif;font-weight:300;font-size:clamp(1.9rem,3.5vw,2.9rem);
             color:#FFFFFF;line-height:1.2;margin:0 0 14px;max-width:560px;'>
    The beauty industry is opaque.<br />WhollyCare is<br /><em style='color:#C98AD4;'>the transparent alternative.</em>
  </h1>

  <p style='font-size:1.05rem;color:rgba(255,255,255,0.75);max-width:500px;
            line-height:1.8;margin-bottom:28px;'>
    WhollyCare cross-compares personal care and beauty prices across CVS, Walgreens,
    Ulta, and Target — filtered by your ingredient preferences. Fragrance-free,
    paraben-free, cruelty-free, sulfate-free. What matters to you is a hard rule.
  </p>

  <!-- Tagline -->
  <div style='display:inline-block;background:rgba(232,124,42,0.18);
              border:1px solid rgba(232,124,42,0.35);border-radius:8px;
              padding:10px 20px;margin-bottom:28px;'>
    <span style='font-family:Fraunces,serif;font-style:italic;font-size:1.1rem;
                 color:#F4A96A;font-weight:300;'>
      The personal care plan that pays you back.
    </span>
  </div>

  <div style='display:flex;gap:12px;flex-wrap:wrap;'>
    <a href="#" style='display:inline-block;background:#E87C2A;color:#FFFFFF;
                       text-decoration:none;font-size:0.9rem;font-weight:600;
                       padding:12px 28px;border-radius:8px;letter-spacing:0.02em;'>
      Join the Waitlist
    </a>
    <a href="https://sentir-solutions.com" target="_blank"
       style='display:inline-block;background:rgba(255,255,255,0.1);color:#FFFFFF;
              border:1px solid rgba(255,255,255,0.25);text-decoration:none;
              font-size:0.9rem;font-weight:400;padding:12px 24px;border-radius:8px;'>
      About Sentir Solutions →
    </a>
  </div>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# INGREDIENT CONSTRAINTS
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>Your Ingredients. Your Rules.</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#4A1A5C;margin:0 0 6px;'>What you won't use is a hard rule — not a preference.</h2>
  <p style='color:#5C4870;font-size:0.95rem;max-width:520px;'>
    WhollyCare runs ingredient constraints before price comparison. A product
    that fails your profile doesn't appear — at any price.
  </p>
</div>
""")

col1, col2, col3 = st.columns(3, gap="medium")

filters = [
    ("Ingredient Avoidance", "#4A1A5C",
     "Fragrance-free, paraben-free, sulfate-free, phthalate-free, formaldehyde-free. Silicone-free. Alcohol-free. Any ingredient you avoid becomes a hard filter."),
    ("Ethical Commitments", "#7A3A8C",
     "Cruelty-free, vegan, reef-safe, sustainably sourced. These aren't \"nice to have\" filters — they're constraints that run first. No brand pays to bypass them."),
    ("Skin & Sensitivity", "#A45AB0",
     "Hypoallergenic, non-comedogenic, eczema-safe, sensitive skin formulated. Dermatologist-tested flags. Specific allergen avoidance (lanolin, propylene glycol, etc.)."),
]

for col, (title, color, desc) in zip([col1, col2, col3], filters):
    with col:
        st.html(f"""
        <div class='wc-card' style='background:#FFFFFF;border:1px solid #DDD0E8;
                                    border-top:3px solid {color};border-radius:10px;
                                    padding:1.75rem;height:100%;'>
          <h3 style='font-size:1rem;font-weight:600;color:#4A1A5C;margin-bottom:0.6rem;'>
            {title}
          </h3>
          <p style='font-size:0.87rem;color:#5C4870;line-height:1.75;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# HOW IT WORKS
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>How It Works</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#4A1A5C;margin:0 0 6px;'>Your values filter first. Savings follow.</h2>
</div>
""")

s1, s2, s3, s4 = st.columns(4, gap="medium")

steps = [
    ("01", "Set your profile", "Your ingredient avoidances, ethical commitments, and skin sensitivity flags. These never change without your explicit action."),
    ("02", "Constraint engine runs", "Every product in every store is checked against your profile. Anything that fails is removed — not deprioritized. Removed."),
    ("03", "Cross-store pricing", "What passes your filter is cross-compared across CVS, Walgreens, Ulta, Target — by unit price (per fl oz, per count), not package size."),
    ("04", "Your care list", "One list, per store, with net savings shown — loyalty discounts and shipping costs included. The number in your pocket."),
]

for col, (num, title, desc) in zip([s1, s2, s3, s4], steps):
    with col:
        st.html(f"""
        <div class='wc-card' style='background:#FFFFFF;border:1px solid #DDD0E8;
                                    border-top:3px solid #A45AB0;border-radius:10px;
                                    padding:1.5rem;'>
          <div style='font-family:Fraunces,serif;font-size:1.8rem;font-weight:300;
                      color:#DDD0E8;margin-bottom:0.75rem;'>{num}</div>
          <h4 style='font-size:0.92rem;font-weight:600;color:#4A1A5C;
                     margin-bottom:0.4rem;'>{title}</h4>
          <p style='font-size:0.84rem;color:#5C4870;line-height:1.7;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# PRICING
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='margin-bottom:8px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>Pricing</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#4A1A5C;margin:0 0 6px;'>Start free. Stay honest.</h2>
</div>
""")

p1, p2, p3, p4 = st.columns(4, gap="medium")

tiers = [
    ("Price Finder",   "Free",   "forever",
     "Cross-store unit-price comparison for personal care and beauty. Always free."),
    ("Care Tracker",   "$5/mo",  "per household",
     "Auto-track your regular products. Buy-off alerts when your brand goes on sale."),
    ("Ingredient Guard", "$12/mo", "per household",
     "Hard ingredient filter engine. Your avoidances are absolute rules — never traded for savings."),
    ("Full Care",      "$19/mo", "per household",
     "Full product history, ingredient database search, loyalty program optimizer, multi-person profiles."),
]

for col, (name, price, period, desc) in zip([p1, p2, p3, p4], tiers):
    with col:
        st.html(f"""
        <div class='wc-card' style='background:#FFFFFF;border:1px solid #DDD0E8;
                                    border-top:3px solid #A45AB0;border-radius:10px;
                                    padding:1.75rem;'>
          <p class='wc-tier-name'>{name}</p>
          <div class='wc-tier-price'>{price}</div>
          <p style='font-size:0.78rem;color:#9A80A8;'>{period}</p>
          <p style='font-size:0.87rem;color:#5C4870;line-height:1.7;margin-top:0.75rem;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:2rem;'></div>")

# ══════════════════════════════════════════════════════════════════════════════
# SINCERE STRATEGY
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:linear-gradient(135deg,#2E0A3D 0%,#4A1A5C 100%);
            border-radius:14px;padding:2.5rem;margin-bottom:20px;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#C98AD4;margin-bottom:1rem;'>The Sincere Strategy®</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.6rem;
             color:#FFFFFF;margin:0 0 1rem;line-height:1.3;'>
    No brand pays to appear in WhollyCare recommendations.<br />
    <em style='color:#C98AD4;'>Not one. Ever.</em>
  </h2>
  <div style='display:flex;flex-wrap:wrap;gap:8px;margin-top:1.25rem;'>
    <span class='wc-sincere'>Zero paid placements — ever</span>
    <span class='wc-sincere'>Ingredient filters are hard rules</span>
    <span class='wc-sincere'>Net savings shown — loyalty & shipping included</span>
    <span class='wc-sincere'>Your personal data is never sold or targeted</span>
    <span class='wc-sincere'>Subscription-only revenue</span>
  </div>
  <p style='color:rgba(255,255,255,0.4);font-size:0.8rem;margin-top:1.5rem;'>
    A <a href="https://sentir-solutions.com" target="_blank"
         style="color:#C98AD4;text-decoration:none;font-weight:500;">Sentir Solutions®</a> company ·
    wholly-care.com · Coming 2026
  </p>
</div>
""")

# ══════════════════════════════════════════════════════════════════════════════
# CTA
# ══════════════════════════════════════════════════════════════════════════════
st.html("""
<div style='background:#FFFFFF;border:1px solid #DDD0E8;border-radius:14px;
            padding:2.5rem;text-align:center;margin-bottom:20px;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.16em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:0.75rem;'>Coming Soon — 2026</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.8rem;
             color:#4A1A5C;margin:0 0 0.75rem;'>
    Be first to know when WhollyCare launches.
  </h2>
  <p style='color:#5C4870;font-size:0.95rem;max-width:460px;margin:0 auto 1.5rem;'>
    We're building WhollyCare after the Sincere Strategy platform is proven across
    food, household, and pet verticals. Join the waitlist and we'll reach out first.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyCare%20Waitlist"
     style='display:inline-block;background:#E87C2A;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:12px 32px;border-radius:8px;'>
    Join the Waitlist →
  </a>
</div>
""")

st.html("""
<div style='text-align:center;padding:1.5rem;color:#9A80A8;font-size:0.8rem;'>
  WhollyCare™ · A <a href="https://sentir-solutions.com" target="_blank"
  style="color:#7A3A8C;text-decoration:none;">Sentir Solutions®</a> Company ·
  Charlottesville, VA ·
  <a href="mailto:tim.hislop@gmail.com" style="color:#7A3A8C;text-decoration:none;">
    tim.hislop@gmail.com
  </a>
</div>
""")
