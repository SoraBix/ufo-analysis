var width = 960, height = 600;
var svg = d3.select("#svg")
	.attr("width", width)
	.attr("height", height)
	.attr("fill", "none")
	.attr("stroke", "#8a8a8a")
	.attr("stroke-linejoin", "round")
	.attr("stroke-linecap", "round");

d3.json("../json/ufo_sighting_density.json", function(data)
{
	plot(data);
});

function plot(data)
{
	d3.json("../json/us.json", function(map)
	{
		var path = d3.geoPath();
		var color = d3.scaleLinear()
			.domain([1, 10])
			.range(["#bfefff", "#1c86ee"]);

		svg.selectAll("path")
			.data(topojson.feature(map, map.objects.counties).features)
			.enter()
			.append("path")
			.attr("d", path)
			.attr("stroke", "none")
			.style("fill", function(d)
			{
				for (key in data)
					if (parseInt(d.id) == key)
					{
						return color(data[key]);
					}
				return "#ffffff";
			});

		svg.append("path")
			.attr("stroke", "#aaa")
			.attr("stroke-width", 0.5)
			.attr("d", path(topojson.mesh(map, map.objects.counties, function(a, b) { return a !== b && (a.id / 1000 | 0) === (b.id / 1000 | 0); })));
		svg.append("path")
			.attr("stroke-width", 0.5)
			.attr("d", path(topojson.mesh(map, map.objects.states, function(a, b) { return a !== b; })));
		svg.append("path")
			.attr("d", path(topojson.feature(map, map.objects.nation)));
	});

	return;
}