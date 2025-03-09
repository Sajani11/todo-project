import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';

export const useTodoStore = defineStore('todoStore', () => {
 
  const tasks = ref([]);
  const newTask = ref({
    title: '',
    description: ''
  });

  const fetchTasks = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/tasks/');
      tasks.value = response.data;
    } catch (error) {
      console.error("Error fetching tasks:", error);
    }
  };

 
  const addTask = async () => {
    if (!newTask.value.title.trim() || !newTask.value.description.trim()) return;
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/tasks/', {
        title: newTask.value.title,
        description: newTask.value.description,
        completed: false
      });
      tasks.value.push(response.data);
      newTask.value.title = '';
      newTask.value.description = '';
    } catch (error) {
      console.error("Error adding task:", error);
    }
  };

  // Remove a task
  const removeTask = async (id) => {
    try {
      await axios.delete(`http://127.0.0.1:8000/api/tasks/${id}/`);
      tasks.value = tasks.value.filter(task => task.id !== id);
    } catch (error) {
      console.error("Error deleting task:", error);
    }
  };


  const toggleComplete = async (task) => {
    try {
      task.completed = !task.completed;
     
      await axios.put(`http://127.0.0.1:8000/api/tasks/${task.id}/`, {
        ...task,
        completed: task.completed
      });
    } catch (error) {
      console.error("Error toggling task completion:", error);
    }
  };

  return { tasks, newTask, fetchTasks, addTask, removeTask, toggleComplete };
});
