import args from './args.js';
import evnt from './events_test.js';
//import * as args from './args.js';

const myList = ['this','is','my list','from index.js'];


/*
args.printElements(myList)
//printElements(myList)
args.printElements()
args.printList(myList)
*/
let obj = {'hola':'mundo'}
evnt.emitter.emit('string','hola mundo');
evnt.emitter.emit('integer',666);
evnt.emitter.emit('list',[1,2,3,'666',{'buey':'no'}]);
evnt.emitter.emit(obj,{'nomanches':'esebuey','soy':'elfedebergas'})