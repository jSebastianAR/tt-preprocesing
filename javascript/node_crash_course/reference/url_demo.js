import url from 'url';

const myUrl = new URL('http://mywebsite.com:8000/hello.html?id=100&status=active');

//Serialized url, both are the same thing
console.log(myUrl.href)
console.log(myUrl.toString());

//Host or root domain
console.log(myUrl.host) //takes the port number
//Hostname
console.log(myUrl.hostname) //doesnt takes the port number
//Pathname
console.log(myUrl.pathname);
//Serialized query
console.log(myUrl.search);
//Params
console.log(myUrl.searchParams);
//Addparam
myUrl.searchParams.append('newParam','Bueyyyy');
let newUrl = myUrl.searchParams
console.log(newUrl);
//Loop through params
myUrl.searchParams.forEach((value,name) => console.log(`name: ${name} value: ${value}`))