var width = 800, height = 500;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height);

var color = d3.scaleOrdinal()
	.domain(["Foggy", "Rainy", "Windy", "Snowy", "Dusty"])
	.range(["#2ecc71", "#3498db", "#e74c3c", "#f1c40f", "#9b59b6"]);

radius = Math.min(width, height) / 2;
g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var pie = d3.pie()
	.sort(null)
	.value(function(d) { return d["count"]; });

var path = d3.arc()
	.outerRadius(radius - 50)
	.innerRadius(0);

var label = d3.arc()
	.outerRadius(radius - 120)
	.innerRadius(radius - 120);

d3.json("../json/weather_calc.json", function(data)
{
	plot(data);
});

function plot(data)
{
	var arc = g.selectAll(".arc")
		.data(pie(data))
		.enter().append("g")
		.attr("class", "arc");

	arc.append("path")
		.attr("d", path)
		.attr("fill", function(d) { return color(d.data.condition); });

	arc.append("text")
		.attr("transform", function(d) { return "translate(" + label.centroid(d) + ")"; })
		.attr("dy", "0.35em")
		.attr("font-size","30px")
		.attr("text-anchor","middle")
		.text(function(d) { return d.data.condition; });

	return;
}