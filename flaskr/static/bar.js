$(document).ready(function() {
    $('.picsw').on('click', function() {
      $.getJSON($SCRIPT_ROOT +'/getbar', {
        'col': event.target.id
      }, function(data) {
        $("#barplot").attr('src',"data:image/gif;base64,"+(data.picture));
      });
      return false;
    });
  });
