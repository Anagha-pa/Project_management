import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  // Check if the user is authenticated by looking for tokens in localStorage
  const tokens = localStorage.getItem('tokens');

  // If tokens are found, render the children components; otherwise, redirect to the login page
  return tokens ? children : <Navigate to="/login" />;
};

export default ProtectedRoute;
