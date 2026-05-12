"""Concise 20-SKU dashboard — boxes with Demand %, Supply %, and 2-3 factors."""
import json, os
OUT = "/sessions/eager-adoring-faraday/mnt/outputs"
DATA = json.load(open(os.path.join(OUT,"dashboard_data.json")))
ORDER = json.load(open(os.path.join(OUT,"sku_order.json")))

# Curated 2-3 concise factors per SKU (festival/weather/geography/disruption)
SKU_FACTORS = {
  "Coriander Leaves Bunch": ["🎉 Eid al-Adha (May 27) — biryani/chutney spike", "☀️ Pre-monsoon heat ↓ yield 25-35%", "🚛 Daily-source from Hosakote/Chikkaballapur"],
  "Banana Robusta": ["🎉 Wedding season + Eid demand surge", "🌪 Cyclone risk on TN/AP coast", "📍 TN (Theni/Trichy) + AP (Kadapa) supply"],
  "Tomato Natti / Local": ["💍 Wedding sambar/rasam staple May-Jun", "☀️ Pre-monsoon fruit-drop ↓ Kolar yield", "📍 Kolar + Madanapalle (AP)"],
  "Curry leaves": ["🍛 Daily SI cooking — constant demand", "🐛 Whitefly pest risk May-Jul", "📍 Karnataka peri-urban + Salem (TN)"],
  "Potato": ["💍 Wedding + Eid biryani — Very High pull", "❄️ Punjab/UP cold storage outflow tail", "⚠️ Cold-storage tariff/rake disruption risk"],
  "Banana Elaichi": ["🎉 Eid + premium daily — steady spike", "📍 Niche TN/Karnataka — only 3 vendors", "⚠️ Vendor concentration risk"],
  "Onion": ["💍 Wedding + Eid + Ramzan — Very High", "📍 Maharashtra Nashik/Lasalgaon dominant", "⚠️ Govt export ban / NAFED MSP risk"],
  "Coconut": ["💍 Wedding + Vat Savitri (Jun 4) spike", "📍 TN Pollachi + Kerala — 350km+ haul", "⛽ Very High fuel sensitivity"],
  "Mint / Pudina Leaves": ["🌙 Ramzan/Eid iftar — Very High pull", "☀️ Heat ↓ yield 30-40%, wilts in transit", "🚛 Daily-source, no buffer"],
  "Drumstick": ["🍛 Wedding sambar staple", "📍 99.7% TN (Dindigul/Theni) — peak May", "⚠️ Single-state dependence — bandh/Cauvery risk"],
  "Tomato Hybrid": ["💍 Wedding + Eid demand", "☀️ Pre-monsoon fruit-drop", "📍 Kolar + Madanapalle arbitrage"],
  "Cucumber Salad/Hybrid/Green": ["🥗 Wedding salad + Iftar demand", "☀️ Heat-tolerant, stable supply", "⚠️ Only 2 vendors — concentration risk"],
  "Spinach Leaves": ["☀️ Off-peak (cool-season) — yield ↓50%", "🚛 Daily-source, ethylene-sensitive", "📍 Karnataka peri-urban only"],
  "Methi Leaves": ["☀️ Summer dip — yield ↓30%", "📍 Karnataka + Rajasthan winter belt", "🚛 Daily cold-room replen"],
  "Sweet Corn": ["🌧 Pre-monsoon harvest peak", "🐛 Stem borer pest May-Jul", "📍 Karnataka (Davangere/Chitradurga)"],
  "Drumstick_dup": [],
  "Papaya": ["📈 Constant demand year-round", "🦠 Ringspot virus risk Jul-Sep", "📍 Kolar/Chikkaballapur + AP"],
  "Mushroom": ["🥗 Premium/cafe channel steady", "❄️ Climate-controlled — weather-insulated", "⚡ Power outage risk at Hosakote facility"],
  "Carrot Ooty": ["💍 Wedding salad demand", "🏔 Nilgiris landslide risk Aug-Sep", "📍 Single vendor, Ooty 300km+ haul"],
  "Chilli Green (Small)": ["🍛 Daily SI staple + pickle season", "🐛 Thrips/mites May-Jul", "📍 Karnataka Bidar + Guntur (AP)"],
  "Namdhari Watermelon, Loose": ["☀️ Peak summer (May) — Very High demand", "🌧 Demand collapses with monsoon (Jun)", "⛽ Heavy 2kg/pc — fuel-sensitive"],
}

