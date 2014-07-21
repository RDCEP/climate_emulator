function Map(){
  var factor = 1,
    width = 880*factor,
    height = 440*factor,
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
    map_regions
  ;

  function get_color(d, i) {
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
    return color_list[region_codes.indexOf(d.properties.abbr) % color_list.length];
  }

  this.draw = function(){
    /*
    Draw geographic map from GeoJSON file. Is only called once.
     */
    svg.append("path")
      .datum(graticule)
      .attr("class", "graticule")
      .attr("d", path)
    ;
    d3.json('/static/js/geo.json', function(error, world){
      map_regions = world_map.selectAll('path')
        .data(world.features)
        .enter()
        .append('path')
        .attr('d', path)
        .attr('class', function(d) {return d.properties.class;})
        .attr('id', function(d) {return d.properties.abbr;})
        .attr('data-abbr', function(d) {return d.properties.abbr;})
        .on('click', function(d) {
          var input_filter = d3.select(this);
          output.change_input_filter(input_filter, d);

        })
      ;
      map_regions.each(function(d, i) {
        var pattern = defs.append('pattern')
          .attr('id', 'pattern-' + d.properties.abbr)
          .attr('width', 16)
          .attr('height', 16)
          .attr('patternUnits', 'userSpaceOnUse');
        pattern.append('rect')
          .attr('width', 16)
          .attr('height', 16)
          .attr('fill', get_color(d, i));
        pattern.append('image')
          .attr('width', 16)
          .attr('height', 16)
          .attr('xlink:href', function() {
            if (d.properties.class == 'water') {
              return '/static/images/map-stripes.png';
            }
            return null;
          })
        ;
      });
    });
  }
}
map = new Map();
if (Options.region_type == 'regional') {
  map.draw();
}
