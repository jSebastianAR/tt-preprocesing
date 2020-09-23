console.log('Hello world')

//types
var myString: string = 'hello world'
myString = 22 + ''
myString.split(' ')


var myNum: number = 666

var myBool: boolean = false || true

var myVar: any = 'hello'
myVar = false

//Trabajando con strings

//Arrays 
var myArray: string[] = ['i1','i2','']
var myArray2: number[] = [1,2,3]
var myArray3: boolean[] = [true,false,true]
var myArray4: any[] = [1,'',{},[],false]

//tuples

//Custom tuples for different kind of variables
var strnumTuple: [string, number]
strnumTuple = ['',2]


//void, undefined, null
let varVoid: void = undefined
var mynull: null = null
var myundefined: undefined = undefined
let employeeName:string = "John";

//Functions

function getsum(x: number,y: number): number{
    return x+y
}

let mysum = (
    x: number | string, 
    y: number | string): number => {
    
    if(typeof(x)=='string'){
        x = parseInt(x)
    }

    if(typeof(y)=='string'){
        y = parseInt(y)
    }

    return x + y
}


//function with an optional parameter spotted by the '?' symbol
function getname(firstname: string, lastname?: string): string{
    
    if(lastname==undefined){
        return firstname
    }
    
    return `${firstname} ${lastname}`
}

function myvoidfunction(): void{
    return 
}

// Interfaces

interface Itodo {
    title: string; 
    text: string;
}

function showtodo(todo: Itodo){
    console.log(`${todo.title} - ${todo.text}`)
}

showtodo({title: 'Eat dinner', text: 'lorem'})

let myTodo:Itodo = {title: 'Buey', text: 'Nooo'}

showtodo(myTodo)

//Classes

class User{
    private name: string;
    protected email: string;
    public age: number;

    constructor(name: string, email: string, age: number){
        this.name = name
        this.email = email
        this.age = age
    }

    register(){
        console.log(`user ${this.name} has been registered!`)
    }

    showMeAge(){
        return this.age
    }

    public ageInYears(){
        return this.age + ' years'
    }

    protected payInvoice(){
        console.log(`${this.name} has pay the invoice`)
    }
}

var john = new User('John', 'elbuey@mrbaigot.com',33)
john.register()

class Member extends User{
    id: number

    //Inheritance of attributes
    constructor(id: number, name: string, email: string, age: number){
        super(name,email,age)
        this.id = id
    }

    //Inheritance of methods    
    payInvoice(){
        super.payInvoice()
    }
}

let timmy = new Member(1212,'El pequeño timmy','Timmy@baigot.com',14)
timmy.payInvoice()

document.write(john.ageInYears())