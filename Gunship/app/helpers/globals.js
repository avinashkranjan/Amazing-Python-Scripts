(function(){
	
	// DOM selector method
	window.$ = function(selector)
	{
		if(selector.charAt(0) == '#')
			return document.getElementById(selector.substr(1, selector.length));
	}
	
	// Check if one rectangle intersects another
	window.intersectRect = function(r1, r2) {
		return !(r2.left > r1.right || 
			r2.right < r1.left || 
			r2.top > r1.bottom ||
			r2.bottom < r1.top);
	}
	
	// Extend objects with properties of another
	window.extend = function(){
		var args = arguments;
		var a = args[0] || {};
		for(var i=1; i<args.length; ++i){
			var b = args[i];
			for(var key in b){
				a[key] = b[key];
			}
		}
		return a;
	}
})();