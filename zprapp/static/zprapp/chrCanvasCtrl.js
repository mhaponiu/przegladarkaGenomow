/**
 * Created by mhaponiu on 23.03.15.
 */

function chrCanvasCtrl($scope) {
    $scope.testowy = "TEKST TESTOWY chrCanvasCtrl";
    var canvas = document.getElementById('canvasChromosom');
    canvas.width = 800;
    canvas.height = 80;
    //with(canvas.style){
    //    backgroundColor="#f1f1f1";
    //    width="100%";
    //    height="auto"
    //}
    canvas.style.backgroundColor="#f1f1f1"
    var context = canvas.getContext('2d');
    context.fillStyle = "rgba(0,100,255,0.2)";
    context.fillRect(0, 20, 800, 40);
    context.fillRect(20, 20, 40, 80);
}