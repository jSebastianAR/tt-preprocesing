const io = require('socket.io').listen(3000);

function io_functions(socket){

    console.log('Server-Socket listen in 3000...')
    
    socket.on('greeting', (msg) => {
        console.log(`hi this is a message from the client: ${msg}`)
        socket.emit('disconnect')
    })

    socket.on('goodbye', msg => {
        console.log(`client says: ${msg}`)
    })

    socket.on('end', () => {
        console.log('Disconnecting')
        socket.disconnect(0) //finish the conection with the client
    })
}

io.on('connection',io_functions)

