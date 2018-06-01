var width = 600, height = 400;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height);

var color = d3.scaleOrdinal()
	.domain(["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "50-60", "60-70", "70-80", "80-90", "90-100", "100-110", "110-120", "120-130", "130-140", "140-150", "150-160", "160-170", "170-180", "180-190", "190+"])
	.range(["#3498db", "#2ecc71", "#e74c3c", "#f1c40f", "#9b59b6"]);

d3.json("distance_military.json", function(data)
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
		.domain(["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "50-60", "60-70", "70-80", "80-90", "90-100", "100-110", "110-120", "120-130", "130-140", "140-150", "150-160", "160-170", "170-180", "180-190", "190+"])
		.rangeRound([80, width - 50]);
	var barWidth = (width - 100) / data.length;
	var bar = svg.selectAll("g")
		.data(data)
		.enter()
		.append("g");
	bar.append("rect")
		.attr("y", function(d) { return y(d["count"]); })
		.attr("x", function(d) { return x(d["range"]); })
		.attr("height", function(d) { return height - 50 - y(d["count"]); })
		.attr("width", barWidth - 9)
		.style("fill", function(d) { return color(d["range"]); });
	var xAxis = d3.axisBottom()
		.scale(x);
	var yAxis = d3.axisLeft()
		.scale(y);
	svg.append("g")
		.attr("transform", "translate(0," + (height - 50) + ")")
		.call(xAxis)
		.selectAll("text")
		.style("text-anchor", "end")
		.attr("dx", "-.8em")
        .attr("dy", ".15em")
		.attr("transform", "rotate(-30)");
	svg.append("g")
		.attr("transform", "translate(80, 0)")
		.call(yAxis);
	svg.append("text")
		.attr("class", "small")
		.attr("x", width/2 - 90)
		.attr("y", height)
		.text("Distance from Military Base (mi.)");
	svg.append("text")
		.attr("class", "small")
		.attr("x", - height / 2)
		.attr("y", 30)
		.style("text-anchor", "middle")
		.style("transform", "rotate(-90deg)")
		.text("UFO Sightings");

	return;
}