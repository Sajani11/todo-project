import { createRouter, createWebHistory } from 'vue-router';
import TodoApp from './components/TodoApp.vue';

const routes = [
    { path: '/', component: TodoApp }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
