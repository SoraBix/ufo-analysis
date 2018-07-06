// var width = 1100, height = 600;
// var svg = d3.select("#svg")
// 	.attr("width", width)
// 	.attr("height", height);

var radar_w = 500,
	radar_h = 500;

// var radar_colorscale = d3.scaleOrdinal(d3.schemaSet1);
var radar_colorscale = d3.scaleOrdinal().domain(["Southeast", "West", "Southwest", "Midwest", "Northeast"])
           .range(["#8ee0d4", "#ffc276", "#b2ec85", "#ff8e85", "#d58fca"]); //, "#fef584", "#90c1dd"

//Legend titles
var radar_LegendOptions = ["Northeast", "Southeast", "West", "Southwest", "Midwest"];

//Data
var radar_d = [
		[ // Northeast
			{axis:"Light",value:0.263},
			{axis:"Triangle",value:0.200},
			{axis:"Circle",value:0.127},
			{axis:"Disk",value:0.147},
			{axis:"Sphere",value:0.093},
			{axis:"Oval",value:0.091},
			{axis:"Fireball",value:0.053},
			{axis:"Diamond",value:0.022}
		],[	// Southeast
			{axis:"Light",value:0.264},
			{axis:"Triangle",value:0.205},
			{axis:"Circle",value:0.113},
			{axis:"Disk",value:0.132},
			{axis:"Sphere",value:0.087},
			{axis:"Oval",value:0.062},
			{axis:"Fireball",value:0.112},
			{axis:"Diamond",value:0.020}
		],[ // West
			{axis:"Light",value:0.306},
			{axis:"Triangle",value:0.177},
			{axis:"Circle",value:0.096},
			{axis:"Disk",value:0.098},
			{axis:"Sphere",value:0.102},
			{axis:"Oval",value:0.059},
			{axis:"Fireball",value:0.141},
			{axis:"Diamond",value:0.017}
		],[ // Southwest
			{axis:"Light",value:0.267},
			{axis:"Triangle",value:0.230},
			{axis:"Circle",value:0.104},
			{axis:"Disk",value:0.096},
			{axis:"Sphere",value:0.104},
			{axis:"Oval",value:0.054},
			{axis:"Fireball",value:0.114},
			{axis:"Diamond",value:0.027}
		],[ // Midwest
			{axis:"Light",value:0.286},
			{axis:"Triangle",value:0.202},
			{axis:"Circle",value:0.105},
			{axis:"Disk",value:0.106},
			{axis:"Sphere",value:0.089},
			{axis:"Oval",value:0.044},
			{axis:"Fireball",value:0.143},
			{axis:"Diamond",value:0.021}
		]
		];

//Options for the Radar chart, other than default
var radar_mycfg = {
  w: radar_w,
  h: radar_h,
  maxValue: 0.35,
  levels: 6,
  ExtraWidthX: 300
}

//Call function to draw the Radar chart
//Will expect that data is in %'s
RadarChart.draw("#radar_plot", radar_d, radar_mycfg);

////////////////////////////////////////////
/////////// Initiate legend ////////////////
////////////////////////////////////////////

var radar_svg = d3.select('#radar')
	.select('#radar_body')
	.selectAll('svg')
	.append('svg')
	.attr("width", radar_w+300)
	.attr("height", radar_h)

//Create the title for the legend
// var radar_text = radar_svg.append("text")
// 	.attr("class", "title")
// 	.attr('transform', 'translate(90,0)') 
// 	.attr("x", radar_w - 70)
// 	.attr("y", 10)
// 	.attr("font-size", "12px")
// 	.attr("fill", "#404040")
// 	.text("What % of owners use a specific service in a week");
		
//Initiate Legend	
var radar_legend = radar_svg.append("g")
	.attr("class", "legend")
	.attr("height", 100)
	.attr("width", 200)
	.attr('transform', 'translate(90,20)') 
	;
	//Create colour squares
	radar_legend.selectAll('rect')
	  .data(radar_LegendOptions)
	  .enter()
	  .append("rect")
	  .attr("x", radar_w + 50)
	  .attr("y", function(d, i){ return i * 40 + 125;})
	  .attr("width", 20)
	  .attr("height", 20)
	  .style("fill", function(d, i){ return radar_colorscale(i);})
	  ;
	//Create text next to squares
	radar_legend.selectAll('text')
	  .data(radar_LegendOptions)
	  .enter()
	  .append("text")
	  .attr("x", radar_w + 75)
	  .attr("y", function(d, i){ return i * 40 + 140;})
	  .attr("font-size", "20px")
	  .attr("fill", "#737373")
	  .text(function(d) { return d; })
	  ;	