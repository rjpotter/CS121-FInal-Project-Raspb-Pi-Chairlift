var forwardButton = $("#forward_button");
var reverseButton = $("#reverse_button");
var slowButton = $("#slow_button");

forwardButton.click(function() {
    console.log(forwardButton.text());
    if (forwardButton.text() === "Spinning Forward") {
        $.ajax({
            url: "/forward_on",
            type: "post",
            success: function(response) {
                console.log(response);
                forwardButton.text("Forward");
            }
        });
    } else {
        $.ajax({
            url: "/forward_off",
            type: "post",
            success: function() {
                forwardButton.text("Spinning Forward");
            }
        })
    }
});

reverseButton.click(function() {
    console.log(reverseButton.text());
    if (reverseButton.text() === "Spinning Reverse") {
        $.ajax({
            url: "/reverse_on",
            type: "post",
            success: function(response) {
                console.log(response);
                reverseButton.text("Reverse");
            }
        });
    } else {
        $.ajax({
            url: "/reverse_off",
            type: "post",
            success: function() {
                reverseButton.text("Spinning Reverse");
            }
        })
    }
});

slowButton.click(function() {
    console.log(slowButton.text());
    if (slowButton.text() === "Slow Down") {
        $.ajax({
            url: "/slow",
            type: "post",
            success: function(response) {
                console.log(response);
                slowButton.text("Full Speed");
            }
        });
    } else {
        $.ajax({
            url: "/forward_on",
            type: "post",
            success: function(response) {
                console.log(response);
                slowButton.text("Slow Down");
            }
        });
    }
});

