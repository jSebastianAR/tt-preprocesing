import path from 'path';
import { constants } from 'buffer';
const filename = import.meta.url;
const name = path.basename(filename);

console.log(filename);
//Full path of current directory
console.log(path.resolve(''));

//Only name of the current file 
console.log(path.basename(filename));

//Only dirname by filename
console.log(path.dirname(name));

//File extension
console.log(path.extname(filename));

//Creating path object
console.log(name)
console.log(path.parse(name));

//Join
/*concatenate strings */
console.log(path.join(path.resolve(''),'test','hello.html'))