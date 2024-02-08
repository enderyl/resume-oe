//init

function colorswitch(){
    //list to store values
    var storage = [];

    //hex value is 6 characters, which can range from 0-9 to a-f -- so it runs 6 times
    for(var i=0;i<6;i++){
        //random number, 0-9
        var num = Math.floor(Math.random() * 10);

        //if the number is 0-5, 
        if(num < 6){
            //50/50 shot to become a letter
            var coinflip = Math.floor(Math.random() * 2);
            //if 0, num becomes letter equiv (0 -> A)
            if(coinflip == 0){
                //number+65 to match to equivalent
                num = num + 65;
                num = num.toString();
                var letter = String.fromCharCode(num);
                //store the letter to the hex value (storage)
                storage[i] = letter;
            }else{
                //store the number, unchanged, to the hex value (storage)
                storage[i] = num;
            }
        }else{
            //store the number, 6-9, to the hex value (storage)
            storage[i] = num;
        }
    }

    //link the hex list (storage) to one word
    var storstring = storage.join("");
    //add #
    var hex = "#" + storstring;
    var place = document.getElementById('content');
    var placekids = place.children;

    //make background color the created hex value
    document.body.style.backgroundColor = hex;
    
    /* for every DIRECT child of #content, create a 
     * matching border (same color).
     * sample code:
     * parent element > BORDER ADDED >  unaffected
     *     #content   >      div     >    p
     */
    for(var i=0;i<placekids.length;i++){
        var current = placekids[i];
        current.style.cssText = "border:2px solid "+hex+"; border-radius:20px;";
    }
}

$(function(){
    var $button = $("#button");
    //get color when site is ready
    colorswitch();

    $("#tooltip").hide();
    $("#textfind").hover(
        function(e){
            $("#tooltip").show();
        },
        function(e){
            $("#tooltip").hide();
        }
    )

    $button.on("click", function(){
        //when button is clicked, new color
        colorswitch();
    });
});
