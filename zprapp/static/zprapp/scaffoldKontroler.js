/**
 * Created by mhaponiu on 26.02.15.
 */

function ScaffoldKontroler($scope, $routeParams, $http) {
    $scope.chr_id = $routeParams.id_chr;
    $scope.id_org = $routeParams.id_org;
    $scope.id_type = $routeParams.id_type

    $scope.loadScaffolds = function(id_org, id_chr){
        var request = {
            method: 'GET',
            url: 'api/organisms/'+$scope.id_org+'/chromosomes/'+$scope.chr_id+'/annotation_types/'+ $scope.id_type +'/annotations/'
        };
        return $http(request)
            .success(function (data) {
                $scope.scflds = data;
            });
    }
    $scope.promiseLoadScaffolds = $scope.loadScaffolds($routeParams.id_org, $routeParams.id_chr);
}