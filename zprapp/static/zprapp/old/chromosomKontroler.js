/**
 * Created by mhaponiu on 18.01.15.
 */
function ChromosomKontroler($scope, $routeParams, Items) {
    $scope.org = Items.organizm($routeParams.id);
    $scope.chromosomy = Items.chromosomy($routeParams.id);
    $scope.wybierzChromosom = function (numerWiersza, nazwa, dlugosc) {
        $scope.wybranyChromosom = numerWiersza;
        $scope.chromosomEdytowany = nazwa;
        $scope.dlugoscEdytowana = dlugosc;
    }
    //formularz Chromosom
    $scope.showNowyChromosom = false;
    $scope.nowyChromosom = {};
    $scope.toggleNowyChromosom = function () {
        $scope.showNowyChromosom = !$scope.showNowyChromosom;
        $scope.nowyChromosom.nazwa = "";
        $scope.nowyChromosom.dlugosc = 0;
    };

    //edycja chromosomu
    $scope.showEdytujChromosom = false;
    $scope.toggleEdytujChromosom = function (nazwaChromosomu) {
        $scope.showEdytujChromosom = !$scope.showEdytujChromosom;
        $scope.chromosomEdytowany = nazwaChromosomu;
    }
    $scope.edytujChromosom = function (pk, staraNazwa, staraDlugosc, nowaNazwa, nowaDlugosc) {
        alert("Edycja chromosomu:\n\n" + staraNazwa + "   o długości " + staraDlugosc + "\n\nna\n\n" + nowaNazwa + "   o długości " + nowaDlugosc);
        $scope.chromosomy = Items.edytujChromosom($scope.org.$$v.id, pk, nowaNazwa, nowaDlugosc);
    }

    //utworzenie nowego chromosomu
    $scope.zapiszNowyChromosom = function (nowyChr) {
        alert("Dodano nowy chromosom:\n\nnazwa:     " + nowyChr.nazwa + "\ndługość:  " + nowyChr.dlugosc);
        $scope.chromosomy = Items.nowyChromosom($scope.org.$$v.id, nowyChr.nazwa, nowyChr.dlugosc);
    }

    //usunięcie chromosomu
    $scope.usunChromosom = function (pk, nazwa) {
        alert("Usuwam chromosom:\n\n" + nazwa + " o pk= " + pk + "id_org:" + $scope.org.$$v.id);
        $scope.chromosomy = Items.usunChromosom($scope.org.$$v.id, pk);
    }
}
