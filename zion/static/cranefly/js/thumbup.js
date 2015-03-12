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