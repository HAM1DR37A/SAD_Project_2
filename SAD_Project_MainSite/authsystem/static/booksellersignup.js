/**
 * Created by saeid on 2/1/2017.
 */

var app = angular.module('booksellersignupapp',[]);

app.controller('booksellersignupcontroller', function ($scope, $http, $window) {
    $scope.signup_response={};
    $scope.status = true;
    $scope.days = ['۱', '۲'];
    $scope.day = $scope.days[0];
    $scope.months = ['فروردین', 'اردیبهشت'];
    $scope.month = $scope.months[0];
    $scope.years = ['۱۳۷۲', '۱۳۷۳'];
    $scope.year = $scope.years[0];
    $scope.send = function () {
        $scope.user = new Object();
        $scope.user.username = $scope.username;
        $scope.user.email = $scope.email;
        $scope.user.password = $scope.password;
        $scope.user.r_password = $scope.r_password;
        $scope.user.first_name = $scope.first_name;
        $scope.user.last_name = $scope.last_name;
        $scope.user.tel_no = $scope.tel_no;
        $scope.user.address = $scope.address;
        $scope.user.day = $scope.day;
        $scope.user.month = $scope.month;
        $scope.user.year = $scope.year;

        if($scope.r_password != $scope.password)
        {
            $scope.status = false;
        }

        console.log($scope.user);

        json_command = JSON.stringify($scope.user);
            $.post( "./", { command : json_command }, function( data ) {

            });

    }
});