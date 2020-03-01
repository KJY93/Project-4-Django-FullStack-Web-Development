// Code to auto-initialize bootstrap-select using Snapappointments plugin
// Credit to Snappointments - https://github.com/snapappointments/bootstrap-select/

document.addEventListener("DOMContentLoaded", function(event) {
    
    // initialize the price slider range
    $("#price_range").ionRangeSlider({
        type: "double",
        grid: true,
        min: 0,
        max: 200,
        from: 0,
        to: 0,
        prefix: "$"
    });
    
    // save the slider instance to a variable so that it can be called later
    // to reset the slider price range upon cliking the reset button and also to get the min and max price selected
    var slider = $("#price_range").data("ionRangeSlider");
        
    // initialize the bootstrap-select plugin
    $("#genreFilter").selectpicker();
    $("#authorFilter").selectpicker();
    
    // if reset button is clicked
    // remove the selected attribute on option tag 
    // and reset the option title to Genre and Author respectively
    $("#resetButton").click(function() {
        
        $("#genreFilter option:selected").prop("selected", false);
        $("#authorFilter option:selected").prop("selected", false);
        
        $('#genreFilter').selectpicker({title: 'Genre'}).selectpicker('render');
        $('#authorFilter').selectpicker({title: 'Author'}).selectpicker('render');
        
        // Fire reset button for price range slider
        slider.reset();

    });
    
    // AJAX call to query and display the books based genre / author / price
    $("#searchButton").click(function() {
        
        // clear the #bookFilteredResult everytime the search button is clicked
        $("#bookFilteredResult").empty();
        
        // 0902 get price selected
        // get min and max price selected
        var from_price = slider.result.from;
        var to_price = slider.result.to;
        
        let genre_selected = $('#genreFilter').val();
        let author_selected = $('#authorFilter').val();
        
        $.ajax({
            url: "./",
            type:'GET',
            data: {
                'from_price': from_price,
                'to_price': to_price,
                'genre_selected': genre_selected,
                'author_selected': author_selected
            },
            dataType: 'html',
            success: function (response) {
                console.log(response);
                $('#bookFilteredResult').html(response);
            }
        });
    });
});
