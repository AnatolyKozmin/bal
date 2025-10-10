<template>
  <div class="first-step">
    <label>
      <span>1. ФИО</span>
      <input v-model="props.form.fio" required />
    </label>
    <label>
      <span>2. Курс обучения</span>
      <input v-model="props.form.course" required />
    </label>
    <label>
      <span>3. Факультет</span>
      <input v-model="props.form.faculty" required />
    </label>
    <label>
      <span>4. Группа обучения (в формате УАиА22-3)</span>
      <input v-model="props.form.group" required placeholder="УАиА22-3" />
    </label>

    <label>
      <span>5. Телефон (в формате 8 (ХХХ) ХХХ – ХХ – ХХ)</span>
      <input v-model="props.form.phone" required placeholder="8 (___) ___-__-__" />
    </label>
    <label>
      <span>6. Почта (gmail.com)</span>
      <input v-model="props.form.email" required placeholder="example@gmail.com" />
    </label>
    <label>
      <span>7. Ссылка на ВК</span>
      <input v-model="props.form.vk" required placeholder="https://vk.com/..." />
    </label>
    <label>
      <span>8. Ссылка на ТГ</span>
      <input v-model="props.form.tg" required placeholder="https://t.me/..." />
    </label>

    <fieldset>
      <legend>9. Успеваемость на последней сессии</legend>
      <label><input type="radio" v-model="props.form.session" value="все 5" required /> все 5</label>
      <label><input type="radio" v-model="props.form.session" value="4 и 5" /> 4 и 5</label>
      <label><input type="radio" v-model="props.form.session" value="есть 3" /> есть 3</label>
      <label><input type="radio" v-model="props.form.session" value="есть пересдачи" /> есть пересдачи</label>
      <label><input type="radio" v-model="props.form.session" value="ещё не сдавал сессию" /> ещё не сдавал сессию</label>
    </fieldset>

    <fieldset>
      <legend>10. Твой размер футболки</legend>
      <label><input type="radio" v-model="props.form.tshirt" value="XS" required /> XS</label>
      <label><input type="radio" v-model="props.form.tshirt" value="S" /> S</label>
      <label><input type="radio" v-model="props.form.tshirt" value="M" /> M</label>
      <label><input type="radio" v-model="props.form.tshirt" value="L" /> L</label>
      <label><input type="radio" v-model="props.form.tshirt" value="XL" /> XL</label>
      <label><input type="radio" v-model="props.form.tshirt" value="XXL" /> XXL</label>
    </fieldset>

    <label>
      <span>11. Есть ли у тебя аллергии на какие-либо продукты или иные особенности питания?</span>
      <textarea v-model="props.form.food" rows="2" @input="autoGrow($event)" />
    </label>

    <fieldset>
      <legend>12. Состоишь ли ты в ССт сейчас?</legend>
      <label><input type="radio" v-model="props.form.sst" value="Нет, не подавался в ССт" required /> Нет, не подавался в ССт</label>
      <label><input type="radio" v-model="props.form.sst" value="Нет, не прошёл в ССт" /> Нет, не прошёл в ССт</label>
      <label><input type="radio" v-model="props.form.sst" value="Да, с октября 2024 года" /> Да, с октября 2024 года</label>
      <label><input type="radio" v-model="props.form.sst" value="Да, с прошлого учебного года" /> Да, с прошлого учебного года</label>
    </fieldset>

    <div class="first-step-controls">
      <button type="submit" class="next-btn">Следующая страница</button>
    </div>
  </div>
</template>

<script setup lang="ts">
function autoGrow(e: Event) {
  const target = e.target as HTMLTextAreaElement
  target.style.height = 'auto'
  target.style.height = target.scrollHeight + 'px'
}
const props = defineProps<{ form: Record<string, any> }>()
</script>

<style scoped>
.first-step {
  padding: 0 1rem;
  box-sizing: border-box;
  max-width: 100%;
}
.first-step label { display: flex; flex-direction: column; gap: 8px; margin-bottom: 6px; }
.first-step input, .first-step textarea { padding: 8px; border-radius: 8px; border: 1px solid #e0e0e0; }
.first-step fieldset { border: 1px solid #eee; border-radius: 8px; padding: 8px; }
.first-step-controls { margin-top: 12px; display:flex; justify-content:center; }
.first-step .next-btn { padding: 10px 18px; border-radius: 10px; }

@media (min-width: 600px) {
  .first-step { padding: 0 0rem; }
}

</style>
