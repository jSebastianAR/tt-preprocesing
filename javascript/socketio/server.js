//
//"type": "module",
/*
const io = require('socket.io')(3000)

//io.on('connection', socket => {
    socket.emit('chat-message','Hello world')
})
*/
/*
import express from 'express'
const app = express() 

import server from 'http'
const server_http = server.Server(app)

import io from 'socket.io'; //Import socket.io
const server_io = io(server_http); //init server_io connection on port 3000

app.set('views','./views')
app.set('view engine','ejs')
app.use(express.static('public'))
app.use(express.urlencoded({extended:true}))

const rooms = {}

app.get('/',(req,res) => {
    res.render('index',{ rooms:rooms })
})

app.post('/room', (req,res) => {
    if(rooms[req.body.room] !=null ){
        return res.redirect('/')
    }
    rooms[req.body.room] = {users: {}}
    console.log(req.body.room)
    res.redirect(req.body.room)
    //send message that new room was created
    server_io.emit('room-created',req.body.room)
})

app.get('/:room',(req,res) => {
    if(rooms[req.params.room] == null){
        return res.redirect('/')
    }
    res.render('room', { roomName: req.params.room })
})

server_http.listen(3000)

//const users = {}

server_io.on('connection', socket => {
    
    //console.log('New User')
    //socket.emit('chat-message','Hello world')
    socket.on('new-user', (room, name) => {
        socket.join(room)
        rooms[room].users[socket.id] = name
        socket.to(room).broadcast.emit('user-connected',name)
    })
    
    socket.on('send-chat-message', (room, message) => {
        socket.to(room).broadcast.emit('chat-message',{message:message,name: rooms[room].users[socket.id]})
    })

    socket.on('disconnect', () => {
        getUserRooms(socket).forEach(room => {
            socket.to(room).broadcast.emit('user-disconnected',rooms[room].users[socket.id])
            delete rooms[room].users[socket.id]    
        })
    })
    
})

//Return all rooms names where the user is connected
function getUserRooms(socket){
    return Object.entries(rooms).reduce((names,[name, room]) => {
        console.log(rooms.users)
        if (rooms.users[socket.id] != null) names.push(name)
        return names
    }, [])
}
"type": "module",
*/
//################################################

const express = require('express')
const app = express()
const server = require('http').Server(app)
const io = require('socket.io')(server)

app.set('views', './views')
app.set('view engine', 'ejs')
app.use(express.static('public'))
app.use(express.urlencoded({ extended: true }))

const rooms = { }

app.get('/', (req, res) => {
  res.render('index', { rooms: rooms })
})

app.post('/room', (req, res) => {
  if (rooms[req.body.room] != null) {
    return res.redirect('/')
  }
  rooms[req.body.room] = { users: {} }
  res.redirect(req.body.room)
  // Send message that new room was created
  io.emit('room-created', req.body.room)
})

app.get('/:room', (req, res) => {
  if (rooms[req.params.room] == null) {
    return res.redirect('/')
  }
  res.render('room', { roomName: req.params.room })
})

server.listen(3000)

io.on('connection', socket => {
  socket.on('new-user', (room, name) => {
    socket.join(room)
    rooms[room].users[socket.id] = name
    socket.to(room).broadcast.emit('user-connected', name)
  })
  socket.on('send-chat-message', (room, message) => {
    socket.to(room).broadcast.emit('chat-message', { message: message, name: rooms[room].users[socket.id] })
  })
  socket.on('disconnect', () => {
    getUserRooms(socket).forEach(room => {
      socket.to(room).broadcast.emit('user-disconnected', rooms[room].users[socket.id])
      delete rooms[room].users[socket.id]
    })
  })
})

function getUserRooms(socket) {
  return Object.entries(rooms).reduce((names, [name, room]) => {
    if (room.users[socket.id] != null) names.push(name)
    return names
  }, [])
}
