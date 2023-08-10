(function(){
	window.ScoreModel = function(options){
		var self = this;
		
		self._points = 0;
		self._multiplier = 1;
		self._maxMultiplier = 20;
		self._enemyChain = self._threshold = 10;
		self._totalEnemies = 0;
		
		self._difficultyLevel = 0;
		self._difficultyChain = 0;
		self.increaseDifficulty = options.increaseDifficulty;
		
		self._powerupLevel = 0;
		self._powerupChain = 0;
		self.increasePowerup = options.increasePowerup;
		
		self._previousHighScore = 0;
		
		self._killChain = 0;
		
		// Stats
		
		self._bulletsFired = 0;
		self._enemiesKilled = 0;
		self._enemiesEscaped = 0;
		self._longestKillChain = 0;
		
		// Load highscore from local storage
		var storedData = localStorage.getItem('gunship');
		if(storedData){
			self._previousHighScore = (JSON.parse(storedData)).score;
		}
		
		// Save the current score to storage if it's higher than the
		// previous high score
		self.save = function(){
			if(self.score() > self._previousHighScore){
				localStorage.setItem('gunship', JSON.stringify({
					date: (new Date()).getTime(),
					score: self.score()
				}));
			}
		}
		
		// Get the multiplier
		self.multiplier = function(){
			return self._multiplier;
		}
		
		// Get the score
		self.score = function(){
			return self._points;
		}
		self.highScore = function(){
			return self._previousHighScore;
		}
		self.longestKillChain = function(){
			return self._longestKillChain;
		}
		
		// Reset the miltiplier
		self.resetMultiplier = function(){
			self._multiplier = 1;
			self._enemyChain = self._threshold;
			self._powerupChain = 0;
			self._killChain = 0;
		}
		
		// Add points to the model
		// Increase the multiplier when 100 points have been added
		self.add = function(points){
			
			self._points += (points * self._multiplier);
			
			// Maintain the killchain values
			self._longestKillChain = Math.max(self._longestKillChain, ++self._killChain);
			
			if(self._multiplier < self._maxMultiplier && --self._enemyChain == 0){
				++self._multiplier;
				self._enemyChain = self._threshold;
			}
			
			// Increment the total enemies
			++self._totalEnemies;
			
			// When the total enemies killed gets past a
			// threshold then callback to make enemies more
			// difficult
			if(++self._difficultyChain == 10){
				self._difficultyChain = 0;
				++self._difficultyLevel;
				if(self.increaseDifficulty)
					self.increaseDifficulty(self._difficultyLevel);
			}
			
			// If the user gets a kill streak of 20 then
			// callback to award an upgrade. Powerup chain is
			// reset each time an enemy escapes but already awarded
			// powerups stay.
			if(++self._powerupChain == 20){
				self._powerupChain = 0;
				++self._powerupLevel;
				if(self.increasePowerup)
					self.increasePowerup(self._powerupLevel);
			}
		}
	}
})();