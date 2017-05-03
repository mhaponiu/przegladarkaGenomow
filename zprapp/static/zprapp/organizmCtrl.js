/**
 * Created by mhaponiu on 03.05.15.
 */

function OrganizmKontroler($scope, $http) {
    $scope.aaa = "ala ma kota";

    $scope.loadOrganisms = function(){
        var request = {
            method: 'GET',
            url: 'api/organisms'
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.orgs = data;
            });
    }
    $scope.promiseLoadOrganisms = $scope.loadOrganisms();

    $scope.deleteOrganism = function(index_in_table){
        var request = {
            method: 'DELETE',
            url: 'api/organisms/'+$scope.orgs[index_in_table]['id']
        };
        return $http(request)
            .success(function (data) {
                //pobierz nowe organizmy
                $scope.promiseLoadOrganisms = $scope.loadOrganisms();
            });
    }
}