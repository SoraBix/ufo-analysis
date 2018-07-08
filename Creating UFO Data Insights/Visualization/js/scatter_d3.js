var width = 1100, height = 600;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height);

d3.json("../json/date_shape.json", function(data)
{
	plot(data);
});

function plot(data)
{
	var colorScale = d3.scaleOrdinal(d3.schemeCategory10);

	var y = d3.scaleLinear()
		.domain([1990, 1999])
		.range([height - 50, 20]);

	var x = d3.scaleTime()
		.domain([new Date("2000-01-01"), new Date("2000-12-31")])
		.range([70, width-70]);

	var parseTime = d3.timeParse("%Y-%m-%d");

	var dot = svg.selectAll(".dot")
		.data(data)
		.enter()
		.append("g")
		.attr("class","dot");

	dot.append("circle")
		.attr("cy", function(d) { return y(d["year"]); })
		.attr("cx", function(d) { return x(parseTime(d["date"])); })
		.attr("r", 5)
		.style("fill", function(d) { return colorScale(d["shape"]); });

	var xAxis = d3.axisBottom()
		.scale(x)
		.tickFormat(d3.timeFormat("%b"));
	var yAxis = d3.axisLeft()
		.scale(y)
		.tickFormat(d3.format("d"));

	svg.append("g")
		.attr("transform", "translate(0," + (height - 20) + ")")
		.call(xAxis);
	svg.append("g")
		.attr("transform", "translate(50, 0)")
		.call(yAxis);

	return;
}

// {u'cylinder': 118, u'sphere': 421, u'cone': 26, u'chevron': 103, u'oval': 267, u'disk': 501, u'unknown': 386, u'flash': 101, u'other': 571, u'circle': 476, u'rectangle': 100, u'diamond': 95, u'triangle': 866, u'cigar': 184, u'formation': 210, u'changing': 142, u'fireball': 522, u'light': 1228, u'teardrop': 52, u'egg': 79}