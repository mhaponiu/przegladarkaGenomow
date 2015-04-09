/**
 * Created by mhaponiu on 25.02.15.
 */

var cucModule = angular.module('CucModule', ['ngRoute']);
cucModule.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
    //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
});

function cucRouteConfig($routeProvider) {
    $routeProvider.
        when('/chromosomy', {
            controller: ChromosomKontroler,
            templateUrl: 'chromosomy'
        }).
        when('/chromosom/:id/scaffoldy', {
            controller: ScaffoldKontroler,
            templateUrl: 'scaffoldy'
        }).
        when('/chromosom/:id_chr/scaffold/:id_sc/sekwencja', {
            controller: SekwencjaKontroler,
            templateUrl: 'sekwencje'
        }).
        otherwise({
            redirectTo: '/chromosomy'
        });
}

//po przeniesieniu do angular 1.2.X nie działa - przeniesione do kontrolerow
// trzeba dane z $http odrazu do scope'a ladowac
//cucModule.factory('Items', function($http, $q){
//    var items = {};
//    items.chromosomy = function () {
//        var request = {
//            method: 'GET',
//            url: 'ajax_chrmy'
//        };
//        var obietnica = $q.defer();
//        $http(request)
//            .success(function (data) {
//                obietnica.resolve(data);
//            });
//        return obietnica.promise;
//    };
//    items.scaffoldy = function (id_chr) {
//        var request = {
//            method: 'GET',
//            url: 'ajax_scfldy',
//            params: {id: id_chr}
//        };
//        var obietnica = $q.defer();
//        $http(request)
//            .success(function (data) {
//                obietnica.resolve(data);
//            });
//        return obietnica.promise;
//    };
//    items.sekwencja = function (id_chr, id_sc) {
//        var request = {
//            method: 'GET',
//            url: 'ajax_scs',
//            params: {id_chr: id_chr, id_sc: id_sc}
//        };
//        var obietnica = $q.defer();
//        $http(request)
//            .success(function (data) {
//                obietnica.resolve(data);
//            });
//        return obietnica.promise;
//    };
//    return items;
//});

cucModule.config(cucRouteConfig);

cucModule.filter("wytnijNaScaffView", function(){
    //wycina ze wszystkich scaffoldow te ktore maja byc widoczne w glownym widoku canvas'a
    return function(data, odkad, dokad){
        if (angular.isArray(data) && angular.isNumber(odkad) && angular.isNumber(dokad)){
            console.log("wytnijNaScaffView in: odkad " + odkad + " dokad: " + dokad);
            var noweScaffoldy = [];
            angular.forEach(data, function(item){
                if (!(
                    (item.fields.start + item.fields.length < odkad) ||
                    (item.fields.start > dokad)
                    )){
                    noweScaffoldy.push(item)
                }
                else{
                    //console.log("odpada id: " + item.pk + " start: " + item.fields.start)
                }
                //noweScaffoldy.push(item)
            })
            return noweScaffoldy;
        }
        else{
            //console.log("wytnijNaScaffView out: odkad " + odkad + " dokad: " + dokad);
            return data
        }
    }
})

cucModule.service("DataBufor", function(){
    var data = {};
    return {
        getData: function(name){
            //console.log("DataBufor: getData: " + name + " value: " + data[name])
            return data[name]
        },
        setData: function(name, value){
            //console.log("DataBufor: setData: " + name + " value: " + value)
            data[name] = value;
        }
    }
})