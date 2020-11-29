import Rails from '@rails/ujs'
import { debounce } from 'lodash-es'
import ApplicationController from './application_controller'

let lastMessageId
const reload = controller => {
  controller.stimulate('ChatReflex#reload')
}
const debouncedReload = debounce(reload, 100)

export default class extends ApplicationController {
  static get targets () {
     return ['list', 'input']
  }

  connect () {
    super.connect()
    this.scroll(100)
    this.reload(this)
  }

  post (event) {
    console.log("post");
    Rails.stopEverything(event)
    lastMessageId = Math.random()
    this.stimulate(
      'ChatReflex#post',
      this.element.dataset.color,
      this.inputTarget.value,
      lastMessageId
    )
  }

  afterPost () {
    this.inputTarget.value = ''
    this.inputTarget.focus()
    this.scroll(1)
  }

  scroll (delay = 10) {
    const lists = document.querySelectorAll('[data-target="chat.list"]')
    setTimeout(() => {
      lists.forEach(e => (e.scrollTop = e.scrollHeight))
    }, delay)
  }

  reload (event) {
    if (!event.detail) return
    const { messageId } = event.detail
    if (messageId === lastMessageId) return
    debouncedReload(this)
  }
}

