"""
Replaces the old glass-pill navbar CSS + HTML with a new Pixelr-style
horizontal top-bar navbar across all HTML files in the buyer-file folder.
"""

import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ── New CSS block to replace the old <style>…</style> nav block ──────────────
NEW_STYLE = """    <!-- Top-Bar Nav Style -->
    <style>
        /* ── Top Bar Navbar ── */
        .top-navbar {
            position: fixed;
            top: 0; left: 0;
            width: 100%;
            background: #fff;
            border-bottom: 1px solid #e8e8e8;
            box-shadow: 0 2px 12px rgba(0,0,0,0.07);
            z-index: 1000;
            transition: box-shadow 0.3s;
        }
        .top-navbar.scrolled {
            box-shadow: 0 4px 24px rgba(0,0,0,0.13);
        }
        .top-navbar-inner {
            max-width: 1320px;
            margin: 0 auto;
            padding: 0 32px;
            height: 68px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 24px;
        }

        /* Logo */
        .tn-logo { flex-shrink: 0; display: flex; align-items: center; }
        .tn-logo img { height: 36px; width: auto; object-fit: contain; display: block; }

        /* Nav Links */
        .tn-links {
            display: flex;
            align-items: center;
            gap: 4px;
            list-style: none;
            margin: 0; padding: 0;
            flex: 1;
            justify-content: center;
        }
        .tn-links > li { position: relative; }
        .tn-links > li > a {
            display: flex;
            align-items: center;
            gap: 5px;
            padding: 8px 14px;
            color: #1a1a1a;
            font-size: 13px;
            font-weight: 600;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            text-decoration: none;
            border-radius: 6px;
            transition: background 0.2s, color 0.2s;
            white-space: nowrap;
        }
        .tn-links > li > a:hover,
        .tn-links > li:hover > a { background: #f4f4f4; color: #000; }
        .tn-links > li > a i {
            font-size: 10px;
            transition: transform 0.25s;
        }
        .tn-links > li:hover > a i { transform: rotate(180deg); }

        /* Dropdown */
        .tn-dropdown {
            position: absolute;
            top: calc(100% + 8px);
            left: 50%;
            transform: translateX(-50%) translateY(6px);
            background: #fff;
            border: 1px solid #e8e8e8;
            border-radius: 14px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.12);
            padding: 8px;
            min-width: 200px;
            list-style: none;
            margin: 0;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.22s, transform 0.22s;
            z-index: 1001;
        }
        .tn-dropdown::before {
            content: '';
            position: absolute;
            top: -20px; left: 0; right: 0; height: 24px;
        }
        .tn-links > li:hover .tn-dropdown {
            opacity: 1;
            pointer-events: auto;
            transform: translateX(-50%) translateY(0);
        }
        .tn-dropdown li { padding: 0; }
        .tn-dropdown a {
            display: block;
            padding: 10px 16px;
            color: #333;
            font-size: 13px;
            font-weight: 500;
            text-decoration: none;
            border-radius: 8px;
            letter-spacing: 0.02em;
            transition: background 0.18s, color 0.18s;
        }
        .tn-dropdown a:hover { background: #f4f4f4; color: #000; }
        .tn-dropdown hr { margin: 4px 8px; border: none; border-top: 1px solid #eee; }

        /* CTA Button */
        .tn-cta {
            flex-shrink: 0;
            background: #1a1a1a;
            color: #fff !important;
            padding: 10px 22px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            text-decoration: none !important;
            white-space: nowrap;
            transition: background 0.2s, transform 0.2s;
        }
        .tn-cta:hover { background: #333; transform: translateY(-1px); }

        /* Body offset so content isn't hidden under fixed bar */
        body { padding-top: 68px; }

        /* ── Mobile Navbar ── */
        .mob-navbar {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0;
            background: #fff;
            border-bottom: 1px solid #e8e8e8;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            z-index: 1000;
        }
        .mob-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 14px 18px;
        }
        .mob-logo img { height: 32px; width: auto; }
        .mob-hamburger {
            width: 28px; height: 22px;
            display: flex; flex-direction: column;
            justify-content: space-between;
            cursor: pointer; border: none; background: transparent; padding: 0;
        }
        .mob-hamburger span {
            display: block; width: 100%; height: 2px;
            background: #1a1a1a; border-radius: 2px;
            transition: 0.3s;
        }
        .mob-hamburger.open span:nth-child(1) { transform: translateY(10px) rotate(45deg); }
        .mob-hamburger.open span:nth-child(2) { opacity: 0; }
        .mob-hamburger.open span:nth-child(3) { transform: translateY(-10px) rotate(-45deg); }

        .mob-menu {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.35s ease;
            background: #fff;
        }
        .mob-menu.open { max-height: 500px; }
        .mob-menu-inner {
            padding: 10px 18px 18px;
            display: flex; flex-direction: column; gap: 4px;
        }
        .mob-menu-inner a {
            display: block;
            padding: 11px 14px;
            color: #1a1a1a;
            font-size: 14px;
            font-weight: 600;
            text-decoration: none;
            border-radius: 8px;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }
        .mob-menu-inner a:hover { background: #f4f4f4; }
        .mob-menu-inner .mob-cta-btn {
            margin-top: 8px;
            background: #1a1a1a;
            color: #fff !important;
            text-align: center;
            border-radius: 999px;
            padding: 13px;
        }
        .mob-menu-inner .mob-cta-btn:hover { background: #333; }

        @media (max-width: 900px) {
            .top-navbar { display: none; }
            .mob-navbar  { display: block; }
            body { padding-top: 62px; }
        }
        @media (max-width: 1100px) {
            .tn-links > li > a { padding: 8px 10px; font-size: 12px; }
            .tn-cta { padding: 9px 16px; font-size: 12px; }
        }
    </style>"""

