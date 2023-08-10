(function(){
	
	// Generate the smoke sprite
	var smokeCache = $('#smokesprite');
	var ctx = smokeCache.getContext('2d');
	
	// Soft gradient circle
	// drawGradientCircle(ctx, 100, 100, 100, '150, 150, 150', 1);
	
	// Hard edged circle
	ctx.strokeStyle = 'rgba(150, 150, 150, 1)';
	ctx.fillStyle = 'rgba(150, 150, 150, 1)';
	drawCircle(ctx, 100, 100, 100, true, true);
	
	var SMOKE_SPRITE = smokeCache;
	
	// Reflection helper methods
	var reflectVertical = function(incidence){
		var r = 0 - (incidence + Math.PI - 0);
		return -Math.PI - incidence;
	}
	var reflectHorizontal = function(incidence){
		var r = 0.5*Math.PI - (incidence + Math.PI - 0.5*Math.PI);
		r = 2 * Math.PI - incidence;
		return -incidence;
	}
	
	window.Particle = function(options){
		window.Particle.instances.push(this);
		
		var self = this;
		
		self.x = options.x;
		self.y = options.y;
		self.speedVariation = options.speedVariation || 0;
		self.angleVariation = options.angleVariation || 0;
		self.lifeVariation = options.lifeVariation || 200;
		self.bounds = options.bounds;
		
		// Allow the colour to be passed in, but default to white
		var color = self.color = options.color || [255, 255, 255];
		self._colorString = color[0]+', '+color[1]+', '+color[2];
		
		self.particleLength = options.particleLength || 10;
		
		self.radius = options.radius;
		
		// Apply the speed variation
		var speedAdjust = (Math.random() * self.speedVariation) - (self.speedVariation / 2);
		self.speed = (options.speed || 10) + speedAdjust;
		
		// Apply life variatino
		var lifeAdjust = (Math.random() * self.lifeVariation) - (self.lifeVariation / 2);
		self.life = (options.life || 300) + lifeAdjust;
		
		// Add the angle variation
		var angleAdjust = (Math.random() * self.angleVariation) - (self.angleVariation / 2);
		var angle = options.angle + angleAdjust;
		// Calculate the cos and sin values once up front based on the
		// initial angle. The angle wont change here once created so no
		// need to re-calculate each update.
		var setAngle = function(angle){
			self.angle = angle;
			self._cos = Math.cos(angle);
			self._sin = -Math.sin(angle);
		}
		setAngle(angle);
		
		self._age = 0;
		
		self.update = function(frameTime, delta){
			self.speed -= (0.05 * delta);
			var speed = self.speed * delta;
			var bounds = self.bounds;
			var x, y;
			
			// Update origin based on the angle
			var calculateCoordinates = function(){
				x = self.x + speed * self._cos;
				y = self.y + speed * self._sin;
			}
			calculateCoordinates();
			
			// Handle vertical reflection when we go out of bounds
			if(x < bounds.left || x > bounds.right){
				setAngle(reflectVertical(self.angle));
				calculateCoordinates()
			}
			
			// Handle horizontal reflection when we go out of bounds
			if(y < bounds.top || y > bounds.bottom){
				setAngle(reflectHorizontal(self.angle));
				calculateCoordinates();
			}
			
			// Store the updated positions
			self.x = x;
			self.y = y;
			
			// Remove if we've been alive too long
			self._age += frameTime;
			if(self._age > self.life)
				self.destroy();
		}
		
		self.draw = function(ctx){
			var x = self.x;
			var y = self.y;
			var opacity = 1-((1/self.life) * self._age);
			var particleLength = self.particleLength;
			
			if(self.radius){
				var radius = (self.radius/2)+(((self.radius/2)/self.life) * self._age);
				opacity = Math.round((opacity * 0.1)*100)/100;
				ctx.save();
				ctx.globalAlpha = opacity;
				ctx.drawImage(SMOKE_SPRITE, x-radius, y-radius, (radius*2), (radius*2));
				ctx.restore();
			}else{
				ctx.lineWidth = 1;
				ctx.strokeStyle = 'rgba('+self._colorString+', '+opacity+')';
				ctx.beginPath();
				ctx.moveTo((x + particleLength * self._cos), (y + particleLength * self._sin));
				ctx.lineTo(x, y);
				ctx.stroke();
			}
		}
		
		self.destroy = function(){
			window.Particle.instances.splice(window.Bullet.instances.indexOf(self), 1);
			self.assetList.remove(self);
		}
	}
	
	window.Particle.instances = [];
})();