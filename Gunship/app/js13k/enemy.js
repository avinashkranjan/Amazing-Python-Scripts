(function(){
	window.Enemy = function(options){
		window.Enemy.instances.push(this);
		
		var self = this;
		
		self.x = options.x;
		self.y = options.y;
		self.bounds = options.bounds;
		self.speed = options.speed || 1.5;
		
		self.escaped = options.escaped;
		self.health = self.originalHealth = options.health || 1;
		
		var color;
		switch(self.health){
			case 2 :
				// Green
				color = [0, 255, 0];
				break;
			case 3 :
				// Blue
				color = [117, 223, 255];
				break;
			case 4 :
				// Purple
				color = [186, 66, 186];
				break;
			case 5 :
				// Red
				color = [255, 43, 43];
				break;
			default :
				color = [255, 255, 255];
		}
		self.color = color;
		self.colorRGBA = 'rgba('+color[0]+', '+color[1]+', '+color[2]+', 1)'
		
		self.update = function(frameTime, delta){
			var bounds = self.bounds;
			var y = self.y += (self.speed * delta);
			
			// If we have traveled out of bounds then call the escaped callback
			// and remove to remove from the game loop and clean up references.
			if(y < bounds.top || y > bounds.bottom){
				if(self.escaped) self.escaped();
				self.health = 0;
				self.destroy();
			}
		}
		
		self.draw = function(ctx){
			ctx.lineWidth = self.health;
			ctx.strokeStyle = self.colorRGBA;
			drawCircle(ctx, self.x, self.y, (12-self.originalHealth)+self.health);
		}
		
		// Rect is based on health - the more health layers we have
		// the bigger the hit area.
		self.getRect = function(){
			var radius = (12 - self.originalHealth) + (self.health*2);
			return {
				top: self.y - radius,
				right: self.x + radius,
				bottom: self.y + radius,
				left: self.x - radius 
			}
		}
		
		// Apply damage to the enemy. Returns true if the enemy
		// was killed in the process, false if not.
		self.damage = function(options){
			
			// Remove damage from our health
			self.health -= options.damage;
			
			// Trigger ane explosion
			self.explode(options);
			
			// Destroy and return true if we were destroyed by the
			// damage.
			if(self.health <= 0){
				self.destroy();
				return true;
			}
			
			// If we get this far then retrn false as we're still
			// alive
			return false;
		}
		
		// Fire an explosion from the enemy
		self.explode = function(options){
			if(options.angleVariation === undefined)
				options.angleVariation = 2;
			for(var i=0; i<10; ++i){
				self.assetList.add(new Particle({
					x: options.x,
					y: options.y,
					speed: options.speed,
					speedVariation: 2.5,
					angle: options.angle,
					angleVariation: options.angleVariation,
					bounds: self.bounds,
					color: self.color
					,life: 500
				}));
			}
		}
		
		self.destroy = function(){
			
			// Draw an explosion for each point of health - more
			// health = more particles. If we've been damaged down
			// to zero from bullets then health will be zero already.
			for(var i=0; i<self.health; ++i){
				self.explode({
					x: self.x,
					y: self.y,
					speed: 5,
					angle: 0,
					angleVariation: 6.28
				});
			}
			
			// Remove from the Enemy instances array and from the
			// asset list
			window.Enemy.instances.splice(window.Enemy.instances.indexOf(self), 1);
			self.assetList.remove(self);
			
			for(var k in self){
				delete self[k];
			}
		}
	}
	window.Enemy.instances = [];
})();