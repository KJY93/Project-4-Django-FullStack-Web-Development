document.addEventListener("DOMContentLoaded", function(event) { 
    
   $("#EnquiryResetButton").click(function() { 
        // reset and clear the form    
       $("#enquiryForm").trigger("reset");
   });
});
