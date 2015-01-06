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
        when('/organizm/:id/chromosom/:cos/markery', {
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
    $scope.marker = "markerXXX";
    $scope.superDane = {};
    //$scope.superDane.organizm = Items.
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
