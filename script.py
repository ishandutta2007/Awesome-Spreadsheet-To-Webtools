import os
import re
import subprocess

def run_cmd(cmd):
    print("Running:", cmd)
    subprocess.run(cmd, shell=True, check=True)

def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

def write_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

# TASK 1: SaaS List
readme = read_readme()

saas_data = [
    {"name": "Microsoft Power Apps", "line": "| **[Microsoft Power Apps](https://powerapps.microsoft.com/)** | Enterprise solution with deep Excel/SharePoint integration. | Starts at $20/user/mo. Free developer plan available (for individual testing). |", "val": 3000000, "val_str": "$3T"},
    {"name": "AppSheet", "line": "| **[AppSheet](https://about.appsheet.com/home/)** | Powerful no-code apps directly from spreadsheets with strong mobile support. | Starts at $5/user/mo. Free tier available (for prototyping, up to 10 users). |", "val": 2000000, "val_str": "$2T"},
    {"name": "Bubble", "line": "| **[Bubble](https://bubble.io/)** | Full visual web application builder with excellent data integration. | Starts at $32/mo. Free tier available (watermarked, basic features, community support). |", "val": 500, "val_str": "$500M"},
    {"name": "Softr", "line": "| **[Softr](https://softr.io/)** | Beautiful client portals, directories, and web apps from Airtable/Google Sheets. | Starts at $49/mo. Free tier available (up to 5 internal or 100 external users). |", "val": 100, "val_str": "$100M"},
    {"name": "Glide", "line": "| **[Glide](https://www.glideapps.com/)** | Turns Google Sheets into mobile-first web & native apps (excellent for PWAs). | Starts at $25/mo. Free tier available (up to 3 apps, limited data/updates). |", "val": 50, "val_str": "$50M"},
    {"name": "Stacker", "line": "| **[Stacker](https://www.stackerhq.com/)** | Transforms spreadsheets/Airtable into business apps and customer portals. | Starts at $59/mo. No free tier (30-day free trial available). |", "val": 20, "val_str": "$20M"},
    {"name": "Adalo", "line": "| **[Adalo](https://www.adalo.com/)** | Mobile app builder with spreadsheet/database integration. | Starts at $45/mo. Free tier available (limited records and features, Adalo branding). |", "val": 20, "val_str": "$20M"},
    {"name": "Noloco", "line": "| **[Noloco](https://noloco.io/)** | No-code web apps and member portals from spreadsheets. | Starts at $39/mo. No free tier (free trial available). |", "val": 5, "val_str": "$5M"},
    {"name": "SpreadSimple", "line": "| **[SpreadSimple](https://spreadsimple.com/)** | Simple websites and apps from Google Sheets/Excel. | Starts at $13/mo. Free tier available (basic features, SpreadSimple branding). |", "val": 2, "val_str": "$2M"},
    {"name": "Clappia", "line": "| **[Clappia](https://clappia.com/)** | No-code apps with workflows from spreadsheets. | Starts at $5/user/mo. Free tier available (limited apps, users, and records). |", "val": 1, "val_str": "$1M"},
    {"name": "SpreadsheetWeb", "line": "| **[SpreadsheetWeb](https://www.spreadsheetweb.com/)** | Converts Excel models into web apps and calculators. | Starts at $25/mo. No free tier (14-day free trial available). |", "val": 1, "val_str": "$1M"},
    {"name": "Appizy", "line": "| **[Appizy](https://www.appizy.com/)** | Excel spreadsheets → interactive web applications. | Starts at €10/mo. Free tier available (basic converter, limited features). |", "val": 1, "val_str": "$1M"}
]

saas_data = sorted(saas_data, key=lambda x: x["val"], reverse=True)

saas_table = "| Product | Description | Pricing | Valuation / Size |\n"
saas_table += "|---------|-------------|---------|------------------|\n"
for item in saas_data:
    line = item["line"].strip()
    line = line[:-1]
    saas_table += f"{line} {item['val_str']} |\n"

old_table = r"\| Product \| Description \| Pricing \|\n\|---------\|-------------\|---------\|\n(?:\|.*\|\n)+"
readme = re.sub(old_table, saas_table, readme)
write_readme(readme)
run_cmd('git add . && git commit -m "Added company size and sorted the SaaS based on that" && git push')

# TASK 2: Open Source Stars
readme = read_readme()

os_data = [
    {"name": "NocoDB", "repo": "nocodb/nocodb", "desc": "The most popular open-source **Airtable alternative**. Turn any SQL database into a spreadsheet-like interface with multiple views (Grid, Kanban, Gallery, Calendar, Form), REST/GraphQL APIs, and automations. Import spreadsheets easily.", "stars": 43000, "cat": "Top Recommendations"},
    {"name": "Appsmith", "repo": "appsmithorg/appsmith", "desc": "Build custom dashboards, admin panels, and CRUD apps with JavaScript extensibility. Great for internal tools.", "stars": 32000, "cat": "Low-Code App Builders"},
    {"name": "ToolJet", "repo": "ToolJet/ToolJet", "desc": "Low-code platform for building internal tools and dashboards with extensive data connectors and code flexibility.", "stars": 28000, "cat": "Low-Code App Builders"},
    {"name": "Budibase", "repo": "budibase/budibase", "desc": "Build internal tools, dashboards, forms, approval apps, and automations. Connects to spreadsheets/databases. Drag-and-drop UI.", "stars": 22000, "cat": "Low-Code App Builders"},
    {"name": "Teable", "repo": "teableio/teable", "desc": "Modern spreadsheet-database.", "stars": 12000, "cat": "Other Notable Open-Source Tools"},
    {"name": "NocoBase", "repo": "nocobase/nocobase", "desc": "Highly extensible no-code platform.", "stars": 11000, "cat": "Other Notable Open-Source Tools"},
    {"name": "Grist", "repo": "gristlabs/grist-core", "desc": "Relational spreadsheet-database hybrid with powerful formulas (including Python), charts, and sharing. Excellent for complex data logic. Self-hostable with SQLite support.", "stars": 6000, "cat": "Top Recommendations"},
    {"name": "Baserow", "repo": "bramw/baserow", "desc": "Open-source no-code database and application builder. Import spreadsheets, build custom apps, and use templates.", "stars": 5000, "cat": "Top Recommendations"},
    {"name": "Rowy", "repo": "buildship-ai/rowy", "desc": "Airtable-like spreadsheet UI with low-code backend functions (JS/TS) on Firebase/Google Cloud.", "stars": 4000, "cat": "Other Notable Open-Source Tools"},
    {"name": "Saltcorn", "repo": "saltcorn/saltcorn", "desc": "Self-hosted no-code application builder.", "stars": 2000, "cat": "Other Notable Open-Source Tools"}
]

