import gdspy
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import os

gds_file = gdspy.GdsLibrary().read_gds('nand2.gds2')
bbox = gds_file.top_level()

if not os.path.exists('svg_layer'):
    os.makedirs('svg_layer')

for i, layer in enumerate(bbox):
    layer.write_svg(f'svg_layer/layer{i}.svg')

svg_files = os.listdir('svg_layer')

if not os.path.exists('png_layer'):
    os.makedirs('png_layer')

for svg in svg_files:
    rlg = svg2rlg('svg_layer/' + svg)
    renderPM.drawToFile(rlg, 'png_layer/' + svg.rstrip('.gds') + '.png')

gdspy.LayoutViewer(cells=bbox)




