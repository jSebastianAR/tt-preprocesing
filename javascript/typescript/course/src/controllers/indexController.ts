import {Request, Response} from 'express'

class IndexController{
    
    public index(req: Request, res: Response){
        //"layout: false" permite evitar que se busque el layout main.hbs 
        //res.render('index', {title:'Welcome to books app',layout:false}); //Retornara el archivo index.hbs, no es necesario agregar rutas ni extensiones debido a que eso se configuro en el server con handlebars
        res.render('index', {title:'Welcome to books app'}); //Retornara el archivo index.hbs, no es necesario agregar rutas ni extensiones debido a que eso se configuro en el server con handlebars
    }    
}

export const indexController = new IndexController();
