import ApplicationController from '../application_controller'

export default class extends ApplicationController {

  get_targets () {
    return ['query', 'activity', 'count', 'list']
  }
  beforePerform (element, reflex) {
    this.activityTarget.hidden = false
    this.countTarget.hidden = true
  }

  perform (event) {
    console.log("perfom")
    event.preventDefault()
    this.stimulate('BookSearchReflex#perform', this.queryTarget.value)
  }
}
