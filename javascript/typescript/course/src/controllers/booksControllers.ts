import {Request, Response} from 'express'
import Book, {IBook} from '../models/book'

class BooksController{

    public async index(req: Request, res: Response): Promise<void>{
        const books:IBook[] = await Book.find().lean() //Hace el query a la bd y .lean() convierte el objeto en json
        res.render('books/index', {title:'Books', books})//manda el titulo Books y envía la variable "books"
    }

    public renderFormBook(req: Request, res: Response){
        res.render('books/add', {
            title: 'Add a book'
        })
    }

    public async saveBook(req: Request, res: Response){
        const {title, author, isbn} = req.body //obtiene los valores del form
        const book:IBook = new Book({title, author, isbn}) //Se crea un nuevo libro del tipo IBook
        await book.save()//hace el query a la bd para guardar

        console.log(req.body)
        res.redirect('/books')//redirecciona a la página
    }

}

export const booksController = new BooksController()