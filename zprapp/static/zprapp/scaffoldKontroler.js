/**
 * Created by mhaponiu on 26.02.15.
 */

function ScaffoldKontroler($scope, $routeParams, $http) {
    $scope.chr_id = $routeParams.id_chr;
    $scope.id_org = $routeParams.id_org;

    $scope.loadScaffolds = function(id_org, id_chr){
        var request = {
            method: 'GET',
            url: 'ajax_scfldy',
            params: {id_org: id_org, id_chr: id_chr}
        };
        return $http(request)
            .success(function (data) {
                $scope.scflds = data;
            });
    }
    $scope.loadMarkers = function(id_org, id_chr){
        var request = {
            method: 'GET',
            url: 'ajax_markers',
            params: {id_org: id_org, id_chr: id_chr}
        };
        return $http(request)
            .success(function (data) {
                $scope.mrkrs = data;
            });
    }

    $scope.loadMarkerMeanings = function(){
        var request = {
            method: 'GET',
            url: 'ajax_meanings'
        };
        return $http(request)
            .success(function (data) {
                $scope.meanings = data;
            });
    }

    //$scope.promiseLoadMarkers = $scope.loadMarkers($routeParams.id_org, $routeParams.id_chr)
    $scope.promiseLoadScaffolds = $scope.loadScaffolds($routeParams.id_org, $routeParams.id_chr);
    //$scope.loadScaffolds($routeParams.id);
    //$scope.scflds = Items.scaffoldy($routeParams.id);
}