// SuccessMessage.jsx
import React from 'react';

const SuccessMessage = ({ message }) => {
 return (
  <div className="bg-white border border-success text-success text-center px-4 py-3 my-3 rounded relative" role="alert">
    <span className="block sm:inline">{Object.values(message)}</span>
  </div>
 );
};

export default SuccessMessage;
