import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import API from '../../services/api';

const ProjectList = () => {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    API.get('Projects/projects/')
      .then((response) => setProjects(response.data))
      .catch((error) => console.error('Error fetching projects:', error));
  }, []);

  return (
    <div>
      <h1>Project List</h1>
      <Link to="/add-project">Add New Project</Link>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            <Link to={`/projects/${project.id}`}>{project.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProjectList;
