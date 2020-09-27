import mongoose, {Schema, model} from 'mongoose'

export interface IBook extends mongoose.Document {
    title: String,
    author: String,
    isbn: String,
}

//Genera el esquema(todos los campos) del libro a guardar en la db
const BookSchema = new Schema({
    title: String,
    author: String,
    isbn: String
})


//Genera el modelo del tipo 'book'libro a guardar en la db
export default model<IBook>('Book',BookSchema)


