/**
 * Created by mhaponiu on 20.12.14.
 */
function Kontroler($scope){
            $scope.wartosc = { startowa : 5};
            $scope.wartosc.pomnozona = 50;

            $scope.pomnoz = function() {
                $scope.wartosc.pomnozona = $scope.wartosc.startowa * 10;
             };
        }

var zprModule = angular.module('ZprAppModule', []);

zprModule.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});
