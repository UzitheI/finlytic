// var $grid = $('.grid').isotope({
//     itemSelector: '.card__room',
//     layoutMode: 'fitRows',
//     filter: ''
//   });
  
//   var filterFns = {


//   };
  

  $('.button-group').each(function (i, buttonGroup) {
    var $buttonGroup = $(buttonGroup);
    $buttonGroup.on('click', 'button', function () {
      $buttonGroup.find('.is-checked').removeClass('is-checked');
      $(this).addClass('is-checked');
    });
  });

  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 100) {
      $('.header').addClass('scrolled');
    } else {
      $('.header').removeClass('scrolled');
    }
  })

  $('input:not([type="checkbox"]), textarea').on('focus', function() {
    if ($(this).val().trim() !== '') {
      $(this).closest('.form-group').addClass('filled');
    }
}).on('blur', function() {
    if ($(this).val().trim() === '') {
      $(this).closest('.form-group').removeClass('filled');
    }
}).on('input', function() {
    if ($(this).val().trim() !== '') {
      $(this).closest('.form-group').addClass('filled');
    } else {
      $(this).closest('.form-group').removeClass('filled');
    }
});


  $('.password-toggler').on('click', function() {
    var inputField = $(this).siblings('input');
    var newType = inputField.attr('type') === 'password' ? 'text' : 'password';
    inputField.attr('type', newType);
    $(this).toggleClass('shown');
  });

$('#filter-btn').on('click', function() {

$(this).toggleClass('reverse');
  $('.filter-wrap').slideToggle(300);
  $('body').toggleClass('overflow-hidden');
})


$('.room-picture-slider').slick({
  infinite:true,
  arrows: true,
  slidesToShow: 1,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});