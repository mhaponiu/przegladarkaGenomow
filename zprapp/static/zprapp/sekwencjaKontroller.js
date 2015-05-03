/**
 * Created by mhaponiu on 26.02.15.
 */

function SekwencjaKontroler($scope, $routeParams, $http) {
    //nieuzywane?
    $scope.chr_id = $routeParams.id_chr;
    $scope.sc_id = $routeParams.id_sc;

    $scope.loadSequence = function (id_org, id_chr, id_sc) {
        var request = {
            method: 'GET',
            url: 'ajax_scs',
            params: {id_org: id_org, id_chr: id_chr, id_sc: id_sc}
        };
        $http(request)
            .success(function (data) {
                $scope.scs = data;
            });
    };
    $scope.loadSequence($routeParams.id_org, $routeParams.id_chr, $routeParams.id_sc);
    //$scope.scs = Items.sekwencja($routeParams.id_chr, $routeParams.id_sc);
}