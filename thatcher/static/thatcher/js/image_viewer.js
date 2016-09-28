(function() {
  const BLUR_RADIUS = 10;

  function relativeEventPosition(event, element) {
    var pos = element.offset();
    return {x: event.pageX - pos.left, y: event.pageY - pos.top};
  }
  function dragPositionsToRect(pos1, pos2) {
    var width, x;
    if (pos2.x >= pos1.x) {
      width = pos2.x - pos1.x;
      x = pos1.x;
    } else {
      width = pos1.x - pos2.x;
      x = pos2.x;
    }
    
    var height, y;
    if (pos2.y >= pos1.y) {
      height = pos2.y - pos1.y;
      y = pos1.y;
    } else {
      height = pos1.y - pos2.y;
      y = pos2.y;
    }

    return {x: x, y: y, height: height, width: width};
  }

  var selections = [];
  var lockedIn = false;
  var saved = false;

  var imageField = $('#image_field');
  imageField.on('mousedown', function(e) {
    if (!lockedIn) {
      if (e.button === 0) {
        var clickPosition = relativeEventPosition(e, $(this));

        var selectionDiv = $('<div/>', {
          class: 'selection',
          style: ('left:' + String(clickPosition.x) + 'px;')
                  + ('top:' + String(clickPosition.y) + 'px;')
        });
        selectionDiv.appendTo(imageField);

        function positionSelectionDiv(rect) {
          selectionDiv.css({'left'   : String(rect.x) + 'px',
                            'top'    : String(rect.y) + 'px',
                            'width'  : String(rect.width) + 'px',
                            'height' : String(rect.height) + 'px'});
        }

        $('body').on('mousemove', function(e) {
          var rect = dragPositionsToRect(clickPosition,
                                         relativeEventPosition(e, imageField));
          positionSelectionDiv(rect);
        });

        function deactivate() {
          $('body').off('mousemove');
          $('body').off('mouseup');
          $('body').off('mouseleave');
        };
        function cancel() {
          deactivate();
          selectionDiv.remove();
        }

        $('body').on('mouseup', function(e) {
          if (e.button === 0) {
            var pos = relativeEventPosition(e, imageField);
            var rect = dragPositionsToRect(clickPosition, pos);
            positionSelectionDiv(rect);

            if (pos.x >= BLUR_RADIUS
                && pos.x <= imageField.width() - BLUR_RADIUS
                && pos.y >= BLUR_RADIUS
                && pos.y <= imageField.height() - BLUR_RADIUS) {
              deactivate();
              selections.push(rect);
            } else {
              cancel();
            }
          }
        });
        $('body').on('mouseleave', cancel);
      }
    }
  });

  function reset() {
    selections = [];
    $('#image_field div').remove();
    lockedIn = false;
    $('#image_field').removeClass('unrotated');
    $('#image_field').removeClass('rotated');
    $('#rotate_button').removeClass('disabled');
    $('#rotate_back_button').addClass('disabled');
    $('#save_button').addClass('inactive');
    $('#save_button').text('Save')
  }

  var imageChooserButtons = $('#image_chooser li').on('click', function(e) {
    if ($(this).data('image-name') !== $('#image_field').data('image-name')) {
      $('#image_chooser li.selected').removeClass('selected');
      $(this).addClass('selected');
      imageField.css('background-image', "url( " + $(this).data('image-url') + ")");
      imageField.data('image-name', $(this).data('image-name'));
      $('#image_description').text($(this).data('image-description'))
      reset();
    }
  });

  $('#reset_button').click(reset);

  $('#rotate_button').click(function() {
    var selectionDivs = $('#image_field > div.selection')
    selectionDivs.removeClass('selection');
    selectionDivs.addClass('rotated');
    selectionDivs.each(function() {
      $(this).css('background-position', '-' + $(this).css('left') + ' -' + $(this).css('top'));
    })

    $('#image_field').addClass('rotated');
    $('#save_button').removeClass('inactive')

    lockedIn = true;
    
    $(this).addClass('disabled');
    $('#rotate_back_button').removeClass('disabled');
  });

  $('#rotate_back_button').click(function() {
    $('#image_field').addClass('unrotated');
    $('#image_field').toggleClass('rotated');

    $('#rotate_button').removeClass('disabled');
    $('#rotate_back_button').addClass('disabled');
  })

  $('#save_button').click(function() {
    if (lockedIn && !saved) {

      var submit_data = {selections: selections,
                   image_name: imageField.data('image-name')}
      var xhttp = new XMLHttpRequest();
      xhttp.open("GET",
        submit_url
        + '?user_id=' + user_id
        + '&content=' + window.btoa(JSON.stringify(submit_data)),
        true);
      xhttp.send();

      $(this).addClass('inactive');
      $(this).text('Saved!')
    }
  })

}).call(this);
