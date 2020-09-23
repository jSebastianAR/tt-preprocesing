var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
console.log('Hello world');
//types
var myString = 'hello world';
myString = 22 + '';
myString.split(' ');
var myNum = 666;
var myBool = false || true;
var myVar = 'hello';
myVar = false;
//Trabajando con strings
//Arrays 
var myArray = ['i1', 'i2', ''];
var myArray2 = [1, 2, 3];
var myArray3 = [true, false, true];
var myArray4 = [1, '', {}, [], false];
//tuples
//Custom tuples for different kind of variables
var strnumTuple;
strnumTuple = ['', 2];
//void, undefined, null
var varVoid = undefined;
var mynull = null;
var myundefined = undefined;
var employeeName = "John";
//Functions
function getsum(x, y) {
    return x + y;
}
var mysum = function (x, y) {
    if (typeof (x) == 'string') {
        x = parseInt(x);
    }
    if (typeof (y) == 'string') {
        y = parseInt(y);
    }
    return x + y;
};
//function with an optional parameter spotted by the '?' symbol
function getname(firstname, lastname) {
    if (lastname == undefined) {
        return firstname;
    }
    return firstname + " " + lastname;
}
function myvoidfunction() {
    return;
}
function showtodo(todo) {
    console.log(todo.title + " - " + todo.text);
}
showtodo({ title: 'Eat dinner', text: 'lorem' });
var myTodo = { title: 'Buey', text: 'Nooo' };
showtodo(myTodo);
//Classes
var User = /** @class */ (function () {
    function User(name, email, age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }
    User.prototype.register = function () {
        console.log("user " + this.name + " has been registered!");
    };
    User.prototype.showMeAge = function () {
        return this.age;
    };
    User.prototype.ageInYears = function () {
        return this.age + ' years';
    };
    User.prototype.payInvoice = function () {
        console.log(this.name + " has pay the invoice");
    };
    return User;
}());
var john = new User('John', 'elbuey@mrbaigot.com', 33);
john.register();
var Member = /** @class */ (function (_super) {
    __extends(Member, _super);
    //Inheritance of attributes
    function Member(id, name, email, age) {
        var _this = _super.call(this, name, email, age) || this;
        _this.id = id;
        return _this;
    }
    //Inheritance of methods    
    Member.prototype.payInvoice = function () {
        _super.prototype.payInvoice.call(this);
    };
    return Member;
}(User));
var timmy = new Member(1212, 'El pequeño timmy', 'Timmy@baigot.com', 14);
timmy.payInvoice();
document.write(john.ageInYears());
