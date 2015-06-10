/**
 * Created by mhaponiu on 25.02.15.
 */

var cucModule = angular.module('CucModule', ['ngRoute', 'ui.bootstrap', 'ngCookies']);

//w configu moga byc tylko providery, service'y trzeba do run dawac
cucModule.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}).config(function($httpProvider){
    //chyba juz nie konieczne
    //$httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
}).run(function($http, $cookies){
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
});

//function cucRouteConfig($routeProvider) {
//    $routeProvider.
//        when('/organizmy', {
//            controller: OrganizmKontroler,
//            templateUrl: 'organizmy'
//        }).
//        when('/chromosomy', {
//            controller: ChromosomKontroler,
//            templateUrl: 'chromosomy'
//        }).
//        when('/chromosom/:id/scaffoldy', {
//            controller: ScaffoldKontroler,
//            templateUrl: 'scaffoldy'
//        }).
//        when('/chromosom/:id_chr/scaffold/:id_sc/sekwencja', {
//            controller: SekwencjaKontroler,
//            templateUrl: 'sekwencje'
//        }).
//        otherwise({
//            redirectTo: '/chromosomy'
//        });
//}

function cucRouteConfig($routeProvider) {
    $routeProvider.
        when('/organizmy', {
            controller: OrganizmKontroler,
            templateUrl: 'templates/organizmy.html'
        }).
        when('/organizm/:id_org/chromosomy', {
            controller: ChromosomKontroler,
            templateUrl: 'templates/chromosomy.html'
        }).
        when('/organizm/:id_org/chromosom/:id_chr/scaffoldy', {
            controller: ScaffoldKontroler,
            templateUrl: 'templates/scaffoldy.html'
        }).
        when('/organizm/:id_org/chromosom/:id_chr/scaffold/:id_sc/sekwencja', {
            controller: SekwencjaKontroler,
            templateUrl: 'templates/sekwencja.html'
        }).
        otherwise({
            redirectTo: '/organizmy'
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
            //console.log("wytnijNaScaffView in: odkad " + odkad + " dokad: " + dokad);
            var noweObiekty = [];
            angular.forEach(data, function(item){
                if (!(
                    (item.fields.start + item.fields.length < odkad) ||
                    (item.fields.start > dokad)
                    )){
                    noweObiekty.push(item)
                }
                else{
                    //console.log("odpada id: " + item.pk + " start: " + item.fields.start)
                }
                //noweScaffoldy.push(item)
            })
            return noweObiekty;
        }
        else{
            //console.log("wytnijNaScaffView out: odkad " + odkad + " dokad: " + dokad);
            return data
        }
    }
}).filter("roundAndFormatBP", function () {
    return function (data, przecinek) {
        if ((angular.isString(data) || angular.isNumber(data)) && angular.isNumber(przecinek)) {
            var data_num = Math.round(Number(data))
            if(przecinek == 0){
                return data_num.toString()+"bp";
            }
            if (data_num) {
                //console.log("lux filtr roundAndformatBP")
                var data_str = data_num.toString();
                var len = data_str.length;
                if (len > 3) {
                    if (len > 6) {
                        //if (len > 9) {
                        //    data_num = Math.round(data_num / 100000000)
                        //    data_num = data_num / 10;
                        //    data_str = data_num.toString()
                        //    data_str = data_str.concat("Gbp")
                        //    return data_str;
                        //}
                        data_num = Math.round(data_num / Math.pow(10, 6-przecinek))
                        data_num = data_num / Math.pow(10, przecinek);
                        data_str = data_num.toString()
                        data_str = data_str.concat("Mbp")
                        return data_str;
                    }
                    data_num = Math.round(data_num / Math.pow(10, 3-przecinek))
                    data_num = data_num / Math.pow(10, przecinek);
                    data_str = data_num.toString()
                    data_str = data_str.concat("kbp")
                    return data_str;

                }
                else {
                    return data_str.concat("bp")
                }
            }
            else {
                //console.log("lipa filtr roundAndformatBP")
                return data;
            }
        }
        else {
            return data;

        }
    }
}).filter("uniqueMeaningsFromMarkers", function(){
    return function(markery, meanings){
        if(angular.isArray(markery) && angular.isArray(meanings)){
            var id = [];
            var mngs = [];
            var m;
            angular.forEach(markery, function(marker){
                m = marker.fields.meaning //to id_meaning tak naprawde
                if(id.indexOf(m) < 0){
                    id.push(m)
                    for(var i=0; i<meanings.length; i++){
                        if(meanings[i].pk == m){
                            mngs.push(meanings[i].fields.mean);
                            break;
                        }
                    }
                }
            })
            var uniqueMeanings = [];
            for(var i=0; i<id.length; i++){
                uniqueMeanings.push({id: id[i], meaning: mngs[i]});
            }
            return uniqueMeanings;
        }
        else{
            return markery;
        }
    }
}).filter("selectMarkersChecked", function() {
    return function (markery, meanings) {
        if (angular.isArray(markery) && angular.isArray(meanings)) {
            var mrkrs_selected=[]
            var id_mean = []
            for(var i=0; i<meanings.length; i++){
                if(meanings[i].check){
                    if(id_mean.indexOf(meanings[i].id) < 0){
                        id_mean.push(meanings[i].id)
                    }
                }
            }
            for(var i=0; i<markery.length; i++){
                if(id_mean.indexOf(markery[i].fields.meaning) >= 0){
                    mrkrs_selected.push(markery[i]);
                }
            }
            return mrkrs_selected;
        }
        else {
            return markery;
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