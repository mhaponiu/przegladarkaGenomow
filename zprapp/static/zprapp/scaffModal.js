/**
 * Created by mhaponiu on 01.05.15.
 */

angular.module('CucModule').controller('ScaffModalCtrl', function($scope, $modal){
    $scope.open = function(){
        var modalIntance = $modal.open({
            templateUrl: 'scaffModalContent.html',
            controller: 'ScaffModalInstance',
            backdrop: "static",
            scope: $scope
        });
        //modalIntance.opened.then(function(){
        //    console.log("OPENED");
        //});
        modalIntance.result.then(function(){
            console.log("CLOSE");
        });
    }

    $scope.toggleTextArea = function(){
        if(!$scope.textarea.visible){
            $scope.roznica = $scope.settings.widok_do - $scope.settings.widok_od;
            var limit = 25000;
            if ($scope.roznica > limit) {
                $scope.open()
            }
            else {
                $scope.textarea.toggle();
                $scope.textarea.loadSequence();
            }
        }
        else {
            $scope.textarea.toggle();
        }
    }
})

//controller wewnatrz okienka modalnego; ma przekazany scope od ScaffModalCtrl
angular.module('CucModule').controller('ScaffModalInstance', function($scope, $modalInstance){
    $scope.ok = function(){
        console.log("OK");
        $modalInstance.dismiss();
        $scope.textarea.toggle();
        $scope.textarea.loadSequence();
    }
    $scope.cancel = function(){
        $modalInstance.close();
    }
})