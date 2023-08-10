(function(){
	window.Background = function(options){
		var self = this;
		
		options = options || {};
		self.width = options.width || 400;
		self.height = options.height || 400;
		
		self.offset = 0;
		
		self.update = function(frameTime, delta){
			self.offset += delta;
			if(self.offset > 50)
				self.offset -= 50;
		}
		
		// Draw the background rect
		self.draw = function(ctx){
			var width = self.width;
			var height = self.height;
			
			ctx.fillStyle = '#000';
			ctx.fillRect(0, 0, width, height);
			
			// Draw a grid on the bg
			drawGrid(ctx, {
				bounds: {
					top: 0,
					right: width,
					bottom: height,
					left: 0
				},
				step: 50,
				offset: self.offset
			});
		}
	}
})();