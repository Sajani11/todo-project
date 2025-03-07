import { createRouter, createWebHistory } from 'vue-router';
import TodoView from './views/TodoView.vue';  // Import TodoView.vue

const routes = [
  { path: '/', component: TodoView },  // Use TodoView as the main route for the app
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
