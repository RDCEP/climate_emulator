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
        world_map = svg.append('g'),
        graticule = d3.geo.graticule(5),
        color,
        colors_used=0,
        nice_colors = [
            [230, 150, 0],
            [86, 180, 233],
            [0, 158, 115],
            [240, 228, 66],
            [0, 114, 178], [213, 94, 0], [204, 121, 167]
        ]
    ;
    this.get_color = function() {
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
                        Options.active_map_colors.splice(region_index, 1);
                        map_region.classed('active', false);
                        if (map_region.classed('land')) {
                            map_region.style('fill', '#3ABF96');
                        } else {
                            map_region.style('fill', '#a3d3e8');
                        }
                        lines = output.get_active();
                        output.redraw(false);
                    } else {
                        color = map.get_color();
                        Options.active_map_region.push(region);
                        Options.active_map_colors.push(color);
                        map_region
                            .classed('active', true)
                            .style('fill', color)
                        ;
                        lines = output.get_active();
                        output.redraw(false);
                        output.colorize(region, color);
                    }
                })
            ;
        });
    }
}
map = new Map();
map.draw();
