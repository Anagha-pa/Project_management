import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000/', // Replace with your backend URL
});

// Add a request interceptor to include tokens
API.interceptors.request.use((config) => {
  const tokens = JSON.parse(localStorage.getItem('tokens'));
  if (tokens) {
    config.headers.Authorization = `Bearer ${tokens.access}`;
  }
  return config;
});

export default API;
