(function($){
$.topbutton = function(op){
    var _op = {
        html : "Top",               //String (Html Code)
        css : undefined,            //String (Css Code)
        scrollSpeed : 150,          //Number (Default : 150)
        scrollAndShow : false      //boolean (Default : false)
    }
    for(key in op){ _op[key] = op[key]; }



    var basicCSS = {
            width : '45px',
            height : '45px',
            background : "#343a40",
            color : "#fff",
            right : '15px',
            bottom: '15px',
            border : "2px solid #495057",
            "border-radius" : '5px',
            "font-size" : '17px'
    };
    if(_op.css != undefined){
        var userCss  = {};
        var arr = op.css.split(";").filter(function(n){ return n != "" });
        for(key in arr){
            var index = arr[key].split(":");
            var uKey = index[0].replace(/(\s*)/g,"");
            var uValue = index[1].replace(/(\s*)/g,"");
            userCss[uKey] = uValue;
        }
        for(key in userCss){ basicCSS[key] = userCss[key]; }
    }
    var attr = "";
    for(key in basicCSS){ attr += key+':'+basicCSS[key]+'; '; }



    var scrollAndShow ="";
    if(_op.scrollAndShow){
        scrollAndShow ="display:none;";
        var px = 100;
        var on = true;
        $(window).scroll(function(){
            if($(this).scrollTop() > px){ if(!on){$('#topButton').fadeIn(); on = true;} }
            else{ if(on){$('#topButton').fadeOut(); on = false;} }
        });
        if($(window).scrollTop() > px){ scrollAndShow = "display:block;"; }
    }



    var html = '<button type="button" id="topButton" style="'+scrollAndShow+'position:fixed; border:none; outline:none; overflow:hidden; cursor:pointer; '+attr+'">'+_op.html+'</button>';
    $('body').append(html);



    $('#topButton').click(function(){
        $('html, body').animate({scrollTop : 0}, parseInt(_op.scrollSpeed));
    });
};
})(jQuery);