os_data = sorted(os_data, key=lambda x: x["stars"], reverse=True)

os_section = "## Open-Source & Self-Hosted Alternatives (Primary Focus)\n\nFree, self-hostable solutions that give you full control over your data and infrastructure. Perfect for privacy, customization, and avoiding vendor lock-in.\n\n"
for item in os_data:
    badge = f"[![GitHub stars](https://img.shields.io/github/stars/{item['repo']}?style=social&color=white)](https://github.com/{item['repo']}/stargazers)"
    os_section += f"- **[{item['name']}](https://github.com/{item['repo']})** {badge} — {item['desc']}  \n"

old_os_section = r"## Open-Source & Self-Hosted Alternatives \(Primary Focus\).*?(?=## Quick Comparison \(Open-Source\))"
readme = re.sub(old_os_section, os_section, readme, flags=re.DOTALL)
write_readme(readme)
run_cmd('git add . && git commit -m "Added github stars and sorted the opensource based on that" && git push')

# TASK 3: Banner
os.makedirs("assets", exist_ok=True)
svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:rgb(131,58,180);stop-opacity:1" />
      <stop offset="50%" style="stop-color:rgb(253,29,29);stop-opacity:1" />
      <stop offset="100%" style="stop-color:rgb(252,176,69);stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#grad1)" rx="20"/>
  <text x="50%" y="45%" font-family="Arial" font-size="40" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">
    Awesome Spreadsheet To Web Tools
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite" />
  </text>
  <text x="50%" y="70%" font-family="Arial" font-size="20" fill="white" text-anchor="middle" dominant-baseline="middle">
    A curated list of tools to convert spreadsheets to web apps
  </text>
</svg>'''
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

readme = read_readme()
banner_md = '<p align="center"><img src="assets/banner.svg" alt="Banner"></p>\n\n'
readme = readme.replace("# Awesome-Spreadsheet-To-Webtools\n", f"# Awesome-Spreadsheet-To-Webtools\n\n{banner_md}")
write_readme(readme)
run_cmd('git add . && git commit -m "added banner" && git push')

# TASK 4: Emojis
readme = read_readme()
readme = readme.replace("## SaaS / Hosted Platforms", "## ☁️ SaaS / Hosted Platforms")
readme = readme.replace("## Open-Source & Self-Hosted Alternatives (Primary Focus)", "## 🌍 Open-Source & Self-Hosted Alternatives (Primary Focus)")
readme = readme.replace("## Quick Comparison (Open-Source)", "## 📊 Quick Comparison (Open-Source)")
readme = readme.replace("## Why Go Open-Source?", "## 💡 Why Go Open-Source?")
readme = readme.replace("## Getting Started", "## 🚀 Getting Started")
readme = readme.replace("## Contributing", "## 🤝 Contributing")
write_readme(readme)
run_cmd('git add . && git commit -m "added emojis" && git push')

# TASK 5: SEO optimized
readme = read_readme()
seo_header = """<meta name="description" content="A curated list of awesome tools to convert spreadsheets like Google Sheets, Excel, and CSV into powerful web apps, internal tools, portals, and dashboards." />
<meta name="keywords" content="spreadsheet to web app, google sheets to web app, excel to web app, internal tools builder, open source nocode, low code platform" />

"""
readme = readme.replace(banner_md, f"{banner_md}{seo_header}")
write_readme(readme)
run_cmd('git add . && git commit -m "seo optimised" && git push')

# TASK 6: Badges left
readme = read_readme()
left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
badges_container = f'<p align="center">\n  {left_badges}\n</p>\n'
readme = readme.replace(seo_header, f"{seo_header}{badges_container}")
write_readme(readme)
run_cmd('git add . && git commit -m "badges to left added" && git push')

# TASK 7: Badges right
readme = read_readme()
right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
readme = readme.replace(f'  {left_badges}\n</p>', f'  {left_badges}\n  {right_badge}\n</p>')
write_readme(readme)
run_cmd('git add . && git commit -m "badges to right added" && git push')

# TASK 8: Star History
readme = read_readme()
folder_name = "Awesome-Spreadsheet-To-Webtools"
star_history = f"""
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F{folder_name}&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/{folder_name}&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
readme = readme + "\n" + star_history
write_readme(readme)
run_cmd('git add . && git commit -m "star history added" && git push')

# TASK 9: Replace chartrepos with chart?repos
readme = read_readme()
readme = readme.replace("chartrepos", "chart?repos")
write_readme(readme)
run_cmd('git add . && git commit -m "fixed star plot" && git push')

# TASK 10: Replace awesome link
readme = read_readme()
readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")
write_readme(readme)
run_cmd('git add . && git commit -m "invalid awesome link fixed" && git push')
