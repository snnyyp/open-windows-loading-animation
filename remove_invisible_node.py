from lxml import etree
import os
import glob

svg_dirs = [
    r"H:\open-windows-loading-animation\SVG SEQUENCE\fluent11-svg-sequence",
    r"H:\open-windows-loading-animation\SVG SEQUENCE\fluent11_30fps_-svg-sequence",
    r"H:\open-windows-loading-animation\SVG SEQUENCE\metro8-svg-sequence",
    r"H:\open-windows-loading-animation\SVG SEQUENCE\metro8_30fps-svg-sequence",
    r"H:\open-windows-loading-animation\SVG SEQUENCE\metro8_inf-svg-sequence",
    r"H:\open-windows-loading-animation\SVG SEQUENCE\metro8_inf_30fps-svg-sequence",
]

for svg_dir in svg_dirs:
    files = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))

    for path in files:
        tree = etree.parse(path)

        for elem in tree.xpath('//*[@style]'):
            style = elem.attrib["style"].replace(" ", "")
            
            if "display:none" in style:
                parent = elem.getparent()

                if parent is not None:
                    parent.remove(elem)

        tree.write(path)
