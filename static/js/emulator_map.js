function Map(){
  var factor = 1,
    width = 960*factor,
    height = 480*factor,
    projection = d3.geo.equirectangular()
      .scale(153*factor)
      .translate([480*factor,240*factor]),
    path = d3.geo.path()
      .projection(projection),
    svg = d3.select("#map").append("svg")
      .attr("width", width)
      .attr("height", height),
    defs = svg.append('defs'),
    world_map = svg.append('g'),
    graticule = d3.geo.graticule(5),
    color,
    allpatterns,
    datum = 'region',
    colors_used=0,
    nice_colors = [
      [230, 150, 0], [86, 180, 233], [0, 158, 115], [240, 228, 66],
      [0, 114, 178], [213, 94, 0], [204, 121, 167]
    ],
    color_map = region_codes
  ;

  function get_color(d) {
    var color_list = [
      //d3.rgb(0, 0, 0),      // black
      d3.rgb(230, 159, 0),  // orange
      d3.rgb(86, 180, 233), // sky blue
      d3.rgb(0, 158, 115),  // bluish green
      d3.rgb(240, 228, 66), // yellow
      d3.rgb(0, 114, 178),  // blue
      d3.rgb(213, 94, 0),   // vermilion
      d3.rgb(204, 121, 167) // reddish purple
    ];
    color = d3.scale.ordinal()
      .domain(color_map)
      .range(color_list);
//    return color(d[Options.check_axis])
//    return color(d.properties.name)
    return color(d)
      .darker(
//        Math.floor(color_map.indexOf(d.properties.name)/(color_list.length*2)) *.5
        Math.floor(color_map.indexOf(d)/(color_list.length*2)) *.5
      );
  }

  function get_fill(d) {
    console.log(d.properties.name);
    if (Math.floor(color_map.indexOf(d.properties.name)/7) % 2 == 1) {
      return 'url(#stripes)';
    }
    return false;
  }

  this.get_color = function() {
    /*
    Return next color in list of nice colors.
     */
    var next_color = nice_colors[(colors_used++) % nice_colors.length];
    var rgb = [ next_color[0], next_color[1], next_color[2] ];
    color = ("#" +
      (0xF00 + rgb[0]).toString(16).substring(1) +
      (0xF00 + rgb[1]).toString(16).substring(1) +
      (0xF00 + rgb[2]).toString(16).substring(1)
    );
    return color;
  };
  this.draw = function(){
    /*
    Draw geographic map from GeoJSON file. Is only called once.
     */
    allpatterns = defs.selectAll('pattern')
      .data(color_map)
      .enter().append('pattern')
      .attr('id', function(d, i) { return "pattern-" + d; })
      .attr('width', 16)
      .attr('height', 16)
      .attr('patternUnits', 'userSpaceOnUse');
    allpatterns
      .append('rect')
      .attr('width', 16)
      .attr('height', 16)
      .attr('fill', function(d, i) { return get_color(d); });
    allpatterns
      .append('image')
      .attr('width', 16)
      .attr('height', 16)
      .attr('xlink:href', function(d, i) {
        if (Math.floor(color_map.indexOf(d)/7) % 2 == 1) {
          return '/static/images/map-stripes.png';
        }
      });
    svg.append("path")
      .datum(graticule)
      .attr("class", "graticule")
      .attr("d", path)
    ;
    d3.json('/static/js/geo.json', function(error, world){
      world_map.selectAll('path')
        .data(world.features)
          .enter().append("path")
          .attr("d", path)
          .attr('class', function(d,i) {
            return d['properties']['class'];
          })
          .attr('id', function(d, i) {
            return d['properties']['name'];
          })
          .on('click', function(d) {
            var map_region = d3.select(this),
              region = d3.select(this).attr('id'),
              region_index = Options.active_map_region.indexOf(region),
              domain,
              lines
            ;
            if (map_region.classed('active')) {
              Options.active_map_region.splice(region_index, 1);
              map_region.classed('active', false);
              if (map_region.classed('land')) {
                map_region.style('fill', '#3ABF96');
              } else {
                map_region.style('fill', '#A3D3E8');
              }
            } else {
              color = map.get_color();
              Options.active_map_region.push(region);
              map_region
                .classed('active', true)
                .style('fill', function(d, i) {
                  return 'url(#pattern-' + d.properties.name + ')';
                })
              ;
            }
            output.show_active();
          })
        ;
    });
  }
}
map = new Map();
map.draw();
