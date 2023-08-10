// A simple global input manager class to manage game controls.
// Keeps a map of all keys that are currently pressed so it
// can be queried to check a game control without individual
// assets having to listen to DOM events.
// 
// Example:
// 
// 	if(Input.up()){
//		// move somewhere...
// 	}
(function(){
	
	var _keys = {};
	var _mouseX = 0;
	var _mouseY = 0;
	
	// Listen to keydown and keyup events to keep a map of all
	// currently pressed keys
	document.addEventListener('keydown', function(e){
		_keys[e.keyCode] = true;
	});
	
	//NOTE: There is a problem here, it's possible for a key to be pressed
	// and released between two frames meaning that the keypress would not
	// be registered.
	document.addEventListener('keyup', function(e){
		delete _keys[e.keyCode];
	});
	
	// Listen to for mousedown event and keep a map of it like we down with
	// keydown events.
	document.addEventListener('mousedown', function(e){
		_keys['leftmouse'] = true;
	});
	document.addEventListener('mouseup', function(e){
		delete _keys['leftmouse'];
	});
	
	// Listen to mousemove, storing the coordinates as we are ready to return
	// them from Input.mouse() method whenever it is called.
	document.addEventListener('mousemove', function(e){
		var rect = window.game.canvas.getBoundingClientRect();
		_mouseX = e.clientX - rect.left;
		_mouseY = e.clientY - rect.top;
	});
	
	// Check if a control is currently down or not
	_isDown = function(keys){
		for(var i=0; i<keys.length; ++i){
			if(_keys[keys[i]] == true){
				return true;
			}
		}
		return false;
	}
	
	window.Input = {
		
		// w, up arrow
		up: function(){
			return _isDown([38, 87]);
		},
		
		// d, right arrow
		right: function(){
			return _isDown([39, 68]);
		},
		
		// s, down arrow
		down: function(){
			return _isDown([40, 83]);
		},
		
		// a, left arrow
		left: function(){
			return _isDown([37, 65]);
		},
		
		// space bar, left mouse
		fire: function(){
			return _isDown([32, 'leftmouse']);
		},
		
		// enter
		restart: function(){
			return _isDown([13]);
		},
		
		// mouse position
		mouse: function(){
			return {x: _mouseX, y: _mouseY};
		}
	};
})();
