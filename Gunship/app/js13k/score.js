(function(){
	window.ScoreBoard = function(options){
		var self = this;
		
		self.bounds = options.bounds;
		self.scoreModel = options.scoreModel;
		
		self.draw = function(ctx){
			ctx.fillStyle = '#fff';
			ctx.font = '18px Arial';
			ctx.textAlign = 'right';
			ctx.fillText(self.scoreModel.multiplier()+'x'+'   '+self.scoreModel.score(), self.bounds.right-20, 30);
		}
	}
})();