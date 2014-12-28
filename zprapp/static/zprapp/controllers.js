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

        items.usunOrganizm = function (nazwaOrg) {
            var obiekt = {nazwa: nazwaOrg };
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

        return items;
      });

function OrganizmKontroler($scope, Items){
    $scope.id_ogranizmu = 1;
    $scope.testowy = "na sztywno dodany tekst w OrganizmKontroler";
    $scope.dane = Items.cos;
    $scope.reqget = Items.organizmy($scope.id_ogranizmu);
    $scope.fun = function(numer){
        $scope.reqget = Items.organizmy(numer);
    };
    $scope.wybierzOrganizm = function(numer_wiersza){
        $scope.wybranyOrganizm = numer_wiersza;
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
    $scope.usunOrganizm = function(nazwa){
        alert("Usunięto organizm:\n\n" + nazwa);
        //aktualizacja listy organizmow
        $scope.reqget = Items.usunOrganizm(nazwa);
    };
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
