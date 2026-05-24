"""
7_Investor.py — WhollyCare Investor Brief
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
import ui.style as style

st.set_page_config(
    page_title="WhollyCare — Investor Brief",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

style.inject()
style.brand_nav()
style.page_header(
    "Investor Brief",
    "WhollyCare -- The personal care plan that pays you back."
)

# Hero
st.html("""
<div style='background:linear-gradient(160deg,#1A0826 0%,#2E0A3D 60%,#1A0826 100%);
            border-radius:16px;padding:52px 44px 44px;color:white;margin-bottom:2rem;'>
  <p style='font-size:0.7rem;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;
            color:#C98AD4;margin-bottom:14px;'>WhollyCare | Sentir Solutions LLC | Charlottesville, VA</p>
  <h1 style='font-size:2.8rem;font-weight:800;color:#fff;margin:0 0 12px;line-height:1.1;'>
    The most loyal category<br>in retail. Finally honest.
  </h1>
  <p style='font-size:1.05rem;color:rgba(255,255,255,0.72);max-width:620px;line-height:1.65;margin-bottom:2rem;'>
    Personal care and beauty is a $100B+ US category where consumers pay significant premiums
    for fragrance-free, paraben-free, and cruelty-free products without knowing whether cheaper
    equivalent-ingredient options exist at the store next door. WhollyCare answers that question --
    honestly, ingredient-first, and without compromise.
  </p>
  <div style='display:flex;gap:18px;flex-wrap:wrap;'>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(201,138,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$100B+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>US personal care and beauty annual spend -- growing 6% YoY</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(201,138,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$500+</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Average household overspend vs. equivalent-ingredient alternatives</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(201,138,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>73%</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Say ingredient transparency matters -- only 12% know how to verify it</div>
    </div>
    <div style='background:rgba(255,255,255,0.06);border:1px solid rgba(201,138,212,0.25);
                border-radius:10px;padding:18px 24px;min-width:140px;flex:1;'>
      <div style='font-size:1.9rem;font-weight:800;color:#E87C2A;'>$0</div>
      <div style='font-size:0.75rem;color:rgba(255,255,255,0.5);margin-top:5px;'>Paid placements. Brands cannot buy their way into a WhollyCare recommendation.</div>
    </div>
  </div>
</div>
""")

# Platform foundation
st.html("""
<div style='background:linear-gradient(135deg,#2E0A3D 0%,#4A1A5C 100%);
            border-radius:12px;padding:2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#C98AD4;margin-bottom:0.75rem;'>Platform Foundation</p>
  <blockquote style='font-family:Fraunces,serif;font-weight:300;font-size:1.2rem;
                     font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "WhollyCare is the most complex Wholly vertical -- ingredient parsing in beauty is harder
     than groceries -- but it is also the most loyalty-driven. Consumers who need fragrance-free
     or cruelty-free products are not price-shopping today because no tool they trust handles
     their constraints correctly. WhollyCare is that tool."
  </blockquote>
  <p style='color:rgba(255,255,255,0.5);font-size:0.82rem;line-height:1.6;margin:0;'>
    WhollyFare is in active pilot -- Tim Hislop family, four Charlottesville grocers, weekly receipts.
    The platform compounds. WhollyFare proves the engine. WhollyWare and WhollyPaws expand it.
    WhollyCare is the vertical where the constraint engine becomes the most defensible moat in the portfolio.
  </p>
</div>
""")

# Why Now
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>Why Now</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#4A1A5C;margin:0 0 0.5rem;'>
    Three forces making this the right moment.
  </h2>
</div>
""")

wn1, wn2, wn3 = st.columns(3, gap="medium")
why_now = [
    (wn1, "Clean beauty movement hit mainstream",
     "EWG Skin Deep has 100M+ annual users. Free-from claims are now a shelf-standard expectation. The demand for ingredient transparency is documented, massive, and still accelerating."),
    (wn2, "Loyalty program complexity hides the real price",
     "CVS ExtraCare, Walgreens Bonus Cash, Ulta Beauty Insider -- savings are real but comparing across programs is nearly impossible. The consumer who should be saving $500/year cannot do the math. WhollyCare can."),
    (wn3, "Ingredient parsing is now tractable",
     "INCI ingredient lists in beauty are notoriously complex. LLM-assisted parsing of those lists against household constraint profiles has crossed the reliability threshold. This is buildable now."),
]
for col, title, body in why_now:
    with col:
        st.html(f"""
        <div style='background:#fff;border-radius:10px;padding:1.4rem 1.2rem;
                    border:1px solid #DDD0E8;border-top:4px solid #7A3A8C;
                    box-shadow:0 2px 10px rgba(0,0,0,0.05);'>
          <div style='font-size:0.92rem;font-weight:700;color:#4A1A5C;margin-bottom:6px;'>{title}</div>
          <div style='font-size:0.83rem;color:#5C4870;line-height:1.6;'>{body}</div>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Sincere Strategy
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>The Sincere Strategy</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#4A1A5C;margin:0 0 0.5rem;'>
    Six commitments. The entire beauty industry cannot make them.
  </h2>
  <p style='color:#5C4870;font-size:0.9rem;max-width:620px;line-height:1.7;'>
    The beauty industry is built on paid placement, influencer affiliate fees, and brand sponsorship.
    WhollyCare structural prohibition on all of it is not a policy statement -- it is a moat that
    the influencer ecosystem cannot cross without destroying their revenue model.
  </p>
</div>
""")

s1, s2 = st.columns(2, gap="medium")
sincere = [
    ("No paid placements. Ever.",
     "In the current beauty ecosystem, brands pay to be recommended through influencers, affiliate programs, and sponsored placement. WhollyCare zero-placement rule makes this structurally impossible. Every recommendation is earned by ingredient and price, not by a check."),
    ("Ingredient constraints are sacrosanct",
     "Fragrance-sensitive, paraben-free, cruelty-free, dye-free -- these constraints run before the price optimizer. A brand cannot pay to bypass a household ingredient filter. The constraint engine is the entire product."),
    ("Net savings always -- including loyalty programs",
     "CVS ExtraCare points, Walgreens Bonus Cash, Ulta Insider rewards -- WhollyCare accounts for all of them and shows the net-of-loyalty price. The comparison is honest, complete, and cross-store."),
    ("Ingredient verification, not just claims",
     "A product that claims fragrance-free but lists parfum on the INCI list fails the filter. WhollyCare parses the actual ingredient list -- not the marketing claim on the front of the bottle."),
    ("Real prices from real circulars",
     "CVS, Walgreens, Ulta, Target, and local pharmacy circulars -- actual weekly prices, not national estimates or partnered inventory. If it is on sale at your CVS this week, WhollyCare knows."),
    ("Skin and health data owned by the household",
     "Sensitive skin profiles, allergen history, ingredient exclusions -- this data belongs to the household. WhollyCare does not sell it to Neutrogena, Oreal, or any brand. Subscription revenue only."),
]
for i, (title, body) in enumerate(sincere):
    col = s1 if i % 2 == 0 else s2
    with col:
        st.html(f"""
        <div style='background:#fff;border:1px solid #DDD0E8;border-left:4px solid #A45AB0;
                    border-radius:6px;padding:1.1rem 1.4rem;margin-bottom:0.85rem;'>
          <div style='font-size:0.92rem;font-weight:700;color:#4A1A5C;margin-bottom:4px;'>{title}</div>
          <div style='font-size:0.83rem;color:#5C4870;line-height:1.65;'>{body}</div>
        </div>
        """)

st.html("""
<div style='background:#F4EEF8;border:1px solid #C9A0D8;border-radius:10px;
            padding:14px 22px;margin-top:4px;font-size:0.88rem;color:#4A1A5C;font-weight:600;line-height:1.55;'>
  The beauty influencer ecosystem cannot adopt the Sincere Strategy without eliminating the affiliate
  revenue that funds it. EWG Skin Deep rates ingredients but does not compare prices.
  WhollyCare does both, honestly, in one tool. That gap is structural and permanent.
</div>
""")

st.html("<div style='height:1.5rem;'></div>")

# Competitive landscape
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>Competitive Landscape</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#4A1A5C;margin:0;'>
    Why the beauty industry opacity is WhollyCare advantage.
  </h2>
</div>
""")

m1, m2 = st.columns(2, gap="medium")
moat = [
    ("EWG rates ingredients but does not compare prices",
     "EWG Skin Deep has 100M+ annual users who trust ingredient safety ratings. But EWG does not tell you what the same fragrance-free product costs at Target vs. CVS vs. Walgreens this week. WhollyCare does both."),
    ("Brands cannot pay to bypass ingredient filters",
     "In the current beauty influencer and affiliate ecosystem, brands pay to be recommended regardless of ingredient profile. WhollyCare zero-placement rule makes this structurally impossible. The constraint engine is the product."),
    ("Unit pricing in beauty is intentionally opaque",
     "A 1.7 fl oz serum at $28 looks cheap next to a 3.4 fl oz at $45. WhollyCare normalizes to per-fl-oz, per-gram, and per-use -- the comparison that reveals actual value across every store and size."),
    ("Loyalty program complexity hides the real price",
     "CVS ExtraCare, Walgreens Bonus Cash, Ulta Beauty Insider -- savings are real but hard to compare across programs. WhollyCare accounts for all of them and shows the net-of-loyalty price."),
]
for i, (title, body) in enumerate(moat):
    col = m1 if i % 2 == 0 else m2
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #DDD0E8;border-left:3px solid #A45AB0;
                    border-radius:6px;padding:1.25rem 1.5rem;margin-bottom:1rem;'>
          <h4 style='font-size:0.92rem;font-weight:600;color:#4A1A5C;margin-bottom:0.4rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#5C4870;line-height:1.75;margin:0;'>{body}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Why Tim
st.html("""
<div style='background:linear-gradient(160deg,#1A0826,#2E0A3D);border:1px solid #7A3A8C;
            border-radius:12px;padding:2rem 2.25rem;margin-bottom:1.5rem;'>
  <p style='font-size:0.7rem;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;
            color:#C98AD4;margin-bottom:0.75rem;'>The Founder</p>
  <p style='font-family:Fraunces,serif;font-weight:300;font-size:1.1rem;
            font-style:italic;color:#FFFFFF;line-height:1.6;margin:0 0 1rem;'>
    "WhollyCare is the vertical where the Sincere Strategy matters most.
     Consumers with fragrance sensitivity, skin allergies, or cruelty-free commitments
     have been failed by every tool that takes affiliate money from the brands they are
     trying to evaluate. WhollyCare cannot be bought. That is the product."
  </p>
  <p style='color:rgba(255,255,255,0.55);font-size:0.83rem;line-height:1.65;margin:0;'>
    Tim Hislop -- Founder, Sentir Solutions LLC -- Full-time at ECS -- Building nights and weekends --
    WhollyFare pilot running now in Charlottesville, VA. The ingredient constraint engine
    that powers WhollyFare Health Guard tier is the foundation of WhollyCare.
    The hardest part is already built.
  </p>
</div>
""")

# Roadmap
st.html("""
<div style='margin-bottom:1rem;'>
  <p style='font-size:0.72rem;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;
            color:#7A3A8C;margin-bottom:6px;'>Roadmap</p>
  <h2 style='font-family:Fraunces,serif;font-weight:300;font-size:1.5rem;color:#4A1A5C;margin:0;'>
    Phases 1-3 prove the platform. WhollyCare launches into a proven moat.
  </h2>
</div>
""")

r1, r2, r3 = st.columns(3, gap="medium")
phases = [
    ("Phase 1-3 -- Prerequisite", "#DDD0E8",
     "WhollyFare, WhollyWare, WhollyPaws validate the Sincere Strategy platform. The constraint engine, circular ingestion, and Found Money math are proven in three verticals before WhollyCare launches."),
    ("Phase 4 -- WhollyCare Launch", "#4A1A5C",
     "Ingredient parsing library for beauty and personal care. CVS, Walgreens, Ulta, Target circular integration. Loyalty program math. EWG Skin Deep integration for independent ingredient verification."),
    ("Phase 5 -- Scale", "#7A3A8C",
     "National. Amazon beauty, Sephora, Dermstore. Dermatologist and allergist B2B licensing. Ingredient database as a public data product. $1M+ ARR. The most defensible Wholly brand by Year 3."),
]
for col, (title, color, desc) in zip([r1, r2, r3], phases):
    with col:
        st.html(f"""
        <div style='background:#FFFFFF;border:1px solid #DDD0E8;border-top:4px solid {color};
                    border-radius:10px;padding:1.5rem;'>
          <h4 style='font-size:0.9rem;font-weight:600;color:#4A1A5C;margin-bottom:0.6rem;'>{title}</h4>
          <p style='font-size:0.85rem;color:#5C4870;line-height:1.75;margin:0;'>{desc}</p>
        </div>
        """)

st.html("<div style='height:1.5rem;'></div>")

# Close
st.html("""
<div style='background:#F8F4FB;border:1px solid #DDD0E8;border-radius:12px;padding:2.25rem;text-align:center;'>
  <h3 style='font-family:Fraunces,serif;font-weight:300;font-size:1.4rem;color:#4A1A5C;margin:0 0 0.6rem;'>
    The most complex vertical. The most loyal category. The most defensible moat.
  </h3>
  <p style='color:#5C4870;font-size:0.88rem;max-width:480px;margin:0 auto 1.25rem;line-height:1.7;'>
    WhollyFare is in pilot now. The constraint engine is proven. WhollyCare inherits it.
    Investment inquiries cover the full Sentir Solutions portfolio.
  </p>
  <a href="mailto:tim.hislop@gmail.com?subject=WhollyCare%20Investor%20Inquiry"
     style='display:inline-block;background:#4A1A5C;color:#FFFFFF;text-decoration:none;
            font-size:0.9rem;font-weight:600;padding:11px 28px;border-radius:8px;'>
    tim.hislop@gmail.com
  </a>
  <p style='color:#9A80A8;font-size:0.78rem;margin-top:1rem;'>
    Full portfolio at
    <a href="https://sentir-solutions.com" target="_blank" style="color:#7A3A8C;text-decoration:none;">
      sentir-solutions.com
    </a>
  </p>
</div>
""")
