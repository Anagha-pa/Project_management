import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import API from '../../services/api';

const ProjectDetail = () => {
  const { id } = useParams();
  const [project, setProject] = useState(null);

  useEffect(() => {
    API.get(`Projects/projects/<int:pk>/${id}/`)
      .then((response) => setProject(response.data))
      .catch((error) => console.error('Error fetching project:', error));
  }, [id]);

  if (!project) return <p>Loading project...</p>;

  return (
    <div>
      <h1>{project.name}</h1>
      <p>{project.description}</p>
      <p>Status: {project.status}</p>
      <p>Start Date: {project.start_date}</p>
      <p>End Date: {project.end_date}</p>
      <Link to={`/edit-project/${id}`}>Edit Project</Link>
    </div>
  );
};

export default ProjectDetail;
