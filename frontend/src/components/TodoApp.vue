<template>
  <div class="app-container">
    <div class="todo-container">
      <h1 class="title">Todo List</h1>

      <!-- Form to Add a New Todo -->
      <form @submit.prevent="addTask" class="todo-form">
        <div class="input-group">
          <input
            type="text"
            class="input"
            v-model="todoStore.newTask.title"
            placeholder="Enter title..."
            required
          />
          <input
            type="text"
            class="input"
            v-model="todoStore.newTask.description"
            placeholder="Enter description..."
            required
          />
        </div>
        <button type="submit" class="btn add-btn">Add Todo</button>
      </form>

      <!-- Todo List -->
      <ul class="todo-list">
        <li v-for="task in todoStore.tasks" :key="task.id" class="todo-item">
          <div class="todo-text">
            <strong>{{ task.title }}</strong>
            <p>{{ task.description }}</p>
          </div>
          <div class="todo-buttons">
            <button @click="deleteTask(task.id)" class="btn delete-btn">Delete</button>
            <button @click="toggleComplete(task)" class="btn complete-btn">
              {{ task.completed ? "Completed" : "Complete" }}
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useTodoStore } from '@/stores/todoStore';  // Import the Pinia store

const todoStore = useTodoStore();  // Access the Pinia store

// Fetch todos when the component mounts
onMounted(() => {
  todoStore.fetchTasks();
});

// Delegate actions to the Pinia store
const addTask = todoStore.addTask;   // Use addTask method from the store
const deleteTask = todoStore.removeTask;  // Use removeTask method from the store
const toggleComplete = todoStore.toggleComplete;
</script>

<style scoped>
/* App Container */
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color:#f3ecec;
  font-family: 'Arial', sans-serif;
}

/* Todo Container */
.todo-container {
  background-color: #fff;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 600px;
  text-align: center;
}

/* Title */
.title {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
}

/* Form Styling */
.todo-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.input-group {
  display: flex;
  gap: 10px;
}

.input {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border-radius: 10px;
  border: 1px solid #ddd;
  outline: none;
}

.input:focus {
  border-color: #6c63ff;
}

/* Button Styling */
.btn {
  padding: 10px;
  font-size: 1rem;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-btn {
  background-color: #6c63ff;
  color: white;
}

.add-btn:hover {
  background-color: #90f582;
}

.delete-btn {
  background-color:#c0392b;
  color: white;
}

.delete-btn:hover {
  background-color:#ce210e;
}

.complete-btn {
  background-color: #0ca54c;
  color: white;
}

.complete-btn:hover {
  background-color: #27ae60;
}

/* Todo List Styling */
.todo-list {
  list-style: none;
  padding: 0;
  margin-top: 20px;
  text-align: left;
}

.todo-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  margin-bottom: 10px;
  background-color: #fafafa;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.todo-text {
  flex-grow: 1;
}

.todo-text strong {
  font-size: 1.2rem;
  color: #333;
}

.todo-text p {
  color: #777;
  font-size: 1rem;
}

.todo-buttons {
  display: flex;
  gap: 10px;
}

.todo-buttons button {
  padding: 8px 15px;
  font-size: 0.9rem;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

/* Responsive Design */
@media (max-width: 600px) {
  .todo-container {
    width: 100%;
    padding: 15px;
  }

  .input-group {
    flex-direction: column;
  }

  .input {
    margin-bottom: 10px;
  }
}
</style>
