function Output() {
    var factor = 1,
        width = 636*factor,
        height = 312*factor,
        margin = 0,
        start_year = 2005,
        end_year = 2100,
        x = d3.scale.linear().domain([start_year, end_year]).range([0 + margin, width - margin]),
        y = d3.scale.linear().domain([305, 250]).range([0 + margin, height]),
        svg = d3.select("#output").append("svg")
            .attr("width", width)
            .attr("height", height),
        graph = svg.append('g'),
        line = d3.svg.line()
            .x(function(d,i) { return x(i+2005); })
            .y(function(d,i) {
                return y(d); })
        ;
    function get_data(rcp) {
        var data = [];
        var o = output_data.filter(function(el) {
            return el.name == rcp;
        })[0]['output'];
        for (i=0;i< o.length;i++) {
            data[i] = o[i]['values'];
        }
        return data;
    }
    this.get_inactive = function() {
        return false;
    };
    this.get_active = function() {
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
        var active = this.get_active();
        if (!active) {
//            active = d3.selectAll('.output-path');
            return [305,250];
        }
        var max = [],
            min = [],
            data = active.data()
        ;
        for (i=0;i<data.length;i++) {
            
            min.push(d3.min(data[i]));
            max.push(d3.max(data[i]));
        }
        return [
            Math.ceil(d3.max(max)),
            Math.floor(d3.min(min))
        ]
    };
    this.draw = function draw_output(rcp) {
        data = get_data(rcp);
        y.domain(this.get_active_domain());
        graph.selectAll('path').
            data(data)
            .enter().append('path')
            .attr("d", line)
            .classed('output-path', true)
            .each(function(d, i) {
                var region = output_data.filter(function(el) {
                    return el.name == rcp;
                })[0]['output'][i]['region'];
                d3.select(this).classed(region, true);
            })
        ;
    };
    this.redraw = function redraw_output(r) {
        if (!(r)) { r =  Options.active_rcp; }
        y.domain(this.get_active_domain());
        data = get_data(r);
        var active = this.get_active(),
            sw
        ;
        if (!active) {
            sw = '1px';
        } else {
            sw = '0';
        }
        graph.selectAll('path')
            .data(data)
            .attr("d", line)
            .style('stroke-width', sw)
        ;
        if (active) {
            active.style('stroke-width', '3px');
        }
    };
    this.colorize = function(region, color) {
        d3.select('.output-path.'+region)
            .style('stroke', color)
            .style('stroke-width', '3px')
        ;
    }
}
output = new Output();
output.draw(Options.active_rcp);
