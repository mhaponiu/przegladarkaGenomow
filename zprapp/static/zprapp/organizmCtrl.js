/**
 * Created by mhaponiu on 03.05.15.
 */

function OrganizmKontroler($scope, $http) {
    $scope.aaa = "ala ma kota";

    $scope.loadOrganisms = function(){
        var request = {
            method: 'GET',
            url: 'ajax_orgs'
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.orgs = data;
            });
    }
    $scope.promiseLoadOrganisms = $scope.loadOrganisms();
}