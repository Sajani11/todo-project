<template>
  <div class="container">
    <h1 class="my-4">Todo List</h1>

    <!-- Form to Add a New Todo -->
    <form @submit.prevent="addTodo" class="mb-4">
      <div class="mb-3">
        <label for="title" class="form-label">Title</label>
        <input
          type="text"
          id="title"
          class="form-control"
          v-model="newTodo.title"
          required />
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <input
          type="text"
          id="description"
          class="form-control"
          v-model="newTodo.description"
          required />
      </div>
      <button type="submit" class="btn btn-primary">Add Todo</button>
    </form>

    <!-- Todo List -->
    <ul class="list-group">
      <li
        v-for="todo in todos"
        :key="todo.id"
        class="list-group-item d-flex justify-content-between align-items-center">
        <div>
          <strong>{{ todo.title }}</strong>
          <p>{{ todo.description }}</p>
        </div>
        <div>
          <button
            @click="deleteTodo(todo.id)"
            class="btn btn-danger btn-sm me-2">
            Delete
          </button>
          <button @click="toggleComplete(todo)" class="btn btn-warning btn-sm">
            {{ todo.completed ? "Mark Incomplete" : "Mark Complete" }}
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TodoApp",
  data() {
    return {
      todos: [],
      newTodo: {
        title: "",
        description: "",
      },
    };
  },
  created() {
    this.fetchTodos();
  },
  methods: {
    async fetchTodos() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/todos/");
        this.todos = response.data;
      } catch (error) {
        console.error(error);
      }
    },
    async addTodo() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/todos/",
          this.newTodo
        );
        this.todos.push(response.data);
        this.newTodo.title = "";
        this.newTodo.description = "";
      } catch (error) {
        console.error(error);
      }
    },
    async deleteTodo(id) {
      try {
        await axios.delete(`http://127.0.0.1:8000/todos/${id}/`);
        this.todos = this.todos.filter((todo) => todo.id !== id);
      } catch (error) {
        console.error(error);
      }
    },
    async toggleComplete(todo) {
      try {
        todo.completed = !todo.completed;
        await axios.put(`http://127.0.0.1:8000/todos/${todo.id}/`, todo);
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
.completed {
  text-decoration: line-through;
  color: #cf3c3c;
}
</style>
