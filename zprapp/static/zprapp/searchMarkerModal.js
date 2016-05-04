/**
 * Created by mhaponiu on 01.05.15.
 */

angular.module('CucModule').controller('SearchMarkerModalCtrl', function($scope, $modal){
    $scope.open = function(){
        var modalIntance = $modal.open({
            templateUrl: 'searchMarkerModalContent.html',
            controller: 'SearchMarkerModalInstance',
            backdrop: "static",
            scope: $scope
        });
        //modalIntance.opened.then(function(){
        //    console.log("OPENED");
        //});
        modalIntance.result.then(function(){
            $scope.markery.visible = false
            console.log("zamknieto modal");
        });
    }

    $scope.szukanyMarker='*';

    // $scope.toggleTextArea = function(){
    //     if(!$scope.textarea.visible){
    //         $scope.roznica = $scope.settings.widok_do - $scope.settings.widok_od;
    //         var limit = 25000;
    //         if ($scope.roznica > limit) {
    //             $scope.open()
    //         }
    //         else {
    //             $scope.textarea.toggle();
    //             $scope.textarea.loadSequence();
    //         }
    //     }
    //     else {
    //         $scope.textarea.toggle();
    //     }
    // }
})

//controller wewnatrz okienka modalnego; ma przekazany scope
angular.module('CucModule').controller('SearchMarkerModalInstance', function($scope, $modalInstance){
    console.log($scope.szukanyMarker)
    console.log('$scope.canvas.meanings.data')
    console.log($scope.canvas.meanings.data)
    console.log('$scope.mrkrs')
    console.log($scope.mrkrs)
    console.log('$scope.canvas.mrkrs')
    console.log($scope.canvas.mrkrs)

    $scope.loguj = function (tekst) {
        console.log(tekst)
        $modalInstance.close();
    }

    $scope.goToPosition = function (start, end) {
        $scope.settings.widok_od = start;
        $scope.settings.widok_do = end;
        $scope.updatePanel()
        $modalInstance.close();
    }

    $scope.zamknijPoprawnie = function(){
        console.log("zamykam");
        $modalInstance.close();
    }
})