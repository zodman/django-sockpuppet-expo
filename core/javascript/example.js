import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'

import debounced from 'debounced'
import BookSearchController from './controllers/book_search_controller'
import ExampleController from './controllers/example_controller'

debounced.initialize()
//import TurboLinks from 'turbolinks'

//TurboLinks.start()

const application = Application.start()
const ssl = location.protocol !== 'https:' ? '' : 's';
const consumer = new WebsocketConsumer(`ws${ssl}://${location.hostname}:${location.port}/ws/sockpuppet-sync`)

application.register("example", ExampleController)
application.register("book-search", BookSearchController)
StimulusReflex.initialize(application, { consumer, debug: true })
