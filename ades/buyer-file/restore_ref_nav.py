"""
Replaces the custom top-bar navbar in all buyer-file HTML files
with the native theme header-3 navbar from reference.html,
substituting ADES logo and links.
"""

import os, re

BASE        = r"e:\ades rework\ades rework\ades\buyer-file"
REF_FILE    = r"e:\ades rework\ades rework\ades\reference.html"

# ── The ADES-branded header to inject (native theme structure) ────────────────
ADES_HEADER = """    <!-- Header Section Start -->
    <header class="header-section">
        <div id="header-sticky" class="header-3">
            <div class="container-fluid">
                <div class="mega-menu-wrapper">
                    <div class="header-main">
                        <div class="logo">
                            <a href="index.html" class="header-logo-2">
                                <img src="assets/img/update new logo.png" alt="ADES logo" style="height:40px;width:auto;">
                            </a>
                        </div>

                        <div class="header-left">
                            <div class="mean__menu-wrapper">
                                <div class="main-menu">
                                    <nav id="mobile-menu">
                                        <ul>
                                            <li>
                                                <a href="index.html">Home</a>
                                            </li>
                                            <li>
                                                <a href="about-1.html">About</a>
                                            </li>
                                            <li class="has-dropdown">
                                                <a href="service-2.html">
                                                    Services <i class="fa-solid fa-chevron-down"></i>
                                                </a>
                                                <ul class="submenu">
                                                    <li><a href="service-mep.html">Integrated MEP</a></li>
                                                    <li><a href="service-electrical.html">Electrical Systems</a></li>
                                                    <li><a href="service-hvac.html">HVAC Engineering</a></li>
                                                    <li><a href="service-phe.html">Plumbing &amp; PHE</a></li>
                                                    <li><a href="service-fire.html">Fire Protection</a></li>
                                                    <li><a href="service-2.html">All Services</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="project-1.html">Projects</a>
                                            </li>
                                            <li class="has-dropdown">
                                                <a href="#">
                                                    Company <i class="fa-solid fa-chevron-down"></i>
                                                </a>
                                                <ul class="submenu">
                                                    <li><a href="team.html">Our Team</a></li>
                                                    <li><a href="faq.html">FAQ</a></li>
                                                    <li><a href="clients.html">Our Clients</a></li>
                                                    <li><a href="blog-1.html">Our Blog</a></li>
                                                </ul>
                                            </li>
                                            <li>
                                                <a href="contact.html">Contact Us</a>
                                            </li>
                                        </ul>
                                    </nav>
                                </div>
                            </div>
                        </div>

                        <div class="header-right d-flex justify-content-end align-items-center">
                            <div class="header__hamburger">
                                <div class="sidebar__toggle">
                                    <div class="header-bar">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
                                            <path d="M19.375 5H0.625C0.45924 5 0.300269 4.93415 0.183058 4.81694C0.065848 4.69973 0 4.54076 0 4.375C0 4.20924 0.065848 4.05027 0.183058 3.93306C0.300269 3.81585 0.45924 3.75 0.625 3.75H19.375C19.5408 3.75 19.6997 3.81585 19.8169 3.93306C19.9342 4.05027 20 4.20924 20 4.375C20 4.54076 19.9342 4.69973 19.8169 4.81694C19.6997 4.93415 19.5408 5 19.375 5Z" fill="currentColor"/>
                                            <path d="M19.375 11.25H0.625C0.45924 11.25 0.300269 11.1842 0.183058 11.0669C0.065848 10.9497 0 10.7908 0 10.625C0 10.4592 0.065848 10.3003 0.183058 10.1831C0.300269 10.0658 0.45924 10 0.625 10H19.375C19.5408 10 19.6997 10.0658 19.8169 10.1831C19.9342 10.3003 20 10.4592 20 10.625C20 10.7908 19.9342 10.9497 19.8169 11.0669C19.6997 11.1842 19.5408 11.25 19.375 11.25Z" fill="currentColor"/>
                                            <path d="M19.375 17.5H0.625C0.45924 17.5 0.300269 17.4342 0.183058 17.3169C0.065848 17.1997 0 17.0408 0 16.875C0 16.7092 0.065848 16.5503 0.183058 16.4331C0.300269 16.3158 0.45924 16.25 0.625 16.25H19.375C19.5408 16.25 19.6997 16.3158 19.8169 16.4331C19.9342 16.5503 20 16.7092 20 16.875C20 17.0408 19.9342 17.1997 19.8169 17.3169C19.6997 17.4342 19.5408 17.5 19.375 17.5Z" fill="currentColor"/>
                                        </svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <!-- Header Section End -->"""

# ── Patterns to strip out everything we previously injected ──────────────────

# Remove old custom inline <style> block for nav
OLD_STYLE_RE = re.compile(
    r'\s*<!-- (?:Top-Bar Nav Style|Custom Glass Nav Style) -->\s*<style>.*?</style>',
    re.DOTALL
)

# Remove Desktop + Mobile custom nav blocks
OLD_DESKTOP_RE = re.compile(
    r'\s*<!-- Desktop Top-Bar Nav -->.*?</div>\s*(?=<!-- Mobile Nav -->|<!-- Header Section|<div id="smooth-wrapper">)',
    re.DOTALL
)
OLD_MOBILE_RE = re.compile(
    r'\s*<!-- Mobile Nav -->.*?(?=<!-- Header Section End -->|<div id="smooth-wrapper">)',
    re.DOTALL
)

# Remove our injected script block
OLD_SCRIPT_RE = re.compile(
    r'\s*<script>\s*// Mobile hamburger toggle.*?</script>',
    re.DOTALL
)

# Remove body padding-top we added
OLD_PADDING_RE = re.compile(r'\s*body\s*\{\s*padding-top:\s*\d+px;\s*\}', re.DOTALL)

# ── Process each HTML file ───────────────────────────────────────────────────
html_files = [f for f in os.listdir(BASE) if f.endswith('.html')]
updated, skipped = [], []

for fname in sorted(html_files):
    fpath = os.path.join(BASE, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        src = f.read()

    # Only touch files that have our custom nav injected
    if 'top-navbar' not in src and 'Top-Bar Nav Style' not in src:
        skipped.append(fname + ' (no custom nav found)')
        continue

    out = src

    # 1. Remove old custom <style> block
    out = OLD_STYLE_RE.sub('', out)

    # 2. Remove old desktop nav div
    out = OLD_DESKTOP_RE.sub('', out)

    # 3. Remove old mobile nav div
    out = OLD_MOBILE_RE.sub('', out)

    # 4. Remove old injected script
    out = OLD_SCRIPT_RE.sub('', out)

    # 5. Inject ADES header right before <!-- Header Section End --> or before smooth-wrapper
    if '<!-- Header Section End -->' in out:
        out = out.replace('<!-- Header Section End -->', ADES_HEADER + '\n')
    elif '<div id="smooth-wrapper">' in out:
        out = out.replace('<div id="smooth-wrapper">', ADES_HEADER + '\n\n    <div id="smooth-wrapper">', 1)
    else:
        # Fallback: inject after offcanvas overlay
        out = out.replace('<div class="offcanvas__overlay"></div>',
                          '<div class="offcanvas__overlay"></div>\n\n' + ADES_HEADER, 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(out)
    updated.append(fname)

print(f"\n✅ Updated {len(updated)} files:")
for f in updated: print(f"   - {f}")
print(f"\n⏭  Skipped {len(skipped)}:")
for f in skipped: print(f"   - {f}")
