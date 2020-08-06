fetch(`http://localhost:5000/search`, {
        method: "POST",
        credentials: "omit",
        dataType: 'json',
        cache: "no-cache",
        headers: new Headers({
                "content-type": "application/json"
        })
})
        .then(function (response) {
                if (response.status !== 200) {
                        console.log(`Looks like there was a problem. Status code: ${response.status}`);
                        console.log(response)
                        return;
                }
                response.json().then(function (data) {
                        console.log(data);
                        initMap(data);
                });
        })
        .catch(function (error) {
                console.log("Fetch error: " + error);
        });


function initMap() {
        let map;
        console.log("initMap");
        //let obj = data;
        //console.log("obj" + obj)
        //console.log(JSON.parse('{ dict_response_dump | tojson | safe }'));
        //let varResponse = JSON.parse('{"search": "Ecouen", "lat": "49.018834", "lng": "2.378926", "summary": "Le château d Écouen est un château du XVIe siècle, situé dans le Val-d Oise, qui abrite depuis 1977 le musée national de la Renaissance.", "url": "https://fr.wikipedia.org/wiki/Ch%C3%A2teau_d%27%C3%89couen"}')
        //let varResponse = JSON.parse('{{ dict_response_dump | tojson}}');
        //let obj = JSON.parse('{"firstName":"John", "lastName":"Doe"}');
        //console.log(varResponse);
        //let latResponse = parseFloat(varResponse.lat);
        //let lngResponse = parseFloat(varResponse.lng);
        //console.log(lat);
        map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: 49.030343, lng: 2.326213 },
                zoom: 14
        });
        console.log("google map function");
        var main_marker = new google.maps.Marker({
                position: new google.maps.LatLng(49.018834, 2.378926),
                map: map
        })
}


function Search() {
        console.log("methode search")
        var data = $("#inputSearch").val();
        $.ajax({
                type: "POST",
                url: "search",
                cache: false,
                data: data,
                dataType: 'text',
                success: function (data) {
                        //initMap();
                        console.log("success")
                },
                error: function (error) {
                        console.log("error")
                }
        });
        console.log(data);
        return data;
}

function checkEnter(e) {
        var characterCode

        if (e && e.which) { //if which property of event object is supported (NN4)
                e = e
                characterCode = e.which //character code is contained in NN4's which property
        }
        else {
                e = event
                characterCode = e.keyCode //character code is contained in IE's keyCode property
        }

        if (characterCode == 13) {
                document.forms[0].submit()
                Search();
                return false
        }
        else {
                return true
        }

}