function addBlock(keyResponse, summaryResponse, urlResponse, searchResponse, addressResponse) {
        let searchBlock = "";
        if (searchResponse.length > 1) {
                let severalSearch = '<b> Mes recherches : </b>'
                document.getElementById("searchs").innerHTML = severalSearch;

        }

        if (searchResponse.length == 3) {
                let severalSearch = "Laisse moi souffler, un peu : "
                document.getElementById("searchs").innerHTML = severalSearch;

        }

        if (searchResponse.length == 7) {
                let severalSearch = "Je fatigue, tu me fatigues... : "
                document.getElementById("searchs").innerHTML = severalSearch;

        }
        if (searchResponse.length > 10) {
                let severalSearch = "Tu crois pas que t'abuses la, plus de 10 recherches : "
                document.getElementById("searchs").innerHTML = severalSearch;

        }
        for (let i = 0; i < searchResponse.length; i++) {
                if (searchResponse.length == 1) {
                        searchBlock += '<b> Ma recherche : </b>' + searchResponse[i] + '<br>';
                } else {
                        searchBlock += '<div style=“overflow-y: auto; overflow-x: none;”"> ' + searchResponse[i] + '<br> </div>';
                }
        }
        document.getElementById("search").innerHTML = searchBlock;
        let urlMapBlock = '<script defer src="https://maps.googleapis.com/maps/api/js?key=' + keyResponse + '&callback=initMap"></script>';
        document.getElementById("script").innerHTML = urlMapBlock;
        if (addressResponse != 'KO') {
                document.getElementById("summary").innerHTML = '<br> ' + ' Grandpy : Bien sûr mon poussin ! La voici :' + addressResponse + '<br> ';
                document.getElementById("relou").innerHTML = " Grandpy : Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? " + summaryResponse + '<br> ' + '<a href=' + urlResponse + ' target="_blank"' + ' > En savoir plus sur Wikipedia</a>';
        } else {
                document.getElementById("summary").innerHTML = '<br> ' + ' Grandpy : Je n ai rien trouvé ' + '<br>';
                document.getElementById("relou").innerHTML = " Grandpy : essaye encore ";

        }
}

function initMap(latResponse, lngResponse) {

        let map;
        map = new google.maps.Map(document.getElementById('map'), {
                center: { lat: latResponse, lng: lngResponse },
                zoom: 14
        });
        console.log("google map function");
        var main_marker = new google.maps.Marker({
                position: new google.maps.LatLng(latResponse, lngResponse),
                map: map
        })

}
function Search() {
        console.log("methode search")
        document.getElementsByTagName('body')[0].style.cursor = 'wait'; //sablier
        var data = $("#inputSearch").val();
        fetch('/search',
                {
                        method: 'POST',
                        mode: 'cors',
                        credentials: 'include',
                        cache: 'no-cache',
                        body: data,
                        headers: {
                                "Content-Type": "application/json",
                                'Access-Control-Allow-Credentials': true,
                                'Access-Control-Allow-Origin': '/search'
                        },
                })

                .then(function (response) {
                        if (response.status !== 200) {
                                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                                console.log(response)
                                return;
                        }
                        response.text().then(function (data) {
                                console.log(data);
                                let varResponse = JSON.parse(data);
                                let latResponse = parseFloat(varResponse.lat);
                                let lngResponse = parseFloat(varResponse.lng);
                                let keyResponse = varResponse.key;
                                let summaryResponse = varResponse.summary;
                                let searchResponse = varResponse.search;
                                let urlResponse = varResponse.url;
                                let addressResponse = varResponse.address;
                                addBlock(keyResponse, summaryResponse, urlResponse, searchResponse, addressResponse);
                                initMap(latResponse, lngResponse);
                                document.getElementsByTagName('body')[0].style.cursor = 'default' //fleche classique
                        });
                })
                .catch(function (error) {
                        console.log("Fetch error: " + error);
                });
        console.log(data);
        return data;
}

function checkEnter(e) {
        var characterCode
        e.preventDefault()
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
                console.log('submit')
                Search();
                return false
        }

}