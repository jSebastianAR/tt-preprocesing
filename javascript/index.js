
const user = {
    name: 'Sebastian',
    lastname: 'Acosta',
    age: 23,
    sayName: function(){
        console.log(`My name is ${this.name}`);

        //Arrow function allows you to use 'this' word to use the object which calls the function    
        const fullName = (param1) => { 
            console.log(`My name is ${this.name} and my lastname is: ${this.lastname} and im ${this.age+param1} years old`);
        };

        fullName(1);
    }
}

user.sayName();


function multiply(x = 2,y = 2){ //Default parameter for both variables is 2
    let a = x;
    let b = y;
    console.log(a*b);
};

multiply(3,3);


let list1 = [1,'2',3,'4',5,'6'];

//for each
let hello = 'Hello';
list1.forEach((product) => {
    console.log(`producto: ${product}`);
});

//map
let list2 = list1.map(item => {
    return item + ' new';
});

console.log(list2);

//filter

let filterlist = list1.filter(item => {
    return item == '3';
});

console.log(filterlist)

const persona = {
    name: 'Sebastian',
    lastname: 'Acosta',
    age: 23,
    sayName: function(){
        return this.name;
    }
}

console.log(persona['sayName']())

//Classes

class ShoppingList{
    constructor(items,nr){
        this.items = items;
        this.nr    = nr; 
    };

    sayList(){
        console.log(`The shopping list is: ${this.items} and the number of items is: ${this.nr}`)
    };

};

const myList = new ShoppingList(['Papitas','Cerveza','Dulces','Limones'],4);

myList.sayList();

class Category{
    constructor(kind,from){
        this.kind = kind;
        this.from = from;
    };

    getKind(){
        console.log(this.kind);
    };

    getFrom(){
        console.log(this.from);
    };
};

class Product extends ShoppingList{
    constructor(items,nr,kind,from,amount,cost){
        super(items,nr);
        this.amount = amount;
        this.cost   = cost;
    };

};

const product = new Product(['Papitas'],1,'Junkfood','México',2,20)

console.log(product);
product.sayList();


const prom = new Promise((resolve,reject) => {
    //Here is async
    setTimeout(() => {
        resolve(200);
    },2000);
});

prom.then(data => {
    console.log(data)
});

const prom2 = new Promise((resolve,reject) => {
    //Here is async
    setTimeout(() => {
        reject(new Error('Something went wrong'));
    },2000);
});

prom2.then(data => {
    console.log(data)
})
.catch(err => console.log(err));

for (element in list1) {
    console.log(`Elemento ${element}`);
}