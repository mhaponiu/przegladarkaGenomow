/**
 * Created by mhaponiu on 10.06.15.
 */
/**
 * Created by mhaponiu on 01.05.15.
 */

angular.module('CucModule').controller('NewOrganizmModalCtrl', function($scope, $modal){
    $scope.open = function(){
        var modalIntance = $modal.open({
            templateUrl: 'NewOrganizmModalContent.html',
            controller: 'NewOrganizmModalInstance',
            backdrop: 'static',
            scope: $scope,
            size: "" //sm lg
        });
        modalIntance.opened.then(function(){
            console.log("OPENED");
        });
        modalIntance.result.then(function(){
            console.log("CLOSE");
        });
    }
})

//controller wewnatrz okienka modalnego; ma przekazany scope
angular.module('CucModule').controller('NewOrganizmModalInstance', function($scope, $modalInstance, Upload, $filter){
    //tablica plikow do wyslania -> wazna kolejnosc
    $scope.files = [] //to lista list jednoelementowych -> potem przefiltruje zeby byla zwykla pojedyncza lista

    // $scope.opisPlikow = [["organizm","gff"], ["chromosom", "gff"], ["scaffold", "gff"],
    //                      ["marker", "gff"], ["meaning","gff"], ["sequence" ,"gff"],
    //                      ["sequence", "fasta"]]
    $scope.opisPlikow = [['organizm info', 'gff / xls'],['sekwencja', 'fasta']]
    //$scope.opisPlikow = [["seq", 'fasta']]

    $scope.name = "" //nazwa nowego organizmu

    $scope.toggleVisible = false; //odpowiada za widocznosc paru rzeczy, ktore sa wzgledem siebie odwrotne

    $scope.progressbar = {}
    $scope.progressbar.visible = $scope.toggleVisible
    $scope.progressbar.value = 0;
    $scope.progressbar.type = ""
    $scope.progressbar.text = $scope.progressbar.value + ' %'
    $scope.progressbar.class = "progress-striped active"

    $scope.message = {} //widomosc wyswietlona po wyslaniu pliku -> i tak serwer ją nadpisze wartosci przykladowe na start wklepane
    $scope.message.visible = false;
    $scope.message.type = 'warning'
    $scope.message.text = "WIADOMOSC"
    $scope.message.buttonClass = 'btn-warning'

    $scope.buttonyVisible = !$scope.toggleVisible

    $scope.$watch('toggleVisible', function(){
        $scope.progressbar.visible = $scope.toggleVisible
        $scope.buttonyVisible = !$scope.toggleVisible
    })

    $scope.disabledUpload = "disabled";

    var checkDisableUpload = function(){
        //proste sprawdzenie czy wszystkie dane zostaly podane
        if($scope.files.length == $scope.opisPlikow.length /*&& $scope.name!=""*/){
            $scope.disabledUpload = ""
        }
        else{ $scope.disabledUpload = "disabled" }
    }

    $scope.$watchCollection('files', checkDisableUpload)
    $scope.$watch('name', checkDisableUpload)

    var uploadFiles = function (files) {
        if (files && files.length) {
            Upload.upload({
                url: 'ajax_newOrganism',
                //fields: {'name': $scope.name},
                file: files
            }).progress(function (evt) {
                var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
                console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
                $scope.progressbar.value = progressPercentage
                $scope.progressbar.text = $scope.progressbar.value + ' %'
                if(progressPercentage == 100){
                    $scope.progressbar.text = "CZEKAJ AZ SERWER PRZETWORZY PRZESLANE PLIKI"
                }
            }).success(function (data, status, headers, config) {
                //po przeslaniu kazdego pliku wali sc
                $scope.progressbar.text = $scope.progressbar.value.toString() + ' % ZAKOŃCZONO'
                $scope.progressbar.class = "progress-striped"
                if (data.success) {
                    $scope.progressbar.type = "success"
                    $scope.message.buttonClass = 'btn-success'
                    $scope.message.type = 'success'
                }
                else {
                    $scope.progressbar.type = "danger"
                    $scope.message.buttonClass = 'btn-danger'
                    $scope.message.type = 'danger'
                }
                $scope.message.text = data.message
                $scope.message.visible = $scope.toggleVisible

                console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
            });
        }
    };


    $scope.uploadStart = function(){
        console.log("upload start");
        $scope.files = $filter("listOfListsToOneList")($scope.files)
        console.log($scope.files)
        $scope.toggleVisible = !$scope.toggleVisible;
        uploadFiles($scope.files)
        //$modalInstance.dismiss();
    }
    $scope.dismissModal = function(){
        $modalInstance.dismiss()
    }
    $scope.cancel = function(){
        console.log("CANCEL")
        $modalInstance.close();
    }
    $scope.test = function(){
        console.log("TEST");
        $scope.files = $filter("listOfListsToOneList")($scope.files)
        console.log($scope.files)
        $scope.toggleVisible = !$scope.toggleVisible;
        uploadFiles($scope.files)

    }
})