/**
 * Created by mhaponiu on 25.05.17.
 */

function ScriblCanvasController($scope, $routeParams, $http, $q) {
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

    $scope.types = []
    $scope.loadTypes = function () {
        var request = {
            method: 'GET',
            url: 'api/organisms/'+  $routeParams.id_org + '/chromosomes/' + $routeParams.id_chr + '/annotation_types/',
        };
        return $http(request)
            .success(function (data) {
                $scope.types = data;
            });
    }

    // $scope.annotations={} //annotation[type_id]
    $scope.loadAnnotations = function (type_id, modified_object) {
        var request = {
            method: 'GET',
            url: 'api/organisms/'+  $routeParams.id_org + '/chromosomes/' + $routeParams.id_chr + '/annotation_types/'+
                type_id + '/annotations/'
        }
        return $http(request)
            .success(function (data) {
                modified_object['annotations']= data
            })
    }
    function* randomColor() {
        yield "CadetBlue"; yield "Olive";  yield "Sienna";
        yield "PaleVioletRed"; yield "Tan"; yield "MediumPurple";
        yield "LightSalmon"; yield "GoldenRod"; yield "YellowGreen";
        while (true){
            yield '#'+Math.floor(Math.random()*16777215).toString(16);
        }
    }
    function colourNameToHex(colour) {
        var colours = {"aliceblue":"#f0f8ff","antiquewhite":"#faebd7","aqua":"#00ffff","aquamarine":"#7fffd4","azure":"#f0ffff", "beige":"#f5f5dc","bisque":"#ffe4c4","black":"#000000","blanchedalmond":"#ffebcd","blue":"#0000ff","blueviolet":"#8a2be2","brown":"#a52a2a","burlywood":"#deb887",
        "cadetblue":"#5f9ea0","chartreuse":"#7fff00","chocolate":"#d2691e","coral":"#ff7f50","cornflowerblue":"#6495ed","cornsilk":"#fff8dc","crimson":"#dc143c","cyan":"#00ffff",
        "darkblue":"#00008b","darkcyan":"#008b8b","darkgoldenrod":"#b8860b","darkgray":"#a9a9a9","darkgreen":"#006400","darkkhaki":"#bdb76b","darkmagenta":"#8b008b","darkolivegreen":"#556b2f",
        "darkorange":"#ff8c00","darkorchid":"#9932cc","darkred":"#8b0000","darksalmon":"#e9967a","darkseagreen":"#8fbc8f","darkslateblue":"#483d8b","darkslategray":"#2f4f4f","darkturquoise":"#00ced1",
        "darkviolet":"#9400d3","deeppink":"#ff1493","deepskyblue":"#00bfff","dimgray":"#696969","dodgerblue":"#1e90ff", "firebrick":"#b22222","floralwhite":"#fffaf0","forestgreen":"#228b22","fuchsia":"#ff00ff",
        "gainsboro":"#dcdcdc","ghostwhite":"#f8f8ff","gold":"#ffd700","goldenrod":"#daa520","gray":"#808080","green":"#008000","greenyellow":"#adff2f", "honeydew":"#f0fff0","hotpink":"#ff69b4", "indianred ":"#cd5c5c","indigo":"#4b0082","ivory":"#fffff0","khaki":"#f0e68c",
        "lavender":"#e6e6fa","lavenderblush":"#fff0f5","lawngreen":"#7cfc00","lemonchiffon":"#fffacd","lightblue":"#add8e6","lightcoral":"#f08080","lightcyan":"#e0ffff","lightgoldenrodyellow":"#fafad2",
        "lightgrey":"#d3d3d3","lightgreen":"#90ee90","lightpink":"#ffb6c1","lightsalmon":"#ffa07a","lightseagreen":"#20b2aa","lightskyblue":"#87cefa","lightslategray":"#778899","lightsteelblue":"#b0c4de",
        "lightyellow":"#ffffe0","lime":"#00ff00","limegreen":"#32cd32","linen":"#faf0e6", "magenta":"#ff00ff","maroon":"#800000","mediumaquamarine":"#66cdaa","mediumblue":"#0000cd","mediumorchid":"#ba55d3","mediumpurple":"#9370d8","mediumseagreen":"#3cb371","mediumslateblue":"#7b68ee",
        "mediumspringgreen":"#00fa9a","mediumturquoise":"#48d1cc","mediumvioletred":"#c71585","midnightblue":"#191970","mintcream":"#f5fffa","mistyrose":"#ffe4e1","moccasin":"#ffe4b5", "navajowhite":"#ffdead","navy":"#000080", "oldlace":"#fdf5e6","olive":"#808000","olivedrab":"#6b8e23","orange":"#ffa500","orangered":"#ff4500","orchid":"#da70d6",
        "palegoldenrod":"#eee8aa","palegreen":"#98fb98","paleturquoise":"#afeeee","palevioletred":"#d87093","papayawhip":"#ffefd5","peachpuff":"#ffdab9","peru":"#cd853f","pink":"#ffc0cb","plum":"#dda0dd","powderblue":"#b0e0e6","purple":"#800080",
        "rebeccapurple":"#663399","red":"#ff0000","rosybrown":"#bc8f8f","royalblue":"#4169e1", "saddlebrown":"#8b4513","salmon":"#fa8072","sandybrown":"#f4a460","seagreen":"#2e8b57","seashell":"#fff5ee","sienna":"#a0522d","silver":"#c0c0c0","skyblue":"#87ceeb","slateblue":"#6a5acd","slategray":"#708090","snow":"#fffafa","springgreen":"#00ff7f","steelblue":"#4682b4",
        "tan":"#d2b48c","teal":"#008080","thistle":"#d8bfd8","tomato":"#ff6347","turquoise":"#40e0d0", "violet":"#ee82ee", "wheat":"#f5deb3","white":"#ffffff","whitesmoke":"#f5f5f5", "yellow":"#ffff00","yellowgreen":"#9acd32"};

        if (typeof colours[colour.toLowerCase()] != 'undefined')
            return colours[colour.toLowerCase()];

        return false;
    }
    function hexToRgbA(hex){
        var c;
        if(/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)){
            c= hex.substring(1).split('');
            if(c.length== 3){
                c= [c[0], c[0], c[1], c[1], c[2], c[2]];
            }
            c= '0x'+c.join('');
            return 'rgba('+[(c>>16)&255, (c>>8)&255, c&255].join(',')+',1)';
        }
        throw new Error('Bad Hex');
    }
    function colorToRgbA(color_string) {
        try{
            return hexToRgbA(color_string)
        }
        catch(e){
            var hex = colourNameToHex(color_string)
            return hexToRgbA(hex)
        }

    }
    semafor = true; // do jednorazowego pobrania danych -> nie wiem czemu 2 razy sie wywoluje
    semafor2 = 2;
    $scope.loadTypes().then(function () {
        colorgenerator = randomColor()
        angular.forEach($scope.types, function (type) {
            type['color'] = {background: colorgenerator.next().value}
        })
    }).then(function () {
        // downloading annotation for every annotation type
        if (semafor){
            var promises = [];
            angular.forEach($scope.types, function (type) {
                promises.push($scope.loadAnnotations(type.id, type))
            });
            semafor = false;
            return $q.all(promises)
        }
    }).then(function () {
        semafor2 -=1;
        // if (!semafor2) {
        if ('annotations' in $scope.types[0]){
            console.log($scope.types)

            //todo czemu to nie dziala skoro to nizej dziala?!
            // angular.forEach($scope.types, function (type) {
            //     var track = chart.addTrack()
            //     angular.forEach(type['annotations'], function (annotate) {
            //         console.log(annotate)
            //         var gene1 = track.addFeature( new BlockArrow('track1', 5, 1450 , '-') );
            //         var rgb = colorToRgbA(type.color.background)
            //         gene1.setColorGradient(rgb)
            //         gene1.name= "gen testowy"
            //         gene1.onMouseover = "fdasfas"
            //         gene1.onClick = "http://www.google.com"
            //     })
            // })


            console.log($scope.types[0].annotations.length)
            for(var i=0; i<$scope.types.length; i++) {
                var type = $scope.types[i]
                console.log("type" + i)
                var track = chart.addTrack()
                for (var j = 0; j < type.annotations.length; j++) {
                    console.log("type" + i + " annotation: " + j)
                    var annotation = type.annotations[j]
                    var start = annotation.start_chr
                    var length = annotation.length
                    var end = start + annotation.length
                    var gene = track.addFeature(new BlockArrow('track', start, length, '+'))
                    var rgb = colorToRgbA(type.color.background)
                    gene.setColorGradient(rgb)
                    gene.name = annotation.name
                    gene.onMouseover = "Start: " + start + " end: " + end
                    gene.onClick = "http://www.google.com"
                }
            }


            // var track1 = chart.addTrack();
            // var gene1 = track1.addFeature(new BlockArrow('track1', 5, 1450, '-'));
            // var rgb = colorToRgbA($scope.types[0].color.background)
            // gene1.setColorGradient(rgb)
            // gene1.name = "gen_testowy"
            // gene1.onMouseover = "Start:900 Length:750";
            // gene1.onClick = "http://www.google.com";
            // var gene2 = track1.addFeature(new BlockArrow('track1', 3500, 2500, '+'));
            // gene2.setColorGradient(rgb)
            // gene3 = track1.addFeature(new BlockArrow('track1', 8100, 1000, '-'));
            // gene3.setColorGradient(rgb)
            // gene4 = track1.addFeature(new BlockArrow('track1', 6200, 1500, '+'));
            // gene4.setColorGradient(rgb)
            // chart.track1.name = 'track 1';



            // track1 = chart.addTrack();
            // gene1 = track1.addFeature(new BlockArrow('track1', 5, 1450, '-'));
            // var rgb = colorToRgbA($scope.types[0].color.background)
            // gene1.setColorGradient(rgb)
            // gene1.name = "gen_testowy"
            // gene1.onMouseover = "Start:900 Length:750";
            // gene1.onClick = "http://www.google.com";
            // gene2 = track1.addFeature(new BlockArrow('track1', 3500, 2500, '+'));
            // gene2.setColorGradient(rgb)
            // gene3 = track1.addFeature(new BlockArrow('track1', 8100, 1000, '-'));
            // gene3.setColorGradient(rgb)
            // gene4 = track1.addFeature(new BlockArrow('track1', 6200, 1500, '+'));
            // gene4.setColorGradient(rgb)
            // chart.track1.name = 'track 1';

            // track2 = chart.addTrack();
            // var rgb2 = colorToRgbA($scope.types[1].color.background)
            // gene5 = track2.addFeature(new BlockArrow('track2', 100, 1000, '-'));
            // gene5.setColorGradient(rgb2)
            // gene6 = track2.addFeature(new BlockArrow('track2', 3500, 1500, '-'));
            // gene6.setColorGradient(rgb2)
            // chart.track2.name = 'track 2';
        }
    }).then(function () {
        if ('annotations' in $scope.types[0]) {
            console.log('draw')
            chart.scrollable = true;
            // chart.scrollValues = [200000, 250000];
            chart.draw()
            // document.getElementById('scroll-wraper').style.width = "900px"
            // chart.redraw()
        }
    })
}