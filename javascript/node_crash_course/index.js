/*import Person from './person.js';
import path from 'path';

const person1 = new Person('Sebas',23);

person1.greeting()*/

import http from 'http';
import path, { dirname } from 'path';
import fs from 'fs';

const server = http.createServer((req,res) => {
    /*
    if(req.url=='/'){
        fs.readFile(path.join(path.resolve(''),'public','index.html'),
        (err,content) => {
            if (err) throw err;
            res.writeHead(200,{'Content-Type':'text/html'})
            res.end(content)
        });
    };

    if(req.url=='/about'){
        fs.readFile(path.join(path.resolve(''),'public','about.html'),
        (err,content) => {
            if (err) throw err;
            res.writeHead(200,{'Content-Type':'text/html'});
            res.end(content);
        });
    }

    if(req.url=='/api/users'){
        const users = [
            {name: 'Jair', age: 18},
            {name: 'Sebastián', age: 23}
        ];

        res.writeHead(200,{'Content-Type':'application/json'});
        res.end(JSON.stringify(users));
    }
    */

    //Build filepath
    let filePath = path.join(path.resolve(''),'public',req.url=='/' ? 'index.html':req.url);
    
    //Extention of the file
    let extName = path.extname(filePath);

    //Initial content-type
    let contentType = 'text/html';

    //Check extension
    switch(extName){
        case '.js':
            contentType = 'text/javascript';
            break;
        case '.css':
            contentType = 'text/css';
            break;
        case '.json':
            contentType = 'application/json';
            break;
        case '.png':
            contentType = 'image/png';
            break;
        case '.jpg':
            contentType = 'image/jpg';
            break;
    };

    //const dir = dirname();
    //console.log(dir);
    //Read file
    fs.readFile(filePath,(err,content) => {
        if (err) {
            if(err.code =='ENOENT'){
                fs.readFile(path.join(path.resolve(''),'public','404.html'),(err,content) => {
                    res.writeHead(200,{'Content-Type':'text/html'});
                    res.end(content,'utf-8');
                });
            }else{
                //SOme server error
                res.writeHead(500);
                res.end(`Server error: ${err.code}`);
            }
        }else{
            res.writeHead(200,{'Content-Type': contentType});
            res.end(content,'utf-8');
        }
    });
});

//const __dirname = dirname();
const PORT = process.env.PORT || 5000;

server.listen(PORT, () => console.log(`Server runnning on port: ${PORT}`));