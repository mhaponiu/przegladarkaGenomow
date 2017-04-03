/**
 * Created by mhaponiu on 23.03.15.
 */

function chrCanvasCtrl($scope, $http, $location, DataBufor, $routeParams) {
    var events = new Events("canvasChromosom");
    var canvas = events.getCanvas();
    var context = events.getContext();
    //context.fillStyle = "#5cb85c";

    with(canvas.style){
        backgroundColor="#f5f5f5";
        //width="100%";
        //height="auto"
    }

    function drawChromosom(x_down, y_down, w, h) {
        //context.beginPath();
        context.rect(x_down, y_down -h, w, h);
        context.fill();
        //context.closePath()
    }

    //wczesniej wpisywane te wartosci bylo na stale ale teraz w sumie niepotrzebne
    //var chr_tab = [29150775, 26165221, 40056285, 29601718, 30950768, 34089568, 20250815]
    ////var chr_tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    //var chr_tab_id = [52, 53, 54, 55, 56, 57, 58]
    //chr_tab_id = [43, 44, 45, 46, 47, 48, 49]

    var chr_tab_id = [];
    var chr_tab = [];
    //wypelniam te tablice pobranymi danymi z bazy;
    $scope.promiseLoadChromosomes.then(function(){
        for(var i=0; i<$scope.chrms.length; i++){
            chr_tab_id.push($scope.chrms[i].pk)
            chr_tab.push($scope.chrms[i].fields.length)
        }
    }).then(function(){
        events.drawStage();
    })



    //do użytku wewnątrz events.setDrawStage jako rodzic powinno byc 'this' events'a
    function drawChromosomCanvas(tablica_chr, rodzic) {
        var wsp = 1.5  //wspolczynik (szer_przerwy / szer_chr)
        if((window.innerWidth) > 991){
            canvas.width = 940;
        }
        else{
            if(window.innerWidth < 765){
                canvas.width = window.innerWidth - 45
            }
            else{
                canvas.width = 720;
            }

        }

        rodzic.clear();
        var liczba_przerw = tablica_chr.length + 1
        //var szer_przerwy = canvas.width * 0.078947
        //var szer_chr = canvas.width * 0.052632
        var szer_chr = canvas.width / (tablica_chr.length + wsp * (tablica_chr.length + 1));
        var szer_przerwy = wsp * szer_chr

        var y_line_start = canvas.height * 0.8;
        var y_line_end = canvas.height * 0.1;
        var x_line_start = szer_przerwy
        var tab_max = Math.max.apply(Math, tablica_chr)
        var max_len_chr = canvas.height * 0.7;
        var delta_x = 0
        var h, x, y, x_text, y_text;
        var napis = 0;
        var h_napis = Math.round(0.5 * (canvas.height - y_line_start))

        var addRegionEventListener = function(wskaznik_rodzica, string_zdarzenia, argument, fun){
            wskaznik_rodzica.addRegionEventListener(string_zdarzenia, function(){
                fun(argument)
            });
        }

        var mouseOut = function(liczba){
            console.log("ZMIENNA = " + liczba)
        }

        for (var i = 0; i < tablica_chr.length; i++) {
            h = (tablica_chr[i] * max_len_chr) / tab_max;
            x = szer_przerwy + delta_x
            y = y_line_start
            rodzic.beginRegion();
            context.save()
            context.fillStyle = "#5cb85c";
            drawChromosom(x, y, szer_chr, h)
            context.restore()
            rodzic.addRegionEventListener("mousedown", function () {
                var mousePos = events.getMousePos();
                var mouseX = mousePos.x;
                var mouseY = mousePos.y;
                //console.log("Mysz w : " + mouseX + "," + mouseY + " chromosom=" + napis);
                //odsylac do odpowiedniego linku ze scaffoldami ->  window.location.replace("#/chromosom/[id_scaff]/scaffoldy")
                DataBufor.setData("chr_length", chr_tab[i]);
                window.location.replace("#/organizm/" + $routeParams.id_org +"/chromosom/" + chr_tab_id[i] + "/scaffoldy")
            });
            //rodzic.addRegionEventListener("mouseout", function () {
            //    console.log("mysz usunieta z pola !")
            //});
            rodzic.closeRegion();
            delta_x += szer_chr + szer_przerwy
            context.save()
            context.font = h_napis.toString()+"px Helvetica"
            //context.font = "50px Helvetica"
            context.fillStyle = "black"
            context.textAlign = "center"
            context.textBaseline = "middle"
            x_text = x + 0.5 * szer_chr
            y_text = y + 0.5 * (canvas.height - y_line_start)
            context.fillText(napis.toString(), x_text, y_text)
            context.restore()
            napis += 1;
        }
    }

    function setDrawStage(tab){
        events.setDrawStage(function(){
            drawChromosomCanvas(tab, this)
        })
    }

    setDrawStage(chr_tab);

    window.onresize = function(){
        events.drawStage();
    }


    $scope.klik = function (){
        var ca = events.getCanvas();
        ca.height = ca.height/2;
        //ca.width = ca.width/2
        events.drawStage();
        console.log(window.innerWidth)
        console.log(window.innerHeight)
        //window.location.href("http://www.onet.pl")
    }


    $scope.guzik = function(){
        console.log("guzik")

        //window.location.href("chromosom/53/scaffoldy")
        //var path = "chromosom/"+"53"+"/scaffoldy"
        //$location.path(path);
    }
}