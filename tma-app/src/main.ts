import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { initializeTelegramWebApp, getTelegramUser } from './tma'

initializeTelegramWebApp()

const apiBase = (import.meta as any).env?.VITE_API_BASE || ''
const u = getTelegramUser()
if (u.id) {
  fetch(`${apiBase}/api/tma/open`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ tg_id: u.id, tg_username: u.username || null })
  }).catch(() => {})
}
createApp(App).mount('#app')
