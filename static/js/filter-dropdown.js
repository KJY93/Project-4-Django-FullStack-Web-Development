// Code to auto-initialize bootstrap-select using Snapappointments plugin
// Credit to Snappointments - https://github.com/snapappointments/bootstrap-select/

document.addEventListener("DOMContentLoaded", function(event) {
        
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

        });
        
});