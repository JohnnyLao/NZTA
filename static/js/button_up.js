$(window).scroll(function() {
        if ($(this).scrollTop() >= 250) {
            $('#scrollToTopButton').fadeIn();
            $('#scrollToTopButton').addClass('animated-button');
        } else {
            $('#scrollToTopButton').fadeOut();
            $('#scrollToTopButton').removeClass('animated-button');
        }
    });