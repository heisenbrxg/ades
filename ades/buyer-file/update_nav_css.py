import os

css_path = r"e:\ades rework\ades rework\ades\buyer-file\assets\css\style-6.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n\n/* ── Navbar Size Adjustments ── */\n")
    f.write(".header-section .header-3 .main-menu ul li > a {\n")
    f.write("    font-size: 18px !important;\n")
    f.write("}\n")
    f.write(".header-section .header-3 .main-menu ul li .submenu li a {\n")
    f.write("    font-size: 16px !important;\n")
    f.write("}\n")
    f.write(".header-section .header-3 .logo img {\n")
    f.write("    height: 55px !important;\n")
    f.write("}\n")
    f.write(".sticky.header-3 .logo img {\n")
    f.write("    height: 50px !important;\n")
    f.write("}\n")

print("Added navbar font and logo sizing to style-6.css")