# ── New Desktop Nav HTML ──────────────────────────────────────────────────────
NEW_DESKTOP_NAV = """    <!-- Desktop Top-Bar Nav -->
    <div class="top-navbar" id="topNavbar">
        <div class="top-navbar-inner">
            <!-- Logo -->
            <div class="tn-logo">
                <a href="index.html">
                    <img src="assets/img/update new logo.png" alt="ADES logo">
                </a>
            </div>

            <!-- Links -->
            <ul class="tn-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="about-1.html">About</a></li>
                <li>
                    <a href="service-2.html">Services <i class="fa-solid fa-chevron-down"></i></a>
                    <ul class="tn-dropdown">
                        <li><a href="service-mep.html">Integrated MEP</a></li>
                        <li><a href="service-electrical.html">Electrical Systems</a></li>
                        <li><a href="service-hvac.html">HVAC Engineering</a></li>
                        <li><a href="service-phe.html">Plumbing &amp; PHE</a></li>
                        <li><a href="service-fire.html">Fire Protection</a></li>
                        <li><hr></li>
                        <li><a href="service-2.html">All Services</a></li>
                    </ul>
                </li>
                <li><a href="project-1.html">Projects</a></li>
                <li>
                    <a href="#">Company <i class="fa-solid fa-chevron-down"></i></a>
                    <ul class="tn-dropdown">
                        <li><a href="team.html">Our Team</a></li>
                        <li><a href="faq.html">FAQ</a></li>
                        <li><a href="clients.html">Our Clients</a></li>
                        <li><a href="blog-1.html">Our Blog</a></li>
                    </ul>
                </li>
                <li><a href="contact.html">Contact Us</a></li>
            </ul>

            <!-- CTA -->
            <a href="contact.html" class="tn-cta">Let's Talk</a>
        </div>
    </div>"""

