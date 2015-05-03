/**
 * Created by mhaponiu on 25.02.15.
 */
function ChromosomKontroler($scope, $http, $routeParams) {
    $scope.napis = "ala ma kota";

    $scope.id_org = $routeParams.id_org;

    $scope.loadChromosomes = function(id_org){
        var request = {
            method: 'GET',
            url: 'ajax_chrmy',
            params: {id_org: id_org}
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.chrms = data;
            });
    }
    $scope.promiseLoadChromosomes = $scope.loadChromosomes($routeParams.id_org);
}