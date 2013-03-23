/*!
 * base.js
 */


$(function(){
    
    $(".stars li").hover(function(){
        var num =  $(this).index()
        active_stars(num)
    }, function(){
        $(".stars li").removeClass("hover")
    })


    function active_stars(num){
        for (var i=0; i<=num; i++){
            $(".stars li").eq(i).addClass("hover")
        }
    }

});