# ── New Mobile Nav HTML ───────────────────────────────────────────────────────
NEW_MOBILE_NAV = """    <!-- Mobile Nav -->
    <div class="mob-navbar" id="mobNavbar">
        <div class="mob-top">
            <div class="mob-logo">
                <a href="index.html">
                    <img src="assets/img/update new logo.png" alt="ADES logo">
                </a>
            </div>
            <button class="mob-hamburger" id="mobHamburger" aria-label="Toggle menu">
                <span></span><span></span><span></span>
            </button>
        </div>
        <div class="mob-menu" id="mobMenu">
            <div class="mob-menu-inner">
                <a href="index.html">Home</a>
                <a href="about-1.html">About</a>
                <a href="service-2.html">Services</a>
                <a href="project-1.html">Projects</a>
                <a href="team.html">Company</a>
                <a href="blog-1.html">Our Blog</a>
                <a href="contact.html">Contact Us</a>
                <a href="contact.html" class="mob-cta-btn">Let's Talk</a>
            </div>
        </div>
    </div>"""

# ── New JS for mobile hamburger + scroll ─────────────────────────────────────
NEW_JS = """    <script>
        // Mobile hamburger toggle
        (function(){
            var btn = document.getElementById('mobHamburger');
            var menu = document.getElementById('mobMenu');
            if(btn && menu){
                btn.addEventListener('click', function(){
                    btn.classList.toggle('open');
                    menu.classList.toggle('open');
                });
            }
            // Scroll shadow
            var nb = document.getElementById('topNavbar');
            if(nb){
                window.addEventListener('scroll', function(){
                    nb.classList.toggle('scrolled', window.scrollY > 10);
                });
            }
        })();
    </script>"""

# ── Regex patterns ────────────────────────────────────────────────────────────
OLD_STYLE_RE = re.compile(
    r'\s*<!--\s*Custom Glass Nav Style\s*-->\s*<style>.*?</style>',
    re.DOTALL
)
OLD_DESKTOP_NAV_RE = re.compile(
    r'\s*<!--\s*Desktop Glass Nav\s*-->\s*.*?(?=\s*<!--\s*Mobile Nav|$)',
    re.DOTALL
)
OLD_MOBILE_NAV_RE = re.compile(
    r'\s*<!--\s*Mobile Nav\s*-->\s*<div class="mobile-header">.*?</div>\s*</div>',
    re.DOTALL
)

# Script patterns for old menuBtn JS
OLD_MENUJS_RE = re.compile(
    r"var menuBtn\s*=.*?(?=\}\)\(\);|\}\);|\Z)",
    re.DOTALL
)
OLD_NAVSCROLL_RE = re.compile(
    r"window\.addEventListener\('scroll'.*?(?=\}\)\(\);|\}\);|\s*//|\Z)",
    re.DOTALL
)

html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]

updated, skipped = [], []

for fname in html_files:
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        src = f.read()

    # Skip files that don't have the old glass nav
    if 'glass-nav' not in src and 'Custom Glass Nav Style' not in src:
        skipped.append(fname + ' (no glass-nav found)')
        continue

    out = src

    # 1. Replace old <style> block
    out = OLD_STYLE_RE.sub('\n' + NEW_STYLE, out, count=1)

    # 2. Replace old Desktop Nav block (everything between <!-- Desktop Glass Nav --> … before <!-- Mobile Nav -->)
    out = re.sub(
        r'(\s*<!-- Desktop Glass Nav -->.*?)(?=\s*<!-- Mobile Nav -->)',
        '\n' + NEW_DESKTOP_NAV + '\n',
        out, count=1, flags=re.DOTALL
    )

    # 3. Replace old Mobile Nav block
    out = re.sub(
        r'\s*<!-- Mobile Nav -->.*?(?=\s*<!-- Header Section End -->|\s*<div id="smooth-wrapper">)',
        '\n' + NEW_MOBILE_NAV + '\n',
        out, count=1, flags=re.DOTALL
    )

    # 4. Remove old menuBtn JS if present
    out = re.sub(r'var menuBtn\s*=\s*document.*?menuBtn\.addEventListener.*?;\s*\}\);?', '', out, flags=re.DOTALL)

    # 5. Inject new JS before </body>
    if 'mobHamburger' not in out:
        out = out.replace('</body>', NEW_JS + '\n</body>', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(out)
    updated.append(fname)

print(f"\n✅ Updated {len(updated)} files:")
for f in sorted(updated): print(f"   - {f}")
print(f"\n⏭  Skipped {len(skipped)}:")
for f in sorted(skipped): print(f"   - {f}")
