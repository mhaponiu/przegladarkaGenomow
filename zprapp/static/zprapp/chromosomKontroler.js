/**
 * Created by mhaponiu on 25.02.15.
 */
function ChromosomKontroler($scope, $http) {
    $scope.napis = "ala ma kota";
    $scope.napis = "ala ma psa";

    $scope.loadChromosomes = function(){
        var request = {
            method: 'GET',
            url: 'ajax_chrmy'
        };
        $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.chrms = data;
            });
    }
    $scope.loadChromosomes();
}