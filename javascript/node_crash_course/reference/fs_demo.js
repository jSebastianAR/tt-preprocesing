import fs from 'fs';
import path from 'path';

//Create folder
/*
fs.mkdir(path.join(path.resolve(''),'test'), {}, err => {
    if(err) throw err;
    console.log('Folder created...');
});
*/
//Create file
/*
fs.writeFile(path.join(path.resolve(''),'test','hello.txt'), 'Hello world!\n', err => {
    if(err) throw err;
    console.log('File written to...');

    //Append file

    fs.appendFile(path.join(path.resolve(''),'test','hello.txt'), 'I love nodejs!', err => {
        if(err) throw err;
        console.log('File written to...');
    
        //Append file
    });
});
*/

/*
//Read file
fs.readFile(path.join(path.resolve(''),'test','hello.txt'), 'utf8', (err,data) => {
    if(err) throw err;
    console.log(data);
});
*/
//Rename file
fs.rename(
    path.join(path.resolve(''),'test','hello.txt'),
    path.join(path.resolve(''),'test','helloworld.txt'),
    (err) => {
        if(err) throw err;
        console.log('File renamed');
});