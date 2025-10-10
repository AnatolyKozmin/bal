<script setup lang="ts">
import { ref, onMounted } from 'vue'

const animatedText = ref('')
const showConsent = ref(false)
const showForm = ref(false)
const showSad = ref(false)
const consentText1 = ref('')
const consentText2 = ref('')
const consentText3 = ref('')
const showConsentButtons = ref(false)
const sadText = ref('')

import { reactive } from 'vue'
import FirstStep from './FirstStep.vue'
const form = reactive({
  fio: '',
  course: '',
  faculty: '',
  group: '',
  phone: '',
  email: '',
  vk: '',
  tg: '',
  session: '',
  tshirt: '',
  food: '',
  sst: '',
})




function nextPage() {
  // Здесь можно добавить логику для отображения следующих вопросов
  alert('Переход на следующую страницу!')
}

function animateSadText() {
  const text = 'Жаль...'
  sadText.value = ''
  let i = 0
  const interval = setInterval(() => {
    sadText.value += text[i]
    i++
    if (i >= text.length) clearInterval(interval)
  }, 120)
}

function askConsent() {
  showConsent.value = true
  consentText1.value = ''
  consentText2.value = ''
  consentText3.value = ''
  showConsentButtons.value = false
  setTimeout(() => {
    consentText1.value = 'Согласен ли ты'
    setTimeout(() => {
      consentText2.value = 'со сбором'
      setTimeout(() => {
        consentText3.value = 'персональных данных?'
        setTimeout(() => {
          showConsentButtons.value = true
        }, 800)
      }, 800)
    }, 800)
  }, 100)
}

function handleConsent(answer: boolean) {
  if (answer) {
    showForm.value = true
    showConsent.value = false
  } else {
    showSad.value = true
    showConsent.value = false
    animateSadText()
  }
}

onMounted(() => {
  // 1. Пишем "првет."
  const typo = 'првет.'
  let i = 0
  const typeInterval = setInterval(() => {
    animatedText.value += typo[i]
    i++
    if (i >= typo.length) {
      clearInterval(typeInterval)
      // 2. Стираем до "р"
      setTimeout(() => {
        let eraseI = typo.length
        const eraseInterval = setInterval(() => {
          eraseI--
          animatedText.value = typo.slice(0, eraseI)
          if (eraseI === 1) {
            clearInterval(eraseInterval)
            // 3. Пишем "привет кандидат."
            setTimeout(() => {
              const finalText = 'Привет, кандидат.'
              let j = 1 // уже есть "р"
              const finalInterval = setInterval(() => {
                animatedText.value += finalText[j]
                j++
                if (j >= finalText.length) {
                  clearInterval(finalInterval)
                  setTimeout(askConsent, 700)
                }
              }, 120)
            }, 350)
          }
        }, 80)
      }, 400)
    }
  }, 120)
})
</script>



<template>
  <div class="greeting">
    <span class="animated" v-if="!showConsent && !showForm && !showSad">{{ animatedText }}</span>
    <div v-if="showConsent && !showForm && !showSad" class="consent-block">
      <div class="consent-text animated">
        <div>{{ consentText1 }}</div>
        <div>{{ consentText2 }}</div>
        <div>{{ consentText3 }}</div>
      </div>
      <div v-if="showConsentButtons" class="consent-buttons">
        <button @click="handleConsent(true)">Да</button>
        <button @click="handleConsent(false)">Нет</button>
      </div>
    </div>
    <span class="animated" v-if="showSad">{{ sadText }}</span>
    <div v-if="showForm">
      <div class="form-header">Анкета кандидата</div>
      <form class="survey-form" @submit.prevent="nextPage">
        <FirstStep :form="form" />
        <!-- Первый шаг (все поля и кнопка перенесены в FirstStep.vue) -->
      </form>
    </div>
  
    <!-- конец корневого блока greeting -->
  </div>
</template>


<style scoped>
/* Базовая разметка и фон */
html, body {
  background: #fff !important;
  min-height: 100vh;
}

.greeting {
  position: relative;
    width: 100%;
    max-width: 100vw;
    min-height: 114vh;
    background: #fff;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    z-index: 999;
    overflow-y: auto;
    text-align: center;
    padding: 0.8rem 4.2rem 1.4rem;
    box-sizing: border-box;
}

.animated {
  font-size: clamp(1.8rem, 5.5vw, 3rem);
  font-weight: 700;
  color: #000;
  letter-spacing: 0.2px;
  white-space: pre-line;
  transition: color 0.2s;
  text-align: center;
  max-width: 100%;
  word-break: break-word;
  overflow-wrap: break-word;
  padding: 0 2.8rem;
  box-sizing: border-box;
}

.consent-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  width: 100%;
}

.consent-text {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-size: clamp(1.2rem, 4vw, 1.6rem);
  line-height: 1.25;
  max-width: 100%;
  word-break: break-word;
  overflow-wrap: break-word;
  padding: 0 2.8rem;
  box-sizing: border-box;
}
.consent-text > div {
  display: block;
  width: 100%;
  text-align: center;
}
.animated { display: block; margin: 0 auto; }

.consent-buttons {
  display: flex;
  gap: 12px;
}
.consent-buttons button {
  padding: clamp(10px, 3vw, 14px) clamp(14px, 4.5vw, 24px);
  border-radius: 12px;
  border: 1px solid #d0d0d0;
  background: #fff;
  font-size: clamp(1rem, 3.2vw, 1.15rem);
  color: #222;
  cursor: pointer;
}
.consent-buttons button:hover { background: #f5f5f5; }

.survey-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
  padding: 0 2.8rem;
  box-sizing: border-box;
}

@media (max-width: 360px) {
  .greeting { padding: 1.4rem; }
  .animated { padding: 0 1rem; }
  .consent-text { padding: 0 1rem; }
  .survey-form { padding: 0 1rem; }
}
.survey-form label,
.survey-form fieldset {
  display: flex;
  flex-direction: column;
  gap: 6px;
  color: #000;
}
.survey-form input,
.survey-form textarea {
  padding: clamp(12px, 3vw, 16px) clamp(12px, 3.2vw, 16px);
  border-radius: 10px;
  border: 1px solid #e0e0e0;
  font-size: clamp(1rem, 2.8vw, 1.05rem);
}
.survey-form textarea { min-height: 48px; max-height: 220px; }
.survey-form fieldset {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 10px 12px;
}
.survey-form legend { font-weight: 600; margin-bottom: 6px; }

/* Mobile tweaks */
@media (max-width: 480px) {
  .animated { font-size: 1.2rem; }
  .consent-text { font-size: 0.98rem; }
  .survey-form { max-width: 94vw; }
}

</style>

