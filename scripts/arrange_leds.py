# MIT Lisence 
# 2020,2021
# 
# Created by BBLED : https://bbled.org/
# Powered by mplusplus Co.Ltd : http://www.mplpl.com
# github: https://github.com/royalcrab/kicad-ledpanel

import pcbnew
import re

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
                mx = (idx // x) * pitch_mm + oy
                if dir != 0:
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
    
#arrange_leds("SK6812",16,16,10,0)
#arrange_leds("C",16,16,10,5,0,0,0)
