import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import ProjectList from './components/Projects/ProjectList';
import ProjectDetail from './components/Projects/ProjectDetail';
import AddEditProject from './components/Projects/AddEditProject';
import ProtectedRoute from './components/Auth/ProtectedRoute';
import TaskList from './components/Task/TaskList';
import TaskDetail from './components/Task/TaskDetail';
import AddEditTask from './components/Task/AddEditTask';

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Public Routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        {/* Protected Routes */}
        <Route path="/" element={<ProtectedRoute><ProjectList /></ProtectedRoute>}/>
        <Route path="/project/:id" element={<ProtectedRoute><ProjectDetail /></ProtectedRoute>}/>
        <Route path="/project/add" element={<ProtectedRoute><AddEditProject /></ProtectedRoute>}/>
        <Route path="/project/edit/:id" element={<ProtectedRoute><AddEditProject /></ProtectedRoute>}/>

        <Route path="/task" element={<ProtectedRoute><TaskList/></ProtectedRoute>}/>
        <Route path="/task/:id" element={<ProtectedRoute><TaskDetail /></ProtectedRoute>}/>
        <Route path="/task/add" element={<ProtectedRoute><AddEditTask /></ProtectedRoute>}/>
        <Route path="/task/edit/:id" element={<ProtectedRoute><AddEditTask /></ProtectedRoute>}/>


        {/* Fallback Route */}
        <Route path="*" element={<Login />} />
      </Routes>
    </Router>
  );
};

export default App;
