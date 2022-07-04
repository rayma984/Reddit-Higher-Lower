//get the element that shows the score
var score = 0
var score_element = document.getElementById("score");

function correct(){
    score += 1;
    score_element.innerHTML = score;
    console.log("correct: " + score);
}
