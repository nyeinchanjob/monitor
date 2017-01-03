var MyApp = angular.module('MyApp', ['ngMaterial', 'ngMessages']);
MyApp.controller('AppCtrl', ['$scope', '$mdDialog', '$mdSidenav', function($scope, $mdDialog, $mdSidenav) {
    $scope.show_brand_detail = false;
    $scope.showSide = false;
    $scope.showSideContent = function() {
        $scope.showSide = !$scope.showSide;
        console.log($scope.showSide);
    };
    $scope.toggleLeft = buildToggler('left');
    function buildToggler(navID) {
        return function() {
            $mdSidenav(navID).toggle();
        };
    }
    $scope.isOpenLeft = function() {
        return true;
    };
    $scope.brand_detail_show = false;
    $scope.show_brand_detail = function() {
        $scope.brand_detail_show = true;
    };
    $scope.hide_brand_detail = function() {
        $scope.brand_detail_show = false;
    };
}]);
