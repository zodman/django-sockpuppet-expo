import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'

import debounced from 'debounced'
import BookSearchController from './controllers/book_search_controller'

debounced.initialize()
//import TurboLinks from 'turbolinks'

//TurboLinks.start()

const application = Application.start()
const consumer = new WebsocketConsumer('ws://localhost:8000/ws/sockpuppet-sync')

//application.register("example", ExampleController)
application.register("book-search", BookSearchController)
StimulusReflex.initialize(application, { consumer, debug: true })
