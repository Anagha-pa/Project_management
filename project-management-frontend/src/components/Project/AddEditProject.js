import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import API from '../../services/api';

const AddEditProject = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    start_date: '',
    end_date: '',
    status: '',
  });

  useEffect(() => {
    if (id) {
      API.get(`Projects/projects/<int:pk>${id}/`)
        .then((response) => setFormData(response.data))
        .catch((error) => console.error('Error fetching project:', error));
    }
  }, [id]);

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (id) {
      API.put(`Projects/projects/<int:pk>${id}/`, formData)
        .then(() => navigate('/'))
        .catch((error) => console.error('Error updating project:', error));
    } else {
      API.post('projects/', formData)
        .then(() => navigate('/'))
        .catch((error) => console.error('Error creating project:', error));
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>{id ? 'Edit Project' : 'Add Project'}</h1>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleInputChange}
        placeholder="Project Name"
        required
      />
      <textarea
        name="description"
        value={formData.description}
        onChange={handleInputChange}
        placeholder="Description"
        required
      />
      <input
        type="date"
        name="start_date"
        value={formData.start_date}
        onChange={handleInputChange}
        required
      />
      <input
        type="date"
        name="end_date"
        value={formData.end_date}
        onChange={handleInputChange}
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

export default AddEditProject;
