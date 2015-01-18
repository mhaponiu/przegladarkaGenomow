/**
 * Created by mhaponiu on 20.12.14.
 */

var zprModule = angular.module('ZprAppModule', []);

zprModule.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
});

//ZprAppModule.factory('Items', function(){
//    var items = {};
//    items.organizmy = function(){
//        var request = {
//            method: 'GET',
//            url: 'zprapp/ajax_organizm'
//        };
//        $http(request).
//            success(function(data){
//                return data['organizm'];
//        });
//    };
//    items.data = "data";
//    return items;
//});

zprModule.factory('Items', function ($http, $q) {
    var items = {};
    items.cos = 'tekst z factory items.cos';
    items.organizmy = function () {
        var request = {
            method: 'GET',
            url: 'ajax_wszystkieOrganizmy'
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };
    items.organizm = function (numer) {
        var obiekt = {id: numer};
        var request = {
            method: 'GET',
            url: 'ajax_organizm',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };
    items.nowyOrganizm = function (nazwaOrg) {
        var obiekt = {nazwa: nazwaOrg};
        var request = {
            method: 'GET',
            url: 'ajax_nowyOrganizm',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.usunOrganizm = function (pk) {
        var obiekt = {id: pk};
        var request = {
            method: 'GET',
            url: 'ajax_usunOrganizm',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.edytujOrganizm = function (pk, nowaNazwa) {
        var obiekt = {id: pk, nazwa: nowaNazwa};
        var request = {
            method: 'GET',
            url: 'ajax_edytujOrganizm',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.chromosomy = function (id_organizmu) {
        var obiekt = {id_org: id_organizmu};
        var request = {
            method: 'GET',
            url: 'ajax_chromosomy',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.chromosom = function (id_org, id_chr) {
        var obiekt = {id_org: id_org, id_chr: id_chr};
        var request = {
            method: 'GET',
            url: 'ajax_jedenchromosom',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.usunChromosom = function (id_org, id_chr) {
        var obiekt = {id_org: id_org, id_chr: id_chr};
        var request = {
            method: 'GET',
            url: 'ajax_usunChromosom',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.nowyChromosom = function (id_org, nazwa, dlugosc) {
        var obiekt = {id_org: id_org, nazwa: nazwa, dlugosc: dlugosc};
        var request = {
            method: 'GET',
            url: 'ajax_nowyChromosom',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.edytujChromosom = function (id_org, id_chr, nazwa, dlugosc) {
        var obiekt = {
            id_org: id_org,
            id_chr: id_chr,
            nazwa: nazwa,
            dlugosc: dlugosc
        };
        var request = {
            method: 'GET',
            url: 'ajax_edytujChromosom',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.markery = function (id_organizmu, id_chr) {
        var obiekt = {id_org: id_organizmu, id_chr: id_chr};
        var request = {
            method: 'GET',
            url: 'ajax_wszystkieMarkery',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.nowyMarker = function (id_org, id_chr, sekwencja, poz_od, poz_do) {
        var obiekt = {id_org: id_org, id_chr: id_chr, sekwencja: sekwencja, poz_od: poz_od, poz_do: poz_do};
        var request = {
            method: 'GET',
            url: 'ajax_nowyMarker',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.usunMarker = function (id_org, id_chr, id_mark) {
        var obiekt = {id_org: id_org, id_chr: id_chr, id_mark: id_mark};
        var request = {
            method: 'GET',
            url: 'ajax_usunMarker',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    items.edytujMarker = function (id_org, id_chr, id_mark, poz_od, poz_do, sekwencja) {
        var obiekt = {
            o: id_org,
            ch: id_chr,
            m: id_mark,
            od: poz_od,
            do: poz_do,
            s: sekwencja
        };
        var request = {
            method: 'GET',
            url: 'ajax_edytujMarker',
            params: obiekt
        };
        var obietnica = $q.defer();
        $http(request)
            .success(function (data) {
                obietnica.resolve(
                    //{obiet: data['organizm']}
                    data
                );
            })
            .error(function (data) {

            });
        var odp = obietnica.promise;
        return odp;
    };

    return items;
});


function zprRouteConfig($routeProvider) {
    $routeProvider.
        when('/organizmy', {
            controller: OrganizmKontroler,
            templateUrl: 'organizmy'
        }).
        when('/organizm/:id/chromosomy', {
            controller: ChromosomKontroler,
            templateUrl: 'organizm/chromosomy'
        }).
        when('/organizm/:id_org/chromosom/:id_chr/markery', {
            controller: MarkerKontroler,
            templateUrl: 'markery'
        }).
        otherwise({
            redirectTo: '/organizmy'
        });
}

zprModule.config(zprRouteConfig);


//do pierwszych prob z wymiana danych
function Kontroler($scope, $http) {
    $scope.wartosc = {startowa: 5};
    $scope.wartosc.pomnozona = 50;
    $scope.slownik = {};

    $scope.pomnoz = function () {
        $scope.wartosc.pomnozona = $scope.wartosc.startowa * 10;
    };
    $scope.dawajgeta = function () {
        var obiekt = {tekst: "wartosctext", id: 7};
        var obiekt_json = angular.toJson(obiekt);
        /*
         *to ponizej dziala tylko dla GET?
         */
        var request = {
            method: 'GET',
            url: 'zprapp/ajax',
            //headers: {
            //    'Content-Type': 'application/json'
            //},
            //params dodaje do URL parametry obiektu
            params: obiekt,
            //tego data jakby w ogole nie widzial potem w diango w slowniku
            data: angular.toJson(obiekt)
        };
        $http(request).
            success(function (data) {
                $scope.slownik = data['klucz'];
            });
    };
}
