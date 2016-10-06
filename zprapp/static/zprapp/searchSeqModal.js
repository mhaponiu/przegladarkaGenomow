/**
 * Created by mhaponiu on 01.04.16.
 */
angular.module('CucModule').controller('SearchSeqModalCtrl', function($scope, $modal){
    $scope.open = function(){
        var modalIntance = $modal.open({
            templateUrl: 'SearchSeqModalContent.html',
            controller: 'SearchSeqModalInstance',
            backdrop: "static",
            scope: $scope,
            size: "" //sm lg
        });
        modalIntance.result.then(function(){
            console.log("CLOSE");
        });
    }

    $scope.sss = "ala ma kota";

})

//controller wewnatrz okienka modalnego; ma przekazany scope od SearchSeqModalCtr
angular.module('CucModule').controller('SearchSeqModalInstance', function($scope, $modalInstance, $http){
    $scope.ok = function(){
        console.log("OK");
        $modalInstance.dismiss();
    }
    $scope.cancel = function(){
        $modalInstance.close();
    }
    $scope.algorytmy = [
      {name:'kmp', id:1},
      {name:'alg2', id:2},
      {name:'alg3', id:3},
    ];
    $scope.wybranyAlg = $scope.algorytmy[0]
    $scope.wzorzec;
    $scope.cel;
    $scope.wynik = ""

    // $scope.searchSeq = function(){
    //     console.log("searchSEQ!!!")
    //    var request = {
    //        method: 'POST',
    //        url: 'ajax_searchSeq',
    //        param: {aaa: "aaaaa", bbb:"bbbb"},
    //        data: {wzorzec: $scope.wzorzec,
    //                cel: $scope.cel}
    //    };
    //    return $http(request)
    //        .success(function (data) {
    //            //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
    //            $scope.wynik = data;
    //        });
    //}
    $scope.searchSeq = function(){
        var request = {
            method: 'POST',
            url: 'ajax_searchSeq',
            //params: {param1: "p1p1p1", param2: "p2p2p2"}, //query string parametr
            data: {wzorzec: $scope.wzorzec, cel: $scope.cel} //ukryte data w poscie
            //headers: {'Content-Type': 'application/x-www-form-urlencoded', //musi tak byc zeby posta dobrze odebralo, wiekszosc bibliotek JS tak robi
            //            'X-Requested-With': 'XMLHttpRequest'} //zeby w django request.is_ajax dawalo true
        };
        $http(request)
            .success(function (data) {
                $scope.wynik = data
            });
    }
})