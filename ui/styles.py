# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

"""
styles.py

Created by Shawn on 2010-06-15.
"""
from PyQt4.QtGui import QColor

# Slice Sizing
SLICE_HELIX_RADIUS = 15
SLICE_HELIX_STROKE_WIDTH = 0.5
SLICE_HELIX_HILIGHT_WIDTH = 2.5

# Slice Colors
bluefill = QColor(153, 204, 255)  # 99ccff
bluestroke = QColor(0, 102, 204)  # 0066cc
bluishstroke = QColor(0, 182, 250)  # 
orangefill = QColor(255, 204, 153)  # ffcc99
orangestroke = QColor(204, 102, 51)  # cc6633
lightorangefill = QColor(255, 234, 183)
lightorangestroke = QColor(234, 132, 81)
grayfill = QColor(238, 238, 238)  # eeeeee (was a1a1a1)
graystroke = QColor(102, 102, 102)  # 666666 (was 424242)

# Path Sizing
PATHHELIXHANDLE_RADIUS = 30
PATHHELIXHANDLE_STROKE_WIDTH = 2
PATH_BASE_WIDTH = 20  # used to size bases (grid squares, handles, etc)
PATH_HELIX_HEIGHT = 2 * PATH_BASE_WIDTH  # staple + scaffold
PATH_HELIX_PADDING = 50 # gap between PathHelix objects in path view
PATH_GRID_STROKE_WIDTH = 0.5
SLICE_HANDLE_STROKE_WIDTH = 1
PATH_STRAND_STROKE_WIDTH = 2
PATH_SELECTBOX_STROKE_WIDTH = 1.5
PCH_BORDER_PADDING = 1
PATH_BASE_HL_STROKE_WIDTH = 2  # PathTool highlight box
MINOR_GRID_STROKE_WIDTH = 0.5
MAJOR_GRID_STROKE_WIDTH = 0.5

# Path Drawing
PATH_XOVER_LINE_SCALE_X = 0.035
PATH_XOVER_LINE_SCALE_Y = 0.035

# Path Colors
minorgridstroke = QColor(153, 153, 153)  # 999999
majorgridstroke = QColor(51, 51, 51)  # 333333
scafstroke = QColor(0, 102, 204)  # 0066cc
handlefill = QColor(0, 102, 204)  # 0066cc
pch_scaf_stroke = QColor(0, 102, 204, 153)
pch_stap_stroke = QColor(204, 0, 0, 153)
pch_disab_stroke = QColor(204, 204, 204, 255)
redstroke = QColor(204, 0, 0)
erasefill = QColor (255, 0, 0, 63)
forcefill = QColor (0, 255, 255, 63)
breakfill = QColor (255, 0, 0, 255)
colorbox_fill = QColor(204, 0, 0)
colorbox_stroke = QColor(102, 102, 102)
stapleColors = [QColor(204, 0, 0),\
                QColor(247, 67, 8),\
                QColor(247, 147, 30),\
                QColor(170, 170, 0),\
                QColor(87, 187, 0),\
                QColor(0, 114, 0),\
                QColor(3, 182, 162),\
                QColor(23, 0, 222),\
                QColor(115, 0, 222),\
                QColor(184, 5, 108),\
                QColor(51, 51, 51)]

#layer limits
ZACTIVESLICEHANDLE = -12
ZPATHHELIXGROUP = -10
ZPATHHELIX = -5
ZSLICEHELIX = -1.0
ZPREXOVERHANDLE = .9
ZXOVERHANDLEPAIR = 1
ZFOCUSRING = 0.0
ZBREAKPOINTHANDLE = 2
ZLOOPHANDLE = 2
ZSKIPHANDLE = 2
ZPATHTOOL = 3
ZBREAKITEM = 2


# Overwrite for Maya
# majorgridstroke = QColor(255, 255, 255)  # ffffff for maya

