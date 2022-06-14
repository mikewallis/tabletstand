#!/usr/bin/python

import drawSvg as draw

# set sizes - really ratios - in px, z is thickness of the card
x=210
y=297
z=3
d = draw.Drawing(x, y, displayInline=False)
# bounding box
r = draw.Rectangle(0,0,x,y, stroke='#1248ff', fill='none')
d.append(r)

# main cut/fold line
d.append(draw.Lines(0, (y/5)*3,
                    (x/10)-(x/20),(y/5)*3,
                    (x/10)-(x/20),((y/5)*3)+z,
                    (x/10)+(x/20),((y/5)*3)+z,
                    (x/10)+(x/20),(y/5)*3,
                    (x/5), (y/5)*3, close=False, fill='none', stroke='red'))
d.append(draw.Line((x/5), (y/5)*3, (x/5), (y/5)*2,fill='none', stroke='red'))
d.append(draw.Line((x/5), (y/5)*2, (x/5)*4, (y/5)*2,fill='none', stroke='green'))
d.append(draw.Line((x/5)*4, (y/5)*2, (x/5)*4, (y/5)*3,fill='none', stroke='red'))
d.append(draw.Lines((x/5)*4, (y/5)*3, 
                    (x/10)*9-(x/20),(y/5)*3,
                    (x/10)*9-(x/20),((y/5)*3)+z,
                    (x/10)*9+(x/20),((y/5)*3)+z,
                    (x/10)*9+(x/20),(y/5)*3,
                    x, (y/5)*3,close=False, fill='none', stroke='red'))

# stand
d.append(draw.Lines((x/2)-(x/16),y-(y/10),
                    (x/2)-(x/16),y-(y/2),
                    (x/2)-(x/32),y-(y/2),
                    (x/2)-(x/32),y-(y/2)-z,
                    (x/2)+(x/32),y-(y/2)-z,
                    (x/2)+(x/32),y-(y/2),
                    (x/2)+(x/16),y-(y/2),
                    (x/2)+(x/16),y-(y/10), 
                    fill='none', stroke='red'))

d.append(draw.Line((x/2)-(x/16),y-(y/10),(x/2)+(x/16),y-(y/10), 
                    fill='none', stroke='green'))

# scores for nurdles

d.append(draw.Line(0,(y/20)*11,(x/5),(y/20)*11,stroke='green'))
d.append(draw.Line(0,(y/20)*10,(x/5),(y/20)*10,stroke='green'))
d.append(draw.Line((x/5)*4,(y/20)*11,x,(y/20)*11,stroke='green'))
d.append(draw.Line((x/5)*4,(y/20)*10,x,(y/20)*10,stroke='green'))

# cutout for tabs
#left
d.append(draw.Lines((x/10)-(x/20),(y/20)*9,
                    (x/10)-(x/20),((y/20)*9)+z,
                    (x/10)+(x/20),((y/20)*9)+z,
                    (x/10)+(x/20),(y/20)*9,
                    fill='none',stroke='red',close='yes'))
#right
d.append(draw.Lines((x/10)*9-(x/20),(y/20)*9,
                    (x/10)*9-(x/20),((y/20)*9)+z,
                    (x/10)*9+(x/20),((y/20)*9)+z,
                    (x/10)*9+(x/20),(y/20)*9,
                    fill='none',stroke='red',close='yes'))
#stand
d.append(draw.Lines((x/2)-(x/32),(y/10),
                   (x/2)+(x/32),(y/10),
                   (x/2)+(x/32),(y/10)+z,
                   (x/2)-(x/32),(y/10)+z,
                   fill='none',stroke='red',close='yes'))
# instructions
d.append(draw.Text('tablet/phone stand for card sized '+str(x)+'x'+str(y)+'px', 7, 10, y-(y/20)))
d.append(draw.Text('print on heavy card', 7, 10, 40, fill='black',font='verdana'))
d.append(draw.Text('Cut on red', 7, 10, 30, fill='red',font='monospace'))  
d.append(draw.Text('Score on green (both sides)', 7, 10, 20, fill='green',font='monospace'))  
d.append(draw.Text('fold tabs into cutouts',7, 10, 10, fill='black'))
#d.setPixelScale(2)  # Set number of pixels per geometry unit

d.saveSvg('stand'+str(x)+'x'+str(y)+'.svg')
