/**
 * Created by mhaponiu on 26.02.15.
 */

function ScaffoldKontroler($scope, $routeParams, $http) {
    $scope.chr_id = $routeParams.id;

    $scope.loadScaffolds = function(id_chr){
        var request = {
            method: 'GET',
            url: 'ajax_scfldy',
            params: {id: id_chr}
        };
        $http(request)
            .success(function (data) {
                $scope.scflds = data;
            });
    }
    $scope.loadScaffolds($routeParams.id);
    //$scope.scflds = Items.scaffoldy($routeParams.id);
}