import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import API from '../../services/api';

const TaskList = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    API.get('Projects/tasks/')
      .then((response) => setTasks(response.data))
      .catch((error) => console.error('Error fetching tasks:', error));
  }, []);

  return (
    <div>
      <h1>Task List</h1>
      <Link to="/add-task">Add New Task</Link>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            <Link to={`/tasks/${task.id}`}>{task.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
