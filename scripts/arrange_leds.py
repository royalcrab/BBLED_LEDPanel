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
        if mod.GetValue() == name:
            ref = mod.GetReference()
            res = re.match(r'\D+(\d+)',ref)
            #print ref
            if res:
                idx = int(res.group(1))-1
                my = (idx % y) * pitch_mm + ox
                if (idx // x) % 2 == 1:
                    my = (y - (idx % y) - 1) * pitch_mm + ox
                    if dir == 2 or dir == 3:
                        rot += 180

                mx = (idx // x) * pitch_mm + oy
                if dir == 1 or dir == 3:
                    tx = mx
                    mx = my
                    my = tx

                #print "idx = %s"%idx
                #print "x = %d"%mx
                #print "y = %d"%my
                mod.SetPosition(pcbnew.wxPointMM(mx,my))
                mod.SetOrientation(rot*10)

                if visible == False:
                    silk = mod.Reference()
                    silk.SetVisible(False)

    pcbnew.Refresh()
    
#arrange_leds("SK6812",10,10,10,0)
#arrange_leds("C0603",10,10,10,0,5,0,0)

#arrange_leds("SK6812MINI",16,16,6.25,2)
#arrange_leds("C0603",16,16,6.25,2,180,5,0)
