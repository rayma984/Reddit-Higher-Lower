//hides the leaving_id div and shows the entering_id div
function show_menus(entering_id, leaving_id) {

    //show the entering, hide the leaving
    document.getElementById(entering_id).style.display = 'block';
    document.getElementById(leaving_id).style.display = "none";
}
