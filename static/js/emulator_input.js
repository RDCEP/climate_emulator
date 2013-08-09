function Input() {
  var factor = 1,
    width = 150,
    height = 100,
    margin = 0,
    start_year = 2005,
    end_year = 2100,
    x = d3.scale.linear().domain([start_year, end_year]).range([0 + margin, width - margin]),
    y = d3.scale.linear().domain([1200, 0]).range([0 + margin, height]),
    input_labels = [
      {label: 'RCP26', top: 0, right: 0, bottom: 0, left: 40},
      {label: 'RCP45', top: 40, right: 0, bottom: 0, left: 0},
      {label: 'RCP60', top: 0, right: 0, bottom: 0, left: 40},
      {label: 'RCP85', top: 0, right: 0, bottom: 0, left: 0}
    ],
    x_axis_ticks = d3.svg.axis()
      .scale(x)
      .orient('top')
      .tickFormat(d3.format(''))
      .ticks(2)
      .tickSize(0)
      .tickPadding(5)
      .tickValues([2005,2100]),
    y_axis_ticks = d3.svg.axis()
      .scale(y)
      .orient('left')
      .tickFormat(d3.format(''))
      .ticks(2)
      .tickSize(0)
      .tickPadding(5)
      .tickValues([0,1200]),
    rel_temp = d3.select('#relative-temp')
      .on('click', function(d, i) {
        Options.temp_type = 'relative';
        output.redraw(Options.active_model, Options.active_rcp);
        d3.select(this).classed('active', true);
        abs_temp.classed('active', false);
      }),
    abs_temp = d3.select('#absolute-temp')
      .on('click', function(d, i) {
        Options.temp_type = 'absolute';
        output.redraw(Options.active_model, Options.active_rcp);
        d3.select(this).classed('active', true);
        rel_temp.classed('active', false);
      }),
    global = d3.select('#global')
      .on('click', function() {
        d3.event.preventDefault();
        output.switch_region();
      })
    ;


  this.get_inactive = function (region) {
    region = ((region != null) ? region : Options.active_map_region);
    return d3.selectAll('.output-path').filter(function(d, i){
      if (Options.active_map_region.indexOf(d3.select(this).classed()) > -1) {
//            if (!(d3.select(this).classed(region))) {
        return false;
      } else {
        return this;
      }
    });
  };


  this.draw_initial = function() {
    var models = d3.select('#models ul')
      .selectAll('li')
      .data(model_names).enter()
      .append('li')
      .attr('id', function(d) {return d; })
      .classed('active', function(d) {
        return d == Options.active_model;
      });
    models.on('click', function(d, i) {
        var input_filter = d3.select(this);
        //TODO: Switch for global regions
        d3.event.preventDefault();
        if (Options.region_type == 'regional') {
          models.classed('active', false);
          input_filter.classed('active', true);
          Options.active_model = d;
          output.redraw(Options.active_model, Options.active_rcp);
        } else {
          output.change_input_filter(input_filter, d);
        }
      })
    ;
    models.append('a')
      .attr('href', function(d, i) { return '/' + d; })
      .html(function(d, i) { return d; })
    ;
    for (i=0;i<input_labels.length;i++) {
      var padding = {top: 0, right: 0, bottom: 0, left: 0};
      if ((i%2) == 0) padding.left = 40;
      if (i < 2) padding.top = 40;
      this.draw(input_labels[i].label, input_data[i], padding);
    }
  };


  this.draw = function(label, data, padding) {
    var id = '#'+label,
      obj = d3.select(id);
      obj.html('');
    var svg = obj.append("svg")
      .attr("width", width + padding.left + padding.right)
      .attr("height", height + padding.top + padding.bottom)
    ;
    d3.select(id)
      .on('click', function(d, i) {
        Options.active_rcp = d3.select(this).attr('id');
        d3.selectAll('#input div').classed('active', false);
        d3.select(this).classed('active', true);
        output.redraw(Options.active_model, Options.active_rcp);
      })
    ;
    var bkgd = svg.append('rect')
        .attr("width", width)
        .attr("height", height)
        .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
      ,
      graph = svg.append('g')
        .attr("transform", "translate(" + padding.left + "," + padding.top + ")"),
      line = d3.svg.line()
        .x(function(d,i) { return x(i+2005); })
        .y(function(d) { return y(d); }),
      x_axis = svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate("+ padding.left + "," + padding.top + ")")
        .call(x_axis_ticks),
      y_axis = svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + padding.left + "," + padding.top + ")")
        .call(y_axis_ticks)
    ;
    x_axis.selectAll('text')
      .attr('transform', function(d,i) {
        var _x = 15;
        if (i == 1) _x = -15;
        return "translate("+_x+",0)"
      });
    y_axis.selectAll('text')
      .attr('transform', function(d,i) {
        var _y = -10;
        if (i == 1) _y = 10;
        return "translate(0,"+_y+")"
      });
    graph.append('path')
      .attr("d", line(data))
      .classed('input-path', true)
    ;
  };
}
input = new Input();
input.draw_initial();