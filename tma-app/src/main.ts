import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { initializeTelegramWebApp } from './tma'

initializeTelegramWebApp()
createApp(App).mount('#app')
