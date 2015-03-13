$(document).ready(function() {
    $("#thumb").click(function(e) {
        e.preventDefault();
        //alert("click!");
        if ($("#thumb").attr("src") == "/static/thumbup_blue.png")
            return;
        var url = window.location.pathname + "thumbup/"
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": url,
            "data": null,
            "success": function(result) {
                    if (!result.content.been_agreed) {
                        $("#likes").html(result.content.likes);
                        $("#thumb").attr("src", "/static/thumbup_blue.png");
                    } else {
                    }
            },
        });
    });
    
    $("#follow").click(function(e) {
        e.preventDefault();
        alert("click follow!");
        var action;
        if ($("#follow").attr("src") == "/static/follow.png")
            action = "follow";
        else if ($("#follow").attr("src") == "/static/unfollow.png")
            action = "unfollow";
        
            
        var url = window.location.pathname + "follow/"
        $.ajax({
            "type": "POST",
            "dataType": "json",
            "url": url,
            "data": {'action': action, 'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
            "success": function(result) {
            
                if (result.content.action_complete) {
                    if (action == "follow")
                        $("#follow").attr("src", "/static/following.png")
                    else if (action == "unfollow")
                        $("#follow").attr("src", "/static/follow.png")
                }

                        
            },
        });
    });
    
    $("#follow").mouseenter(function(e) {
        e.preventDefault();
        //alert("mouse enter!");
        if ($("#follow").attr("src") == "/static/following.png")
            $("#follow").attr("src", "/static/unfollow.png" );
       
    });
    
    $("#follow").mouseleave(function(e) {
        e.preventDefault();
        //alert("mouse leave!");
        if ($("#follow").attr("src") == "/static/unfollow.png")
            $("#follow").attr("src", "/static/following.png" );
       
    });



});



/*
window.onload = initPage;

function initPage() {
    thumb = document.getElementById("thumb");
    thumb.onclick = flipThumb;
}

function clicktest() {
    alert("click!");
}

function flipThumb() {
    request = createRequest();
    if (request == null) {
        alert("Unable to create request");
        return;
    }
    var url = window.location.pathname + "thumbup/";
    request.open("POST", url, true);
    request.onreadystatechange = updateLikes;
    request.send(null);
    
}

function updateLikes() {
    if (request.readyState == 4) {
        if (request.status == 200) {
            alert("server response"); 
            var been_agreed = JSON.parse(request.responseText).been_agreed;
            alert(been_agreed);

        }
    }
   
}

function createRequest() {
    try {
        request = new XMLHttpRequest();
    } catch (tryMS) {
        try {
            request = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (otherMS) {
            try {
                request = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (failed) {
                request = null;
            }
        }
    
    } 
    return request;
}
*/
