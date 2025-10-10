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

function autoGrow(e: Event) {
  const target = e.target as HTMLTextAreaElement
  target.style.height = 'auto'
  target.style.height = target.scrollHeight + 'px'
}

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
        <label>
          <span>1. ФИО</span>
          <input v-model="form.fio" required />
        </label>
        <label>
          <span>2. Курс обучения</span>
          <input v-model="form.course" required />
        </label>
        <label>
          <span>3. Факультет</span>
          <input v-model="form.faculty" required />
        </label>
        <label>
          <span>4. Группа обучения (в формате УАиА22-3)</span>
          <input v-model="form.group" required placeholder="УАиА22-3" />
        </label>
        <label>
          <span>5. Телефон (в формате 8 (ХХХ) ХХХ – ХХ – ХХ)</span>
          <input v-model="form.phone" required placeholder="8 (___) ___-__-__" />
        </label>
        <label>
          <span>6. Почта (gmail.com)</span>
          <input v-model="form.email" required placeholder="example@gmail.com" />
        </label>
        <label>
          <span>7. Ссылка на ВК</span>
          <input v-model="form.vk" required placeholder="https://vk.com/..." />
        </label>
        <label>
          <span>8. Ссылка на ТГ</span>
          <input v-model="form.tg" required placeholder="https://t.me/..." />
        </label>
        <fieldset>
          <legend>9. Успеваемость на последней сессии</legend>
          <label><input type="radio" v-model="form.session" value="все 5" required /> все 5</label>
          <label><input type="radio" v-model="form.session" value="4 и 5" /> 4 и 5</label>
          <label><input type="radio" v-model="form.session" value="есть 3" /> есть 3</label>
          <label><input type="radio" v-model="form.session" value="есть пересдачи" /> есть пересдачи</label>
          <label><input type="radio" v-model="form.session" value="ещё не сдавал сессию" /> ещё не сдавал сессию</label>
        </fieldset>
        <fieldset>
          <legend>10. Твой размер футболки</legend>
          <label><input type="radio" v-model="form.tshirt" value="XS" required /> XS</label>
          <label><input type="radio" v-model="form.tshirt" value="S" /> S</label>
          <label><input type="radio" v-model="form.tshirt" value="M" /> M</label>
          <label><input type="radio" v-model="form.tshirt" value="L" /> L</label>
          <label><input type="radio" v-model="form.tshirt" value="XL" /> XL</label>
          <label><input type="radio" v-model="form.tshirt" value="XXL" /> XXL</label>
        </fieldset>
        <label>
          <span>11. Есть ли у тебя аллергии на какие-либо продукты или иные особенности питания?</span>
          <textarea v-model="form.food" rows="2" @input="autoGrow($event)" />
        </label>
        <fieldset>
          <legend>12. Состоишь ли ты в ССт сейчас?</legend>
          <label><input type="radio" v-model="form.sst" value="Нет, не подавался в ССт" required /> Нет, не подавался в ССт</label>
          <label><input type="radio" v-model="form.sst" value="Нет, не прошёл в ССт" /> Нет, не прошёл в ССт</label>
          <label><input type="radio" v-model="form.sst" value="Да, с октября 2024 года" /> Да, с октября 2024 года</label>
          <label><input type="radio" v-model="form.sst" value="Да, с прошлого учебного года" /> Да, с прошлого учебного года</label>
        </fieldset>
        <button type="submit" class="next-btn">Следующая страница</button>
      </form>
    </div>
  .form-header {
    font-size: 1.5rem;
    font-weight: bold;
    color: #222;
    margin-bottom: 18px;
    text-align: center;
    width: 100%;
  }

    <!-- конец корневого блока greeting -->
  </div>
</template>


<style scoped>


html, body {
  background: #fff !important;
  min-height: 100vh;
}


.greeting {
  position: relative;
  width: 100%;
  max-width: 100vw;
  min-height: 100vh;
  background: #fff;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  z-index: 999;
  overflow-y: auto;
}
.animated {
  font-size: 2.2rem;
  font-weight: bold;
  color: #000;
  letter-spacing: 2px;
  white-space: pre;
  transition: color 0.3s;
}
.consent-block {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}
.consent-text {
  text-align: center;
}
.consent-buttons {
  display: flex;
  gap: 18px;
}
.consent-buttons button {
  padding: 10px 24px;
  border-radius: 10px;
  border: 1px solid #d0d0d0;
  background: #fff;
  font-size: 1.1rem;
  font-weight: 500;
  color: #222;
  cursor: pointer;
  transition: background 0.2s;
}
.consent-buttons button:hover {
  background: #f0f0f0;
}
.survey-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
  width: 100%;
  max-width: 400px;
  margin: 0 auto;
}
.survey-form label, .survey-form fieldset {
  display: flex;
  flex-direction: column;
  gap: 6px;
  color: #000;
}
.survey-form input, .survey-form textarea {
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid #d0d0d0;
  font-size: 16px;
  resize: none;
}
.survey-form textarea {
  min-height: 40px;
  max-height: 200px;
}
.survey-form fieldset {
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  padding: 10px 12px;
  gap: 8px;
}
.survey-form legend {
  font-weight: 500;
  margin-bottom: 6px;
  color: #000;
}
.survey-form span {
  color: #000;
}

</style>

