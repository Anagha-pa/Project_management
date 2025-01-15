import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import API from '../../services/api';

const AddEditTask = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    status: '',
  });

  useEffect(() => {
    if (id) {
      API.get(`Projects/tasks/<int:pk>/${id}/`)
        .then((response) => setFormData(response.data))
        .catch((error) => console.error('Error fetching task:', error));
    }
  }, [id]);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (id) {
      API.put(`Projects/tasks/<int:pk>/${id}/`, formData)
        .then(() => navigate('/tasks'))
        .catch((error) => console.error('Error updating task:', error));
    } else {
      API.post('Projects/tasks/', formData)
        .then(() => navigate('/tasks'))
        .catch((error) => console.error('Error creating task:', error));
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>{id ? 'Edit Task' : 'Add Task'}</h1>
      <input
        type="text"
        name="title"
        value={formData.name}
        onChange={handleInputChange}
        placeholder="Task Title"
        required
      />
      <textarea
        name="description"
        value={formData.description}
        onChange={handleInputChange}
        placeholder="Description"
        required
      />
      <select
        name="status"
        value={formData.status}
        onChange={handleInputChange}
        required
      >
        <option value="">Select Status</option>
        <option value="Pending">Pending</option>
        <option value="In Progress">In Progress</option>
        <option value="Completed">Completed</option>
      </select>
      <button type="submit">Save</button>
    </form>
  );
};

export default AddEditTask;
