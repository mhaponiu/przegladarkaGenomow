/**
 * Created by mhaponiu on 25.02.15.
 */
function ChromosomKontroler($scope, $http, $routeParams) {
    $scope.napis = "ala ma kota";

    $scope.id_org = $routeParams.id_org;
    $scope.types = {} //slownik [id_chr]=lista typow z api

    $scope.loadTypes = function (id_chr) {
        var request = {
            method: 'GET',
            url: 'api/organisms/'+ $scope.id_org + '/chromosomes/' + id_chr + '/annotation_types/',
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.types[id_chr] = data;
            });
    }

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