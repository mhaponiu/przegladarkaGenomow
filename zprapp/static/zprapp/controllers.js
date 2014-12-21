/**
 * Created by mhaponiu on 20.12.14.
 */
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

var zprModule = angular.module('ZprAppModule',[]);

zprModule.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});
