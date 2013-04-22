function Output() {
  var factor = 1,
    margin = {top: 0, right: 0, bottom: 0, left: 0},
    padding = {top: 40, right: 40, bottom: 0, left: 0},
    outer_width = 676,
    outer_height = 352,
    width = outer_width - padding.left - padding.right,
    height = outer_height - padding.top - padding.bottom,
    default_domain = {
      relative: {min_domain: -.1, max_domain: 2.5, offset: 0},
      absolute: {min_domain: 230 - 273.15, max_domain: 305 - 273.15,
                 offset: 273.15}
    }
    min_domain = default_domain.relative.min_domain,
    max_domain = default_domain.relative.max_domain,
    offset = default_domain.relative.offset,
    start_year = 2005,
    end_year = 2100,
    x = d3.scale.linear().domain([start_year, end_year]).range([0, width]),
    y = d3.scale.linear().domain([max_domain, min_domain]).range([0, height]),
    svg = d3.select("#output div").append("svg")
      .attr("width", width + padding.left + padding.right)
      .attr("height", height + padding.top + padding.bottom),
    graph = svg.append('g')
      .attr("transform", "translate(" + padding.left + "," + padding.top + ")"),
    line = d3.svg.line()
      .x(function(d,i) { return x(i+2005); })
      .y(function(d,i) {
        return y(d-offset); }),
    x_axis_ticks = d3.svg.axis()
      .scale(x)
      .orient('top')
      .tickSize(0)
      .tickPadding(5)
      .tickFormat(d3.format('C')),
    y_axis_ticks = d3.svg.axis()
      .scale(y)
      .tickSize(0)
      .tickPadding(5)
      .orient('right'),
    data
    ;
  function draw_axes() {
    svg.selectAll('.axis').remove();
    svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + padding.top + ")")
      .call(x_axis_ticks);
    svg.append("g")
      .attr("class", "y axis")
      .attr("transform", "translate(" + width + "," + padding.top + ")")
      .call(y_axis_ticks);
  }
  function get_data(rcp) {
    /*
    Get temperature data based on temp_type (absolute|relative).
     */
    var data = [],
      offset;
    var o = output_data.filter(function(el) {
      return el.name == rcp;
    })[0]['output'];
    for (i=0;i<o.length;i++) {
      data[i] = o[i][Options.temp_type];
    }
    return data;
  }
  this.get_inactive = function() {
    return false;
  };
  this.get_active = function() {
    /*
    Get active regions from map
    */
    var active = '',
      regions = Options.active_map_region,
      rcp = Options.active_rcp
      ;
    if (regions.length > 0) {
      for (i=0;i<regions.length;i++) {
        active += ('.'+regions[i]+',');
      }
    } else {
      return false;
    }
    return d3.selectAll(active.slice(0,-1));
  };
  this.get_active_domain = function() {
    /*
    Get domain of active regions
     */
    var active = this.get_active(),
      thisdata = data,
      min = [], max = [];

    if (!active) {
//      thisdata = active.data();
//      return [max_domain, min_domain];
    } else {
      thisdata = data
    }
    for (i=0;i<thisdata.length;i++) {
      min.push(d3.min(thisdata[i]) - offset);
      max.push(d3.max(thisdata[i]) - offset);
    }
    return [
      Math.ceil(d3.max(max)*10)/10,
      Math.floor(d3.min(min)*10)/10
    ]
  };
  this.draw = function draw_output(rcp) {
    /*
    Draw temperature graph. Only called on page load, otherwise we use
    redraw().
     */
    data = get_data(rcp);
    y.domain(this.get_active_domain());
    graph.selectAll('path').
      data(data)
      .enter().append('path')
      .attr("d", line)
      .style('stroke-width', '2px')
      .classed('output-path', true)
      .each(function(d, i) {
        var region = output_data.filter(function(el) {
          return el.name == rcp;
        })[0]['output'][i]['region'];
        d3.select(this).classed(region, true);
      })
    ;
    draw_axes();
  };
  this.redraw = function redraw_output(r) {
    /*
    Redraw temperature graph.
     */
    if (!(r)) { r = Options.active_rcp; }

    data = get_data(r);
    var active = this.get_active();
    graph.selectAll('path')
      .data(data)
    ;
    y.domain(this.get_active_domain());
    graph.selectAll('path')
      .transition()
      .duration(300)
      .attr("d", line);
    graph.selectAll('path')
      .style('stroke-width', function() {
        if (!active) {
          return '2px';
        }
        return '0';
      })
    ;
    if (active) {
      active.style('stroke-width', '3px');
//      graph.selectAll('circle')
//        .data(active.data()).enter()
//        .append('circle')
//        .attr('r', 5)
//        .attr('cx', function(d, i) {return x(i+2005);})
//        .attr('cy', function(d, i) {console.log(d, i); return y(d[i]);})
//        .style('fill', 'none')
//        .style('stroke', 1)
//        .style('pointer-events', 'all')
//        .append('title')
//        .text(function(d) {return d;})
    }
    draw_axes();
  };
  this.colorize = function(region, color) {
    /*
    Colors temperature path that corresponds to geographic region. Only
    called when regions are clicked.
     */
    d3.select('.output-path.'+region)
      .style('stroke', color)
      .style('stroke-width', '3px')
    ;
  };
  this.graph = graph;
}
output = new Output();
output.draw(Options.active_rcp);