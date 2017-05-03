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
angular.module('CucModule').controller('SearchSeqModalInstance', function($scope, $modalInstance, $http, $filter, DataBufor){
    $scope.ok = function(){
        console.log("OK");
        $modalInstance.dismiss();
    }
    $scope.cancel = function(){
        $modalInstance.close();
    }
    $scope.algorytmy = [
      {name:'KMP', id:1, params:{} },
      {name:'Boyer', id:2, params:{} },
      {name:'SW', id:3, params:{win:2, gap:4} },
      {name:'BLAST', id:4, params:{w:7, t:3, c:3}},
    ];
    $scope.wybranyAlg = $scope.algorytmy[0]
    $scope.wzorzec;
    $scope.cel;
    $scope.wynik = ""
    $scope.wybranyOrg = $scope.orgs[0]
    $scope.showTable = false

    // TODO na sztywno wpisany zeby szybciej pokazac -> usunac nizej
    $scope.wzorzec = "CTTCAGCAAAG"

    $scope.searchSeq = function(){
        var request = {
            method: 'POST',
            url: 'ajax_searchSeq',
            //params: {param1: "p1p1p1", param2: "p2p2p2"}, //query string parametr
            data: { pattern: $scope.wzorzec,
                    // cel: $scope.cel,
                    org: $scope.wybranyOrg['pk'] } //ukryte data w poscie
        };
        $http(request)
            .success(function (data) {
                $scope.wynik = $filter("multipleLineWhenManyPos")(data)
                // console.log($scope.wynik)
                $scope.showTable = true
            });
    }

    $scope.teleport = function (item) {
        console.log(item)
        DataBufor.setData('view_from', item['pos']) //pos to pozycja wzgledna wzgledem poczatku scaffoldu
        DataBufor.setData('view_to', item['pos'] + $scope.wzorzec.length)
        DataBufor.setData('scf_id', item['scf_id'])
        window.location.replace("#/organisms/" + item['org_id'] +"/chromosomes/" + item['chr_id'] + "/annotations")

    }

})