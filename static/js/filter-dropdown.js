// Code to auto-initialize bootstrap-select using Snapappointments plugin
// Credit to Snappointments - https://github.com/snapappointments/bootstrap-select/

document.addEventListener("DOMContentLoaded", function(event) {
    
    // initialize the price slider range
    $("#price_range").ionRangeSlider({
        type: "double",
        grid: true,
        min: 0,
        max: 1000,
        from: 0,
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
            url: absolute_path_uri,
            type:'GET',
            data: {
                // 0902
                'from_price': from_price,
                'to_price': to_price,
                
                'genre_selected': genre_selected,
                'author_selected': author_selected
            },
            dataType: 'json',
            success: function (response) {
                
                // declare an empty array to store the book title id
                let book_title_id = [];
                
                // loop through the JSON response and save the book title id to the empty array declared above
                for (let item = 0; item < response.length; item++) {
                    book_title_id.push(response[item]['id']);
                }
                
                let book_id_record = [];
                let book_item_record = [];
                          
                for (let rec = 0; rec < response.length; rec++) {
                    // save the book record to the array if the record is unique
                    if (book_id_record.includes(response[rec]['id']) !== true) {
                        book_id_record.push(response[rec]['id']);
                        book_item_record.push({'id':response[rec]['id'] , 'author':[response[rec]['author__name']] ,'title':response[rec]['title'], 'price':response[rec]['price'], 'image':response[rec]['image']});                     
                    }
                    else {
                        // loop through all the records
                        // if multiple author exist for a book, proceed to add it to the author list of that book
                        for (let j=0; j < book_item_record.length; j++) {
                            if (response[rec]['id'] === book_item_record[j]['id']) {
                                book_item_record[j]['author'].push(response[rec]['author__name']);
                            } 
                        }
                    }
                }
                
                // loop the book_item_record and populate the products page
                for (let k = 0; k < book_item_record.length; k++) {
                    $("#bookFilteredResult").append(
                        `<div class="col-sm-12 col-md-6 col-lg-4 mt-3">
                            <div class="card itemImg" id="allBooks">
                                <img class="card-img-top" src=${book_item_record[k]['image']} alt="book image for ${book_item_record[k]['title']}">
                                <div class="card-body">
                                    <h5 class="card-title">${book_item_record[k]['title']}</h5>
                                    <p class="card-text">
                                        <div class="author">
                                            by ${book_item_record[k]['author']}
                                        </div>
                                        
                                        <div class="price">
                                            $${book_item_record[k]['price']}
                                        </div>                
                                    </p>
                                </div>
                            </div>
                        </div>`                    
                    );
                }
            }
        });
    });
});
