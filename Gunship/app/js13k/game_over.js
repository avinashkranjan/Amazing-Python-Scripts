(function(){
	window.GameOver = function(options){
		var self = this;
		
		self.bounds = options.bounds;
		self.scoreModel = options.scoreModel;
		self.bulletsFired = options.bulletsFired;
		self.enemiesKilled = options.enemiesKilled;
		self.enemiesescaped = options.enemiesescaped;
		self.x = self.bounds.right/2;
		self.y = self.bounds.bottom/2-100;
		
		self._framesPassed = 0;
		self.position = 0;
		
		//HACK
		self.y = (self.bounds.bottom/2-120) - (50 - (self.position*50));
		
		self.update = function(frameTime, delta){
			if(self.position < 1){
				self._framesPassed += frameTime;
				self.position = Math.min(1, (1/500)*self._framesPassed);
				self.y = (self.bounds.bottom/2-120) - (50 - (self.position*50));
			}
		}
		
		self.draw = function(ctx){
			var x = self.x;
			var y = self.y;
			var bounds = self.bounds;
			var opacity = self.position;
			
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = 'rgba(255, 255, 255, 1)';
			ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
			ctx.fillRect(0, 0, bounds.right, bounds.bottom);
			ctx.stroke();
			
			ctx.fillStyle = 'rgba(255, 255, 255, '+opacity+')';
			ctx.textAlign = 'center';
			ctx.font = '36px Arial';
			drawTextLine(ctx, 'Game Over!', x, y);
			
			var score = self.scoreModel.score();
			var highScore = self.scoreModel.highScore();
			var message;
			if(score > highScore){
				message = [
					'You set a new high score!',
					'Score: '+score,
					'Previous best: '+highScore
				];
			}else{
				message = [
					'You can do better than that!',
					'Score: '+score,
					'Previous best: '+highScore
				]
			}
			message = message.concat([
				'Highest multiplier: '+self.scoreModel.score(),
				'Bullets fired: '+self.bulletsFired,
				'Enemies killed: '+self.enemiesKilled,
				'Longest kill chain: '+self.scoreModel.longestKillChain(),
				'Enemies escaped: '+self.enemiesescaped
			]);
			
			drawParagraph(ctx, message, x, y+40, 'center');
			
			ctx.textAlign = 'center';
			ctx.font = '18px Arial';
			ctx.fillText('Press [Enter] to try again', x, y+230);
		}
	};
})();