import express from 'express';
import exphbs from 'express-handlebars'
import path from 'path'

//Importing routes
import IndexRoutes from './routes/index'
import BooksRoutes from './routes/books'

//Initializations
const app = express()
import './database'

//Settings for servers
const root_path = path.join(__dirname, 'views')
console.log(root_path)
app.set('port', process.env.PORT || 3000) //Se establece el puerto donde escuchara la aplicacion (un puerto dado por servicio en la nube o el puerto 3000)
app.set('views',path.join(__dirname, 'views')) //Se establece el directorio de las vistas a desplegar para el usuario
//Se establece que se usara handlebars, es decir como funcionara nuestro modulo de plantillas
app.engine('.hbs', exphbs({
    extname: '.hbs', //se establece la extencion de los archivos a entender}
    layoutsDir: path.join(app.get('views'),'layouts'), //Se establece la carpeta donde están los layouts
    partialsDir: path.join(app.get('views'),'partials'), //Se establece la carpeta donde están los partials
    helpers: require('./lib/helpers'), //Se importan librerías extra desde el archivo helpers.ts
    defaultLayout: 'main'
}))
app.set('view engine', '.hbs') //se establece la configuracion previa establecida en app.engine
//Middlewares
app.use(express.json()) //permiten interpretar jsons que lleguen al server
app.use(express.urlencoded({extended:false})) //permite interpretar datos enviados a través de formularios html

//Routes
app.use('/',IndexRoutes)
app.use('/books', BooksRoutes) //Se establece la ruta raíz '/' e indexROutes contendrá todo el resto de rutas que contiene ese path

//Static files
app.use(express.static(path.join(__dirname, 'public')))//se establece la carpeta publica de la aplicacion (habrá archivos .css,.html)

//Starting server
app.listen(app.get('port'), () => {
    console.log(`Server on port ${app.get('port')}`)
})