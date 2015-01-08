/**
 * Created by mhaponiu on 20.12.14.
 */

var zprModule = angular.module('ZprAppModule',[]);

zprModule.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});

//ZprAppModule.factory('Items', function(){
//    var items = {};
//    items.organizmy = function(){
//        var request = {
//            method: 'GET',
//            url: 'zprapp/ajax_organizm'
//        };
//        $http(request).
//            success(function(data){
//                return data['organizm'];
//        });
//    };
//    items.data = "data";
//    return items;
//});

zprModule.factory('Items',function($http, $q) {
        var items = {};
        items.cos = 'tekst z factory items.cos';
        items.organizmy = function() {
            var request = {
                method: 'GET',
                url: 'ajax_wszystkieOrganizmy'
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };
        items.organizm = function(numer) {
            var obiekt = {id: numer};
            var request = {
                method: 'GET',
                url: 'ajax_organizm',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };
        items.nowyOrganizm = function (nazwaOrg) {
            var obiekt = {nazwa: nazwaOrg };
            var request = {
                method: 'GET',
                url: 'ajax_nowyOrganizm',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.usunOrganizm = function (pk) {
            var obiekt = {id: pk };
            var request = {
                method: 'GET',
                url: 'ajax_usunOrganizm',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.edytujOrganizm = function(pk, nowaNazwa) {
            var obiekt = {id: pk, nazwa: nowaNazwa };
            var request = {
                method: 'GET',
                url: 'ajax_edytujOrganizm',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.chromosomy = function(id_organizmu){
            var obiekt = {id_org: id_organizmu};
            var request = {
                method: 'GET',
                url: 'ajax_chromosomy',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.chromosom = function(id_org, id_chr){
            var obiekt = {id_org: id_org, id_chr: id_chr};
            var request = {
                method: 'GET',
                url: 'ajax_jedenchromosom',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.usunChromosom = function(id_org, id_chr){
            var obiekt = {id_org: id_org, id_chr: id_chr};
            var request = {
                method: 'GET',
                url: 'ajax_usunChromosom',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.nowyChromosom = function(id_org, nazwa, dlugosc){
            var obiekt = {id_org: id_org, nazwa: nazwa, dlugosc: dlugosc};
            var request = {
                method: 'GET',
                url: 'ajax_nowyChromosom',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.edytujChromosom = function(id_org, id_chr, nazwa, dlugosc){
            var obiekt = {
                id_org: id_org,
                id_chr: id_chr,
                nazwa: nazwa,
                dlugosc: dlugosc
            };
            var request = {
                method: 'GET',
                url: 'ajax_edytujChromosom',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.markery = function(id_organizmu, id_chr){
            var obiekt = {id_org: id_organizmu, id_chr: id_chr};
            var request = {
                method: 'GET',
                url: 'ajax_wszystkieMarkery',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.nowyMarker = function(id_org, id_chr, sekwencja, poz_od, poz_do){
            var obiekt = {id_org: id_org, id_chr: id_chr, sekwencja: sekwencja, poz_od: poz_od, poz_do: poz_do};
            var request = {
                method: 'GET',
                url: 'ajax_nowyMarker',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.usunMarker = function(id_org, id_chr, id_mark){
            var obiekt = {id_org: id_org, id_chr: id_chr, id_mark: id_mark};
            var request = {
                method: 'GET',
                url: 'ajax_usunMarker',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        items.edytujMarker = function(id_org, id_chr, id_mark, poz_od, poz_do, sekwencja){
            var obiekt = {
                o: id_org,
                ch: id_chr,
                m: id_mark,
                od: poz_od,
                do: poz_do,
                s: sekwencja
            };
            var request = {
                method: 'GET',
                url: 'ajax_edytujMarker',
                params: obiekt
            };
            var obietnica = $q.defer();
            $http(request)
                .success(function(data){
                    obietnica.resolve(
                        //{obiet: data['organizm']}
                        data
                    );
                })
                .error(function(data){

                });
            var odp = obietnica.promise;
            return  odp;
        };

        return items;
      });


function OrganizmKontroler($scope, Items){
    //$scope.id_ogranizmu = 1;
    //$scope.testowy = "na sztywno dodany tekst w OrganizmKontroler";
    //$scope.dane = Items.cos;
    $scope.reqget = Items.organizmy();
    $scope.wybierzOrganizm = function(numerWiersza, nazwa, kluczGlowny){
        $scope.wybranyOrganizm = numerWiersza;
        $scope.organizmEdytowany = nazwa;
        //kluczOrganizmu chyba niepotrzebny - nigdzie nie uzywany
        $scope.kluczOrganizmu = kluczGlowny;
        //$scope.showEdytujOrganizm = false
    };

    //formularz Nowy Organizm
    $scope.showNowyOrganizm = false;
    $scope.toggleNowyOrganizm = function(){
        $scope.showNowyOrganizm = !$scope.showNowyOrganizm;
        $scope.nowyOrganizm = "";
    };
    $scope.dodano = function(napis){
        $scope.showNowyOrganizm = false;
        alert("Dodano nowy organizm:\n\n" + napis);
        //aktualizacja listy organizmow
        $scope.reqget = Items.nowyOrganizm($scope.nowyOrganizm);
    };

    //usuniecie organizmu
    $scope.usunOrganizm = function(pk, nazwa){
        alert("Usunięto organizm   " + nazwa);
        //aktualizacja listy organizmow
        $scope.reqget = Items.usunOrganizm(pk);
    };

    //edycja organizmu
    $scope.showEdytujOrganizm = false;
    $scope.toggleEdytujOrganizm = function (nazwaOrganizmu){
        $scope.showEdytujOrganizm = !$scope.showEdytujOrganizm;
        $scope.organizmEdytowany = nazwaOrganizmu;
    };
    $scope.edytujOrganizm = function (pk, staraNazwa, nowaNazwa){
        alert("ZMIENIONO NAZWĘ ORGANIZMU\n\nStara nazwa:     " + staraNazwa + "\n\nNowa nazwa:    " + nowaNazwa);
        $scope.showEdytujOrganizm = !$scope.showEdytujOrganizm;
        $scope.reqget = Items.edytujOrganizm(pk, nowaNazwa);
    }
}

function zprRouteConfig($routeProvider){
    $routeProvider.
        when('/organizmy', {
            controller: OrganizmKontroler,
            templateUrl: 'organizmy'
        }).
        when('/organizm/:id/chromosomy', {
            controller: ChromosomKontroler,
            templateUrl: 'organizm/chromosomy'
        }).
        when('/organizm/:id_org/chromosom/:id_chr/markery', {
            controller: MarkerKontroler,
            templateUrl: 'markery'
        }).
        otherwise({
            redirectTo:'/organizmy'
        });
}

zprModule.config(zprRouteConfig);

function ChromosomKontroler($scope, $routeParams, Items){
    $scope.org = Items.organizm($routeParams.id);
    $scope.chromosomy = Items.chromosomy($routeParams.id);
    $scope.wybierzChromosom = function(numerWiersza, nazwa, dlugosc){
        $scope.wybranyChromosom = numerWiersza;
        $scope.chromosomEdytowany = nazwa;
        $scope.dlugoscEdytowana = dlugosc;
    }
    //formularz Chromosom
    $scope.showNowyChromosom = false;
    $scope.nowyChromosom = {};
    $scope.toggleNowyChromosom = function(){
        $scope.showNowyChromosom = !$scope.showNowyChromosom;
        $scope.nowyChromosom.nazwa = "";
        $scope.nowyChromosom.dlugosc = 0;
    };

    //edycja chromosomu
    $scope.showEdytujChromosom = false;
    $scope.toggleEdytujChromosom = function(nazwaChromosomu){
        $scope.showEdytujChromosom = !$scope.showEdytujChromosom;
        $scope.chromosomEdytowany = nazwaChromosomu;
    }
    $scope.edytujChromosom = function(pk, staraNazwa, staraDlugosc, nowaNazwa, nowaDlugosc){
        alert("Edycja chromosomu:\n\n" + staraNazwa + "   o długości " + staraDlugosc + "\n\nna\n\n" + nowaNazwa + "   o długości " + nowaDlugosc);
        $scope.chromosomy = Items.edytujChromosom($scope.org.$$v.id, pk, nowaNazwa, nowaDlugosc);
    }

    //utworzenie nowego chromosomu
    $scope.zapiszNowyChromosom = function (nowyChr){
        alert("Dodano nowy chromosom:\n\nnazwa:     " + nowyChr.nazwa + "\ndługość:  " + nowyChr.dlugosc);
        $scope.chromosomy = Items.nowyChromosom($scope.org.$$v.id, nowyChr.nazwa, nowyChr.dlugosc);
    }

    //usunięcie chromosomu
    $scope.usunChromosom = function(pk, nazwa){
        alert("Usuwam chromosom:\n\n" + nazwa + " o pk= "+ pk + "id_org:" + $scope.org.$$v.id);
        $scope.chromosomy = Items.usunChromosom($scope.org.$$v.id, pk);
    }
}

function MarkerKontroler($scope, $routeParams, Items){
    $scope.jakistamtext = "jakis tam markerowy text";
    $scope.superDane = {}; //dane nadrzędne dotyczące organizmu i chromosomu
    //w funkcji zrobic $scope.superDane.organizm.$$v.nazwa
    $scope.superDane.organizm = Items.organizm($routeParams.id_org);
    $scope.superDane.chromosom = Items.chromosom($routeParams.id_org, $routeParams.id_chr);
    $scope.superDane.markery = Items.markery($routeParams.id_org, $routeParams.id_chr);

    //formularz Marker
    $scope.showNowyMarker = false;
    $scope.nowyMarker = {};
    $scope.toggleNowyMarker = function (){
        $scope.showNowyMarker = !$scope.showNowyMarker;
        $scope.nowyMarker.pozycja_od = null;
        $scope.nowyMarker.pozycja_do = null;
        $scope.nowyMarker.sekwencja = "";
    }
    $scope.zapiszNowyMarker = function (nowyMarker){
        alert("Utworzyłeś nowy marker \n\npozycja od:  " + nowyMarker.pozycja_od + "\npozycja do:  " + nowyMarker.pozycja_do + "\nsekwencja:  " + nowyMarker.sekwencja);
        $scope.superDane.markery = Items.nowyMarker($routeParams.id_org, $routeParams.id_chr, $scope.nowyMarker.sekwencja, $scope.nowyMarker.pozycja_od, $scope.nowyMarker.pozycja_do);
    }

    $scope.wybranyMarker = {};
    $scope.markerEdytowany = {};
    //$scope.markerEdytowany.fields = {};

    $scope.wybierzMarker = function(index, poz_od, poz_do, sek){
        $scope.wybranyMarker.index = index;
        $scope.wybranyMarker.marker = $scope.superDane.markery.$$v[index];
        //$scope.wybranyMarker.marker = marker;
        $scope.markerEdytowany.pozycja_od = poz_od;
        $scope.markerEdytowany.pozycja_do = poz_do;
        $scope.markerEdytowany.sekwencja = sek;

        $scope.wskazywanyMarker = $scope.superDane.markery.$$v[index];

    }

    //usuwanie markera
    $scope.usunMarker = function (marker){
        alert("Usunięto marker o id: " + marker.pk);
        $scope.superDane.markery = Items.usunMarker($routeParams.id_org, $routeParams.id_chr, marker.pk)
    }

    //edycja markera
    $scope.showEdytujMarker = false;
    $scope.toggleEdytujMarker = function(){
        $scope.showEdytujMarker = !$scope.showEdytujMarker;
        //$scope.markerEdytowany = $scope.wybranyMarker.marker;
    }

    $scope.edytujMarker = function(marker){
        alert("zapisano zmiany\nsekwencja: " + marker.sekwencja + "\nod: " + marker.pozycja_od + "\ndo: " + marker.pozycja_do + "\npk: " + $scope.wybranyMarker.marker.pk);
        $scope.superDane.markery = Items.edytujMarker($routeParams.id_org,
                                                        $routeParams.id_chr,
                                                        $scope.wybranyMarker.marker.pk,
                                                        marker.pozycja_od,
                                                        marker.pozycja_do,
                                                        marker.sekwencja);
    }
    $scope.showWszystkieMarkery=false;


}

function CanvasCtrl($scope,$routeParams, Items){
    //$scope.canvasText = "canvasowy text";
    //$scope.canvasText = $scope.jakistamtext;
    //$scope.canvasText = $scope.superDane.chromosom;
    $scope.guzik = function(){
        //alert("guzik");
        //alert($scope.canvasText.$$v.dlugosc);
        $scope.canvasText = $scope.superDane.markery;
        //$scope.canvasText = $scope.superDane.markery.$$v[0].fields.sekwencja;
    }

    var init = function(){
        $scope.canvasText = $scope.superDane.chromosom.$$v.dlugosc;
        drawCanvas();
        //alert("INIT sie wykonał");
    }
    //$scope.$watch('superDane.chromosom', init);
    $scope.$watch('superDane.chromosom', init);
    $scope.$watch('superDane.organizm', init);
    $scope.$watch('superDane.markery', init);


    var drawCanvas = function() {
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

        for(var i=0; i< $scope.superDane.markery.$$v.length; i++){
            var odkad = 800 * $scope.superDane.markery.$$v[i].fields.pozycja_od / $scope.superDane.chromosom.$$v.dlugosc;
            var dokad = 800 * $scope.superDane.markery.$$v[i].fields.pozycja_do / $scope.superDane.chromosom.$$v.dlugosc;
            //zeby namalować chociaż cienki pasek jak bedzie bardzo mały
            if(dokad - odkad < 3){
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

//do pierwszych prob z wymiana danych
function Kontroler($scope, $http){
            $scope.wartosc = { startowa : 5};
            $scope.wartosc.pomnozona = 50;
            $scope.slownik ={};

            $scope.pomnoz = function() {
                $scope.wartosc.pomnozona = $scope.wartosc.startowa * 10;
             };
            $scope.dawajgeta = function() {
                var obiekt = {tekst: "wartosctext", id: 7};
                var obiekt_json = angular.toJson(obiekt);
                /*
                 *to ponizej dziala tylko dla GET?
                 */
                var request = {
                    method: 'GET',
                    url: 'zprapp/ajax',
                    //headers: {
                    //    'Content-Type': 'application/json'
                    //},
                    //params dodaje do URL parametry obiektu
                    params: obiekt,
                    //tego data jakby w ogole nie widzial potem w diango w slowniku
                    data: angular.toJson(obiekt)
                };
                $http(request).
                    success(function(data){
                        $scope.slownik = data['klucz'];
                });
            };
        }
