set bg_rgb,[1,1,1]
load /Users/Song/sastbx/gui/sasqt/sastbx_examples/shapeup/output/bio32m5_1JSG.ccp4, map1
isomesh m1,map1,0.0988425566949
color blue, m1
png maps_5_view1
turn x, 90
png maps_5_view2
turn x,-90
turn y,90
png maps_5_view3
