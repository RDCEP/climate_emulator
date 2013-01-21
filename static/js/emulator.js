/**
 * Created with PyCharm.
 * User: njmattes
 * Date: 1/17/13
 * Time: 6:24 PM
 * To change this template use File | Settings | File Templates.
 */

var factor = 1,
    width = 960*factor,
    height = 500*factor,
    projection = d3.geo.equirectangular()
        .scale(150*factor)
        .translate([480*factor,250*factor]),
    path = d3.geo.path()
        .projection(projection),
    svg = d3.select("#map").append("svg")
        .attr("width", width)
        .attr("height", height),
    world_map = svg.append('g'),
    graticule = d3.geo.graticule(5)
    ;
svg.append("path")
    .datum(graticule)
    .attr("class", "graticule")
    .attr("d", path);

//d3.json('/static/js/topo_003.json', function(error, world) {
//    console.log(world);
//    world_map.insert('path', '.graticule')
//        .datum(topojson.object(world, world.objects.topo))
//        .attr('d', path)
//        .attr('class', 'land');
//});

//        .datum(topojson.object(world, world.objects.land))
//        .attr("class", "land")
//        .attr("d", path);
//    svg.insert("path", ".graticule")
//        .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a.id !== b.id; }))
//        .attr("class", "boundary")
//        .attr("d", path);


d3.json('/static/js/geo.json', function(error, world){
    world_map.selectAll('path')
        .data(world.features)
        .enter().append("path")
        .attr("d", path)
        .attr('class', function(d,i) {
            return d['properties']['class'];
        });

})