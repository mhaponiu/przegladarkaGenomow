/**
 * Created by mhaponiu on 25.05.17.
 */

function ScriblCanvasController($scope, $routeParams, $http) {
    $scope.id_chr = $routeParams.id_chr;
    $scope.id_org = $routeParams.id_org;
    $scope.test = "TEST"
    var canvas = document.getElementById('scribl')
    canvas.style.backgroundColor = "#f5f5f5";
    chart = new Scribl(canvas, 720);
    canvas.style.width = "900px"

    // <div id="scroll-wraper" style="width: 900px;">

    chart.laneSizes = 18;
    chart.laneBuffer = 2;
    chart.trackBuffer = 40;
    chart.glyph.text.color = 'white';



    track1 = chart.addTrack();
    gene1 = track1.addFeature( new BlockArrow('track1', 5, 750 , '-') );
    gene1.name = "dupa"
    gene1.onMouseover = "Start:900 Length:750";
    gene1.onClick = "http://www.google.com";
    gene2 = track1.addFeature( new BlockArrow('track1', 3500, 2500, '+') );
    gene3 = track1.addFeature( new BlockArrow('track1', 8100, 1000, '-') );
    gene4 = track1.addFeature( new BlockArrow('track1', 6200, 1500, '+') );
    chart.track1.name = 'track 1';

    track2 = chart.addTrack();
    gene5 = track2.addFeature( new BlockArrow('track2', 100, 1000, '-') );
    gene6 = track2.addFeature( new BlockArrow('track2', 3500, 1500, '-') );
    chart.track2.name = 'track 2';

    chart.scrollable = true;
    chart.scrollValues = [200000, 250000];
    chart.draw()
    document.getElementById('scroll-wraper').style.width = "900px"
    chart.draw()

    $scope.button = function () {
        // alert('zmniejszamy skale!')
        chart.scale.min = 500
        chart.scale.max = 1000
        chart.tick.major.size = 1000;
        chart.redraw()
        // chart.draw()
    }
    // $scope.loadScaffolds = function(id_org, id_chr){
    //     var request = {
    //         method: 'GET',
    //         url: 'api/organisms/'+$scope.id_org+'/chromosomes/'+$scope.chr_id+'/annotation_types/'+ $scope.id_type +'/annotations/'
    //     };
    //     return $http(request)
    //         .success(function (data) {
    //             $scope.scflds = data;
    //         });
    // }
}