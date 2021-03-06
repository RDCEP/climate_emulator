var pt = '<div class="data-dz-preview data-dz-file-preview">' +
        '<div class="data-dz-details"><span class="data-dz-filename">' +
        '<span data-dz-name></span></span> [<span class="data-dz-size" data-dz-size>' +
        '</span>]<div class="data-dz-progress">' +
        '<span class="data-dz-upload" data-dz-uploadprogress></span></div>' +
        '<span class="data-dz-success-mark"><span></span></span>' +
        '<span class="dz-error-mark"><span></span></span>' +
        '<div class="dz-error-message"><span data-dz-errormessage></span></div>' +
        '</div>';
var emulator_dropzone = new Dropzone("form#dz", {
  paramName: 'csv',
  acceptedFiles: 'text/csv',
  uploadMultiple: false,
  addRemoveLinks: true,
  previewTemplate: pt,
  success: function(file, response) {
    d3.selectAll('.dz-error-message').remove();
    d3.selectAll('.data-dz-preview').remove();

    window.input_data[4] = response.input;
    input.draw('CUSTOM', response.input, {left:0, right:0, top:0, bottom:0});
    var event = document.createEvent("SVGEvents");
    event.initEvent("click",true,true);
    document.getElementById('CUSTOM').dispatchEvent(event);
  },
  error: function(file, error, xhr) {
    d3.selectAll('.dz-error-message').remove();
    d3.selectAll('.data-dz-preview').remove();

    var d = d3.select('#dz')
      .append('div')
      .attr('class', 'data-dz-preview dz-error-message');
    d.append('span')
      .attr('data-dz-errormessage', true)
      .text(error);
  }
});