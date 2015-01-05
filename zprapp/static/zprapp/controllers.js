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
        items.organizmy = function(numer) {
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

                })
            var odp = obietnica.promise;
            return  odp;
        }
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

                })
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

                })
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

                })
            var odp = obietnica.promise;
            return  odp;
        };

        items.chromosomy = function(id_organizmu){
            var obiekt = {id_org: id_organizmu};
            var request = {
                method: 'GET',
                url: 'ajax_chromosom',
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

                })
            var odp = obietnica.promise;
            return  odp;
        };

        return items;
      });


function OrganizmKontroler($scope, Items){
    //$scope.id_ogranizmu = 1;
    //$scope.testowy = "na sztywno dodany tekst w OrganizmKontroler";
    //$scope.dane = Items.cos;
    $scope.reqget = Items.organizmy($scope.id_ogranizmu);
    //$scope.fun = function(numer){
    //    $scope.reqget = Items.organizmy(numer);
    //};
    $scope.wybierzOrganizm = function(numerWiersza, nazwa, kluczGlowny){
        $scope.wybranyOrganizm = numerWiersza;
        $scope.organizmEdytowany = nazwa;
        $scope.kluczOrganizmu = kluczGlowny;
        //$scope.showEdytujOrganizm = false
    }

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

function chromosomRouteConfig($routeProvider){
    $routeProvider.
        when('/organizm/:id/chromosom', {
            controller: ChromosomKontroler,
            templateUrl: 'organizm/chromosomy'
        });
}

zprModule.config(chromosomRouteConfig);

function ChromosomKontroler($scope, $routeParams){
    $scope.idOrg = $routeParams.id;
    //alert($routeParams.id);
    $scope.chromosomy = $scope.reqget;


    //przekazuje url do MarkerKontroler w celu nadaniu ngInclude odpowiedniego adresu
    $scope.dlaMarkera = {};
    $scope.dlaMarkera.url = 'markery';
    //gdy linijka nizej odkomentowana, nie załącza markery.html
    //$scope.dlaMarkera.url = '';
    $scope.dlaMarkera.numer = 88888;
}

function MarkerKontroler($scope, $routeParams){
    $scope.marker = "markerXXX";
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
