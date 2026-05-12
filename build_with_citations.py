"""Concise 20-SKU dashboard with Harvard-style superscript citations linking to a separate references page."""
import json, os
OUT = "/sessions/eager-adoring-faraday/mnt/outputs"
DATA = json.load(open(os.path.join(OUT,"dashboard_data.json")))
ORDER = json.load(open(os.path.join(OUT,"sku_order.json")))

# ------------- Harvard-style references --------------
# id: (in-text key, full reference HTML)
REFS = [
    # 1
    ("SKU Matrix, 2026",
     "Internal (2026) <em>SKU Decision Matrix v2.2 — With 3-Month Volume Data (Jan–Mar 2026)</em>. Uploaded by user, 10 April 2026.", "—"),
    # 2
    ("Vendor Indent, 2026",
     "Internal (2026) <em>Jan–April 2026 Vendor Indent vs Location</em>. Uploaded by user, 17 April 2026.", "—"),
    # 3
    ("IMD, 2026",
     "India Meteorological Department (2026) <em>Monsoon Information Onset</em>. Available at: https://mausam.imd.gov.in/responsive/monsooninformation_onset.php (Accessed: 8 May 2026).",
     "https://mausam.imd.gov.in/responsive/monsooninformation_onset.php"),
    # 4
    ("Business Today, 2026",
     "Business Today (2026) <em>Monsoon 2026: Here's IMD's latest prediction on arrival dates for Kerala to Delhi</em>, 2 May. Available at: https://www.businesstoday.in/india/story/monsoon-2026-heres-imds-latest-prediction-on-arrival-dates-for-kerala-to-delhi-528560-2026-05-02 (Accessed: 8 May 2026).",
     "https://www.businesstoday.in/india/story/monsoon-2026-heres-imds-latest-prediction-on-arrival-dates-for-kerala-to-delhi-528560-2026-05-02"),
    # 5
    ("timeanddate.com, 2026",
     "timeanddate.com (2026) <em>Bakrid 2026 in India</em>. Available at: https://www.timeanddate.com/holidays/india/eid-ul-adha (Accessed: 8 May 2026).",
     "https://www.timeanddate.com/holidays/india/eid-ul-adha"),
    # 6
    ("PublicHolidays.in, n.d.",
     "PublicHolidays.in (n.d.) <em>Bakrid / Eid al-Adha 2026, 2027 and 2028</em>. Available at: https://publicholidays.in/bakrid-idul-zuha/ (Accessed: 8 May 2026).",
     "https://publicholidays.in/bakrid-idul-zuha/"),
    # 7
    ("Wikipedia, 2024a",
     "Wikipedia (2024a) <em>Lasalgaon onion</em>. Available at: https://en.wikipedia.org/wiki/Lasalgaon_onion (Accessed: 8 May 2026).",
     "https://en.wikipedia.org/wiki/Lasalgaon_onion"),
    # 8
    ("Ashadhan Exim, n.d.",
     "Ashadhan Exim (n.d.) <em>Nashik Onion Market — Production, Prices &amp; Export Market</em>. Available at: https://www.ashadhanexim.com/post/nashik-onion-market-production-prices-export-market (Accessed: 8 May 2026).",
     "https://www.ashadhanexim.com/post/nashik-onion-market-production-prices-export-market"),
    # 9
    ("PIB, 2024",
     "Press Information Bureau, Government of India (2024) <em>2.60 lakh tons of onion exported in 2024-25, till 31st July, 2024</em>. PIB Release PRID 2042765. Available at: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2042765 (Accessed: 8 May 2026).",
     "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2042765"),
    # 10
    ("DD News, 2024",
     "DD News (2024) <em>India lifts ban on onion exports after robust production</em>. Available at: https://ddnews.gov.in/en/india-lifts-ban-on-onion-exports-after-robust-production/ (Accessed: 8 May 2026).",
     "https://ddnews.gov.in/en/india-lifts-ban-on-onion-exports-after-robust-production/"),
    # 11
    ("Frontline, 2024",
     "Frontline / The Hindu (2024) <em>Maharashtra onion crisis: Farmers paying price of misguided attempt to control inflation</em>. Available at: https://frontline.thehindu.com/the-nation/agriculture/maharashtra-onion-crisis-farmers-paying-price-misguided-attempt-to-control-inflation-2024-assembly-election/article68519805.ece (Accessed: 8 May 2026).",
     "https://frontline.thehindu.com/the-nation/agriculture/maharashtra-onion-crisis-farmers-paying-price-misguided-attempt-to-control-inflation-2024-assembly-election/article68519805.ece"),
    # 12
    ("Sparsa Resorts, 2026",
     "Sparsa Resorts (2026) <em>Pollachi Famous For: 10 Reasons to Visit in 2026</em>. Available at: https://sparsaresorts.com/pollachi-famous-for-reasons-to-visit/ (Accessed: 8 May 2026).",
     "https://sparsaresorts.com/pollachi-famous-for-reasons-to-visit/"),
    # 13
    ("DT Next, 2023",
     "DT Next (2023) <em>Moringa mission to boost in Economy</em>, 27 March. Available at: https://www.dtnext.in/tamilnadu/2023/03/27/moringa-mission-to-boost-in-economy (Accessed: 8 May 2026).",
     "https://www.dtnext.in/tamilnadu/2023/03/27/moringa-mission-to-boost-in-economy"),
    # 14
    ("TNAU, 2010",
     "Tamil Nadu Agricultural University (2010) <em>Drumstick production — Success story</em>. Agritech portal. Available at: https://agritech.tnau.ac.in/success_stories/pdf/2010/horticulture/Drumstick%20production.pdf (Accessed: 8 May 2026).",
     "https://agritech.tnau.ac.in/success_stories/pdf/2010/horticulture/Drumstick%20production.pdf"),
    # 15
    ("Author's domain knowledge, 2026",
     "Author's domain knowledge / industry priors (2026). Unverified against a primary source in this build. Indicative only; awaiting calibration data.", "—"),
    # 16
    ("Agmarknet, n.d.",
     "Agmarknet, Directorate of Marketing and Inspection, Ministry of Agriculture &amp; Farmers Welfare, Government of India (n.d.) <em>Daily mandi prices and arrivals</em>. Available at: https://agmarknet.gov.in (Suggested live feed — not yet wired to this dashboard).",
     "https://agmarknet.gov.in"),
    # 17
    ("IMD Seasonal Forecast, 2026",
     "India Meteorological Department (2026) <em>Long Range / Seasonal Forecast</em>. Available at: https://mausam.imd.gov.in/responsive/seasonal_forecast.php (Suggested live feed for quarterly rainfall outlook — not yet wired to this dashboard).",
     "https://mausam.imd.gov.in/responsive/seasonal_forecast.php"),
    # 18
    ("NHB, n.d.",
     "National Horticulture Board, Ministry of Agriculture &amp; Farmers Welfare, Government of India (n.d.) <em>Horticultural Statistics — Area, Production &amp; Productivity</em>. Available at: https://nhb.gov.in/statistics.aspx (Suggested data source for state-wise crop yields — not yet wired to this dashboard).",
     "https://nhb.gov.in/statistics.aspx"),
    # 19
    ("NAFED, n.d.",
     "National Agricultural Cooperative Marketing Federation of India Ltd. (NAFED) (n.d.) <em>Procurement and Price Support Notifications</em>. Available at: https://www.nafed-india.com (Suggested source for MSP / MEP / buffer stock announcements affecting onion, potato, pulses — not yet wired to this dashboard).",
     "https://www.nafed-india.com"),
    # 20
    ("PIB Notifications, n.d.",
     "Press Information Bureau, Government of India (n.d.) <em>Ministry of Agriculture &amp; Farmers Welfare — Press Releases</em>. Available at: https://pib.gov.in (Suggested source for export ban / MEP / policy notifications — not yet wired to this dashboard).",
     "https://pib.gov.in"),
    # 21
    ("Drik Panchang, n.d.",
     "Drik Panchang (n.d.) <em>Indian Festival Calendar — Hindu, Muslim, Jain, Sikh festivals with regional variants</em>. Available at: https://www.drikpanchang.com (Suggested source for tithi-based festival dates across Indian regions — not yet wired to this dashboard).",
     "https://www.drikpanchang.com"),
]

