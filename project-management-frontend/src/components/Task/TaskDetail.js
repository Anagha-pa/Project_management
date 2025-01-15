import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import API from '../../services/api';

const TaskDetail = () => {
  const { id } = useParams();
  const [task, setTask] = useState(null);

  useEffect(() => {
    API.get(`Projects/tasks/<int:pk>/${id}/`)
      .then((response) => setTask(response.data))
      .catch((error) => console.error('Error fetching task:', error));
  }, [id]);

  if (!task) return <p>Loading task...</p>;

  return (
    <div>
      <h1>{task.name}</h1>
      <p>{task.description}</p>
      <p>Status: {task.status}</p>
      <Link to={`/edit-task/${id}`}>Edit Task</Link>
    </div>
  );
};

export default TaskDetail;
