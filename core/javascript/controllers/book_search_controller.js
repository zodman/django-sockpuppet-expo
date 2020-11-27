import ApplicationController from './application_controller'

export default class extends ApplicationController {

//  static targets = 
    static get targets () {
     return ['query', 'activity', 'count', 'list']
    }

  beforePerform (element, reflex) {
      console.log("beforePerform")
    this.activityTarget.hidden = false
    this.countTarget.hidden = true
  }

  perform (event) {
    console.log("perfom")
    event.preventDefault()
    this.stimulate('BookSearchReflex#perform', this.queryTarget.value)
  }
}
