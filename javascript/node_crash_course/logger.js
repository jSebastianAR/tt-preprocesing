import EventEmitter from 'events';
//import {v4 as uuidv4, validate as uuidVal} from 'uuid';
import * as uuid from 'uuid';

console.log(uuid.v4());

class Logger extends EventEmitter{
    log(msg){
        //Call event
        this.emit('message',{id: uuid.v4(),msg});
    };
};

export default Logger;

/*
THIS CODE MUST BE IN INDEX.JS

import Logger from './logger.js';

const newLogger = new Logger();

newLogger.on('message', (data) => console.log('Called listener',data));
newLogger.log('Hello world! 1');
newLogger.log('Hello world! 2');
newLogger.log('Hello world! 3');
*/ 