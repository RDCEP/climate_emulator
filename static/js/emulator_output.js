function Output() {
  /*
   Set up initial variables
   ------------------------
   General layout
   */
  var margin = {top: 0, right: 0, bottom: 0, left: 0},
    padding = {top: 40, right: 40, bottom: 10, left: 10},
    outer_width = 656,
    outer_height = 352,
    inner_width = outer_width - margin.left - margin.right,
    inner_height = outer_height - margin.top - margin.bottom,
    width = outer_width - padding.left - padding.right,
    height = outer_height - padding.top - padding.bottom,
    offset = 0
  ;
  /*
   Data domain
   */
  var default_domain = {
      relative: {min_domain: -.1, max_domain: 2.5, offset: 0},
      absolute: {min_domain: 230 - 273.15, max_domain: 305 - 273.15,
                 offset: 273.15}
    },
    min_domain = default_domain.relative.min_domain,
    max_domain = default_domain.relative.max_domain,
    min_d, max_d,
    start_year = 2005,
    end_year = 2100,
    x = d3.scale.linear().domain([start_year, end_year]).range([0, width]),
    y = d3.scale.linear().domain([max_domain, min_domain]).range([0, height])
  ;
  
  /*
   Graph entities
   */
  var svg = d3.select('#graph').append('svg')
      .attr('width', width + padding.left + padding.right)
      .attr('height', height + padding.top + padding.bottom)
      .append('g')
      .attr('transform', 'translate(' + padding.left + ',' + padding.top + ')'),
    line = d3.svg.line()
      .x(function(d, i) { return x(i + start_year); })
      .y(function(d) { return y(d - offset); }),
    x_axis_ticks = d3.svg.axis()
      .scale(x)
      .orient('top')
      .tickSize(1)
      .tickPadding(5)
      .tickFormat(d3.format('C')),
    y_axis_ticks = d3.svg.axis()
      .scale(y)
      .tickSize(1)
      .tickPadding(5)
      .orient('right'),  // left / right
    tooltip = d3.select('#output').append('div').attr('id', 'tooltip'),
    datum = 'region', //Options.check_axis
    color_map = region_codes,
    data,
    graph,
    color,
    dots_layer,
    dots,
    paths,
    points,
    segments,
    y_grid,
    histogram,
    x_axis,
    y_axis,
    histobars,
    hover_active = false
  ;

  tooltip_over = function(d, i) {
    var tdots = get_active_regions(i)._dots;
    if (tdots) {
      tooltip.html('');
      tdots.style('fill', '#eee')
        .classed('visible', true)
        .style('visibility', 'visible')
        .sort(function(a, b) {
          return d3.descending(a.data, b.data);
        })
        .each(function(dd) {
          var _h = '<b style="color:' + get_color(dd) + '">';
          _h += dd[datum] + '</b>:&nbsp;'+ dd.data + '<br>';
          tooltip
            .html(tooltip.html() + _h);
        });
      tooltip
        .style('left', (i * width / (points - 1) + padding.left + (width / (points - 1) / 2)) + 20 + 'px')
        .style('top', (parseFloat(d3.select(tdots[0][0]).attr('cy')) + 30) + 'px')
        .style('opacity', .8);
    }
  };

  tooltip_out = function(d, i) {
    d3.selectAll('.dot-'+i)
      .classed('visible', false)
      .style('visibility', 'hidden');
    tooltip.html('')
      .style('opacity', 0);
  };

  /*
   End variables
   */

  function get_data(model, rcp) {
    /*
    Get temperature data based on model, rcp, and temp_type (absolute|relative).
     */
    var data = [],
      offset;
    var o = output_data.filter(function(el) {
      return el.model == model;
    })[0][rcp];
    for (i=0;i<o.length;i++) {
      data[i] = o[i][Options.temp_type];
    }
    return data;
  }


  function flat_data(d, o) {
    /*
     Combine datum, region, and index into one object for rollover circles
     */
    _d = [];
    for (i=0; i<d.length; ++i) {
      _t = {data: d[i], region: o.region};
      _d.push(_t);
    }
    return _d;
  }


  function flat_histo(data, l) {
    _d = []
    for (i=0;i<data.length;++i) {
      _d.push(data[i].data[l-1]);
    }
    return _d;
  }


  function get_domain(data) {
    /*
     Update y domain based on updated data min and max
     */
    min_d = d3.min(data, function(d) { return d3.min(d.data); });
    max_d = d3.max(data, function(d) { return d3.max(d.data); });
    max_domain = max_d + ((max_d - min_d) / 10);
    min_domain = min_d - ((max_d - min_d) / 10);
    if (Options.temp_type == 'relative') {
      min_domain = -0.1;
    }
    return [max_domain, min_domain];
  }


  function draw_axes(data) {
    /*
     Redraw graph axes. Called from draw() and redraw().
     */
    y.domain(get_domain(data));
    x_axis.transition()
      .call(x_axis_ticks);
    y_axis.transition()
      .call(y_axis_ticks
        .tickSize(0)
        .tickFormat(d3.format('.1f'))
    );
    y_grid.transition()
      .call(y_axis_ticks
        .tickSize(width, 0, 0)
        .tickFormat('')
    );
  }


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
    return color(d[datum])
      .darker(
        Math.floor(color_map.indexOf(d[datum])/(color_list.length*2)) *.5
      );
  }


  function get_color_flat(d) {
    var color_list = [
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
    return color(d)
      .darker(
        Math.floor(color_map.indexOf(d)/(color_list.length*2)) *.5
      );
  }


  function get_stroke(d) {
    /*
     Alternates between solid and dashed lines
     */
//    if (Math.floor(color_map.indexOf(d[Options.check_axis])/7) % 2 == 1) {
    if (Math.floor(color_map.indexOf(d[datum])/7) % 2 == 1) {
      return '2,5';
    }
    return 'none';
  }


  function get_active_regions(i) {
    /*
    Only for Emulator
    Get active regions from map
    */
    var active_paths = '',
      active_dots = '',
      regions = Options.active_map_region,
      rcp = Options.active_rcp
      ;
    if (regions.length > 0) {
      for (j=0;j<regions.length;j++) {
        active_paths += ('.'+regions[j]+',');
        active_dots += ('.dot-'+regions[j]+'.dot-'+i+',');
      }
      return {
        _paths: d3.selectAll(active_paths.slice(0,-1)),
        _dots: d3.selectAll(active_dots.slice(0,-1))
      }
    }
    return false;
  }


  function draw(data, model, rcp) {
    points = d3.max(data, function(d, i) {
      return d.data.length;
    });
    if (Options.region_type == 'global') {
      output.draw_histogram(flat_histo(data, points));
    }
    paths = graph.selectAll('.output-path')
      .data(data, function(d) {return data.indexOf(d);});
    paths.enter()
      .append('path');
    paths.transition()
      .duration(1000)
      .attr('d', function(d, i) {
        return line(d.data);
      })
      .attr('class', function(d) {
        return 'output-path ' + d.region;
      })
      .style('visibility', function(d) {
        if (Options.active_map_region.length > 0) {
          if (Options.active_map_region.indexOf(d.region) != -1) {
            return 'visible';
          } else {
            return 'hidden';
          }
        }
        return 'visible';
      })
      .style('stroke', function(d) {
        if (Options.active_map_region.length > 0) {
          return get_color(d);
        } else {
          return '#999';
        }
      })
      .style('stroke-dasharray', function(d) {
        if (Options.active_map_region.length > 0) {
          return get_stroke(d);
        } else {
          return 'none';
        }
      })
      .style('stroke-linecap', 'round')
    ;
    paths.exit()
      .transition()
      .remove();
    dots_layers = dots_layer.selectAll('.dot-layer')
      .data(data, function(d) {return data.indexOf(d);});
    dots_layers.exit().transition().remove();
    dots_layers.enter()
      .append('g')
      .attr('class', 'dot-layer')
      .attr('id', function(d) { return 'dots-'+ d.region; })
    ;
    dots = dots_layers.selectAll('.dot')
      .data(function(d, i) {return flat_data(d.data, d); });
    dots.exit().remove();
    dots.enter()
      .append('circle')
      .attr('r', 5)
      .attr('cx', function(d, i) { return x(i+start_year ); })
      .attr('cy', function(d) { return y(d.data); })
      .attr('class', function(d, i) {
        return 'dot-' + i + ' dot-' + d.region + ' dot';
      })
      .style('stroke', function(d) {return get_color(d); })
      .style('visibility', 'hidden')
    ;
  }


  function build_initial(data, model, rcp) {
    y_axis = svg.append('g')
      .attr('class', 'y axis')
      .attr("transform", "translate(" + width + ",0)");
    histogram = svg.append('g')
      .attr('id', 'histo');
    y_grid = svg.append('g')
      .attr('id', 'y_grid')
      .attr('class', 'grid');
    x_axis = svg.append('g')
      .attr('class', 'x axis')
      .attr("transform", "translate(0,0 )");
    graph = svg
      .append('g')
      .attr('class', 'output-area');
    dots_layer = svg
      .append('g')
      .attr('class', 'all-dots');
    draw_axes(data);
    draw(data, model, rcp);
    var segments_layer = svg.append('g')
      .attr('class', 'segments');
    segments = segments_layer.selectAll('.data-region')
      .data(data[0].data)
      .enter()
      .append('rect');
    segments
      .style('fill', 'none')
      .style('pointer-events', 'none')
      .attr('width', width / (points - 1))
      .attr('height', height)
      .attr('x', function(d, i) {
        return (i * width / (points - 1)) - (width / (points - 1) / 2);
      })
      .attr('y', 0)
      .on('mouseover', tooltip_over)
      .on('mouseout', tooltip_out);
    segments.append('g')
      .attr('transform', 'translate('+width / (points - 1)/2+', 0)')
      .attr('class', 'grid-roll')
      .append('line')
      .attr('x2', 0)
      .attr('y2', -height);
  }


  this.change_input_filter = function(input_filter, data) {
    /*
     This is a stubbed out abstract function for filtering output paths
     based on both map regions and models.
     */
    var _id = input_filter.attr('id'),
      _index = Options.active_map_region.indexOf(_id)
    ;
    //TODO: Switch for global regions
    if (input_filter.classed('active')) {
      Options.active_map_region.splice(_index, 1);
      input_filter.classed('active', false);
      if (input_filter.classed('land')) {
        input_filter.style('fill', '#3ABF96');
      } else if (input_filter.classed('water')) {
        input_filter.style('fill', '#A3D3E8');
      } else {
        input_filter.style('background-color', '#999999');
      }
    } else {
      Options.active_map_region.push(_id);
      input_filter.classed('active', true);
      if (Options.region_type == 'regional') {
        color = map.get_color(data);
        input_filter.style('fill', function(d, i) {
          return 'url(#pattern-' + d.properties.name + ')';
        });
      } else {
        color = map.get_color(data);
        input_filter
          .style('background-color', function(d, i) {
            return get_color_flat(data);
          })
          .style('color', 'white')
        ;
      }
    }
    output.show_active();
  };


  this.show_active = function() {
    var active = get_active_regions();
    if (active) {
      paths.style('visibility', 'hidden');
      dots.style('visibility', 'hidden');
      active._paths.style('visibility', 'visible')
        .style('stroke', function(d) {
          return get_color(d);
        })
        .style('stroke-dasharray', function(d) {
          return get_stroke(d);
        })
        .style('stroke-width', '2px')
      ;
      segments.style('pointer-events', 'all');
    } else {
      dots.style('visibility', 'hidden');
      paths.style('visibility', 'visible')
        .style('stroke', '#999')
        .style('stroke-dasharray', 'none')
        .style('stroke-width', '2px')
      ;
    }
  };


  this.redraw = function(model, rcp) {
    //TODO: Don't need model and rcp as args. Get these from Options object.
    /*
     Update graphs on .input changes.
     */
    var url;
    if (Options.region_type == 'regional') {
      url = '/model/' + model + '/rcp/' + rcp + '/temp/' + Options.temp_type;
    } else if (Options.region_type == 'global') {
      url = '/rcp/' + rcp + '/temp/' + Options.temp_type;
    }
    d3.selectAll('.ajax-loader').style('display', 'block');
    d3.json(url, function(error, data) {
      draw_axes(data.data);
      draw(data.data, model, rcp);
      d3.selectAll('.ajax-loader').style('display', 'none');
    });
  };


  this.build = function(model, rcp) {
    /*
     Draws initial graph on page load. Builds hover effects.
     */
    d3.selectAll('.ajax-loader').style('display', 'block');
    Options.active_model = model;
    url = '/model/' + model + '/rcp/' + rcp + '/temp/' + Options.temp_type;
    d3.json(url, function(error, data) {
      build_initial(data.data, model, rcp);
      d3.selectAll('.ajax-loader').style('display', 'none');
    });
  };


  this.switch_region = function(region_type) {
    Options.active_map_region = [];
    Options.region_type = region_type;
    if (region_type == 'regional') {
      color_map = region_codes;
      d3.select('#map')
        .style('display', 'block');
      d3.selectAll('#models li')
        .classed('active', false)
        .attr('style', '');
      d3.select('#'+Options.active_model)
        .classed('active', true);
    } else if (region_type == 'global') {
      d3.selectAll('.land').style('fill', '#3ABF96');
      d3.selectAll('.water').style('fill', '#A3D3E8');
      color_map = model_codes;
      d3.selectAll('#models li')
        .classed('active', false);
      d3.select('#map')
        .style('display', 'none');
    }
    this.redraw(Options.active_model, Options.active_rcp);
  };


  this.draw_histogram = function(data) {
    var histodata = d3.layout.histogram()
      .bins(y.ticks(y_axis_ticks.ticks()[0]))
      (data);
    histobars = histogram.selectAll('.bar')
      .data(histodata)
    histobars.enter()
//      .append('g');
      .append('rect');

    histobars.attr('class', 'bar')
      .attr('transform', function(d, i) {
        var _w = width - (width * (d.y / histodata.length)),
          _h
        ;
        _h = Math.abs(y(0) - y(histodata[0].dx)) * (histodata.length - i);
        _h = Math.abs(y(d.x+ d.dx));
        return 'translate(' + _w + ',' + _h + ')';
      });
    histobars//.append('rect')
      .attr('x', 1)
      .attr('height', function(d, i) {
        return Math.abs(y(0) - y(histodata[0].dx));
      })
      .attr('width', function(d, i) {
        return width * (d.y / histodata.length);
      })
      .style('fill', '#dddddd')
    ;
    histobars.exit()
      .remove();
//    bar.append("text")
//      .attr("dy", ".75em")
//      .attr("y", 6)
//      .attr("x", x(histodata[0].dx) / 2)
//      .attr("text-anchor", "middle")
//      .text(function(d) { return formatCount(d.y); });

  };

}
/*
 Instantiate graph and draw on page load.
 */
var output = new Output();
output.build('CCSM4', 'RCP26');