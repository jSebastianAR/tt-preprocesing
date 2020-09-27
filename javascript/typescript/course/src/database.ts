import mongoose from 'mongoose'
import {mongodb} from './keys'

//Conecta a la bd de mongo
mongoose.connect(mongodb.URI, {
    useNewUrlParser: true
})

//Una vez conectada
.then(db => console.log('db is connected'))
//Si hubo error de conexión
.catch(err => {console.log(err)})