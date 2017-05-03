/**
 * Created by mhaponiu on 01.04.16.
 */
angular.module('CucModule').controller('SearchSeqModalCtrl', function ($scope, $modal) {
    $scope.open = function () {
        var modalIntance = $modal.open({
            templateUrl: 'SearchSeqModalContent.html',
            controller: 'SearchSeqModalInstance',
            backdrop: "static",
            scope: $scope,
            size: "" //sm lg
        });
        modalIntance.result.then(function () {
            console.log("CLOSE");
        });
    }

    $scope.sss = "ala ma kota";

})

//controller wewnatrz okienka modalnego; ma przekazany scope od SearchSeqModalCtr
angular.module('CucModule').controller('SearchSeqModalInstance', function ($scope, $modalInstance, $http, $filter, DataBufor) {
    $scope.ok = function () {
        console.log("OK");
        $modalInstance.dismiss();
    }
    $scope.cancel = function () {
        $modalInstance.close();
    }
    $scope.algorytmy = [
        {name: 'KMP', id: 1, params: {}},
        {name: 'Boyer', id: 2, params: {}},
        {name: 'SW', id: 3, params: {win: 2, gap: 4}},
        {name: 'BLAST', id: 4, params: {w: 7, t: 3, c: 3}},
    ];
    $scope.wybranyAlg = $scope.algorytmy[0]
    $scope.wzorzec;
    $scope.cel;
    $scope.wynik = ""
    $scope.wybranyOrg = $scope.orgs[0]
    $scope.showTable = false

    // sciagniecie chromosomow dla organizmu
    $scope.org_chromosomes = {}
    loadChromosomes = function (org_id) {
        var request = {
            method: 'GET',
            url: 'api/organisms/' + org_id + '/chromosomes/'
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.org_chromosomes[org_id] = data;
            });
    }

    //sciagniecie typow dla chromosomu
    $scope.chr_types = {}
    loadTypes = function (id_chr) {
        var request = {
            method: 'GET',
            url: 'api/chromosomes/' + id_chr + '/annotation_types/'
        };
        return $http(request)
            .success(function (data) {
                //trzeba odrazu dane wsadzac to obiektu scope - nie potrafie ich przekazac przez returna
                $scope.chr_types[id_chr] = data;
            });
    }

    $scope.$watch('wybranyOrg', function () {
        // $scope.wybranyChr_id= $scope.wybranyOrg.chromosomes[0]
        // $scope.listaChr = $scope.wybranyOrg.chromosomes
        loadChromosomes($scope.wybranyOrg.id).then(function () {
            $scope.listChromosomow = $scope.org_chromosomes[$scope.wybranyOrg.id]
            // debugger
            $scope.wybranyChr = $scope.listChromosomow[0]
            // console.log($scope.wybranyChr.number)
        })
    })
    $scope.$watch('wybranyChr', function () {
        loadTypes($scope.wybranyChr.id).then(function () {
            $scope.listaTypow = $scope.chr_types[$scope.wybranyChr.id]
            // console.log($scope.listaTypow)
            $scope.wybranyTyp = $scope.listaTypow[0]
            // console.log($scope.wybranyTyp.name)
        })
    })


    // TODO na sztywno wpisany zeby szybciej pokazac -> usunac nizej
    $scope.wzorzec = "CTTCAGCAAAG"

    $scope.searchSeq = function () {
        var request = {
            method: 'POST',
            url: '/api/calc',
            //params: {param1: "p1p1p1", param2: "p2p2p2"}, //query string parametr
            data: {
                pattern: $scope.wzorzec,
                alg_id: $scope.wybranyAlg['id'],
                alg_name: $scope.wybranyAlg['name'],
                alg_params: {dupa: 234},
                annotation_params: {
                    chr_id: $scope.wybranyChr.id,
                    org_id: $scope.wybranyOrg.id,
                    type_id: $scope.wybranyTyp.id
                }
            } //ukryte data w poscie
        };
        $http(request)
            .success(function (data) {
                $scope.wynik = $filter("multipleLineWhenManyPos")(data)
                $scope.showTable = true
            });
    }

    $scope.teleport = function (item) {
        console.log(item)
        DataBufor.setData('view_from', item['pos']) //pos to pozycja wzgledna wzgledem poczatku scaffoldu
        DataBufor.setData('view_to', item['pos'] + $scope.wzorzec.length)
        DataBufor.setData('annotation_id', item['annotation_id'])
        // window.location.replace("#/organisms/" + item['org_id'] +"/chromosomes/" + item['chr_id'] + "/annotations")
        window.location.replace("#/organisms/" + item['org_id'] + "/chromosomes/" + item['chr_id'] + '/types/' + 54 + "/annotations")

    }

})