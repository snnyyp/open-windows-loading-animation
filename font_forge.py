import fontforge
import os
import glob
import psMat


svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\fluent11-svg-sequence'
svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\fluent11_30fps-svg-sequence'
svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\metro8-svg-sequence'
svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\metro8_30fps-svg-sequence'
svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\metro8_inf-svg-sequence'
svg_dir = r'H:\open-windows-loading-animation\SVG SEQUENCE\metro8_inf_30fps-svg-sequence'
start = 0xE000

font = fontforge.activeFont()
# font = fontforge.font()

font.encoding = 'UnicodeFull'
font.em = 2048
font.ascent = font.em
font.descent = 0
font.os2_typolinegap = 0
font.hhea_linegap  = 0

files = sorted(glob.glob(os.path.join(svg_dir.replace('_30fps', ''), '*.svg')))

if '_30fps' in svg_dir:
    files = files[::2]

for i, path in enumerate(files):
    code = start + i

    glyph = font.createChar(code)

    glyph.importOutlines(path)
    glyph.removeOverlap()
    glyph.round()
    glyph.width = font.em
    # glyph.comment = path
