/**
 * Created by saeid on 1/3/2017.
 */

var app = angular.module('signupapp',[]);

app.controller('signupcontroller', function ($scope, $http, $window) {
    $scope.signup_response={};
    $scope.status = true;
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