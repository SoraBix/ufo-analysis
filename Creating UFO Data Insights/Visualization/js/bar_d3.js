var width = 1100, height = 600;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height);

d3.json("../json/population_group.json", function(data)
{
	plot(data);
});

function plot(data)
{
	var max = d3.max(data, function (d) { return d["count"]; });
	var y = d3.scaleLinear()
		.domain([0, max])
		.range([height - 50, 20]);
	var x = d3.scaleBand()
		.domain(Array.apply(null, {length: 189}).map(Number.call, Number))
		.rangeRound([80, width - 50]);
	var barWidth = (width - 100) / data.length;
	var bar = svg.selectAll("g")
		.data(data)
		.enter()
		.append("g");
	bar.append("rect")
		.attr("y", function(d) { return y(d["count"]); })
		.attr("x", function(d) { return x(d["id"]); })
		.attr("height", function(d) { return height - 50 - y(d["count"]); })
		.attr("width", barWidth - 9)
		.style("fill", "#1e90ff");
	var xAxis = d3.axisBottom()
		.scale(x)
		.tickFormat("");
	var yAxis = d3.axisLeft()
		.scale(y);
	svg.append("g")
		.attr("transform", "translate(0," + (height - 50) + ")")
		.call(xAxis);
	svg.append("g")
		.attr("transform", "translate(80, 0)")
		.call(yAxis);
	svg.append("text")
		.attr("class", "small")
		.attr("x", - height / 2)
		.attr("y", 30)
		.style("text-anchor", "middle")
		.style("transform", "rotate(-90deg)")
		.text("UFO Sightings");
	svg.append("text")
		.attr("class", "small")
		.attr("x", width / 2)
		.attr("y", (height / 2) + 270)
		.text("Population Density");

	return;
}