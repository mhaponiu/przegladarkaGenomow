/**
 * Created by mhaponiu on 20.12.14.
 */

function OrganizmKontroler($scope, Items){
    $scope.id_ogranizmu = 1;
    $scope.testowy = "na sztywno dodany tekst w OrganizmKontroler";
    $scope.dane = Items.cos;
    $scope.reqget = Items.organizmy($scope.id_ogranizmu);
    $scope.fun = function(numer){
        $scope.reqget = Items.organizmy(numer);
    };
}

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
            var obiekt = {tekst: "get z factory", id: numer};
            var request = {
                method: 'GET',
                url: 'ajax_organizm',
                params: obiekt};
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
            //slownik do przetestowania ng-repeat
           var slownik =  [
                {nazwa: 'org slownikowy1', ident: 1},
                {nazwa: 'org slownikowy2', ident: 2},
                {nazwa: 'org slownikowy3', ident: 3}
            ];
            //return slownik;
            //alert(slownik[0].nazwa);
            var odp = obietnica.promise;
            var odpjson = angular.fromJson(odp);
            //alert(odpjson.nazwa);

            var kseroJsonaOdDjango = [
                {"fields": {"nazwa": "pomidor"}, "model": "zprapp.organizm", "pk": 1},
                {"fields": {"nazwa": "cebula"}, "model": "zprapp.organizm", "pk": 2},
                {"fields": {"nazwa": "jablko"}, "model": "zprapp.organizm", "pk": 3}
            ];
            var json_kseroJsonaOdDjango = angular.toJson(kseroJsonaOdDjango);
            var deserialized_json_kseroJsonaOdDjango = angular.fromJson(json_kseroJsonaOdDjango);
            return  odp;
        }
        return items;
      });

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
