<template>
  <div class="app-container">
    <div class="todo-container">
      <h1 class="title">Todo List</h1>

      <!-- Form to Add a New Todo -->
      <form @submit.prevent="addTodo" class="todo-form">
        <div class="input-group">
          <input
            type="text"
            class="input"
            v-model="newTodo.title"
            placeholder="Enter title..."
            required />
          <input
            type="text"
            class="input"
            v-model="newTodo.description"
            placeholder="Enter description..."
            required />
        </div>
        <button type="submit" class="btn add-btn">Add Todo</button>
      </form>

      <!-- Todo List -->
      <ul class="todo-list">
        <li v-for="todo in todos" :key="todo.id" class="todo-item">
          <div class="todo-text">
            <strong>{{ todo.title }}</strong>
            <p>{{ todo.description }}</p>
          </div>
          <div class="todo-buttons">
            <button @click="deleteTodo(todo.id)" class="btn delete-btn">delete</button>
            <button @click="toggleComplete(todo)" class="btn complete-btn">
              {{ todo.completed ? "delete" : "complete" }}
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "TodoApp",
  setup() {
    const todos = ref([]);
    const newTodo = ref({ title: "", description: "" });

    const fetchTodos = async () => {
      try {
        const response = await axios.get("http://localhost:8000/todos/");
        todos.value = response.data;
      } catch (error) {
        console.error(error);
      }
    };

    const addTodo = async () => {
      try {
        const response = await axios.post("http://127.0.0.1:8000/todos/", newTodo.value);
        todos.value.push(response.data);
        newTodo.value.title = "";
        newTodo.value.description = "";
      } catch (error) {
        console.error(error);
      }
    };

    const deleteTodo = async (id) => {
      try {
        await axios.delete(`http://127.0.0.1:8000/todos/${id}/`);
        todos.value = todos.value.filter((todo) => todo.id !== id);
      } catch (error) {
        console.error(error);
      }
    };

    const toggleComplete = async (todo) => {
      try {
        todo.completed = !todo.completed;
        await axios.put(`http://127.0.0.1:8000/todos/${todo.id}/`, todo);
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      fetchTodos();
    });

    return { todos, newTodo, addTodo, deleteTodo, toggleComplete };
  },
};
</script>

<style scoped>
.app-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #b6c2cf, #ddf1f7); /* Blue gradient background */
  width: 100vw;
  padding: 20px;
}

.todo-container {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

.title {
  color:#007bff;
  font-size: 2rem;
  margin-bottom: 20px;
}

.todo-form {
  display: flex;
  flex-direction: column;
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.btn {
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.add-btn {
  background: #007bff;
  color: white;
  font-size: 1rem;
}

.todo-list {
  margin-top: 20px;
  list-style: none;
  padding: 0;
}

.todo-item {
  background: #f9f9f9;
  padding: 10px;
  border-radius: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.todo-buttons {
  display: flex;
  gap: 10px;
}

.delete-btn {
  background: #ff4757;
  color: white;
}

.complete-btn {
  background: #1dd1a1;
  color: white;
}
</style>
