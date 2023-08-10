(function(){
	
	var TARGET_DELTA = 60/1000;
	var getTime = function(){
		if(window.performance && window.performance.now){
			return performance.now();
		}else{
			return (new Date()).getTime();
		}
	}
	
	// A collection for managing assets in the game loop.
	var AssetList = function(){
		var self = this;
		
		self._assets = [];
		
		// Add an asset
		self.add = function(asset){
			asset.assetList = self;
			self._assets.push(asset);
			return asset;
		}
		
		// Remove an asset
		self.remove = function(asset){
			var i = self._assets.indexOf(asset);
			if(i > -1)
				self._assets.splice(i, 1);
			return asset;
		}
		
		// Update all assets
		self.update = function(frameTime, delta){
			self._assets.forEach(function(asset){
				if(asset.update)
					asset.update(frameTime, delta);
			});
		}
		
		// Draw all assets
		self.draw = function(ctx){
			self._assets.forEach(function(asset){
				if(asset.draw)
					asset.draw(ctx);
			});
		}
	};
	
	window.GameLoop = function(options){
		var self = this;
		
		// Extend this with options passed in
		extend(self, options);
		
		self.ctx = self.canvas.getContext('2d');
		self.width = self.canvas.width;
		self.height = self.canvas.height;
		
		self._running = false;
		self.paused = false;
		
		self._lastUpdate = getTime();
		
		// Start the game loop
		// Initialize the game and queue an update to start the loop
		self.run = function(){
			
			self.assets = new AssetList();
			
			// Only initialize and start the update loop if this
			// if the first time we've run up.
			if(!self._running){
				
				// Call initialize and wait for the start() callback
				// before setting up game assets.
				self.initialize(self.assets, function(){
					self.setupGameAssets(self.assets);
					self._setup = true;
				});
				
				self._running = true;
				self._queueUpdate();
			}else{
				self.setupGameAssets(self.assets);
			}
		}
		
		// Pause the game loop
		self.pause = function(pause){
			self.paused = pause;
		}
		
		// Queue an update
		self._queueUpdate = function(){
			setTimeout(self._update, 0);
		}
		
		// Queue a draw
		self._queueDraw = function(){
			if(window.requestAnimationFrame){
				window.requestAnimationFrame(self._draw);
			}else{
				window.setTimeout(self._draw, 1000/60)
			}
		}
		
		// Update game logic
		self._update = function(){
			var now = getTime();
			var frameTime = now - self._lastUpdate;
			var delta = TARGET_DELTA * frameTime;
			self._lastUpdate = now;
			
			// Update each game asset and the passed in callback
			// If the game is paused then we don't update assets,
			// but we do still draw them.
			if(!self.paused){
				self.assets.update(frameTime, delta);
				if(self._setup){
					self.update(frameTime, delta);
				}
			}
			
			//TODO: Clear pressed keys from the input manager
			
			// Queue the next draw
			self._queueDraw();
		}
		
		// Draw a frame
		self._draw = function(now){
			
			// Draw each game asset and update the passed in callback
			self.assets.draw(self.ctx);
			self.draw();
			
			// Queue the next update
			self._queueUpdate();
		}
	}
})();