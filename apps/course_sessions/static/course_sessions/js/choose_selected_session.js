var picker = document.getElementById("session-picker");
var selected = selectedOption();
function updateLink(){
    selected = selectedOption();
}
function selectedOption(){
    return (picker.options[picker.selectedIndex].value);
}