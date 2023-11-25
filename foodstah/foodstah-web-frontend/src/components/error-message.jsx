// ErrorMessage.jsx
import React from 'react';

const ErrorMessage = ({ message }) => {
 return (
  <div className="bg-light border border-danger text-danger text-center px-4 py-3 my-3 rounded relative" role="alert">
    <span className="block sm:inline">{Object.values(message)[0]}</span>
  </div>
 );
};

export default ErrorMessage;
