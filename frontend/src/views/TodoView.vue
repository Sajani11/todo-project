
<template>
    <div>
      <h1>My To-Do Application</h1>
      <TodoApp /> 
    </div>
  </template>
  
  <script setup>
  import TodoApp from '../components/TodoApp.vue';  
  </script>
  
  <style scoped>
 
  h1 {
    color: blue;
    font-size: 2em;
    text-align: center;
  }
  
  div {
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 8px;
  }
  </style>
  