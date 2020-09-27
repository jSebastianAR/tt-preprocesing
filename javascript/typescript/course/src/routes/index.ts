import {Router} from 'express'

const router: Router = Router()

import {indexController} from '../controllers/indexController'
/*
router.get('/', indexController.index)

router.get('/add', (req, res) => {
     res.send('Form')
})

router.get('/about', (req, res) => res.render('about'))
*/

router.get('/',indexController.index)

export default router;