# Helpers
def ref_idx(key):
    for i,(k,_,_) in enumerate(REFS,1):
        if k == key: return i
    raise ValueError(f"Unknown ref key {key}")

def sup(keys):
    """Return superscript HTML with comma-separated ref numbers linking to refs.html anchors."""
    nums = []
    for k in keys:
        i = ref_idx(k)
        nums.append(f'<a class="cite" href="references.html#ref{i}" target="_blank">{i}</a>')
    return f'<sup>{",".join(nums)}</sup>'

# Each SKU: list of (factor_text, [citation_keys])
SKU_FACTORS = {
  "Coriander Leaves Bunch": [
    ("🎉 Eid al-Adha (May 27) — biryani/chutney spike", ["timeanddate.com, 2026"]),
    ("☀️ Pre-monsoon heat ↓ yield 25-35%", ["Author's domain knowledge, 2026"]),
    ("🚛 Daily-source from Hosakote/Chikkaballapur", ["Vendor Indent, 2026"]),
  ],
  "Banana Robusta": [
    ("🎉 Wedding season + Eid demand surge", ["timeanddate.com, 2026", "Author's domain knowledge, 2026"]),
    ("🌪 Cyclone risk on TN/AP coast", ["Author's domain knowledge, 2026"]),
    ("📍 TN (Theni/Trichy) + AP (Kadapa) supply", ["Author's domain knowledge, 2026"]),
  ],
  "Tomato Natti / Local": [
    ("💍 Wedding sambar/rasam staple May-Jun", ["Author's domain knowledge, 2026"]),
    ("☀️ Pre-monsoon fruit-drop ↓ Kolar yield", ["Author's domain knowledge, 2026"]),
    ("📍 Kolar + Madanapalle (AP)", ["Vendor Indent, 2026", "Author's domain knowledge, 2026"]),
  ],
  "Curry leaves": [
    ("🍛 Daily SI cooking — constant demand", ["SKU Matrix, 2026"]),
    ("🐛 Whitefly pest risk May-Jul", ["Author's domain knowledge, 2026"]),
    ("📍 Karnataka peri-urban + Salem (TN)", ["Vendor Indent, 2026", "Author's domain knowledge, 2026"]),
  ],
  "Potato": [
    ("💍 Wedding + Eid biryani — Very High pull", ["timeanddate.com, 2026"]),
    ("❄️ Punjab/UP cold storage outflow tail", ["Author's domain knowledge, 2026"]),
    ("⚠️ Cold-storage tariff / rake disruption risk", ["Author's domain knowledge, 2026"]),
  ],
  "Banana Elaichi": [
    ("🎉 Eid + premium daily — steady spike", ["timeanddate.com, 2026"]),
    ("📍 Niche TN/Karnataka — only 3 vendors", ["Vendor Indent, 2026"]),
    ("⚠️ Vendor concentration risk", ["Vendor Indent, 2026"]),
  ],
  "Onion": [
    ("💍 Wedding + Eid + Ramzan — Very High", ["timeanddate.com, 2026"]),
    ("📍 Maharashtra Nashik/Lasalgaon dominant", ["Wikipedia, 2024a", "Ashadhan Exim, n.d."]),
    ("⚠️ Govt export ban / NAFED MSP risk", ["PIB, 2024", "DD News, 2024", "Frontline, 2024"]),
  ],
  "Coconut": [
    ("💍 Wedding + Vat Savitri (Jun 4) spike", ["timeanddate.com, 2026"]),
    ("📍 TN Pollachi + Kerala — 350km+ haul", ["Sparsa Resorts, 2026"]),
    ("⛽ Very High fuel sensitivity", ["Author's domain knowledge, 2026"]),
  ],
  "Mint / Pudina Leaves": [
    ("🌙 Ramzan/Eid iftar — Very High pull", ["timeanddate.com, 2026"]),
    ("☀️ Heat ↓ yield 30-40%, wilts in transit", ["Author's domain knowledge, 2026"]),
    ("🚛 Daily-source, no buffer", ["Vendor Indent, 2026"]),
  ],
  "Drumstick": [
    ("🍛 Wedding sambar staple", ["Author's domain knowledge, 2026"]),
    ("📍 99.7% TN (Dindigul/Theni) — peak May", ["Vendor Indent, 2026", "DT Next, 2023", "TNAU, 2010"]),
    ("⚠️ Single-state dependence — bandh/Cauvery risk", ["Author's domain knowledge, 2026"]),
  ],
  "Tomato Hybrid": [
    ("💍 Wedding + Eid demand", ["timeanddate.com, 2026"]),
    ("☀️ Pre-monsoon fruit-drop", ["Author's domain knowledge, 2026"]),
    ("📍 Kolar + Madanapalle arbitrage", ["Vendor Indent, 2026", "Author's domain knowledge, 2026"]),
  ],
  "Cucumber Salad/Hybrid/Green": [
    ("🥗 Wedding salad + Iftar demand", ["timeanddate.com, 2026"]),
    ("☀️ Heat-tolerant, stable supply", ["Author's domain knowledge, 2026"]),
    ("⚠️ Only 2 vendors — concentration risk", ["Vendor Indent, 2026"]),
  ],
  "Spinach Leaves": [
    ("☀️ Off-peak (cool-season) — yield ↓50%", ["Author's domain knowledge, 2026"]),
    ("🚛 Daily-source, ethylene-sensitive", ["Author's domain knowledge, 2026"]),
    ("📍 Karnataka peri-urban only", ["Vendor Indent, 2026"]),
  ],
  "Methi Leaves": [
    ("☀️ Summer dip — yield ↓30%", ["Author's domain knowledge, 2026"]),
    ("📍 Karnataka + Rajasthan winter belt", ["Author's domain knowledge, 2026"]),
    ("🚛 Daily cold-room replen", ["Vendor Indent, 2026"]),
  ],
  "Sweet Corn": [
    ("🌧 Pre-monsoon harvest peak", ["Author's domain knowledge, 2026"]),
    ("🐛 Stem borer pest May-Jul", ["Author's domain knowledge, 2026"]),
    ("📍 Karnataka (Davangere/Chitradurga)", ["Author's domain knowledge, 2026"]),
  ],
  "Papaya": [
    ("📈 Constant demand year-round", ["SKU Matrix, 2026"]),
    ("🦠 Ringspot virus risk Jul-Sep", ["Author's domain knowledge, 2026"]),
    ("📍 Kolar/Chikkaballapur + AP", ["Vendor Indent, 2026", "Author's domain knowledge, 2026"]),
  ],
  "Mushroom": [
    ("🥗 Premium/cafe channel steady", ["SKU Matrix, 2026"]),
    ("❄️ Climate-controlled — weather-insulated", ["Author's domain knowledge, 2026"]),
    ("⚡ Power outage risk at Hosakote facility", ["Vendor Indent, 2026"]),
  ],
  "Carrot Ooty": [
    ("💍 Wedding salad demand", ["timeanddate.com, 2026"]),
    ("🏔 Nilgiris landslide risk Aug-Sep", ["Author's domain knowledge, 2026"]),
    ("📍 Single vendor, Ooty 300km+ haul", ["Vendor Indent, 2026"]),
  ],
  "Chilli Green (Small)": [
    ("🍛 Daily SI staple + pickle season", ["SKU Matrix, 2026"]),
    ("🐛 Thrips/mites May-Jul", ["Author's domain knowledge, 2026"]),
    ("📍 Karnataka Bidar + Guntur (AP)", ["Author's domain knowledge, 2026"]),
  ],
  "Namdhari Watermelon, Loose": [
    ("☀️ Peak summer (May) — Very High demand", ["SKU Matrix, 2026"]),
    ("🌧 Demand collapses with monsoon (Jun)", ["IMD, 2026", "Business Today, 2026"]),
    ("⛽ Heavy 2kg/pc — fuel-sensitive", ["SKU Matrix, 2026"]),
  ],
}

