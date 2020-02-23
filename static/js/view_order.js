document.addEventListener("DOMContentLoaded", function(event) {
    $.fn.DataTable.ext.pager.numbers_length =5;
    $("#purchaseTable").DataTable();
} );