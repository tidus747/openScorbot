printerOffset = 0.4;

shaftDiameter = 4+printerOffset;
wheelDiameter = 32;
shaftMargin = 4;
shaftHeight = 7;
shaftBevel = 0;
wheelHeigh = 1;
wheelGrooveDepth = 0;

encoderInnerRadius = 9;
encoderOuterRadius = 15;
encoderSlitWidth = 1+printerOffset;
encoderSlitMargin = 3;
encoderSlitCount = 20;

shaftR = shaftDiameter/2;
wheelR = wheelDiameter/2;

putScrew = true;
screwDiameter = 1.15+printerOffset;

encoderSlitLength = encoderOuterRadius-encoderInnerRadius;



difference () {

	rotate_extrude($fn=200) polygon( points=[[shaftR,0],[wheelR,0],[wheelR-wheelGrooveDepth,wheelHeigh/2],[wheelR,wheelHeigh],[shaftR+shaftMargin,wheelHeigh],[shaftR+shaftMargin,shaftHeight],[shaftR+shaftBevel,shaftHeight],[shaftR,shaftHeight-shaftBevel]] );
	
	union() {
		for(i=[0:encoderSlitCount-1]) {
			rotate(a = [0,0,(360/encoderSlitCount)*i]) {
				translate(v=[0,encoderInnerRadius+(encoderSlitLength/2),wheelHeigh/2]) {
					cube(size = [encoderSlitWidth,encoderSlitLength,wheelHeigh+1],center = true);
				}
			}
		}
	}
    
    if(putScrew){
    rotate([90,0,0])
    translate([0,wheelHeigh+shaftHeight/2,-3])
    cylinder(h = shaftMargin+2+printerOffset, r1 = screwDiameter, $fa = 20, $fs = 0.1, r2 = screwDiameter, center = true);
    }
    
}



