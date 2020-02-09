document.addEventListener("DOMContentLoaded", function(event) { 
    
    // code adapted from https://codereview.stackexchange.com/questions/177945/convert-rating-value-to-visible-stars-using-fontawesome-icons
    // author of answer with UID "I wrestled a bear once"
    
    // Round the ratings to nearest half
    
    let ratings = Math.round(parseFloat(average_ratings) * 2) / 2;
    
    let returnedStars = [];
    
    let starRatingsConversion = convertToStars(ratings);
    
    function convertToStars(ratings) {
        // Append all the filled whole stars
        for (var i = ratings; i >= 1; i--) {
            returnedStars.push('<i class="fas fa-star" style="color: gold;"></i>&nbsp;');
        }
        
        // If there is a half a star, append it
        if (i == .5) {
            returnedStars.push('<i class="fas fa-star-half-alt" style="color: gold;"></i>&nbsp;');
        }
        
        // Fill the empty stars
        for (let i = (5 - ratings); i >= 1; i--) {
            returnedStars.push('<i class="far fa-star" style="color: gold;></i>&nbsp;');
        }
        
        return returnedStars.join('');   
    }
    
    $("#starRating").append(starRatingsConversion);
    
});
