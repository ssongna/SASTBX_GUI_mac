set bg_rgb,[1,1,1]
load querym8_1Z1S.ccp4, map1
isomesh m1,map1,0.092504799013
color blue, m1
png maps_8_view1
turn x, 90
png maps_8_view2
turn x,-90
turn y,90
png maps_8_view3
