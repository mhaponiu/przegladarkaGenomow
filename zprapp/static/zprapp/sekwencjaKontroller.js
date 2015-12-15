/**
 * Created by mhaponiu on 26.02.15.
 */

function SekwencjaKontroler($scope, $routeParams, $http, clipboard) {
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
    $scope.alert={}
    $scope.alert.show = true
    $scope.alert.type="danger"
    $scope.alert.toggleShow = function(){
        $scope.alert.show = !$scope.alert.show
    }

    var limitCopy = 500000

    $scope.copySeq = function(){
        console.log($scope.scs.length)
        //$scope.copyFail("copy error")
        if($scope.scs.length > limitCopy){
            $scope.copyFail("copy error (ponad " + limitCopy + " znaków)")
        }
        else{
            try {
                clipboard.copyText($scope.scs)
                $scope.copySuccess()
            } catch (err){
                $scope.copyFail(err)
            }

            //console.log(a.scope.onCopied)
            console.log("skopiowano")
        }
    }
    //document.getElementById("copySeqBtn")
    $scope.alert.msg = "ERROR"
    $scope.copySuccess = function(){
        console.log("skopiowano")
        $scope.alert.msg = "Skopiowano sekwencję do schowka."
        $scope.alert.type = "success"
        $scope.alert.show=false
    }
    $scope.copyFail = function(err) {
        $scope.alert.msg = err + ":    za dużo znaków do skopiowania"
        $scope.alert.show=false
    }
}