/**
 * Created by mhaponiu on 26.02.15.
 */

function ScaffoldKontroler($scope, $routeParams, Items) {
    $scope.chr_id = $routeParams.id;
    $scope.scflds = Items.scaffoldy($routeParams.id);
}