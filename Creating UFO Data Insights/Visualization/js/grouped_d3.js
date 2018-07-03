var width = 1000, height = 500;
var margin = {top: 25, bottom: 30, right: 20, left: 40};
var svg = d3.select("#svg")
	.attr("width", width + margin.left + margin.right)
	.attr("height", height + margin.top + margin.bottom);

d3.json("../json/region_sighting.json", function(data)
{
	plot(data);
});

function plot(data)
{
	// var max = d3.max(data, function(d) { return d3.max(keys, function(key) { return d[key]; }); })
	var max = 250;

	var x0 = d3.scaleBand()
		.rangeRound([50, width])
		.paddingInner(0.05)
		.domain(["West", "South West", "Mid West", "South East", "North East"]);

	var x1 = d3.scaleBand()
		.padding(0.05)
		.domain(["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"])
		.rangeRound([50, x0.bandwidth()]);

	var y = d3.scaleLinear()
		.rangeRound([height, 0])
		.domain([0, max]);

	var z = d3.scaleOrdinal(d3.schemeCategory10);
		// .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);
	// var colorScale = d3.scaleOrdinal(d3.schemeCategory10);

	var frame = svg;

	var keys = ["1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999"];

	frame.append("g")
		.selectAll("g")
		.data(data)
		.enter()
		.append("g")
		.attr("transform", function(d) { return "translate(" + x0(d["state"]) + ",0)"; })
		.selectAll("rect")
		.data(function(d) { return keys.map(function(key) { return {key: key, value: d[key]}; }); })
		.enter().append("rect")
		.attr("x", function(d) { return x1(d.key); })
		.attr("y", function(d) { return y(d.value); })
		.attr("width", x1.bandwidth())
		.attr("height", function(d) { return height - y(d.value); })
		.attr("fill", function(d) { return z(d.key); });

	frame.append("g")
		.attr("class", "axis")
		.attr("transform", "translate(0," + height + ")")
		.call(d3.axisBottom(x0));

	// frame.append("g")
	// 	.attr("class", "axis")
	// 	.call(d3.axisLeft(y).ticks(null, "s"))
	// 	.append("text")
	// 	.attr("x", 2)
	// 	.attr("y", y(y.ticks().pop()) + 0.5)
	// 	.attr("dy", "0.32em")
	// 	.attr("fill", "#000")
	// 	.attr("font-weight", "bold")
	// 	.attr("text-anchor", "start")
	// 	.text("Sightings");

	var yAxis = d3.axisLeft()
		.scale(y);

	svg.append("g")
		.attr("transform", "translate(50, 0)")
		.call(yAxis);

	svg.append("text")
		.attr("class", "small")
		.attr("x", - height / 2)
		.attr("y", 10)
		.style("text-anchor", "middle")
		.style("transform", "rotate(-90deg)")
		.text("UFO Sightings");

	var legend = frame.append("g")
		.attr("font-family", "sans-serif")
		.attr("font-size", 10)
		.attr("text-anchor", "end")
		.selectAll("g")
		.data(keys.slice().reverse())
		.enter()
		.append("g")
		.attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

	legend.append("rect")
		.attr("x", width - 19)
		.attr("width", 19)
		.attr("height", 19)
		.attr("fill", z);

	legend.append("text")
		.attr("x", width - 24)
		.attr("y", 9.5)
		.attr("dy", "0.32em")
		.text(function(d) { return d; });







	// var max = d3.max(data, function (d) { return d["count"]; });
	// var y = d3.scaleLinear()
	// 	.domain([0, max])
	// 	.range([height - 50, 20]);
	// var x = d3.scaleBand()
	// 	.domain(Array.apply(null, {length: 189}).map(Number.call, Number))
	// 	.rangeRound([80, width - 50]);









	// var barWidth = (width - 100) / data.length;
	// var bar = svg.selectAll("g")
	// 	.data(data)
	// 	.enter()
	// 	.append("g");
	// bar.append("rect")
	// 	.attr("y", function(d) { return y(d["count"]); })
	// 	.attr("x", function(d) { return x(d["id"]); })
	// 	.attr("height", function(d) { return height - 50 - y(d["count"]); })
	// 	.attr("width", barWidth - 9)
	// 	.style("fill", "#1e90ff");
	// var xAxis = d3.axisBottom()
	// 	.scale(x)
	// 	.tickFormat("");
	// var yAxis = d3.axisLeft()
	// 	.scale(y);
	// svg.append("g")
	// 	.attr("transform", "translate(0," + (height - 50) + ")")
	// 	.call(xAxis);
	// svg.append("g")
	// 	.attr("transform", "translate(80, 0)")
	// 	.call(yAxis);
	// svg.append("text")
	// 	.attr("class", "small")
	// 	.attr("x", - height / 2)
	// 	.attr("y", 30)
	// 	.style("text-anchor", "middle")
	// 	.style("transform", "rotate(-90deg)")
	// 	.text("UFO Sightings");

	return;
}