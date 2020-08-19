//
//"type": "module",
/*
const io = require('socket.io')(3000)

//io.on('connection', socket => {
    socket.emit('chat-message','Hello world')
})
*/
import io from 'socket.io'; //Import socket.io

const server = io(3000); //init server connection on port 3000

server.on('connection', socket => {
    socket.emit('chat-message','Hello world')
})