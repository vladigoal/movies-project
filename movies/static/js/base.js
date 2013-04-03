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
    //Init carousels
    carousel_init("carousel1", $("header"))
    carousel_init("carousel2", $(".month_wrapper"))
    $(".news_wrapper .history .carousel_wrapper").each(function(){
        carousel_init($(this).attr("id"), $("."+$(this).attr("id")))
    })

    //Set listeners for all described carousels
    for (var c in carousels){
        carousels[c].obj.find(".arrow").click(function(e){
            if(can_click){
                var classes = $(this).attr("class").split(" ")
                can_click = false
                var timer = setTimeout(function(){resetClick()}, 700)
                var crs_name = $(this).attr("carousel")
                carousels[crs_name].l_margin = parseInt(carousels[crs_name].obj.find(".items_list").css("margin-left"))
                
                if(classes.length > 1 && classes[1] == "right"){
                    if(Math.abs(carousels[crs_name].l_margin) < (carousels[crs_name].width) - carousels[crs_name].obj.find(".carousel-inner").outerWidth()){
                        carousels[crs_name].obj.find(".items_list").animate({
                            marginLeft: '-='+carousels[crs_name].item_with
                        }, 700)
                    }    
                }else{
                    if(carousels[crs_name].l_margin < 0){
                        carousels[crs_name].obj.find(".items_list").animate({
                            marginLeft: '+='+carousels[crs_name].item_with
                        }, 700)
                    }
                }
                
            }
            return false
        })

        carousels[c].obj.find(".arrow").hover(function(){
            var classes = $(this).attr("class").split(" ")
            var crs_name = $(this).attr("carousel")
            carousels[crs_name].l_margin = parseInt(carousels[crs_name].obj.find(".items_list").css("margin-left"))
            if(classes.length > 1 && classes[1] == "right"){
                if(Math.abs(carousels[crs_name].l_margin) < (carousels[crs_name].width) - carousels[crs_name].obj.find(".carousel-inner").outerWidth()){
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
        carousels[crs_name].obj = obj
        carousels[crs_name].l_margin = 0
        carousels[crs_name].item_with = obj.find(".items_list li").outerWidth(true)
        carousels[crs_name].len = obj.find(".items_list li").length
        carousels[crs_name].width = carousels[crs_name].item_with * carousels[crs_name].len
        obj.find(".items_list").width(carousels[crs_name].width)
    }

    function resetClick(){
        can_click = true
    }
    /*</Carousel>*/

    /*<Movies of the month>*/
    //See all click event
    var open = false
    var top_carousel_h = $(".month_wrapper .carousel_wrapper").height()
    var items_list_width = $(".month_wrapper .items_list").width()
    $(".see_all").click(function(){
        var obj = $(".month_wrapper .carousel_wrapper")
        var speed = 600
        if(open){
            obj.stop(true, false).animate({
                height: top_carousel_h
            }, speed, function(){
                obj.find(".items_list").width(items_list_width)
                $(".month_wrapper .arrow").show()
                open = false
            })
        }else{
            obj.find(".items_list").removeAttr("style")
            var open_height = obj.find(".carousel-inner").height()
            obj.stop(true, false).animate({
                height: open_height
            }, speed, function(){
                $(".month_wrapper .arrow").hide()
                open = true
            })  
        }
        
        return false
    })

    //item hover
    $(".month_wrapper .item").hover(function(){
        $(this).find(".transp").show()
    }, function(){
        $(this).find(".transp").hide()
    })

    $("#popup").on('shown', function () {
        if($(window).height() < $("#popup").height() + 20){
            $("body").height($("#popup").height() + 20)
            $("body").addClass("low")
        }else{
            $("body").height($(window).height())
        }

        if($(window).width() < $("#popup").width() + 50){
            $("body").height($("#popup").height() + 50)
            $("body").addClass("narrow")
        }else{
            $("body").width($(window).width())
        }

        $("header").hide()
        $(".main-wrap").hide()
    })

    $("#popup").on('hidden', function () {
        $("body").removeAttr("style")
        $("body").removeClass("low")
        $("body").removeClass("narrow")
        $("header").show()
        $(".main-wrap").show()  
    })
    /*</Movies of the month>*/
});
