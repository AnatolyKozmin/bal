<script setup lang="ts">
import { ref, onMounted } from 'vue'

const animatedText = ref('')

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
              const finalText = 'привет, кандидат!'
              let j = 1 // уже есть "р"
              const finalInterval = setInterval(() => {
                animatedText.value += finalText[j]
                j++
                if (j >= finalText.length) clearInterval(finalInterval)
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
    <span class="animated">{{ animatedText }}</span>
  </div>
</template>


<style scoped>
.greeting {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: #fff;
}
.animated {
  font-size: 2.2rem;
  font-weight: bold;
  color: #000;
  letter-spacing: 2px;
  white-space: pre;
  transition: color 0.3s;
}
</style>


