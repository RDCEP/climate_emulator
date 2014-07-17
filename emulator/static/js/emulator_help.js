d3.selectAll('.help-button')
  .on('mouseover', function() {
    var help = d3.select(this)
      .attr('id') + '-text';
    d3.select('#'+help)
      .style('display', 'block')
      .style('left', function() {
//        return d3.event.x + 'px';
        return d3.mouse(document.getElementById('wrapper'))[0] + 20 + 'px';
      })
      .style('top', function() {
//        return d3.event.y + 'px';
        return d3.mouse(document.getElementById('wrapper'))[1] - 20 + 'px';
      });

  })
  .on('mouseout', function() {
    var help = d3.select(this)
      .attr('id') + '-text';
    d3.select('#'+help)
      .style('display', 'none');
//      .style('left')
  });