/**
 * Created by mhaponiu on 18.01.15.
 */
function OrganizmKontroler($scope, Items) {
    //$scope.id_ogranizmu = 1;
    //$scope.testowy = "na sztywno dodany tekst w OrganizmKontroler";
    //$scope.dane = Items.cos;
    $scope.reqget = Items.organizmy();
    $scope.wybierzOrganizm = function (numerWiersza, nazwa, kluczGlowny) {
        $scope.wybranyOrganizm = numerWiersza;
        $scope.organizmEdytowany = nazwa;
        //kluczOrganizmu chyba niepotrzebny - nigdzie nie uzywany
        $scope.kluczOrganizmu = kluczGlowny;
        //$scope.showEdytujOrganizm = false
    };

    //formularz Nowy Organizm
    $scope.showNowyOrganizm = false;
    $scope.toggleNowyOrganizm = function () {
        $scope.showNowyOrganizm = !$scope.showNowyOrganizm;
        $scope.nowyOrganizm = "";
    };
    $scope.dodano = function (napis) {
        $scope.showNowyOrganizm = false;
        alert("Dodano nowy organizm:\n\n" + napis);
        //aktualizacja listy organizmow
        $scope.reqget = Items.nowyOrganizm($scope.nowyOrganizm);
    };

    //usuniecie organizmu
    $scope.usunOrganizm = function (pk, nazwa) {
        alert("Usunięto organizm   " + nazwa);
        //aktualizacja listy organizmow
        $scope.reqget = Items.usunOrganizm(pk);
    };

    //edycja organizmu
    $scope.showEdytujOrganizm = false;
    $scope.toggleEdytujOrganizm = function (nazwaOrganizmu) {
        $scope.showEdytujOrganizm = !$scope.showEdytujOrganizm;
        $scope.organizmEdytowany = nazwaOrganizmu;
    };
    $scope.edytujOrganizm = function (pk, staraNazwa, nowaNazwa) {
        alert("ZMIENIONO NAZWĘ ORGANIZMU\n\nStara nazwa:     " + staraNazwa + "\n\nNowa nazwa:    " + nowaNazwa);
        $scope.showEdytujOrganizm = !$scope.showEdytujOrganizm;
        $scope.reqget = Items.edytujOrganizm(pk, nowaNazwa);
    }
}