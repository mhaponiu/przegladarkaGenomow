/**
 * Created by mhaponiu on 02.04.15.
 */

function scaffCanvasCtrl($scope){
    $scope.promiseLoadScaffolds.then(console.log("then po promiseLoadScaffolds"))
    var events = new Events("canvasScaffold");
    var canvas = events.getCanvas();
    var context = events.getContext();
    canvas.style.backgroundColor="#f5f5f5";
    document.getElementById("span_od").style.backgroundColor = "#c7c7c7";
    document.getElementById("span_do").style.backgroundColor = "#c7c7c7";;
}