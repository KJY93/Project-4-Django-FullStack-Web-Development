$(document).ready(function() {
    
    // best sellers book slider
    $('.bestSellers').slick({
        autoplay: true,
        arrows: true,
        slidesToShow: 7,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1020,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 425,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });

    // new and trending book slider
    $('.newAndTrending').slick({
        autoplay: true,
        arrows: true,
        slidesToShow: 7,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1020,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 425,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    
    // best deal book slider
    $('.bestDeal').slick({
        autoplay: true,
        arrows: true,
        slidesToShow: 7,
        slidesToScroll: 1,
        responsive: [{
                breakpoint: 1020,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 425,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
    
})

	