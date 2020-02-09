document.addEventListener("DOMContentLoaded", function(event) {    
    
    // Based on windows size, add the text-centering class to the div containing the image and book details in show_book_details.template.html file
    let mediaQuerysize = window.matchMedia("(max-width: 575.98px)");
    
    // recommit 0902 only use one container the main one
    function ElementDimension(e) {
        if (e.matches) {
            $(".bookDetailsContainer").addClass("text-center");
        }
        else {
            $(".bookDetailsContainer").removeClass("text-center");
        }
    }

    // Call the function at run time in order to resize the canvas element dimension
    ElementDimension(mediaQuerysize);

    // attach listener to respond on state changes
    mediaQuerysize.addListener(ElementDimension);

});