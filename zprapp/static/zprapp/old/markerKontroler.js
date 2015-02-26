/**
 * Created by mhaponiu on 18.01.15.
 */
function MarkerKontroler($scope, $routeParams, Items) {
    $scope.jakistamtext = "jakis tam markerowy text";
    $scope.superDane = {}; //dane nadrzędne dotyczące organizmu i chromosomu
    //w funkcji zrobic $scope.superDane.organizm.$$v.nazwa
    $scope.superDane.organizm = Items.organizm($routeParams.id_org);
    $scope.superDane.chromosom = Items.chromosom($routeParams.id_org, $routeParams.id_chr);
    $scope.superDane.markery = Items.markery($routeParams.id_org, $routeParams.id_chr);

    //formularz Marker
    $scope.showNowyMarker = false;
    $scope.nowyMarker = {};
    $scope.toggleNowyMarker = function () {
        $scope.showNowyMarker = !$scope.showNowyMarker;
        $scope.nowyMarker.pozycja_od = null;
        $scope.nowyMarker.pozycja_do = null;
        $scope.nowyMarker.sekwencja = "";
    }
    $scope.zapiszNowyMarker = function (nowyMarker) {
        alert("Utworzyłeś nowy marker \n\npozycja od:  " + nowyMarker.pozycja_od + "\npozycja do:  " + nowyMarker.pozycja_do + "\nsekwencja:  " + nowyMarker.sekwencja);
        $scope.superDane.markery = Items.nowyMarker($routeParams.id_org, $routeParams.id_chr, $scope.nowyMarker.sekwencja, $scope.nowyMarker.pozycja_od, $scope.nowyMarker.pozycja_do);
    }

    $scope.wybranyMarker = {};
    $scope.markerEdytowany = {};
    //$scope.markerEdytowany.fields = {};

    $scope.wybierzMarker = function (index, poz_od, poz_do, sek) {
        $scope.wybranyMarker.index = index;
        $scope.wybranyMarker.marker = $scope.superDane.markery.$$v[index];
        //$scope.wybranyMarker.marker = marker;
        $scope.markerEdytowany.pozycja_od = poz_od;
        $scope.markerEdytowany.pozycja_do = poz_do;
        $scope.markerEdytowany.sekwencja = sek;

        $scope.wskazywanyMarker = $scope.superDane.markery.$$v[index];

    }

    //usuwanie markera
    $scope.usunMarker = function (marker) {
        alert("Usunięto marker o id: " + marker.pk);
        $scope.superDane.markery = Items.usunMarker($routeParams.id_org, $routeParams.id_chr, marker.pk)
    }

    //edycja markera
    $scope.showEdytujMarker = false;
    $scope.toggleEdytujMarker = function () {
        $scope.showEdytujMarker = !$scope.showEdytujMarker;
        //$scope.markerEdytowany = $scope.wybranyMarker.marker;
    }

    $scope.edytujMarker = function (marker) {
        alert("zapisano zmiany\nsekwencja: " + marker.sekwencja + "\nod: " + marker.pozycja_od + "\ndo: " + marker.pozycja_do + "\npk: " + $scope.wybranyMarker.marker.pk);
        $scope.superDane.markery = Items.edytujMarker($routeParams.id_org,
            $routeParams.id_chr,
            $scope.wybranyMarker.marker.pk,
            marker.pozycja_od,
            marker.pozycja_do,
            marker.sekwencja);
    }
    $scope.showWszystkieMarkery = false;


}

function CanvasCtrl($scope, $routeParams, Items) {
    //$scope.canvasText = "canvasowy text";
    //$scope.canvasText = $scope.jakistamtext;
    //$scope.canvasText = $scope.superDane.chromosom;
    $scope.reqpost = "REQPOST_PUSTY";
    $scope.guzik = function () {
        //alert("guzik");
        //alert($scope.canvasText.$$v.dlugosc);
        //$scope.canvasText = $scope.superDane.markery;
        $scope.reqpost = Items.posttt(2);
        //$scope.reqpost = Items.posttt(3);
        //var item = Items.posttt(numer);
        //$scope.canvasText = item;
        //$scope.canvasText = $scope.superDane.markery.$$v[0].fields.sekwencja;
    }

    var init = function () {
        $scope.canvasText = $scope.superDane.chromosom.$$v.dlugosc;
        drawCanvas();
        //alert("INIT sie wykonał");
    }
    //$scope.$watch('superDane.chromosom', init);

    //bo uzywam superDanych ktore przyjda pozniej asynchronicznie, bez pozniejszego
    //wywolania init'a nie rysuje ani nie widzi tych zmiennych
    //poza tym i tak trzeba przerysowywac canvas gdy dane sie zmienia
    $scope.$watch('superDane.chromosom', init);
    $scope.$watch('superDane.organizm', init);
    $scope.$watch('superDane.markery', init);


    var drawCanvas = function () {
        var canvas = document.getElementById('canvasMarker');
        canvas.width = 800;
        canvas.height = 80;
        var context = canvas.getContext('2d');
        //context.lineJoin = "round";

        //tło
        context.fillStyle = "rgba(0,100,255,0.2)";
        context.fillRect(0, 20, 800, 40);

        function drawMarker(odkad, dokad) {
            //var odkad = 800 * pozycja_od / $scope.superDane.chromosom.$$v.dlugosc;
            //var dokad = 800 * pozycja_do / $scope.superDane.chromosom.$$v.dlugosc;
            context.fillRect(odkad, 0, dokad - odkad, 80);
        }

        //narysuj wszystkie markery
        context.fillStyle = "rgba(255,0,0,0.5)";
        //drawMarker(900, 5000);
        //drawMarker(5300, 5800);
        //drawMarker(50000, 52000);

        for (var i = 0; i < $scope.superDane.markery.$$v.length; i++) {
            var odkad = 800 * $scope.superDane.markery.$$v[i].fields.pozycja_od / $scope.superDane.chromosom.$$v.dlugosc;
            var dokad = 800 * $scope.superDane.markery.$$v[i].fields.pozycja_do / $scope.superDane.chromosom.$$v.dlugosc;
            //zeby namalować chociaż cienki pasek jak bedzie bardzo mały
            if (dokad - odkad < 3) {
                dokad = odkad + 3;
            }
            drawMarker(odkad, dokad);
        }

        //context.font = "18pt Calibri";
        //context.fillStyle = "black";
        //context.fillText($scope.superDane.markery.$$v[0].fields.sekwencja, 120, 43);
        //context.fillText($scope.superDane.markery.$$v.length, 120, 43);


    }


}
