var pt = '<div class="data-dz-preview data-dz-file-preview">' +
        '<div class="data-dz-details"><span class="data-dz-filename">' +
        '<span data-dz-name></span></span> [<span class="data-dz-size" data-dz-size>' +
        '</span>]<div class="data-dz-progress">' +
        '<span class="data-dz-upload" data-dz-uploadprogress></span></div>' +
        '<span class="data-dz-success-mark"><span></span></span>' +
        '<span class="dz-error-mark"><span></span></span>' +
        '<div class="dz-error-message"><span data-dz-errormessage></span></div>' +
        '</div>';
$('form').dropzone({
  paramName: 'csv',
  acceptedFiles: 'text/csv',
  uploadMultiple: false,
  addRemoveLinks: true,
  previewTemplate: pt,
  success: function(file, response) {
    window.response = response;
    window.input_data[4] = response['input'];
    input.draw('CUSTOM', {left:0, right:0, top:0, bottom:0});
  }
});