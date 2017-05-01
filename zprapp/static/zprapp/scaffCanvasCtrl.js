/**
 * Created by mhaponiu on 02.04.15.
 */

function scaffCanvasCtrl($scope, $filter, DataBufor, $http, $routeParams) {
//PANEL SETTINGS
    var initSettings = function () {
        $scope.settings = {};
        $scope.settings.defaults = {};
        $scope.settings.defaults.zoom = 50;
        $scope.settings.defaults.skok = 200000;
        $scope.settings.defaults.widok_od = 0;
        $scope.settings.defaults.widok_do = DataBufor.getData("chr_length")
        $scope.settings.defaults.skala = 2;

        $scope.settings.reset = function () {
            $scope.settings.zoom = $scope.settings.defaults.zoom;
            $scope.settings.skok = $scope.settings.defaults.skok;
            $scope.settings.widok_od = $scope.settings.defaults.widok_od;
            $scope.settings.widok_do = $scope.settings.defaults.widok_do;
            $scope.settings.skala = $scope.settings.defaults.skala;
            $scope.settings.tmp = {};
            $scope.settings.tmp.widok_od = $scope.settings.defaults.widok_od;
            $scope.settings.tmp.widok_do = $scope.settings.defaults.widok_do;
            $scope.textarea.text = $scope.textarea.defaults.text;
            $scope.textarea.visible = false;
            updatePanel();
        }
        $scope.settings.reset();
    }
    //initSettings()

    //pole z tekstem sekwencji aktualnie wyswietlanej
    $scope.textarea = {};
    $scope.textarea.text = "jakis tam tekst inicjalizacyjny";
    $scope.textarea.defaults = {};
    $scope.textarea.defaults.text = "<<< czekaj... >>>"
    $scope.textarea.ikona = "glyphicon glyphicon-eye-close"
    $scope.textarea.visible = false;
    $scope.textarea.reset = function(){
        $scope.textarea.text = $scope.textarea.defaults.text;
    }
    $scope.textarea.toggle = function () {
        $scope.textarea.visible = !$scope.textarea.visible;
        if ($scope.textarea.visible) {
            $scope.textarea.reset();
            $scope.textarea.ikona = "glyphicon glyphicon-eye-open"
        }
        else {
            $scope.textarea.ikona = "glyphicon glyphicon-eye-close"
        }
    }
    $scope.textarea.loadSequence = function(){
        var request = {
            method: 'GET',
            url: 'api/organisms/' + $routeParams.id_org + '/chromosomes/' + $routeParams.id_chr + '/annotation_types/' + $scope.tmp_annotation_type + '/sequence/',
            params: {
                start: $scope.settings.widok_od,
                end: $scope.settings.widok_do
            }
        };
        return $http(request)
            .success(function (data) {
                $scope.textarea.text = data;
            });
    }


    //-------------canvas data aktualnych scaffoldow------------------------------------
    $scope.canvas = {};
    $scope.canvas.data = []; //scaffoldy na aktualny main view
    $scope.canvas.defaults = {}
    $scope.canvas.skala = 2;


//######################### GLOWNA INICJALIZACJA ########################################################
    $scope.promiseLoadScaffolds.then(function () {
        return pobierzChromosomeLength();
    }).then(function () {
        initSettings();
        //$scope.canvas.getViewData(); -> wykonywany juz w initSettings()?
    }).then(function(){
        var view_from = DataBufor.getData('view_from') //jest to wzgledem skafoldu
        var view_to = DataBufor.getData('view_to') // jest to wzgledem skafoldu
        var start_scf = 0

        if(angular.isNumber(view_from, view_to) && view_from < view_to){
            var scf_id = DataBufor.getData('scf_id')
            console.log($scope.scflds)

            for(var i = 0; i < $scope.scflds.length; i++){
                if($scope.scflds[i]['pk'] == scf_id){
                    start_scf = $scope.scflds[i]['fields']['start_chr']
                    break
                }
            }
            $scope.settings.widok_od = start_scf + view_from
            $scope.settings.widok_do = start_scf + view_to
        }
    }).then(function(){
        setDrawStage()
    })
//######################### KONIEC GLOWNA INICJALIZACJA ########################################################


    //wywolywanie ma sens dopiero gdy istnieje juz $scope.scflds   =>   $scope.promiseLoadScaffolds
    $scope.canvas.getViewData = function () {
        console.log("getViewDATA")
        console.log($scope.scflds)
        $scope.canvas.data = $filter("wytnijNaScaffView")($scope.scflds, $scope.settings.widok_od, $scope.settings.widok_do)
        //sortowanie rosnace po fields.order
        $scope.canvas.data.sort(function(a,b){
            return a.start_chr - b.start_chr;
        })
    }

    //pomocnicze guziki do wywolan asynchronicznych
    $scope.klik = function () {
        console.log("KLIK")
        console.log($scope.canvas.mrkrs)

        //$scope.canvas.meanings = $filter("uniqueMeaningsFromMarkers")($scope.mrkrs, $scope.meanings);
        //console.log($scope.canvas.meanings);
        //console.log($scope.meanings);
    }
    $scope.guzik = function () {
        console.log("GUZIK")
        ajaxRequest()
    }

    var ajaxRequest = function(){
        var request = {
            method: 'POST',
            url: 'ajax_post',
            params: {param1: "p1p1p1", param2: "p2p2p2"}, //query string parametr
            data: {data1: "d1d1d1", data2: "d2d2d2"} //ukryte data w poscie
            //headers: {'Content-Type': 'application/x-www-form-urlencoded', //musi tak byc zeby posta dobrze odebralo, wiekszosc bibliotek JS tak robi
            //            'X-Requested-With': 'XMLHttpRequest'} //zeby w django request.is_ajax dawalo true
        };
        $http(request)
            .success(function (data) {
                console.log(data)
            });
    }

    var updatePanel = function(){
        $scope.settings.tmp.widok_od = $scope.settings.widok_od;
        $scope.settings.tmp.widok_do = $scope.settings.widok_do;
        $scope.canvas.getViewData();
        if($scope.textarea.visible){
            $scope.textarea.toggle();
        }

        setDrawStage();
    }
    
    $scope.updatePanel = function(){
        updatePanel()
    }

    $scope.skokLewo = function(){
        console.log("skokLewo")
        var skok = $scope.settings.skok;
        var widok_od = $scope.settings.widok_od;
        var widok_do = $scope.settings.widok_do;
        var delta = widok_do - widok_od;
        var nowy_widok_od = widok_od;
        var nowy_widok_do = widok_do;
        nowy_widok_od = widok_od - skok;
        nowy_widok_do = widok_do - skok;
        if(nowy_widok_od < 0 || nowy_widok_do < 0){
            $scope.settings.widok_od = 0;
            $scope.settings.widok_do = delta;
        }
        else{
            $scope.settings.widok_od = nowy_widok_od;
            $scope.settings.widok_do = nowy_widok_do;
        }
        updatePanel();
    }

    $scope.skokPrawo = function(){
        console.log("skokPrawo")
        var skok = $scope.settings.skok;
        var widok_od = $scope.settings.widok_od;
        var widok_do = $scope.settings.widok_do;
        var delta = widok_do - widok_od;
        var max = DataBufor.getData("chr_length");
        var nowy_widok_od = widok_od;
        var nowy_widok_do = widok_do;
        nowy_widok_od = widok_od + skok;
        nowy_widok_do = widok_do + skok;
        if(nowy_widok_od > max || nowy_widok_do > max){
            $scope.settings.widok_do = max;
            $scope.settings.widok_od = max - delta;
        }
        else{
            $scope.settings.widok_od = nowy_widok_od;
            $scope.settings.widok_do = nowy_widok_do;
        }
        updatePanel();
    }

    $scope.zoomIn = function(){
        console.log("zoomIN")
        var zoom = $scope.settings.zoom / 100;
        var widok_od = $scope.settings.widok_od;
        var widok_do = $scope.settings.widok_do;
        var delta = widok_do - widok_od;
        if(delta <= 20) return;
        var nowa_delta = delta * zoom;
        var max = DataBufor.getData("chr_length");
        var nowy_widok_od = widok_od;
        var nowy_widok_do = widok_do;

        nowy_widok_od = Math.round((widok_od + widok_do)/2 - nowa_delta/2);
        nowy_widok_do = Math.round((widok_od + widok_do)/2 + nowa_delta/2);

        $scope.settings.widok_od = nowy_widok_od;
        $scope.settings.widok_do = nowy_widok_do;
        updatePanel()

    }

    $scope.zoomOut = function(){
        console.log("zoomOUT")
        var zoom = 1 / ($scope.settings.zoom / 100);
        var widok_od = $scope.settings.widok_od;
        var widok_do = $scope.settings.widok_do;
        var delta = widok_do - widok_od;
        var nowa_delta = delta * zoom;
        var max = DataBufor.getData("chr_length");
        var nowy_widok_od = widok_od;
        var nowy_widok_do = widok_do;
        nowy_widok_od = Math.round((widok_od + widok_do)/2 - nowa_delta/2);
        nowy_widok_do = Math.round((widok_od + widok_do)/2 + nowa_delta/2);

        if (nowy_widok_od <= 0 && nowy_widok_do >= max) {
            nowy_widok_od = 0
            nowy_widok_do = max;
        }
        else {
            if (nowy_widok_od <= 0) {
                nowy_widok_od = 0;
                nowy_widok_do = Math.round(nowa_delta);
            }
            if (nowy_widok_do >= max) {
                nowy_widok_do = max
                nowy_widok_od = max - Math.round(nowa_delta);
            }
        }

        $scope.settings.widok_od = nowy_widok_od;
        $scope.settings.widok_do = nowy_widok_do;

        updatePanel()
    }

    $scope.logIn = function(){
        console.log("logIn")
        $scope.settings.widok_od = $scope.settings.tmp.widok_od;
        $scope.settings.widok_do = $scope.settings.tmp.widok_do;
        updatePanel()
    }

    //zwraca promise http
    var pobierzChromosomeLength = function () {
        var request = {
            method: 'GET',
            url: 'ajax_chrmy',
            params: {id_chr_len: $scope.chr_id}
        };
        return $http(request)
            .success(function (data) {
                DataBufor.setData("chr_length", data[0].fields.length);
            });
    }

    function podziel(n, odkad, dokad) {
        //zwraca tablice z powtarzajacymi sie wartosciami -> uzyc uniquePodziel
        var tablica = [];
        if (n < 1) {
            return [odkad, dokad];
        }
        var new_podzial = Math.abs(dokad + odkad) / 2;
        //podziel(n-1, odkad, new_podzial);
        //podziel(n-1, new_podzial, dokad);
        tablica = tablica.concat(podziel(n - 1, odkad, new_podzial), podziel(n - 1, new_podzial, dokad));
        return tablica;
    }

    function uniquePodziel(n, odkad, dokad) {
        var tablica = podziel(n, odkad, dokad);
        for (var i = 1; i < (tablica.length - 1); i++) {
            if (tablica[i] == tablica[i - 1]) {
                tablica.splice(i, 1);
                i--;
            }
        }
        return tablica;
    }


//-------------------------CANVAS----------------------
    var events = new Events("canvasScaffold");
    var canvas = events.getCanvas();
    var context = events.getContext();
    canvas.style.backgroundColor = "#f5f5f5";
    document.getElementById("span_od").style.backgroundColor = "#c7c7c7";
    document.getElementById("span_do").style.backgroundColor = "#c7c7c7";
    document.getElementById("zoom_procent").style.backgroundColor = "#c7c7c7";

    function drawRectangle(x_down, y_down, w, h) {
        context.save();
        context.rect(x_down, y_down -h, w, h);
        context.fill();
        context.restore();
    }

    function fitCanvasToScreenAndSkala(){
        if((window.innerWidth) > 991) {
            canvas.width = 940;
            $scope.settings.skala = 3;
        }
        else{
            if(window.innerWidth < 765) {
                canvas.width = window.innerWidth - 45;
                $scope.settings.skala = 1;
            }
            else {
                canvas.width = 720;
                $scope.settings.skala = 2;
            }
        }
    }

    function drawPreview(x_from, x_to, y, height){
        context.save();
        //linia
        context.beginPath()
        context.lineWidth = 2;
        context.strokeStyle = "black";
        context.moveTo(x_from, y);
        context.lineTo(x_to, y);
        context.stroke();
        //prostokat podgladu
        //context.fillStyle = "rgba(91, 192, 222, 0.5)"
        context.fillStyle = "rgba(92, 184, 92, 0.6)";
        var length = x_to - x_from;
        var max_real = DataBufor.getData("chr_length")
        var odkad_real = $scope.settings.widok_od;
        var dokad_real = $scope.settings.widok_do;
        var odkad = x_from + (odkad_real/max_real) * length;
        var dokad = x_from + (dokad_real/max_real) * length;
        //namalowanie na sile za kreski gdy bylaby za mala
        var prog = 0.005 * length;
        context.beginPath();//nie wiem czy to musi byc -> nie zaszkodzi a moze bledow uniknie;
        if(dokad - odkad < prog){
            drawRectangle(odkad, y + 0.5*height, prog, height)
        }
        else{
            drawRectangle(odkad, y + 0.5*height, dokad-odkad, height)
        }
        context.restore()
    }

    function drawComaVertically(x, y, h){
        context.save();
        context.beginPath();
        context.lineWidth = 2;
        context.strokeStyle = "black";
        context.moveTo(x, y-(h/2));
        context.lineTo(x, y+(h/2));
        context.stroke();
        context.restore();
    }

    function drawLabelText(x, y, h, text){
        h = 0.75*h;
        context.save();
        context.font = h.toString() + "px Helvetica";
        context.fillStyle = "black";
        context.textAlign = "center";
        context.textBaseline = "bottom";
        context.fillText(text, x, y);
        context.restore();
    }

    function drawSkala(x_from, x_to, y){
        //main line
        context.save();
        context.beginPath();
        context.lineWidth = 2;
        context.strokeStyle = "black";
        context.moveTo(x_from, y);
        context.lineTo(x_to, y);
        context.stroke();
        context.restore();

        var h_coma = canvas.height * 0.05;
        var n_podzial = $scope.settings.skala;
        //n_podzial = 2;
        var data = uniquePodziel(n_podzial, $scope.settings.widok_od, $scope.settings.widok_do);
        var skok = (x_to - x_from) / Math.pow(2, n_podzial);
        var przecinek = 1;
        if($scope.settings.widok_do - $scope.settings.widok_od < 2000000){
            przecinek=2;
        }
        if($scope.settings.widok_do - $scope.settings.widok_od < 1000000){
            przecinek=3;
        }
        if($scope.settings.widok_do - $scope.settings.widok_od < 10000){
            przecinek=4;
        }
        if($scope.settings.widok_do - $scope.settings.widok_od < 1000){
            przecinek=0;
        }
        for(var i= 0, item; i < data.length; i++){
            item = $filter("roundAndFormatBP")(data[i],przecinek);
            drawComaVertically(x_from + i*skok, y, h_coma);
            drawLabelText(x_from + i*skok, y-h_coma/2, h_coma, item);
            //pomocnicza podzialka
            drawComaVertically(x_from + i*skok+skok/2, y, h_coma/2);
        }
    }

    function drawMainViewScaff(x_from, x_to, y, h){
        function drawScaff(from, to){
            drawRectangle(from, y+h/2, to-from, h);
        }
        context.save();
        //glowny prostokat z obramowaniem
        context.fillStyle = "#fdfdfd";
        context.beginPath();
        context.lineWidth = 1;
        drawRectangle(x_from, y+h/2, x_to-x_from, h);
        context.stroke();
        context.restore()

        context.save();
        //context.fillStyle = "rgba(91, 192, 222, 0.5)"; //niebieski
        //context.fillStyle = "rgba(217, 83, 79, 0.9)"; //czerwony-rozowy
        //context.fillStyle = "#855E42"; //braz
        context.fillStyle = "#B5A642"; //oliwka
        var i, k, item, odkad, dokad;//dla glownej petli

        //rysujemy scaffoldy
        for(i = 0;i<=$scope.canvas.data.length-1; i++){
            item = $scope.canvas.data[i];
            odkad = (item.start_chr - $scope.settings.widok_od)
                    *(x_to - x_from) / ($scope.settings.widok_do - $scope.settings.widok_od) + x_from;
            dokad = (item.start_chr + item.length - $scope.settings.widok_od)
                    *(x_to - x_from) / ($scope.settings.widok_do - $scope.settings.widok_od) + x_from;
            if(i==0 && item.start_chr < $scope.settings.widok_od){
                odkad = x_from;
                if(item.start_chr + item.length > $scope.settings.widok_do){
                    dokad = x_to;
                }
            }
            else{
                if(i==$scope.canvas.data.length-1 && item.start_chr + item.length > $scope.settings.widok_do){
                    dokad = x_to;
                }
            }
            context.beginPath();
            drawScaff(odkad, dokad);
        }
        context.restore();

    }

    function drawScaffCanvas(parent){
        fitCanvasToScreenAndSkala();
        parent.clear();
        var x_margin = 0.05;
        var y_margin = 0.1;
        var x_left_margin = canvas.width * x_margin;
        var x_right_margin = canvas.width * (1-x_margin);
        var y_up_margin = canvas.height * y_margin;
        var y_down_margin = canvas.height * (1 - y_margin);
        var height = y_down_margin - y_up_margin;
        var width = x_right_margin - x_left_margin;
        //context.lineWidth = 0.001;

        var h_preview = height * 0.1;
        drawPreview(x_left_margin,
                    x_right_margin,
                    y_down_margin - h_preview/2,
                    h_preview);

        var h_skala = height * 0.1;
        drawSkala(x_left_margin,
                  x_right_margin,
                  height * 0.8);

        var h_mainView = height * 0.2;
        drawMainViewScaff(x_left_margin,
                          x_right_margin,
                          y_up_margin + h_mainView,
                          h_mainView);

        //drawRectangle(50, 50, data[0].fields.length / 10, data[0].fields.length / 10)
    }

    function setDrawStage(){
        events.setDrawStage(function(){
            drawScaffCanvas(this)
        })
    }
    //setDrawStage(chr_tab);
    window.onresize = function(){
        events.drawStage();
    }
}