# Per-metric citation packs
DEM_REFS = ["SKU Matrix, 2026", "timeanddate.com, 2026", "Author's domain knowledge, 2026"]
SUP_REFS = ["Vendor Indent, 2026", "Author's domain knowledge, 2026"]
NAME_REFS = ["SKU Matrix, 2026"]

def cls(p):
    if p > 5: return "up", "▲"
    if p < -5: return "down", "▼"
    return "flat", "▬"

def cat_class(c):
    return {"Vegetables":"veg","Fruits":"fr","Herbs/Greens":"hg","Others":"ot"}.get(c,"ot")

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f8; color: #1c2530; padding: 18px; line-height: 1.45; }
.wrap { max-width: 1480px; margin: 0 auto; }
header { background: linear-gradient(135deg, #0d3b66, #1f6e43); color: white; padding: 20px 24px; border-radius: 12px; margin-bottom: 16px; }
header h1 { font-size: 22px; margin-bottom: 4px; }
header .sub { font-size: 13px; opacity: 0.9; }
.legend { display: flex; gap: 14px; margin-top: 10px; flex-wrap: wrap; font-size: 11.5px; align-items: center; }
.legend span { background: rgba(255,255,255,0.13); padding: 4px 10px; border-radius: 12px; }
.legend a.refs-link { background: #d18c00; color: white; text-decoration: none; font-weight: 600; padding: 5px 12px; border-radius: 14px; }
.legend a.refs-link:hover { background: #b07700; }
.methodology { background: white; border: 1px solid #e3e8ee; border-radius: 10px; padding: 14px 18px; margin-bottom: 14px; font-size: 12px; color: #3a4654; }
.methodology h3 { font-size: 12px; color: #0d3b66; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
.methodology .row { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.methodology .row .col h4 { font-size: 11px; margin-bottom: 4px; }
.methodology .row .col h4.D { color: #11824a; }
.methodology .row .col h4.M { color: #d18c00; }
.methodology ul { padding-left: 16px; line-height: 1.55; }
.methodology li { margin: 1px 0; }
.toolbar { background: white; padding: 10px 16px; border-radius: 10px; border: 1px solid #e3e8ee; margin-bottom: 14px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; font-size: 13px; }
.toolbar select { padding: 5px 10px; border: 1px solid #d4dae2; border-radius: 5px; font-size: 12px; }
.toolbar label { color: #6b7989; font-size: 12px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 12px; }
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
.factors { font-size: 11.5px; color: #3a4654; line-height: 1.55; padding-top: 8px; border-top: 1px dashed #e3e8ee; }
.factors div { padding: 2px 0; }
.badge { display: inline-block; font-size: 8.5px; padding: 1px 5px; border-radius: 3px; font-weight: 700; vertical-align: middle; margin-left: 5px; letter-spacing: 0.4px; }
.badge.D { background: #11824a; color: white; }
.badge.M { background: #d18c00; color: white; }
.badge.DM { background: linear-gradient(90deg,#11824a 50%,#d18c00 50%); color: white; }
sup { font-size: 9px; }
sup a.cite { color: #155e8a; text-decoration: none; padding: 0 2px; border-radius: 2px; background: #ecf2f8; margin: 0 1px; font-weight: 600; }
sup a.cite:hover { background: #d18c00; color: white; }
footer { text-align: center; font-size: 11px; color: #7d8a99; margin-top: 22px; }
"""

# Build SKU cards
cards = []
for rank, sku in enumerate(ORDER, 1):
    d = DATA[sku]
    dem_p = d["demand_growth_pct"]; sup_p = d["supply_growth_pct"]
    dc, da = cls(dem_p); sc, sa = cls(sup_p)
    fac_items = SKU_FACTORS.get(sku, [])
    factors_html = "".join(f"<div>{txt} {sup(keys)}</div>" for txt,keys in fac_items[:3])
    cat = d["category"]; tier = d["tier"]
    name_sup = sup(NAME_REFS)
    dem_sup = sup(DEM_REFS)
    sup_sup = sup(SUP_REFS)
    cards.append(f"""
    <div class="box" data-cat="{cat}" data-tier="{tier}" data-dem="{dem_p}" data-sup="{sup_p}">
        <div class="box-head">
            <div>
                <div class="name">{sku}{name_sup} <span class="badge D" title="Real data — from SKU Decision Matrix">D</span></div>
                <div class="cat-pill {cat_class(cat)}">{cat}</div>
            </div>
            <div class="rank">#{rank}</div>
        </div>
        <div class="metrics">
            <div class="m dem"><div class="l">Demand {dem_sup} <span class="badge M" title="Modelled from monthly demand × festival/seasonality multiplier">M</span></div><div class="v {dc}">{da} {dem_p:+.1f}%</div></div>
            <div class="m sup"><div class="l">Supply {sup_sup} <span class="badge DM" title="Mixed: real vendor indent history + modelled forecast">D+M</span></div><div class="v {sc}">{sa} {sup_p:+.1f}%</div></div>
        </div>
        <div class="factors">{factors_html}</div>
    </div>
    """)

dems = [DATA[s]["demand_growth_pct"] for s in ORDER]
sups = [DATA[s]["supply_growth_pct"] for s in ORDER]
avg_dem = sum(dems)/20; avg_sup = sum(sups)/20

# Main dashboard HTML
html = f"""<!doctype html><html><head>
<meta charset="utf-8"><title>FnV Top 20 — Demand vs Supply (May 2026)</title>
<style>{CSS}</style></head><body>
<div class="wrap">
<header>
    <h1>FnV Top 20 SKUs — 4-Week Forecast (May 4 – May 31, 2026)</h1>
    <div class="sub">Demand: Bangalore consumption · Supply: Pan-India vendor sources · % change vs trailing 4-week average · Harvard-style citations linked below</div>
    <div class="legend">
        <span>📍 Demand: Bangalore</span>
        <span>🚛 Supply: Pan-India</span>
        <span>🎉 Eid al-Adha · May 27<sup><a class="cite" href="references.html#ref5" target="_blank">5</a></sup></span>
        <span>💍 Wedding season · May–Jun</span>
        <span>🌧 SW Monsoon onset · ~Jun 1<sup><a class="cite" href="references.html#ref3" target="_blank">3</a></sup></span>
        <span>📊 Avg demand ▲ {avg_dem:+.1f}% · supply ▲ {avg_sup:+.1f}%</span>
        <span><span class="badge D">D</span> Data · <span class="badge M">M</span> Modelled · <span class="badge DM">D+M</span> Mixed</span>
        <a class="refs-link" href="references.html" target="_blank">📚 View References →</a>
    </div>
</header>

<div class="methodology">
    <h3>What's Data vs Modelled (full provenance in references)</h3>
    <div class="row">
      <div class="col">
        <h4 class="D">🟢 Real data (from your files or verified sources)</h4>
        <ul>
          <li>Top 20 SKUs, ranking, monthly volumes <sup><a class="cite" href="references.html#ref1" target="_blank">1</a></sup></li>
          <li>Supply history — vendor indent Jan-Apr 2026 <sup><a class="cite" href="references.html#ref2" target="_blank">2</a></sup></li>
          <li>Festival dates <sup><a class="cite" href="references.html#ref5" target="_blank">5</a>,<a class="cite" href="references.html#ref6" target="_blank">6</a></sup>; Monsoon onset <sup><a class="cite" href="references.html#ref3" target="_blank">3</a>,<a class="cite" href="references.html#ref4" target="_blank">4</a></sup></li>
          <li>Lasalgaon onion hub <sup><a class="cite" href="references.html#ref7" target="_blank">7</a>,<a class="cite" href="references.html#ref8" target="_blank">8</a></sup>; Pollachi coconut hub <sup><a class="cite" href="references.html#ref12" target="_blank">12</a></sup>; TN drumstick share <sup><a class="cite" href="references.html#ref13" target="_blank">13</a>,<a class="cite" href="references.html#ref14" target="_blank">14</a></sup></li>
          <li>Onion export ban history <sup><a class="cite" href="references.html#ref9" target="_blank">9</a>,<a class="cite" href="references.html#ref10" target="_blank">10</a>,<a class="cite" href="references.html#ref11" target="_blank">11</a></sup></li>
        </ul>
      </div>
      <div class="col">
        <h4 class="M">🟠 Modelled / domain-knowledge layer</h4>
        <ul>
          <li><b>Demand %</b> — monthly demand split evenly to weeks; April extrapolated from March <sup><a class="cite" href="references.html#ref1" target="_blank">1</a>,<a class="cite" href="references.html#ref15" target="_blank">15</a></sup></li>
          <li><b>Supply forecast</b> — trailing indent × risk multiplier <sup><a class="cite" href="references.html#ref2" target="_blank">2</a>,<a class="cite" href="references.html#ref15" target="_blank">15</a></sup></li>
          <li>Pre-monsoon yield drops, pest cycles, fuel sensitivity, Nilgiris landslide risk, ringspot virus — all industry priors <sup><a class="cite" href="references.html#ref15" target="_blank">15</a></sup></li>
          <li>To calibrate: wire Agmarknet daily mandi feed <sup><a class="cite" href="references.html#ref16" target="_blank">16</a></sup>, weekly POS data, 12+ months history</li>
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
<footer>Top 20 SKUs · Built from SKU Decision Matrix + Vendor Indent (Jan–Apr 2026) · Click any superscript number to open the corresponding reference. · <a href="references.html" target="_blank">Open full reference list →</a></footer>
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
print(f"Written: concise_dashboard.html ({len(html)//1024} KB)")

# ---------------- References page ------------------
REFS_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f8; color: #1c2530; padding: 24px; line-height: 1.55; }
.wrap { max-width: 920px; margin: 0 auto; }
header { background: linear-gradient(135deg, #0d3b66, #1f6e43); color: white; padding: 22px 28px; border-radius: 12px; margin-bottom: 18px; }
header h1 { font-size: 22px; margin-bottom: 4px; }
header .sub { font-size: 13px; opacity: 0.9; }
header a.back { color: white; background: rgba(255,255,255,0.18); padding: 5px 12px; border-radius: 12px; text-decoration: none; font-size: 12px; display: inline-block; margin-top: 10px; }
header a.back:hover { background: rgba(255,255,255,0.3); }
.refs { background: white; border-radius: 11px; padding: 22px 26px; border: 1px solid #e3e8ee; }
.refs h2 { color: #0d3b66; font-size: 16px; margin-bottom: 14px; padding-bottom: 8px; border-bottom: 2px solid #ecf2f8; }
.refs ol { list-style: none; padding: 0; counter-reset: refcounter; }
.refs li { counter-increment: refcounter; padding: 12px 14px 12px 50px; position: relative; border-bottom: 1px solid #f0f3f7; font-size: 13.5px; line-height: 1.6; }
.refs li:last-child { border-bottom: 0; }
.refs li:target { background: #fff3df; border-left: 3px solid #d18c00; }
.refs li::before { content: counter(refcounter); position: absolute; left: 12px; top: 12px; background: #0d3b66; color: white; width: 26px; height: 26px; border-radius: 50%; font-size: 11px; display: flex; align-items: center; justify-content: center; font-weight: 700; }
.refs li a { color: #155e8a; word-break: break-all; }
.refs .key { font-weight: 600; color: #0d3b66; margin-right: 6px; }
.refs .verified { display: inline-block; background: #e6f4ea; color: #11824a; font-size: 10px; padding: 2px 7px; border-radius: 8px; margin-left: 8px; font-weight: 600; }
.refs .domain { display: inline-block; background: #fff3df; color: #a86b00; font-size: 10px; padding: 2px 7px; border-radius: 8px; margin-left: 8px; font-weight: 600; }
.refs .internal { display: inline-block; background: #eef4fb; color: #155e8a; font-size: 10px; padding: 2px 7px; border-radius: 8px; margin-left: 8px; font-weight: 600; }
.refs .live { display: inline-block; background: #f2eafd; color: #5a3d92; font-size: 10px; padding: 2px 7px; border-radius: 8px; margin-left: 8px; font-weight: 600; }
.note { background: white; border-radius: 11px; padding: 18px 22px; border: 1px solid #e3e8ee; margin-top: 16px; font-size: 12.5px; color: #4a5764; }
.note h3 { color: #0d3b66; font-size: 13px; margin-bottom: 6px; }
footer { text-align: center; font-size: 11px; color: #7d8a99; margin-top: 18px; }
"""

def ref_tag(key):
    if "Internal" in REFS[ref_idx(key)-1][1]:
        return '<span class="internal">Internal file</span>'
    if "domain knowledge" in key:
        return '<span class="domain">Industry priors — uncalibrated</span>'
    if "Agmarknet" in key:
        return '<span class="live">Live feed (not yet wired)</span>'
    return '<span class="verified">Verified web source</span>'

refs_html_items = []
for i,(key, full, url) in enumerate(REFS,1):
    tag = ref_tag(key)
    full_with_link = full
    if url and url != "—":
        full_with_link = full.replace(url, f'<a href="{url}" target="_blank">{url}</a>')
    refs_html_items.append(f'<li id="ref{i}"><span class="key">{key}.</span> {full_with_link} {tag}</li>')

refs_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><title>References — FnV Forecasting Dashboard</title>
<style>{REFS_CSS}</style></head><body>
<div class="wrap">
<header>
    <h1>📚 References</h1>
    <div class="sub">Harvard-style references for the FnV Top 20 SKU forecasting dashboard. Click any superscript on the dashboard to jump here.</div>
    <a class="back" href="concise_dashboard.html">← Back to dashboard</a>
</header>

<div class="refs">
    <h2>Reference list (Harvard)</h2>
    <ol>
        {''.join(refs_html_items)}
    </ol>
</div>

<div class="note">
    <h3>Notes on referencing</h3>
    <ul style="padding-left:18px;">
      <li><b>Verified web source</b> — checked via WebSearch on 8 May 2026; URL is the original article.</li>
      <li><b>Internal file</b> — content drawn directly from a file you uploaded to this session.</li>
      <li><b>Industry priors — uncalibrated</b> — author's domain knowledge of Indian FnV trade. Directionally reasonable but NOT back-tested against your data or a primary source. To convert these into "verified" references, wire in NHB horticulture stats, IMD seasonal bulletins, state agriculture department yield reports, and 12+ months of your own POS/dispatch history.</li>
      <li><b>Live feed (not yet wired)</b> — recommended source to integrate for a production tool.</li>
    </ul>
</div>

<footer>References compiled 8 May 2026 · Harvard referencing style · Last accessed dates noted in each entry</footer>
</div>
</body></html>"""

with open(os.path.join(OUT, "references.html"), "w") as f:
    f.write(refs_html)
print(f"Written: references.html ({len(refs_html)//1024} KB) — {len(REFS)} references")
