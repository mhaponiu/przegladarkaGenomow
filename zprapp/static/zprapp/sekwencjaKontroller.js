/**
 * Created by mhaponiu on 26.02.15.
 */

function SekwencjaKontroler($scope, $routeParams, Items) {
    $scope.chr_id = $routeParams.id_chr;
    $scope.sc_id = $routeParams.id_sc;
    $scope.scs = Items.sekwencja($routeParams.id_chr, $routeParams.id_sc);
}