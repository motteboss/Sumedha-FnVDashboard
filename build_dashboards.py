"""Build Demand and Supply HTML dashboards from dashboard_data.json"""
import json, os

OUT_DIR = "/sessions/eager-adoring-faraday/mnt/outputs"
with open(os.path.join(OUT_DIR, "dashboard_data.json")) as f:
    DATA = json.load(f)
with open(os.path.join(OUT_DIR, "sku_order.json")) as f:
    ORDER = json.load(f)
with open(os.path.join(OUT_DIR, "factors.json")) as f:
    FACTORS = json.load(f)

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f4f6f8; color: #1c2530; line-height: 1.45; }
.wrap { max-width: 1480px; margin: 0 auto; padding: 24px; }
header { background: linear-gradient(135deg, #0d3b66, #155e8a); color: white; padding: 28px 24px; border-radius: 12px; margin-bottom: 22px; box-shadow: 0 4px 14px rgba(0,0,0,0.08); }
header h1 { font-size: 26px; margin-bottom: 6px; }
header .sub { opacity: 0.85; font-size: 14px; }
header .ctx { display:flex; gap:18px; margin-top:14px; flex-wrap:wrap; }
header .ctx span { background: rgba(255,255,255,0.13); padding: 6px 12px; border-radius: 18px; font-size: 12px; }
.kpi-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 22px; }
.kpi { background: white; padding: 16px 18px; border-radius: 10px; border: 1px solid #e3e8ee; }
.kpi .label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; color: #6b7989; margin-bottom: 6px; }
.kpi .val { font-size: 24px; font-weight: 600; color: #0d3b66; }
.kpi .delta { font-size: 12px; margin-top: 4px; }
.up { color: #11824a; }
.down { color: #c0392b; }
.flat { color: #7d8a99; }
.toolbar { display:flex; gap:12px; margin-bottom:18px; flex-wrap: wrap; align-items: center; background:white; padding:14px 18px; border-radius:10px; border:1px solid #e3e8ee; }
.toolbar label { font-size: 12px; color:#6b7989; margin-right: 6px; }
.toolbar select, .toolbar input { padding: 6px 10px; border: 1px solid #d4dae2; border-radius: 6px; font-size: 13px; background: white; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(440px, 1fr)); gap: 16px; }
.card { background: white; border-radius: 11px; border: 1px solid #e3e8ee; padding: 16px 18px; transition: box-shadow .2s; cursor: pointer; }
.card:hover { box-shadow: 0 6px 18px rgba(0,0,0,0.07); }
.card h3 { font-size: 16px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
.rank { background: #0d3b66; color: white; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: 600; }
.tags { margin: 6px 0 10px; display: flex; gap: 6px; flex-wrap: wrap; }
.tag { font-size: 10px; padding: 2px 8px; border-radius: 10px; background: #ecf2f8; color: #2c4763; text-transform: uppercase; letter-spacing: 0.4px; }
.tag.cat-veg { background:#e6f4ea; color:#1c6e3f; }
.tag.cat-fr { background:#fdecea; color:#a8392c; }
.tag.cat-hg { background:#e7f1f9; color:#1a5483; }
.tag.cat-ot { background:#f2eafd; color:#5a3d92; }
.tag.high { background:#0d3b66; color:white; }
.tag.med { background:#fff3df; color:#a86b00; }
.tag.review { background:#fdecea; color:#a8392c; }
.numbers { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 8px 0; }
.numbers .n { background: #f7f9fb; padding: 8px 10px; border-radius: 8px; }
.numbers .n .l { font-size: 10px; color: #6b7989; text-transform: uppercase; }
.numbers .n .v { font-size: 16px; font-weight: 600; color: #1c2530; }
.spark { height: 64px; margin: 8px 0 6px; }
.fctlist { font-size: 11.5px; color: #4a5764; margin-top: 6px; }
.fctlist b { color: #1c2530; }
.fctline { padding: 3px 0; border-top: 1px dashed #eee; }
.fctline:first-child { border-top: 0; }
.legend { background: white; padding: 14px 18px; border-radius: 10px; border: 1px solid #e3e8ee; margin-top: 22px; font-size: 12.5px; color: #4a5764; }
.legend h4 { margin-bottom: 8px; color: #0d3b66; font-size: 13px; }
.legend ul { padding-left: 18px; }
.legend li { margin: 3px 0; }
.modal { position: fixed; inset: 0; background: rgba(8,17,30,0.6); display: none; align-items: center; justify-content: center; z-index: 1000; padding: 24px; }
.modal.open { display: flex; }
.modal-body { background: white; border-radius: 12px; max-width: 920px; width: 100%; max-height: 90vh; overflow-y: auto; padding: 26px; }
.modal-body h2 { color: #0d3b66; margin-bottom: 4px; }
.modal-body .close { float: right; cursor: pointer; font-size: 22px; color: #6b7989; line-height:1; }
.modal-body section { margin-top: 18px; }
.modal-body section h3 { color: #155e8a; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; border-bottom: 2px solid #ecf2f8; padding-bottom: 4px; }
.modal-body .chart-wrap { height: 260px; }
.fact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.fact-grid .fc { background: #f7f9fb; padding: 11px 13px; border-radius: 8px; }
.fact-grid .fc h4 { font-size: 11px; text-transform: uppercase; color: #6b7989; margin-bottom: 4px; letter-spacing: 0.5px; }
.fact-grid .fc p, .fact-grid .fc li { font-size: 12.5px; color: #1c2530; }
.fact-grid .fc ul { padding-left: 18px; }
.fest-row { display:flex; justify-content:space-between; align-items:center; padding: 6px 8px; border-bottom:1px solid #f0f3f7; font-size: 12.5px; }
.fest-row:last-child{border-bottom:0;}
.fest-lvl { font-size:10px; padding:2px 7px; border-radius:8px; }
.fest-lvl.very_high{background:#0d3b66;color:white;}
.fest-lvl.high{background:#155e8a;color:white;}
.fest-lvl.med{background:#5a85a8;color:white;}
.fest-lvl.low{background:#c0d2e0;color:#1c2530;}
.geo-bar { display:flex; height:18px; border-radius:4px; overflow:hidden; margin: 6px 0; }
.geo-bar div { display:flex; align-items:center; justify-content:center; color:white; font-size:10px; font-weight:600; }
.alert { background:#fff3df; border-left: 3px solid #d18c00; padding: 8px 12px; margin: 8px 0; font-size:12.5px; color:#664400; border-radius: 4px; }
.alert.danger { background:#fdecea; border-color:#c0392b; color:#7a1d10; }
.alert.success { background:#e6f4ea; border-color:#11824a; color:#155f33; }
footer { text-align:center; font-size:11px; color:#7d8a99; margin-top:30px; padding: 14px;}
"""

def cat_class(c):
    return {"Vegetables":"cat-veg","Fruits":"cat-fr","Herbs/Greens":"cat-hg","Others":"cat-ot"}.get(c,"cat-ot")

def growth_class(p):
    if p > 5: return "up"
    if p < -5: return "down"
    return "flat"

def growth_arrow(p):
    if p > 5: return "▲"
    if p < -5: return "▼"
    return "▬"


# Build pages
def make_dashboard(mode):
    """mode: 'demand' or 'supply'"""
    is_dem = mode == "demand"
    title = "FnV Demand Forecast — Bangalore Consumption" if is_dem else "FnV Supply Forecast — Pan-India Sources"
    accent_color = "#0d3b66" if is_dem else "#1f6e43"
    cards_html = []
    embedded = {}
    for rank, sku in enumerate(ORDER, 1):
        d = DATA[sku]
        embedded[sku] = d
        growth = d["demand_growth_pct"] if is_dem else d["supply_growth_pct"]
        fc_avg = d["fc_avg_demand"] if is_dem else d["fc_avg_supply"]
        recent4 = (d["hist_demand"] if is_dem else d["hist_supply"])[-4:]
        recent_avg = sum(w["value"] for w in recent4)/4 if recent4 else 0
        # Top factors
        if is_dem:
            fests = []
            for fc in d["forecast_demand"]:
                for f in fc.get("festivals",[]):
                    if f not in fests: fests.append(f)
            note = d["forecast_demand"][0].get("note","")
            top_factor = ", ".join(fests[:2]) or note or "—"
        else:
            risks = []
            for fc in d["forecast_supply"]:
                for r in fc.get("risks",[]):
                    if r not in risks: risks.append(r)
            top_factor = "; ".join(risks[:2]) or "—"
        # Top source location
        locs = d["vendor_locations"]
        top_loc = max(locs.items(), key=lambda x:x[1])[0] if locs else "—"
        cat = d["category"]
        cards_html.append(f"""
        <div class="card" data-sku="{sku}" data-cat="{cat}" data-tier="{d['tier']}" data-growth="{growth:.1f}" onclick="openDetail('{sku}')">
            <h3>
                <span><span class="rank">#{rank}</span> {sku}</span>
                <span class="{growth_class(growth)}" style="font-size:14px;">{growth_arrow(growth)} {abs(growth):.1f}%</span>
            </h3>
            <div class="tags">
                <span class="tag {cat_class(cat)}">{cat}</span>
                <span class="tag {'high' if d['tier']=='High' else 'med'}">{d['tier']} Tier</span>
                <span class="tag {'review' if d['decision']=='Review' else ''}">{d['decision']}</span>
            </div>
            <div class="numbers">
                <div class="n"><div class="l">{'Recent wk avg (Apr)' if is_dem else 'Recent wk avg supply'}</div><div class="v">{recent_avg:,.0f}</div></div>
                <div class="n"><div class="l">4-wk Forecast (May)</div><div class="v">{fc_avg:,.0f}</div></div>
                <div class="n"><div class="l">{'Source mix' if not is_dem else '3M total'}</div><div class="v">{top_loc if not is_dem else f"{d['demand_total_3m']:,.0f}"}</div></div>
            </div>
            <canvas class="spark" id="spark-{mode}-{rank}"></canvas>
            <div class="fctlist">
                <div class="fctline"><b>{('Festival/Event drivers' if is_dem else 'Supply risk overlays')}:</b> {top_factor}</div>
            </div>
        </div>
        """)
    # KPI summary
    growths = [DATA[s]["demand_growth_pct" if is_dem else "supply_growth_pct"] for s in ORDER]
    avg_growth = sum(growths)/len(growths)
    upcount = sum(1 for g in growths if g > 5)
    downcount = sum(1 for g in growths if g < -5)
    total_fc = sum((DATA[s]["fc_avg_demand"] if is_dem else DATA[s]["fc_avg_supply"]) for s in ORDER)
    sorted_g = sorted(zip(ORDER, growths), key=lambda x: x[1], reverse=True)
    top_grow = sorted_g[0]
    top_fall = sorted_g[-1]

    html = f"""<!doctype html>
<html><head>
<meta charset="utf-8">
<title>{title}</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header style="background: linear-gradient(135deg, {accent_color}, #1f6e43);" >
    <h1>{title}</h1>
    <div class="sub">Top 20 SKUs · 4-week rolling forecast (May 4 – May 31, 2026) · Built {('from monthly demand x weekly seasonal/festival overlay' if is_dem else 'from vendor indent (Jan–Apr 2026) x supply-geography risk model')}</div>
    <div class="ctx">
        <span>📍 Demand: Bangalore consumption</span>
        <span>🚛 Supply: Pan-India vendor sources</span>
        <span>📅 History window: 12 weeks (Feb–Apr 2026)</span>
        <span>🔮 Forecast horizon: 4 weeks</span>
        <span>🎉 Festival overlay: Eid al-Adha, Buddha Purnima, Wedding season, Vat Savitri</span>
    </div>
</header>

<div class="kpi-row">
  <div class="kpi"><div class="label">SKUs tracked</div><div class="val">20</div><div class="delta flat">All ‘Keep’ tier · 1 ‘Review’ (Watermelon)</div></div>
  <div class="kpi"><div class="label">Avg {'demand' if is_dem else 'supply'} growth (next 4 wks)</div><div class="val {growth_class(avg_growth)}">{growth_arrow(avg_growth)} {avg_growth:+.1f}%</div><div class="delta">vs trailing 4-wk avg</div></div>
  <div class="kpi"><div class="label">SKUs growing</div><div class="val up">{upcount}</div><div class="delta">{downcount} declining · {20-upcount-downcount} flat</div></div>
  <div class="kpi"><div class="label">Largest mover (↑)</div><div class="val up" style="font-size:18px;">{top_grow[0]}</div><div class="delta up">{top_grow[1]:+.1f}%</div></div>
  <div class="kpi"><div class="label">Largest mover (↓)</div><div class="val down" style="font-size:18px;">{top_fall[0]}</div><div class="delta down">{top_fall[1]:+.1f}%</div></div>
  <div class="kpi"><div class="label">Total forecast volume / wk</div><div class="val">{total_fc:,.0f}</div><div class="delta flat">{'units/bunches/kg per week (Bangalore demand)' if is_dem else 'units indented per week (national supply)'}</div></div>
</div>

<div class="toolbar">
    <label>Category:</label>
    <select id="filter-cat" onchange="applyFilters()">
        <option value="">All</option>
        <option>Vegetables</option><option>Fruits</option><option>Herbs/Greens</option><option>Others</option>
    </select>
    <label>Tier:</label>
    <select id="filter-tier" onchange="applyFilters()">
        <option value="">All</option><option>High</option><option>Medium</option>
    </select>
    <label>Trend:</label>
    <select id="filter-trend" onchange="applyFilters()">
        <option value="">All</option>
        <option value="up">Growth ≥ 5%</option>
        <option value="down">Decline ≥ 5%</option>
        <option value="flat">Flat (-5 to +5%)</option>
    </select>
    <label>Sort:</label>
    <select id="filter-sort" onchange="applyFilters()">
        <option value="rank">Rank (volume)</option>
        <option value="growth-desc">Growth (high → low)</option>
        <option value="growth-asc">Growth (low → high)</option>
        <option value="fc-desc">Forecast volume (high → low)</option>
    </select>
</div>

<div class="grid" id="grid">
{''.join(cards_html)}
</div>

<div class="legend">
    <h4>How to read this dashboard</h4>
    <ul>
      <li><b>Recent wk avg</b> = last 4 weeks' average ({'Bangalore consumption' if is_dem else 'pan-India vendor indent'}); <b>4-wk Forecast</b> = projected average per week May 4–31 2026.</li>
      <li><b>Growth %</b> = forecast avg vs trailing 4-week avg. ▲ = growth, ▼ = decline, ▬ = flat.</li>
      <li><b>{'Festival/Event drivers' if is_dem else 'Supply risk overlays'}</b> are pulled from the calendar applied to each SKU. Click any card to see weekly history, forecast, and the full factor list.</li>
      <li><b>Methodology:</b> {'Forecast = Mar daily demand × extrapolated trend (Jan-Feb→Mar) × festival multiplier × seasonality adjustment (e.g., greens heat-yield, watermelon monsoon collapse).' if is_dem else 'Forecast = trailing 4-week vendor indent × supply geography risk multiplier (pre-monsoon greens yield, TN dependency, Maharashtra rabi tail, harvest-peak upside).'}</li>
    </ul>
</div>

<footer>Bangalore FnV Forecasting Tool · Top 20 SKUs · Built from SKU Decision Matrix v2-2 + Vendor Indent (Jan-Apr 2026)</footer>
</div>

<div class="modal" id="modal" onclick="if(event.target===this)closeDetail()">
    <div class="modal-body" id="modal-body"></div>
</div>

<script>
const DATA = {json.dumps(embedded)};
const ORDER = {json.dumps(ORDER)};
const FACTORS = {json.dumps(FACTORS)};
const MODE = {json.dumps(mode)};

function fmt(n){{ return Math.round(n).toLocaleString('en-IN'); }}

// Render sparklines
function renderSparks() {{
    ORDER.forEach((sku, i) => {{
        const id = 'spark-' + MODE + '-' + (i+1);
        const el = document.getElementById(id);
        if (!el) return;
        const d = DATA[sku];
        const hist = MODE === 'demand' ? d.hist_demand.slice(-12) : d.hist_supply.slice(-12);
        const fc = MODE === 'demand' ? d.forecast_demand : d.forecast_supply;
        const labels = hist.map(h=>h.week_start.slice(5)).concat(fc.map(f=>f.week_start.slice(5)));
        const histVals = hist.map(h=>h.value).concat(Array(fc.length).fill(null));
        const fcVals = Array(hist.length-1).fill(null).concat([hist[hist.length-1].value]).concat(fc.map(f=>f.value));
        new Chart(el, {{
            type:'line',
            data:{{
                labels: labels,
                datasets:[
                    {{label:'History', data: histVals, borderColor:'#0d3b66', backgroundColor:'rgba(13,59,102,0.06)', fill:true, tension:0.3, pointRadius:0, borderWidth:1.6}},
                    {{label:'Forecast', data: fcVals, borderColor:'#d18c00', backgroundColor:'rgba(209,140,0,0.10)', fill:true, tension:0.3, pointRadius:0, borderWidth:1.6, borderDash:[4,3]}}
                ]
            }},
            options:{{
                plugins:{{legend:{{display:false}},tooltip:{{enabled:true,callbacks:{{label:c=>fmt(c.parsed.y)}}}}}},
                scales:{{x:{{display:false}},y:{{display:false,beginAtZero:true}}}},
                maintainAspectRatio:false,
                responsive:true
            }}
        }});
    }});
}}

function applyFilters() {{
    const cat = document.getElementById('filter-cat').value;
    const tier = document.getElementById('filter-tier').value;
    const trend = document.getElementById('filter-trend').value;
    const sort = document.getElementById('filter-sort').value;
    const grid = document.getElementById('grid');
    let cards = Array.from(grid.querySelectorAll('.card'));
    cards.forEach(c => {{
        const cm = !cat || c.dataset.cat === cat;
        const tm = !tier || c.dataset.tier === tier;
        const g = parseFloat(c.dataset.growth);
        const trm = !trend || (trend==='up' && g>=5) || (trend==='down' && g<=-5) || (trend==='flat' && g>-5 && g<5);
        c.style.display = (cm && tm && trm) ? '' : 'none';
    }});
    if (sort) {{
        cards.sort((a,b)=>{{
            if (sort==='rank') return parseInt(a.querySelector('.rank').textContent.slice(1)) - parseInt(b.querySelector('.rank').textContent.slice(1));
            if (sort==='growth-desc') return parseFloat(b.dataset.growth) - parseFloat(a.dataset.growth);
            if (sort==='growth-asc') return parseFloat(a.dataset.growth) - parseFloat(b.dataset.growth);
            if (sort==='fc-desc') {{
                const av = DATA[a.dataset.sku][MODE==='demand'?'fc_avg_demand':'fc_avg_supply'];
                const bv = DATA[b.dataset.sku][MODE==='demand'?'fc_avg_demand':'fc_avg_supply'];
                return bv - av;
            }}
        }});
        cards.forEach(c => grid.appendChild(c));
    }}
}}

function openDetail(sku) {{
    const d = DATA[sku];
    const f = d.factors || {{}};
    const isDem = MODE === 'demand';
    const hist = (isDem? d.hist_demand : d.hist_supply).slice(-12);
    const fc = isDem? d.forecast_demand : d.forecast_supply;
    const total = (Object.values(d.vendor_locations || {{}}).reduce((a,b)=>a+b,0)) || 1;
    const sortedLocs = Object.entries(d.vendor_locations || {{}}).sort((a,b)=>b[1]-a[1]);
    const sortedVendors = Object.entries(d.vendors || {{}}).sort((a,b)=>b[1]-a[1]);
    const colors = ['#0d3b66','#155e8a','#2d80b1','#5a9fc4','#8cb9d0','#b8d3e2','#ddebf3'];
    const geoBar = sortedLocs.map(([loc,v],i)=>`<div style="background:${{colors[i%7]}};width:${{(v/total*100).toFixed(1)}}%;" title="${{loc}}: ${{fmt(v)}} (${{(v/total*100).toFixed(1)}}%)">${{(v/total*100)>=8?loc:''}}</div>`).join('');

    let festHtml = '';
    if (isDem && f.festivals_demand) {{
        festHtml = f.festivals_demand.map(([n,l])=>`<div class="fest-row"><span>${{n}}</span><span>${{l}}</span></div>`).join('');
    }}

    let nationalFestHtml = '';
    if (isDem) {{
        nationalFestHtml = (FACTORS.festival_cal||[]).filter(fe => {{
            const i = (fe.impact||'').toLowerCase();
            const lower = sku.toLowerCase();
            return lower.split(/[\\s,/()]/).some(t => t.length>3 && i.includes(t)) ||
              (lower.includes('coriander') && i.includes('coriander')) ||
              (lower.includes('mint') && (i.includes('mint')||i.includes('pudina'))) ||
              (lower.includes('tomato') && i.includes('tomato')) ||
              (lower.includes('banana') && i.includes('banana')) ||
              (lower.includes('coconut') && i.includes('coconut'));
        }}).map(fe => `<div class="fest-row"><span><b>${{fe.name}}</b> <span style="color:#7d8a99;">· ${{fe.date.replace(/_to_/,' → ')}}</span></span><span class="fest-lvl ${{fe.level}}">${{fe.level.replace('_',' ').toUpperCase()}}</span></div>`).join('');
    }}

    document.getElementById('modal-body').innerHTML = `
        <span class="close" onclick="closeDetail()">×</span>
        <h2>${{sku}}</h2>
        <div style="color:#6b7989;font-size:13px;">${{d.category}} · ${{d.tier}} Tier · ${{d.decision}} · 3M demand: ${{fmt(d.demand_total_3m)}} · Total indent (Jan-Apr): ${{fmt(d.supply_total)}}</div>

        <section>
            <h3>${{isDem?'Weekly demand — 12-week history + 4-week forecast':'Weekly supply (vendor indent) — 12-week history + 4-week forecast'}}</h3>
            <div class="chart-wrap"><canvas id="detail-chart"></canvas></div>
        </section>

        ${{!isDem ? `
        <section>
            <h3>Supply geography (Jan-Apr 2026)</h3>
            <div class="geo-bar">${{geoBar}}</div>
            <div style="font-size:12px;color:#6b7989;">Top sources: ${{sortedLocs.slice(0,5).map(([l,v])=>l+' ('+fmt(v)+')').join(' · ')}}</div>
            <div style="margin-top:10px;font-size:12.5px;"><b>Vendors (${{sortedVendors.length}}):</b> ${{sortedVendors.slice(0,4).map(([v,q])=>v+' ('+fmt(q)+')').join(' · ')}}</div>
        </section>
        ` : `
        <section>
            <h3>Festival & event drivers (next 90 days)</h3>
            ${{nationalFestHtml || '<div style="color:#7d8a99;font-size:12.5px;">No major festival driver in window for this SKU.</div>'}}
        </section>
        `}}

        <section>
            <h3>Factors layered into forecast</h3>
            <div class="fact-grid">
                ${{f.festivals_demand && isDem ? `<div class="fc"><h4>SKU-specific festival demand</h4>${{festHtml}}</div>` : ''}}
                ${{f.weather ? `<div class="fc"><h4>Weather sensitivity</h4><p>${{f.weather}}</p></div>` : ''}}
                ${{f.harvest_origin ? `<div class="fc"><h4>Harvest origin</h4><ul>${{f.harvest_origin.map(o=>'<li>'+o+'</li>').join('')}}</ul></div>` : ''}}
                ${{f.monsoon_impact ? `<div class="fc"><h4>Monsoon impact</h4><p>${{f.monsoon_impact}}</p></div>` : ''}}
                ${{f.disruption ? `<div class="fc"><h4>Disruption flags</h4><ul>${{f.disruption.map(o=>'<li>'+o+'</li>').join('')}}</ul></div>` : ''}}
                ${{f.fuel_sensitivity ? `<div class="fc"><h4>Fuel / freight sensitivity</h4><p>${{f.fuel_sensitivity}}</p></div>` : ''}}
            </div>
        </section>

        ${{!isDem ? `<section>
            <h3>Forecast detail (May 4 - May 31, 2026)</h3>
            ${{fc.map(w => `<div class="alert"><b>Wk ${{w.week_start}}:</b> ${{fmt(w.value)}} units · Risks: ${{(w.risks||[]).join(', ')||'—'}}</div>`).join('')}}
        </section>` : `<section>
            <h3>Forecast detail (May 4 - May 31, 2026)</h3>
            ${{fc.map(w => `<div class="alert ${{(w.festivals||[]).length?'success':''}}"><b>Wk ${{w.week_start}}:</b> ${{fmt(w.value)}} units · Drivers: ${{[(w.festivals||[]).join(', '), w.note].filter(Boolean).join(' · ')||'baseline'}}</div>`).join('')}}
        </section>`}}
    `;
    document.getElementById('modal').classList.add('open');
    setTimeout(()=>{{
        const ctx = document.getElementById('detail-chart');
        const labels = hist.map(h=>h.week_start).concat(fc.map(f=>f.week_start));
        const histVals = hist.map(h=>h.value).concat(Array(fc.length).fill(null));
        const fcVals = Array(hist.length-1).fill(null).concat([hist[hist.length-1].value]).concat(fc.map(f=>f.value));
        new Chart(ctx, {{
            type:'line',
            data:{{
                labels,
                datasets:[
                    {{label:'History', data:histVals, borderColor:'#0d3b66', backgroundColor:'rgba(13,59,102,0.10)', fill:true, tension:0.3, pointRadius:3, borderWidth:2}},
                    {{label:'Forecast', data:fcVals, borderColor:'#d18c00', backgroundColor:'rgba(209,140,0,0.15)', fill:true, tension:0.3, pointRadius:3, borderWidth:2, borderDash:[6,4]}}
                ]
            }},
            options:{{
                plugins:{{legend:{{position:'top',labels:{{boxWidth:10}}}},tooltip:{{callbacks:{{label:c=>c.dataset.label+': '+fmt(c.parsed.y)}}}}}},
                scales:{{y:{{beginAtZero:true,ticks:{{callback:v=>fmt(v)}}}}}},
                responsive:true,
                maintainAspectRatio:false
            }}
        }});
    }},50);
}}
function closeDetail(){{ document.getElementById('modal').classList.remove('open'); }}

document.addEventListener('DOMContentLoaded', renderSparks);
</script>
</body></html>"""
    return html

with open(os.path.join(OUT_DIR, "demand_dashboard.html"), "w") as f:
    f.write(make_dashboard("demand"))
with open(os.path.join(OUT_DIR, "supply_dashboard.html"), "w") as f:
    f.write(make_dashboard("supply"))
print("Dashboards written.")
