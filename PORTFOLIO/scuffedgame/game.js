$('head').append("<style>body {width:800px; margin: auto} header, footer {text-align: center; height: 100px; line-height: 100px; background: lightblue} footer{clear: both} div {width:100px; height: 100px; float:left; background-color: #999; margin: 50px} .red {color:red;} .green{color:green} .blue{color:blue} .yellow{color:yellow} </style>");
$('body').prepend("<header><h1>How many tiles...? 8<input type=radio name=tilenumber value=8> 12<input type=radio name=tilenumber value=12> 16<input type=radio name=tilenumber value=16></h1></header><main></main><footer><h2></h2></footer>");

$(function(){
    
    /* each color is a class, ex: .red{color:red}. the color is not visible bc it's the text color; it's stored invisibly under a different selector. it will be converted to background color when clicked on. */
    var colors = ['red','blue','green','yellow','red','blue','green','yellow'];
    var colors1 = ['red','blue','green','yellow','red','blue','green','yellow','red','red','yellow','yellow'];
    var colors2 = ['red','blue','green','yellow','red','blue','green','yellow','red','blue','green','yellow','red','blue','green','yellow'];

    function shuffle(colors){
        let currentIndex = colors.length;

        //shuffle until there are no more elements to shuffle
        while (currentIndex>0) {
            //pick an element (that hasn't been removed)
            randomIndex = Math.floor(Math.random() * currentIndex);
            currentIndex--;

            //swap it with the element being held
            [colors[currentIndex], colors[randomIndex]] = [
            colors[randomIndex], colors[currentIndex]];
        }

        //credit to coolaj (+17 contributors) from stackoverflow, link below
        //https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
    }

    var $tileNum = $('input:radio');
    var $main = $('main');
    var newtile = ('<div></div>');
    initshuffle();

    function initshuffle(){
        //when the radio buttons are clicked
        $tileNum.on('click', function(){
            //remove everything inside of <main>
            $main.children().remove();

            //get value of button, loop appropriate div (tile) amt
            var amt = $(this).val();
            for(var i=0;i<amt;i++){
                $main.append(newtile).hide();
            };
            $main.each(function(index){
                $(this).delay(700*index).fadeIn(700);
            });


            //according to the amount, shuffle the appropriate list
            if(amt==8){
                shuffle(colors);
            }else if(amt==12){
                shuffle(colors1);
            }else{
                shuffle(colors2);
            }

            //assign each tile a color again based on #
            $('div').each(function(index){
                if(amt==8){
                    $(this).addClass(colors[index]);
                }else if(amt==12){
                    $(this).addClass(colors1[index]);
                }else{
                    $(this).addClass(colors2[index]);
                }
            });
        });
    }

    //when an object in main is clicked, the color is checked and changed to the background color
    $main.on('click', 'div', function(e){
        var $this = $(this);
        var current = $this.css('color');
        $this.css('background-color', current);
        //selected is a tracker class used a LOT in analyse()
        $this.addClass('selected');
        analyse();
    });

    //basically everything related to evaluating matches
    function analyse() {
        var opened = $('div.selected');
        var count =  $(opened).length; 
        if(count>=2){
            //check color values of both 'selected' tiles
            var first = $(opened[0]).css('color');
            var second = $(opened[1]).css('color');
            //if the same,
            if(first == second){
                //animate them disappearing
                $(opened).animate({
                    opacity: 0.0,
                }, 1000);
                $(opened).addClass('matched');

            }else{
                //if different, make them both revert to the og color
                //this took >2 hrs....why was it so simple....not perfect but whatever it works ig
                setTimeout(function(){$(opened).css('background-color','#999')} , 1000);
            }
            //reset selected # to 0
            $(opened).removeClass('selected');
        }
    }

});
