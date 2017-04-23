/**
 * Created by mhaponiu on 26.02.15.
 */

function ScaffoldKontroler($scope, $routeParams, $http) {
    $scope.chr_id = $routeParams.id_chr;
    $scope.id_org = $routeParams.id_org;

    $scope.loadScaffolds = function(id_org, id_chr){
        var request = {
            method: 'POST',
            url: 'api/annotations/',
            data: {id: "id_chr"}
        };
        return $http(request)
            .success(function (data) {
                $scope.scflds = data;
            });
    }
    $scope.promiseLoadScaffolds = $scope.loadScaffolds($routeParams.id_org, $routeParams.id_chr);
}