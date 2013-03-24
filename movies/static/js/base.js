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


    /*<Carousel>*/
    can_click = true
    var carousels =  {}
    carousel_init("carousel1", $("header .carousel_wrapper"))

    for (var crs in carousels){
        $("#"+crs+" .arrow").click(function(e){
            if(can_click){
                var classes = $(this).attr("class").split(" ")
                can_click = false
                var timer = setTimeout(function(){resetClick()}, 700)
                var crs_name = $(this).parent().attr("id")
                var obj = $("#"+crs_name)
                carousels[crs_name].l_margin = parseInt(obj.find("ul").css("margin-left"))
                
                if(classes.length > 1 && classes[1] == "right"){
                    if(Math.abs(carousels[crs_name].l_margin) < (carousels[crs_name].width) - obj.find(".carousel-inner").outerWidth()){
                        obj.find("ul").animate({
                            marginLeft: '-='+carousels[crs_name].item_with
                        }, 700)
                    }    
                }else{
                    if(carousels[crs_name].l_margin < 0){
                        obj.find("ul").animate({
                            marginLeft: '+='+carousels[crs_name].item_with
                        }, 700)
                    }
                }
                
            }
            return false
        })
        
        $("#"+crs+" .arrow").hover(function(){
            var classes = $(this).attr("class").split(" ")
            var crs_name = $(this).parent().attr("id")
            var obj = $("#"+crs_name)
            carousels[crs_name].l_margin = parseInt(obj.find("ul").css("margin-left"))
            if(classes.length > 1 && classes[1] == "right"){
                if(Math.abs(carousels[crs_name].l_margin) < (carousels[crs_name].width) - obj.find(".carousel-inner").outerWidth()){
                    $(this).addClass("hover")
                }
            }else{
                if(carousels[crs_name].l_margin < 0){
                    $(this).addClass("hover")
                }
            }
        }, function(){
            $(this).removeClass("hover")
        })
    }


    function carousel_init(crs_name, obj){
        carousels[crs_name] = {}
        carousels[crs_name].l_margin = 0
        carousels[crs_name].item_with = obj.find("ul li").outerWidth(true)
        carousels[crs_name].len = obj.find("ul li").length
        carousels[crs_name].width = carousels[crs_name].item_with * carousels[crs_name].len
        obj.find("ul").width(carousels[crs_name].width)
    }

    function resetClick(){
        can_click = true
    }
    /*</Carousel>*/

});
