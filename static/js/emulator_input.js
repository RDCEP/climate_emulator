function Input() {
    var factor = 1,
        width = 150*factor,
        height = 150*factor,
        margin = 0,
        start_year = 2005,
        end_year = 2100,
        x = d3.scale.linear().domain([start_year, end_year]).range([0 + margin, width - margin]),
        y = d3.scale.linear().domain([1200, 0]).range([0 + margin, height]),
        input_labels = ['RCP26', 'RCP45', 'RCP60', 'RCP85']
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
    
    this.draw = function() {
        for (i=0;i<input_labels.length;i++) {
            var id = '#'+input_labels[i],
                svg = d3.select(id).append("svg")
                    .attr("width", width)
                    .attr("height", height)
                ;
                d3.select(id)
                    .on('click', function(d, i) {
                        Options.active_rcp = d3.select(this).attr('id');
                        output.redraw(Options.active_rcp);
                        var ob = d3.select(this);
                        d3.selectAll('#input div').classed('active', false);
                        ob.classed('active', true);
                    });
                var graph = svg.append('g'),
                line = d3.svg.line()
                    .x(function(d,i) { return x(i+2005); })
                    .y(function(d) { return y(d); })
            ;
            var o = input_data[i];
            graph.append('path')
                .attr("d", line(o))
                .classed('input-path', true)
            ;
        }
    }
}
input = new Input();
input.draw();
