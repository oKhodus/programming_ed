/*
task1 - global and functional scopes
*/

let $new_var = 10
function GLFN_scopes() {
    let arr = []
    for (let i = 0; i < $new_var; i++) {
        arr.push(i)
    }
    console.log(arr)
    
}
GLFN_scopes()

/*
task2 - block scopes
*/

function block_scopes(n) {
    if (n > 0) {
        let i = 1
        console.log(i)
    }
    else {
        let i = 0
        console.log(i)
    }
    
}

block_scopes(3)

/*
task3 - Lexin scopes
*/

function l_scopes(n) {
    if (n > 0){
        return returned_lscopes()
    }
}

function returned_lscopes() {
    console.log("Oh, n is more than 0")
}

l_scopes(1)

/*
task4 - let and var--loop scopes
*/

function letvar_loop() {
    for (let i = 2; i < 10; i++) {
        var $variable = i
        let $let = i ** 2
        console.log($variable, $let)   
    }
}
letvar_loop()



"use strict";

let message = "Hello";

console.log(message, "World");


let admin;
let $name;

$name = 'John';
admin = $name;
alert(admin);

alert("I'm JavaScript");

let $planetName = 'Earth';
let $usersName;

let $myname = "Oleksii";
alert(`hello, ${$myname}`);

let result = prompt("What's your name?");
alert(`hello, ${result}`)