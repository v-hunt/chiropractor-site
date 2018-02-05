(function ($) {
    'use strict';
	
    // magnific-popup active code 
    if ($.fn.magnificPopup) {
        $('.magnific-popup').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            }
        });
	// Video Btn Code
	$('.video_btn').magnificPopup({
		disableOn: 0,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: true,
		fixedContentPos: false
	});
    }

    // counterup active code
    if ($.fn.counterUp) {
        $('.counter').counterUp({
            delay: 10,
            time: 3000
        });
    }

    // ScrollUp Active Code
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 2000,
            easingType: 'easeInOutQuart',
            scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>'
        });
    }

    // MatchHeight Active Code
    if ($.fn.matchHeight) {
        $('.item').matchHeight();
    }

    // meanmenu active code
    if ($.fn.meanmenu) {
        $('.main_menu_area .mainmenu nav').meanmenu();
    }

    // wow active code
    new WOW().init();

    // PreventDefault a click
    $("a[href='#']").on('click', function ($) {
        $.preventDefault();
    });

    // countdown active code
    $('[data-countdown]').each(function () {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function (event) {
            $(this).find(".days").html(event.strftime("%D"));
            $(this).find(".hours").html(event.strftime("%H"));
            $(this).find(".minutes").html(event.strftime("%M"));
            $(this).find(".seconds").html(event.strftime("%S"));
        });
    });

	// Pre loader
	if ( !$("html").is(".ie6, .ie7, .ie8") ) {
		$("#preloader").delay(1000).fadeOut("slow");
	}
	else {
		$("#preloader").css("display","none");
	}

	// Nivo Slider
	$('#slider').nivoSlider({
		prevText: '<i class="fa fa-angle-left"></i>',
		nextText: '<i class="fa fa-angle-right"></i>',
		controlNav: false,
	});

})(jQuery);