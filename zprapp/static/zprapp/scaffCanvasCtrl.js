/**
 * Created by mhaponiu on 02.04.15.
 */

function scaffCanvasCtrl($scope, $filter, DataBufor, $http) {
//PANEL SETTINGS
    var initSettings = function () {
        $scope.settings = {};
        $scope.settings.defaults = {};
        //FIXME ladniej niby ale nie dziala bo sie caly obiekt nadpisuje -> pokombinowac z with($scope.settings.defaults){}
        //$scope.settings.defaults = {
        //    zoom: 2,
        //    skok: 10000,
        //    widok_od: 0,
        //    widok_do: DataBufor.getData("chr_length")
        //}
        $scope.settings.defaults.zoom = 2;
        $scope.settings.defaults.skok = 10000;
        $scope.settings.defaults.widok_od = 0;
        $scope.settings.defaults.widok_do = DataBufor.getData("chr_length")

        $scope.settings.reset = function () {
            //FIXME ladniej niby ale nie dziala bo sie caly obiekt nadpisuje -> pokombinowac z with($scope.settings.defaults){}
            //$scope.settings = {
            //    zoom: $scope.settings.defaults.zoom,
            //    skok: $scope.settings.defaults.skok,
            //    widok_od: $scope.settings.defaults.widok_od,
            //    widok_do: $scope.settings.defaults.widok_do,
            //    tmp: {
            //        widok_od: $scope.settings.defaults.widok_od,
            //        widok_do: $scope.settings.defaults.widok_do
            //    }
            //}
            $scope.settings.zoom = $scope.settings.defaults.zoom;
            $scope.settings.skok = $scope.settings.defaults.skok;
            $scope.settings.widok_od = $scope.settings.defaults.widok_od;
            $scope.settings.widok_do = $scope.settings.defaults.widok_do;
            $scope.settings.tmp = {};
            $scope.settings.tmp.widok_od = $scope.settings.defaults.widok_od;
            $scope.settings.tmp.widok_do = $scope.settings.defaults.widok_do;
        }
        $scope.settings.reset();
    }
    //initSettings()

    //pole z tekstem sekwencji aktualnie wyswietlanej
    $scope.textarea = {};
    $scope.textarea.text = "BBBBBBBBBBBBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDZZZZZZZZZZZZZZZZZZZZZZZOOOOOOOOOOOOOOOOOOOODDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUUUUUUGGGGGGGGGGGGGGGGGGGGIIIIIIIIIIIIIIIIITTTTTTTTTTTEEEEEEEEEEKKKKKKKKSSSSSTTTTTTT"
    $scope.textarea.ikona = "glyphicon glyphicon-eye-close"
    $scope.textarea.visible = false;
    $scope.textarea.toggle = function () {
        $scope.textarea.visible = !$scope.textarea.visible;
        if ($scope.textarea.visible) {
            $scope.textarea.ikona = "glyphicon glyphicon-eye-open"
        }
        else {
            $scope.textarea.ikona = "glyphicon glyphicon-eye-close"
        }
    }

    //pomocnicze guziki do wywolan asynchronicznych
    $scope.klik = function () {
        console.log("KLIK")
        DataBufor.setData("chr_length", 777);
    }
    $scope.guzik = function () {
        console.log("GUZIK")
        console.log(DataBufor.getData("chr_length"));
    }


//-------------canvas data aktualnych scaffoldow------------------------------------
    $scope.canvas = {};
    $scope.canvas.data = [];
    $scope.canvas.skala = {}
    $scope.canvas.podglad = {}

    //wywolywanie ma sens dopiero gdy istnieje juz $scope.scflds   =>   $scope.promiseLoadScaffolds
    $scope.canvas.getViewData = function () {
        console.log("getViewDATA")
        $scope.canvas.data = $filter("wytnijNaScaffView")($scope.scflds, $scope.settings.widok_od, $scope.settings.widok_do)
    }

    //zwraca promise http
    var pobierzChromosomeLength = function () {
        var request = {
            method: 'GET',
            url: 'ajax_chrmy',
            params: {id: $scope.chr_id}
        };
        return $http(request)
            .success(function (data) {
                DataBufor.setData("chr_length", data[0].fields.length);
            });
    }

    $scope.promiseLoadScaffolds.then(function () {
        return pobierzChromosomeLength();
    }).then(function () {
        initSettings();
        $scope.canvas.getViewData();
    })


//-------------------------CANVAS----------------------
    var events = new Events("canvasScaffold");
    var canvas = events.getCanvas();
    var context = events.getContext();
    canvas.style.backgroundColor = "#f5f5f5";
    document.getElementById("span_od").style.backgroundColor = "#c7c7c7";
    document.getElementById("span_do").style.backgroundColor = "#c7c7c7";
    ;

}