(function(){
	window.FrameTimer = function(options){
		var self = this;
		
		self._frames = [];
		self._graph = [];
		self._fps = 0;
		self.bounds = options.bounds;
		
		// History array of delta values passed into update()
		self._deltaHistory = [];
		
		// History array ms between calls to draw()
		self._drawHistory = [];
		self._lastDraw = 0;
		
		// Calculates FPS by sampling previous frames. Keep trask of the last 30
		// frameTime values, when we have 30 we take the average and use it to
		// calculate the frame rate.
		self.update = function(frameTime, delta){
			self._deltaHistory.push(delta);
			if(self._deltaHistory.length > self.bounds.right) self._deltaHistory.shift();
		}
		
		self.draw = function(ctx){
			
			// Work out and store how long it's been since the last draw
			var now = performance.now();
			var ms = now - self._lastDraw;
			self._drawHistory.push(ms);
			if(self._drawHistory.length > self.bounds.right) self._drawHistory.shift();
			self._lastDraw = now;
			
			// Draw the two graphs the full width of the bounds
			self.drawGraph(ctx, self._drawHistory, 'rgba(255, 0, 0, 0.5)');
			self.drawGraph(ctx, self._deltaHistory, 'rgba(0, 255, 0, 0.5)');
		}
		
		self.drawGraph = function(ctx, graph, color){
			var points = [];
			for(var i=0; i<graph.length; ++i){
				points.push([i, 50-graph[i]]);
			}
			ctx.strokeStyle = color;
			if(points.length){
				drawShape(ctx, points, {x: self.bounds.right-graph.length, y: 0}, false, true);
			}
		}
	}
})();