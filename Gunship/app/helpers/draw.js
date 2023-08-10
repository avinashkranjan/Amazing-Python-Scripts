(function(){
	// Helper method to draw a shape from an array of points
	window.drawShape = function(ctx, points, tx, mirror, stroke, fill){
		ctx.beginPath();
		ctx.moveTo(tx.x+points[0][0], tx.y+points[0][1]);
		
		// Draw the path
		var numPoints = points.length;
		var i;
		for(i=1; i<numPoints; ++i){
			ctx.lineTo(tx.x+points[i][0], tx.y+points[i][1]);
		}
		
		// If mirror is true then run through the points again and draw a
		// mirrored version
		if(mirror == true){
			for(i=numPoints-1; i>-1; --i){
				ctx.lineTo(tx.x+(-points[i][0]), tx.y+points[i][1]);
			}
		}
		
		// Apply line styles
		if(fill == true) ctx.fill();
		if(stroke == true) ctx.stroke();
	}
	
	// Helper function for drawing circles
	window.drawCircle = function(ctx, x, y, r, stroke, fill){
		ctx.beginPath();
		ctx.arc(x, y, r, 0, 2*Math.PI);
		
		if(fill == true) ctx.fill();
		if(stroke !== false) ctx.stroke();
	}
	
	window.drawGradientCircle = function(ctx, x, y, r, color, opacity){
		ctx.beginPath();
		var gradient = ctx.createRadialGradient(x, y, 5, x, y, r);
		gradient.addColorStop(0, 'rgba('+color+', '+opacity+')');
		gradient.addColorStop(0.5, 'rgba('+color+', '+opacity+')');
		gradient.addColorStop(1, 'rgba('+color+', 0)');
		ctx.fillStyle = gradient;
		
		ctx.arc(x, y, r, 0, 2*Math.PI);
		ctx.fill();
	}
	
	// Helper function for drawing arcs
	window.drawArc = function(ctx, x, y, rotation, start, end){
		ctx.beginPath();
		ctx.arc(x, y, rotation, start, end);
		ctx.stroke();
	}
	
	// Helper function to draw a grid in a bounding box
	window.drawGrid = function(ctx, options){
		var bounds = options.bounds;
		var step = options.step;
		var offset = options.offset;
		var verticalSteps = Math.floor(bounds.bottom / step);
		
		ctx.lineWidth = 1;
		ctx.strokeStyle = 'rgba(80, 80, 80, 1)';
		ctx.beginPath();
		
		var y;
		for(var i=0; i<verticalSteps; ++i){
			y = i*step + offset;
			ctx.moveTo(bounds.left, y);
			ctx.lineTo(bounds.right, y);
		}
		ctx.stroke();
	}
	
	// Draw a line of text
	window.drawTextLine = function(ctx, text, x, y){
		ctx.fillStyle = 'rgba(255, 255, 255, 1)';
		ctx.fillText(text, x, y);
	}
	
	// Draw a paragraph of text
	window.drawParagraph = function(ctx, para, x, y, textAlign){
		if(textAlign == undefined) textAlign = 'left';
		var headingX = x;
		switch(textAlign){
			case 'left' :
				x -= 200;
				headingX = x - 20;
				break;
		}
		
		ctx.textAlign = textAlign
		ctx.font = '18px Arial';
		drawTextLine(ctx, para[0], headingX, y);
		
		y += 10;
		ctx.font = '14px Arial';
		for(var i=1; i<para.length; ++i){
			drawTextLine(ctx, para[i], x, y+(20*i));
		}
	}
})();