let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:


function generateTarget() {
	var randomval = Math.floor(Math.random() * 10);  

	return randomval;
}

function getAbsoluteDistance(guess,secretval) {
		var userval = 0;  

	if(guess <= secretval) {
		userval = secretval - guess;
	}
	else {
		userval = guess - secretval;
	}

	return userval;
}


function compareGuesses(userguess,computerguess,secretval) {
	var userval = 0;  
	var computerval = 0;  
	var boolchecker = false;

	if(userguess <= secretval) {
		userval = getAbsoluteDistance(userguess,secretval);
	}
	else {
		userval = getAbsoluteDistance(userguess,secretval);
	}

	if(computerguess <= secretval) {
		computerval = getAbsoluteDistance(computerguess,secretval);
	}
	else {
		computerval = getAbsoluteDistance(computerguess,secretval);
	}


	if(userval == computerval) {
		boolchecker = true;
	}
	else if(userval > computerval) {
		boolchecker = false;
	}
	else {
		boolchecker = true;
	}

	return boolchecker;
}


function updateScore(winner) {
	if(winner === "human") {
		humanScore = humanScore +1;
	}
	else {
		computerScore = computerScore + 1;
	}
}


function advanceRound() {
	currentRoundNumber = currentRoundNumber +1;
}


document.getElementById("human-guess").onchange = function() {

var inputval = document.getElementById("human-guess").value;

if(inputval > 9) {
alert("Please input value between 0 - 9");
document.getElementById("human-guess").value = 0;
}
else if(inputval < 0) {
alert("Please input value between 0 - 9");
document.getElementById("human-guess").value = 0;
}


};




