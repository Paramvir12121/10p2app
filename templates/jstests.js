function startTimer() {
    // Get the current time
    var currentTime = new Date();
  
    // Calculate the elapsed time in seconds
    var elapsedTime = Math.floor((currentTime - startTime) / 1000);
    var freeTime = elapsedTime/5;
    // Update the timer element with the elapsed time
    document.getElementById("timer").innerHTML = elapsedTime;
    //document.getElementById("timer").innerHTML = freeTime;
  
    // Call this function again after 1 second
    setTimeout(startTimer, 1000);
  }
  
  // Set the start time to the current time
  var startTime = new Date();
  
  // Start the timer
  startTimer();