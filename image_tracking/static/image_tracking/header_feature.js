(function() {
	function dance() {
    // data = [{"x": , "y": },
    // {"x": , "y":},
    // {"x": , "y":}]
	var circle = d3.selectAll("#circle-dance circle"),
		span = d3.select(".circle-dance-x"),
		data = d3.range(1).map(function() { 
			return 100 + Math.random() * (screen.width-250); 
		});
	circle.data(data).attr("cx", function(d) { return d; });
	}
	dance();
	setInterval(dance, 750);
})();
