var width = 1100, height = 600;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height);

d3.json("../json/region_sighting.json", function(data)
{
	plot(data);
});

function plot(data)
{
	var colorScale = d3.scaleOrdinal(d3.schemeCategory10);

	// var max = d3.max(data, function (d) { return d["count"]; });
	var max = 230;

	var x = d3.scaleLinear()
		.domain([1990, 1999])
		.range([70, width - 200]);

	var y = d3.scaleLinear()
		.domain([0, max])
		.range([height - 50, 20]);

	var lineGenerator = d3.line();

	for(var i in data)
	{
		var points = [[x(1990), y(data[i]["1990"])],
			[x(1991), y(data[i]["1991"])],
			[x(1992), y(data[i]["1992"])],
			[x(1993), y(data[i]["1993"])],
			[x(1994), y(data[i]["1994"])],
			[x(1995), y(data[i]["1995"])],
			[x(1996), y(data[i]["1996"])],
			[x(1997), y(data[i]["1997"])],
			[x(1998), y(data[i]["1998"])],
			[x(1999), y(data[i]["1999"])]];

		var color = colorScale(data[i]["state"]);
		var pathData = lineGenerator(points);

		svg.append("path")
			.attr("fill", "none")
			.attr("stroke", color)
			.attr("stroke-linejoin", "round")
			.attr("stroke-linecap", "round")
			.attr("stroke-width", 1.5)
			.attr("d", pathData);
	}

	var xAxis = d3.axisBottom()
		.scale(x)
		.tickFormat(d3.format("d"));
	var yAxis = d3.axisLeft()
		.scale(y)
		.tickFormat(d3.format("d"));

	svg.append("g")
		.attr("transform", "translate(0," + (height - 20) + ")")
		.call(xAxis);
	svg.append("g")
		.attr("transform", "translate(50, 0)")
		.call(yAxis);

	var options = ["South East", "West", "South West", "Mid West", "North East"];

	var legend = svg.append("g")
		.attr("class", "legend")
		.attr("height", 100)
		.attr("width", 200)
		.attr('transform', 'translate(0,0)');

	legend.selectAll('rect')
		.data(options)
		.enter()
		.append("rect")
		.attr("x", width - 180)
		.attr("y", function(d, i){ return i * 40 + 125;})
		.attr("width", 20)
		.attr("height", 20)
		.style("fill", function(d){ return colorScale(d);});

	legend.selectAll('text')
		.data(options)
		.enter()
		.append("text")
		.attr("x", width - 150)
		.attr("y", function(d, i){ return i * 40 + 140;})
		.attr("font-size", "20px")
		.attr("fill", "#737373")
		.text(function(d) { return d; });

	svg.append("text")
		.attr("class", "small")
		.attr("x", (width / 2) + 380)
		.attr("y", (height / 2) + 285)
		.text("Year");

	return;
}