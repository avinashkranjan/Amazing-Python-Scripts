(function(){
	window.Bullet = function(options){
		window.Bullet.instances.push(this);
		
		var self = this;
		
		self.x = options.x;
		self.y = options.y;
		self.speedVariation = options.speedVariation || 0;
		self.angleVariation = options.angleVariation || 0;
		self.bounds = options.bounds;
		
		// Add the angle variation
		var angleAdjust = (Math.random() * self.angleVariation) - (self.angleVariation / 2);
		var angle = self.angle = options.angle + angleAdjust;
		
		// Apply the speed variation
		var speedAdjust = (Math.random() * self.speedVariation) - (self.speedVariation / 2);
		self.speed = (options.speed || 10) + speedAdjust;
		
		// Calculate the cos and sin values once up front based on the
		// initial angle. The angle wont change here once created so no
		// need to re-calculate each update.
		self._cos = Math.cos(angle);
		self._sin = -Math.sin(angle);
		
		self.update = function(frameTime, delta){
			self.speed -= (0.05 * delta);
			var speed = self.speed * delta;
			var bounds = self.bounds;
			
			// Update origin based on the angle
			var x = self.x += speed * self._cos;
			var y = self.y += speed * self._sin;
			
			// Remove if we have traveled out of bounds
			if(x < bounds.left || x > bounds.right || y < bounds.top || y > bounds.bottom){
				self.destroy({explode: true});
			}
		}
		
		self.draw = function(ctx){
			var x = self.x;
			var y = self.y;
			
			ctx.lineWidth = 1;
			ctx.strokeStyle = 'rgba(255, 255, 255, 1)';
			ctx.beginPath();
			ctx.moveTo((x + 20 * self._cos), (y + 20 * self._sin));
			ctx.lineTo(x, y);
			ctx.stroke();
		}
		
		self.destroy = function(options){
			window.Bullet.instances.splice(window.Bullet.instances.indexOf(self), 1);
			self.assetList.remove(self);
			
			// Particle explosion that bounces off the screen
			if(options && options.explode){
				for(var i=0; i<5; ++i){
					self.assetList.add(new Particle({
						x: self.x,
						y: self.y,
						speed: self.speed,
						speedVariation: 2.5,
						angle: self.angle,
						angleVariation: 2,
						bounds: self.bounds
						,life: 500
					}));
				}
			}
		}
		
		self.hits = function(target){
			var enemy = target.getRect();
			var x = self.x;
			var y = self.y;
			
			if(x > enemy.left && x < enemy.right && y > enemy.top && y < enemy.bottom){
				return true;
			}else{
				return false;
			}
		}
	}
	
	window.Bullet.instances = [];
})();