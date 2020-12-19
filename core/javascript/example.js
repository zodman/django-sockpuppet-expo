import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import CableReady from 'cable_ready'
import debounced from 'debounced'
import TurboLinks from 'turbolinks'
import Rails from "@rails/ujs"
import ApplicationController from './controllers/application_controller'
import BookSearchController from './controllers/book_search_controller'
import ExampleController from './controllers/example_controller'
import ChatController from './controllers/chat_controller'
import CalendarController from './controllers/calendar_controller'

debounced.initialize()
Rails.start()
TurboLinks.start()

const application = Application.start()
const ssl = location.protocol !== 'https:' ? '' : 's';
const consumer = new WebsocketConsumer(`ws${ssl}://${location.hostname}:${location.port}/ws/sockpuppet-sync`)

consumer.subscriptions.create('ChatChannel', {
  received (data) {
    if (data.cableReady) CableReady.perform(data.operations)
  }
})

application.register("example", ExampleController)
application.register("book-search", BookSearchController)
application.register("chat", ChatController)
application.register("calendar", CalendarController)
application.register("application", ApplicationController)

StimulusReflex.initialize(application, { consumer, debug: true })
