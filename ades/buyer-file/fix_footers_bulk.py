import os
import re

directory = r"e:\ades rework\ades\buyer-file"
files = [f for f in os.listdir(directory) if f.endswith(".html")]

footer_standard = """<!-- Footer Section -->
<footer class="footer-area-four text-white">
    <div class="footer-wrapper p-5">
        <div class="container">
            <div class="row gy-4 text-start">
                <!-- Column 1: Company -->
                <div class="col-xl-3 col-lg-3 col-md-6">
                    <div class="footer-menu">
                        <h4 class="title text-white mb-4">Quick Links</h4>
                        <ul class="list-unstyled">
                            <li><a href="index.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Home</a></li>
                            <li><a href="about-1.html" class="text-white opacity-75 text-decoration-none d-block mb-2">About ADES</a></li>
                            <li><a href="service-2.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Services</a></li>
                            <li><a href="project-1.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Our Projects</a></li>
                            <li><a href="clients.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Our Clients</a></li>
                            <li><a href="faq.html" class="text-white opacity-75 text-decoration-none d-block mb-2">FAQ</a></li>
                            <li><a href="contact.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Contact Us</a></li>
                        </ul>
                    </div>
                </div>
                <!-- Column 2: Engineering -->
                <div class="col-xl-3 col-lg-3 col-md-6">
                    <div class="footer-menu">
                        <h4 class="title text-white mb-4">Engineering</h4>
                        <ul class="list-unstyled">
                            <li><a href="service-mep.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Integrated MEP</a></li>
                            <li><a href="service-electrical.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Electrical Systems</a></li>
                            <li><a href="service-hvac.html" class="text-white opacity-75 text-decoration-none d-block mb-2">HVAC Engineering</a></li>
                            <li><a href="service-phe.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Plumbing & PHE</a></li>
                            <li><a href="service-fire.html" class="text-white opacity-75 text-decoration-none d-block mb-2">Fire Protection</a></li>
                        </ul>
                    </div>
                </div>
                <!-- Column 3: Presence -->
                <div class="col-xl-3 col-lg-3 col-md-6">
                    <div class="footer-menu">
                        <h4 class="title text-white mb-4">Our Presence</h4>
                        <ul class="list-unstyled">
                            <li class="text-white opacity-75 mb-2"><strong>Chennai</strong> (HQ)</li>
                            <li class="text-white opacity-75 mb-2"><strong>Coimbatore</strong></li>
                            <li class="text-white opacity-75 mb-2"><strong>Trichy</strong></li>
                            <li class="text-white opacity-75 mb-2"><strong>Tirupattur</strong></li>
                            <li class="text-white opacity-75 mb-2"><strong>UAE</strong> (Middle East)</li>
                        </ul>
                    </div>
                </div>
                <!-- Column 4: Contact -->
                <div class="col-xl-3 col-lg-3 col-md-6">
                    <div class="footer-contact">
                        <h4 class="title text-white mb-4">Get In Touch</h4>
                        <p class="text-white opacity-75">No. 19, 2nd Cross Street, Lake Area, Nungambakkam, Chennai - 34<br>info@ades.pro<br>+91-44-4265 8822</p>
                    </div>
                </div>
            </div>
            <div class="row pt-4 mt-4" style="border-top: 1px solid rgba(255,255,255,0.1);">
                <div class="col-12 text-center">
                    <p class="mb-0 small opacity-50">&copy; 2026 ADES - Engineering Excellence. All rights reserved.</p>
                </div>
            </div>
        </div>
    </div>
</footer>"""

def fix_footer(content):
    # This regex looks for the FIRST <footer> or <!-- Footer and replaces EVERYTHING until it hits the script section
    # Special care for the "Double Footer" case in index.html and others
    
    # 1. Clean up potential double footer starts
    content = re.sub(r'<footer class="footer-area-four pt-80">[\s\S]*?<footer', '<footer', content)
    
    # 2. Main Footer Replacement
    # We target the footer area and its contents, ending before the closing tags of wrappers/body
    pattern = re.compile(r'(?:<!-- Footer Section -->\s*)?<footer[\s\S]*?</footer>', re.IGNORECASE)
    
    # If there are multiple footers, this will replace each with the standard (handled by sub)
    # But usually we want to replace the whole block from the first footer to the last footer
    
    all_footers = list(pattern.finditer(content))
    if not all_footers:
        return content
    
    first_start = all_footers[0].start()
    last_end = all_footers[-1].end()
    
    new_content = content[:first_start] + footer_standard + content[last_end:]
    return new_content

for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = fix_footer(content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed footer in {filename}")

print("Site-wide footer standardization complete.")
