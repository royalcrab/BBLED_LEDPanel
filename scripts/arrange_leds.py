# MIT Lisence 
# 2020,2021
# 
# Created by BBLED : https://bbled.org/
# Powered by mplusplus Co.Ltd : http://www.mplpl.com
# github: https://github.com/royalcrab/BBLED_LEDPanel

import pcbnew
import re

# name    : "SK6812MINI", "C0603", "0.1uF", "etc"
# x       : length of the column
# y       : length of the raw
# pitch_mm: pitch between each pair of parts
# dir     : 0/2 virtical, 1/3 horizontal, 2,3 reverse in even raws or columns
# ox      : offset x
# oy      : offset y
# visible : visibility of reference silk

def arrange_leds(name,x,y,pitch_mm,dir=0,rot=0,ox=0,oy=0,visible=False):
    board = pcbnew.GetBoard()
    mods = board.GetModules()

    for mod in mods:
        r = rot
        if mod.GetValue() == name:
            ref = mod.GetReference()
            res = re.match(r'\D+(\d+)',ref)
            #print ref
            if res:
                idx = int(res.group(1))-1
                my = (idx % y) * pitch_mm
                if (idx // x) % 2 == 1:
                    my = (y - (idx % y) - 1) * pitch_mm
                else:
                    if (dir == 2 or dir == 3):
                        r += 180

                mx = (idx // x) * pitch_mm
                if dir == 1 or dir == 3:
                    tx = mx
                    mx = my
                    my = tx

                mx += ox
                my += oy

                #print "idx = %s"%idx
                #print "x = %d"%mx
                #print "y = %d"%my
                mod.SetPosition(pcbnew.wxPointMM(mx,my))
                mod.SetOrientation(r*10)

                if visible == False:
                    silk = mod.Reference()
                    silk.SetVisible(False)

    pcbnew.Refresh()
   

#arrange_leds("BBLED_SK6812MINI",16,16,6.25,3)
#arrange_leds("0.1uF",16,16,6.25,3,180,0,3)

