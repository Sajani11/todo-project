import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { createPinia } from 'pinia';  // Import Pinia
import 'bootstrap/dist/css/bootstrap.min.css';


const app = createApp(App);

// Use of Pinia for state management
app.use(createPinia());
app.use(router);
app.mount('#app');
