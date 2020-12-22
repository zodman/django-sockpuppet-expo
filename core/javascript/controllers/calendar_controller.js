import ApplicationController from './application_controller'

export default class extends ApplicationController {
  static get targets () {
    return ['input']
  }
  select (event) {
    event.preventDefault()
    this.buttons.forEach(el => el.classList.remove('active'))
    event.target.classList.add('active')
    this.inputTarget.value = event.target.innerText
  }

  get buttons () {
    return this.element.querySelectorAll('.btn')
  }

  addClasses(element) {
    let toId = element.dataset.toId
    let toElement
    if (toId) {
      toElement = document.getElementById(toId)
    } else {
      toElement = element
    }
    let classes = element.dataset.addClasses.split(' ')
    toElement.classList.add(...classes)
  }

  afterNewCalendarEvent(element) {
    this.addClasses(element)
  }

}
