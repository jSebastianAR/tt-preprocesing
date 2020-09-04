import EventEmitter from 'events';
//import args from './args';

class Emitter extends EventEmitter{

    string_received(string){
        if(typeof(string)=='string'){
            console.log(`I have received a string`)
            console.log(string+'\n')
        }
    }

    integer_received(integer){
        if(typeof(integer)=='number'){
            console.log(`I have received an integer: ${integer}`)
        }
    }

    list_received(list){
        if(Array.isArray(list)){
            console.log(`I have received a list`)
            console.log(list)
        }
    }

    obj_received(object){
        if(typeof(object)=='object'){
            console.log(`I have received an object`)
            console.log(object)
        }
    }

}

const emitter = new Emitter()

emitter.on('string',emitter.string_received);
emitter.on('integer',emitter.integer_received);
emitter.on('list',emitter.list_received);
emitter.on({'hola':'mundo'},emitter.obj_received);

const exports = {
    'emitter':emitter
}

export default exports;