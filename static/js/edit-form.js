document.addEventListener("DOMContentLoaded", function(event) {
    
    // loop through all the books to get each book new quantity
    for (let i = 0; i < row_of_record; i++) {
        $(`#qty${i+1}`).on('keyup input', function() {
            var newqty = $(`#qty${i+1}`).val();
            var bookId = $(`#book_id${i+1}`).val();
            var qtyInCart = parseInt($("#qtyInCart").text());

            $.ajax({
                type: 'get',
                dataType: 'json',
                url: 'update/' + bookId,
                data: {
                    'newqty': newqty,
                    'bookId': bookId,
                    'divId':i+1
                },
                success: function(response) {
                    $(`#totalBookPrice${response[i]['row_id']}`).text("$" + response[i]["total_price"]);
                    $(`#qtyAvailable${response[i]['row_id']}`).text(response[i]["available_quantity"] + " available");
                    $("#qtyInCart").text(response[row_of_record]['new_total_quantity']);
                    $("#total_payable_amount").text(response[row_of_record+1]['new_total_amount']);
                }
            });
        });
    }
});