def cls(p):
    if p > 5: return "up", "▲"
    if p < -5: return "down", "▼"
    return "flat", "▬"

def cat_class(c):
    return {"Vegetables":"veg","Fruits":"fr","Herbs/Greens":"hg","Others":"ot"}.get(c,"ot")

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f8; color: #1c2530; padding: 18px; }
.wrap { max-width: 1480px; margin: 0 auto; }
header { background: linear-gradient(135deg, #0d3b66, #1f6e43); color: white; padding: 20px 24px; border-radius: 12px; margin-bottom: 16px; }
header h1 { font-size: 22px; margin-bottom: 4px; }
header .sub { font-size: 13px; opacity: 0.9; }
.legend { display: flex; gap: 14px; margin-top: 10px; flex-wrap: wrap; font-size: 11.5px; }
.legend span { background: rgba(255,255,255,0.13); padding: 4px 10px; border-radius: 12px; }
.toolbar { background: white; padding: 10px 16px; border-radius: 10px; border: 1px solid #e3e8ee; margin-bottom: 14px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; font-size: 13px; }
.toolbar select { padding: 5px 10px; border: 1px solid #d4dae2; border-radius: 5px; font-size: 12px; }
.toolbar label { color: #6b7989; font-size: 12px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 12px; }
.box { background: white; border: 1px solid #e3e8ee; border-radius: 10px; padding: 14px 15px; transition: box-shadow .15s; }
.box:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.06); }
.box-head { display: flex; justify-content: space-between; align-items: flex-start; gap: 6px; margin-bottom: 10px; }
.box-head .name { font-size: 14px; font-weight: 600; line-height: 1.25; color: #1c2530; }
.box-head .rank { background: #0d3b66; color: white; font-size: 10px; padding: 2px 7px; border-radius: 8px; font-weight: 600; min-width: 24px; text-align: center; }
.cat-pill { display: inline-block; font-size: 9px; padding: 1px 6px; border-radius: 6px; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.4px; font-weight: 600; }
.cat-pill.veg { background: #e6f4ea; color: #1c6e3f; }
.cat-pill.fr { background: #fdecea; color: #a8392c; }
.cat-pill.hg { background: #e7f1f9; color: #1a5483; }
.cat-pill.ot { background: #f2eafd; color: #5a3d92; }
.metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px; }
.m { padding: 8px 10px; border-radius: 7px; }
.m .l { font-size: 9.5px; color: #6b7989; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 2px; font-weight: 600; }
.m .v { font-size: 18px; font-weight: 700; line-height: 1.1; }
.m.dem { background: #eef4fb; }
.m.dem .l { color: #155e8a; }
.m.sup { background: #eef7f1; }
.m.sup .l { color: #1f6e43; }
.up { color: #11824a; }
.down { color: #c0392b; }
.flat { color: #7d8a99; }
.factors { font-size: 11.5px; color: #3a4654; line-height: 1.5; padding-top: 8px; border-top: 1px dashed #e3e8ee; }
.factors div { padding: 2px 0; }
.badge { display: inline-block; font-size: 8.5px; padding: 1px 5px; border-radius: 3px; font-weight: 700; vertical-align: middle; margin-left: 5px; letter-spacing: 0.4px; }
.badge.D { background: #11824a; color: white; }
.badge.M { background: #d18c00; color: white; }
.badge.DM { background: linear-gradient(90deg,#11824a 50%,#d18c00 50%); color: white; }
.methodology { background: white; border: 1px solid #e3e8ee; border-radius: 10px; padding: 14px 18px; margin-bottom: 14px; font-size: 12px; color: #3a4654; }
.methodology h3 { font-size: 12px; color: #0d3b66; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
.methodology .row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.methodology .row .col h4 { font-size: 11px; margin-bottom: 4px; }
.methodology .row .col h4.D { color: #11824a; }
.methodology .row .col h4.M { color: #d18c00; }
.methodology ul { padding-left: 16px; line-height: 1.55; }
.methodology li { margin: 1px 0; }
footer { text-align: center; font-size: 11px; color: #7d8a99; margin-top: 22px; }
"""

cards = []
for rank, sku in enumerate(ORDER, 1):
    d = DATA[sku]
    dem_p = d["demand_growth_pct"]; sup_p = d["supply_growth_pct"]
    dc, da = cls(dem_p); sc, sa = cls(sup_p)
    factors = SKU_FACTORS.get(sku, [])
    factors_html = "".join(f"<div>{f}</div>" for f in factors[:3])
    cat = d["category"]; tier = d["tier"]
    cards.append(f"""
    <div class="box" data-cat="{cat}" data-tier="{tier}" data-dem="{dem_p}" data-sup="{sup_p}">
        <div class="box-head">
            <div>
                <div class="name">{sku} <span class="badge D" title="Real data — from SKU Decision Matrix">D</span></div>
                <div class="cat-pill {cat_class(cat)}">{cat}</div>
            </div>
            <div class="rank">#{rank}</div>
        </div>
        <div class="metrics">
            <div class="m dem"><div class="l">Demand <span class="badge M" title="Modelled — extrapolated from monthly demand × festival/seasonality multiplier">M</span></div><div class="v {dc}">{da} {dem_p:+.1f}%</div></div>
            <div class="m sup"><div class="l">Supply <span class="badge DM" title="Mixed — history is real vendor indent (Data); 4-week forecast is modelled with risk multipliers">D+M</span></div><div class="v {sc}">{sa} {sup_p:+.1f}%</div></div>
        </div>
        <div class="factors">{factors_html}<div style="margin-top:4px;font-size:10px;color:#7d8a99;">Factors: <span class="badge M">M</span> domain knowledge / industry priors</div></div>
    </div>
    """)

# KPIs
dems = [DATA[s]["demand_growth_pct"] for s in ORDER]
sups = [DATA[s]["supply_growth_pct"] for s in ORDER]
avg_dem = sum(dems)/20; avg_sup = sum(sups)/20

html = f"""<!doctype html><html><head>
<meta charset="utf-8"><title>FnV Top 20 — Demand vs Supply (May 2026)</title>
<style>{CSS}</style></head><body>
<div class="wrap">
<header>
    <h1>FnV Top 20 SKUs — 4-Week Forecast (May 4 – May 31, 2026)</h1>
    <div class="sub">Demand: Bangalore consumption · Supply: Pan-India vendor sources · % change vs trailing 4-week average</div>
    <div class="legend">
        <span>📍 Demand: Bangalore</span>
        <span>🚛 Supply: Pan-India</span>
        <span>🎉 Eid al-Adha · May 27</span>
        <span>💍 Wedding season · May–Jun</span>
        <span>🌧 SW Monsoon onset · ~Jun 5</span>
        <span>📊 Avg demand ▲ {avg_dem:+.1f}% · supply ▲ {avg_sup:+.1f}%</span>
        <span><span class="badge D">D</span> = Real data · <span class="badge M">M</span> = Modelled · <span class="badge DM">D+M</span> = Mixed</span>
    </div>
</header>

<div class="methodology">
    <h3>What's Data vs Modelled</h3>
    <div class="row">
      <div class="col">
        <h4 class="D">🟢 Real data (from your files)</h4>
        <ul>
          <li>Top 20 SKU list, ranking, category, tier, decision (SKU Decision Matrix)</li>
          <li>Monthly demand for Jan / Feb / Mar 2026 (SKU Decision Matrix)</li>
          <li>Vendor indent projections by SKU + date + vendor + location, Jan 1 – Apr 17 2026 (Vendor Indent file)</li>
          <li>Vendor names and source locations (Hosakote, Kolar, Chikkaballapur, TN, Safal, etc.)</li>
        </ul>
      </div>
      <div class="col">
        <h4 class="M">🟠 Modelled / domain-knowledge layer</h4>
        <ul>
          <li><b>Demand %</b> — monthly demand split evenly to weeks; April extrapolated from March; May = trend × festival multiplier × seasonality (uncalibrated)</li>
          <li><b>Supply forecast</b> — trailing 4-wk indent × risk multiplier (greens heat-yield 0.8×, drumstick TN peak 1.15×, onion MH tail 0.95×)</li>
          <li><b>Factors</b> — festival calendar, harvest origins beyond your file (MH/Punjab/UP/Kerala), monsoon/cyclone, pest, fuel sensitivity — all industry priors, not back-tested</li>
          <li><b>Numbers are directional, not predictive.</b> To turn this into a real forecaster: add weekly POS/dispatch + 12+ months history + indent-fulfilment % + live IMD/Agmarknet feeds</li>
        </ul>
      </div>
    </div>
</div>

<div class="toolbar">
    <label>Category:</label>
    <select id="fc" onchange="ap()"><option value="">All</option><option>Vegetables</option><option>Fruits</option><option>Herbs/Greens</option><option>Others</option></select>
    <label>Tier:</label>
    <select id="ft" onchange="ap()"><option value="">All</option><option>High</option><option>Medium</option></select>
    <label>Sort:</label>
    <select id="fs" onchange="ap()"><option value="rank">Rank</option><option value="dd">Demand growth (high→low)</option><option value="da">Demand growth (low→high)</option><option value="sd">Supply growth (high→low)</option><option value="sa">Supply growth (low→high)</option></select>
</div>

<div class="grid" id="g">
{''.join(cards)}
</div>
<footer>Top 20 SKUs · Built from SKU Decision Matrix + Vendor Indent (Jan–Apr 2026) · ▲ = growth ≥5%, ▼ = decline ≥5%, ▬ = flat · Hover any <span class="badge D">D</span> / <span class="badge M">M</span> / <span class="badge DM">D+M</span> badge for source detail</footer>
</div>
<script>
function ap() {{
    const c = document.getElementById('fc').value;
    const t = document.getElementById('ft').value;
    const s = document.getElementById('fs').value;
    const g = document.getElementById('g');
    let bx = Array.from(g.querySelectorAll('.box'));
    bx.forEach(b => {{
        const cm = !c || b.dataset.cat === c;
        const tm = !t || b.dataset.tier === t;
        b.style.display = (cm && tm) ? '' : 'none';
    }});
    if (s !== 'rank') {{
        bx.sort((a,b) => {{
            if (s === 'dd') return parseFloat(b.dataset.dem) - parseFloat(a.dataset.dem);
            if (s === 'da') return parseFloat(a.dataset.dem) - parseFloat(b.dataset.dem);
            if (s === 'sd') return parseFloat(b.dataset.sup) - parseFloat(a.dataset.sup);
            if (s === 'sa') return parseFloat(a.dataset.sup) - parseFloat(b.dataset.sup);
        }});
    }} else {{
        bx.sort((a,b) => parseInt(a.querySelector('.rank').textContent.slice(1)) - parseInt(b.querySelector('.rank').textContent.slice(1)));
    }}
    bx.forEach(b => g.appendChild(b));
}}
</script></body></html>"""

with open(os.path.join(OUT, "concise_dashboard.html"), "w") as f:
    f.write(html)
print("Written: concise_dashboard.html")
print(f"Size: {len(html)//1024} KB")
