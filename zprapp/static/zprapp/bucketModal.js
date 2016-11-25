/**
 * Created by mhaponiu on 24.11.16.
 */
angular.module('CucModule').controller('BucketModalCtrl', function ($scope, $modal, DataBufor) {

    $scope.koszyk = []
    $scope.ile_w_koszyku = 0;

    // $scope.$watch('koszyk', function () {
    //     $scope.ile_w_koszyku = $scope.koszyk.length
    // })

    $scope.open = function () {
        // DataBufor.setData('view_from', 0)
        // DataBufor.setData('view_to', 50)
        if (angular.equals($scope.koszyk, [])) {
            alert("KOSZYK JEST PUSTY")
        }
        else {
            var modalIntance = $modal.open({
                templateUrl: 'BucketModalContent.html',
                controller: 'BucketModalInstance',
                backdrop: "static",
                scope: $scope,
                size: "" //sm lg
            });
            modalIntance.result.then(function () {
                console.log("CLOSE");
            });
        }
    }
})

//controller wewnatrz okienka modalnego; ma przekazany scope od SearchSeqModalCtr
angular.module('CucModule').controller('BucketModalInstance', function ($scope, $modalInstance, $http) {
    $scope.ok = function () {
        console.log("OK");
        $modalInstance.dismiss();
    }
    $scope.cancel = function () {
        $modalInstance.close();
    }
    // $scope.koszyk = ['item1', 'item2', $scope.ile_w_koszyku];

})