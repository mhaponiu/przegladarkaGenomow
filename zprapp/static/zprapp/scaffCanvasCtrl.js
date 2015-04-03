/**
 * Created by mhaponiu on 02.04.15.
 */

function scaffCanvasCtrl($scope){
    $scope.promiseLoadScaffolds.then(console.log("then po promiseLoadScaffolds"))
    var events = new Events("canvasScaffold");
    var canvas = events.getCanvas();
    var context = events.getContext();
    with(canvas.style){
        backgroundColor="#f5f5f5";
        //width="100%";
        //height="auto"
    }
}