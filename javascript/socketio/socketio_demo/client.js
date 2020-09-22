const io = require('socket.io-client');

class ClientIO{
    
    constructor(path){
        this.path = path
        this.socket = null
    }

    emitters(params){
        this.socket.emit(params[0],params[1]) //Sends the data
        this.socket.emit('end'); //ends the conection with the server
    }

    connection(path){
        this.socket = io.connect(this.path) //returns a socket with the conection with the server
    }
  
    sendmsg(params){
        this.emitters(params)
    }
}

const client = new ClientIO('http://localhost:3000')
client.connection()

client.socket.on('connect', () => {
    console.log(`Sendind msg for conn: ${client.socket.connected}`)
    client.sendmsg(['goodbye','goodbye from a socketio client!'])
})

client.socket.on('disconnect', () => {
    console.log(`finishing conn: ${client.socket.connected}`)
    client.socket.disconnect()
})