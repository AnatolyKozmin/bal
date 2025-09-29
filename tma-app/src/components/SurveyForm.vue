<script setup lang="ts">
import { reactive, computed } from 'vue'

const apiBase = (import.meta as any).env?.VITE_API_BASE || ''

type FormData = {
  firstName: string
  lastName: string
  patronymic: string
  group: string
  faculty: string
  studentId: string
}

const form = reactive<FormData>({
  firstName: '',
  lastName: '',
  patronymic: '',
  group: '',
  faculty: '',
  studentId: ''
})

const groupPattern = /^[А-ЯA-ZЁ]{2,5}\d{2}-\d{1,2}$/

const isValid = computed(() => {
  return (
    form.firstName.trim().length > 1 &&
    form.lastName.trim().length > 1 &&
    form.patronymic.trim().length > 1 &&
    groupPattern.test(form.group.trim()) &&
    form.faculty.trim().length > 0 &&
    form.studentId.trim().length >= 4
  )
})

function submit() {
  const payload = { ...form }
  fetch(`${apiBase}/api/registrations`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
    .then(async (r) => {
      if (!r.ok) throw new Error(await r.text())
      return r.json()
    })
    .then(() => {
      alert('Заявка отправлена!')
    })
    .catch((e) => {
      alert('Ошибка отправки: ' + e)
    })
}
</script>

<template>
  <form class="survey" @submit.prevent="submit">
    <label>
      <span>Имя</span>
      <input v-model.trim="form.firstName"  />
    </label>

    <label>
      <span>Фамилия</span>
      <input v-model.trim="form.lastName"  />
    </label>

    <label>
      <span>Отчество</span>
      <input v-model.trim="form.patronymic"/>
    </label>

    <label>
      <span>Группа (формат ПИ23-1)</span>
      <input v-model.trim="form.group" placeholder="ПИ23-1" />
    </label>

    <fieldset class="faculty">
      <legend>Факультет</legend>
      <label class="radio"><input type="radio" name="faculty" value="ИТиАБД" v-model="form.faculty" /> ИТиАБД</label>
      <label class="radio"><input type="radio" name="faculty" value="ВШУ" v-model="form.faculty" /> ВШУ</label>
      <label class="radio"><input type="radio" name="faculty" value="НАБ" v-model="form.faculty" /> НАБ</label>
      <label class="radio"><input type="radio" name="faculty" value="СНиМК" v-model="form.faculty" /> СНиМК</label>
      <label class="radio"><input type="radio" name="faculty" value="ФЭБ" v-model="form.faculty" /> ФЭБ</label>
      <label class="radio"><input type="radio" name="faculty" value="Финфак" v-model="form.faculty" /> Финфак</label>
      <label class="radio"><input type="radio" name="faculty" value="Юрфак" v-model="form.faculty" /> Юрфак</label>
    </fieldset>

    <label>
      <span>№ студ. билета</span>
      <input v-model.trim="form.studentId" placeholder="123456" />
    </label>

    <button :disabled="!isValid" type="submit">Отправить</button>
  </form>
  <p class="hint">Демо: данные пока не отправляются на сервер.</p>
  </template>

<style scoped>
.survey {
  display: grid;
  gap: 12px;
}
label {
  display: grid;
  gap: 6px;
}
input, select, button {
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid #d0d0d0;
  font-size: 16px;
}
button[disabled] {
  opacity: 0.5;
}
.hint {
  color: #666;
  font-size: 13px;
}
.faculty {
  display: grid;
  gap: 8px;
  border: 1px solid #e0e0e0;
  padding: 10px 12px;
  border-radius: 10px;
}
.radio {
  display: flex;
  align-items: center;
  gap: 8px;
}
</style>


