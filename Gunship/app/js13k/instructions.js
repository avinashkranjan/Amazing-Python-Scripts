(function(){
	
	var CONTROLS = [
		'Controls:',
		'Move left and right using [a] and [d] or arrow left and right.',
		'Aim cannons with mouse cursor.',
		'Fire with [space] or left mouse button.',
		'Pause and resume with [p].'
	];
	
	var GAME = [
		'Game:',
		'Shoot enemies to score points.',
		'Chain kills to increase your multiplier and power up your cannon.',
		'If an enemy gets past you, the score multiplier is reset!',
		'Hitting an enemy with your ship will trigger an explosion and',
		'kill all enemies.',
		'But if you get hit three times it\'s Game Over!'
	];
	
	window.Instructions = function(options){
		var self = this;
		
		self.bounds = options.bounds;
		self.x = self.bounds.right/2;
		self.y = 70;
		self.start = options.start;
		self.message = options.message || 'Press [p] to resume!';
		
		self.update = function(frameTime, delta){
			if(Input.restart()){
				if(self.start) self.start();
				self.assetList.remove(self);
			}
		}
		
		self.draw = function(ctx){
			var x = self.x;
			var y = self.y;
			var bounds = self.bounds;
			
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = 'rgba(255, 255, 255, 1)';
			ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
			ctx.fillRect(0, 0, bounds.right, bounds.bottom);
			ctx.stroke();
			
			ctx.font = '36px Arial';
			ctx.textAlign = 'center';
			drawTextLine(ctx, 'Gunship13k', x, y);
			
			drawParagraph(ctx, GAME, x, y+50);
			drawParagraph(ctx, CONTROLS, x, y+230);
			
			ctx.textAlign = 'center';
			ctx.font = '18px Arial';
			drawTextLine(ctx, self.message, x, y+450);
		}
	};
})();
