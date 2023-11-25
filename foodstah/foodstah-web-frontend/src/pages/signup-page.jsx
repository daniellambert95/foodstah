import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

import NavigationHeader from '../components/navigation-header';
import ErrorMessage from '../components/error-message';


const SignUp = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    // password2: '',
   });

  const [errorMessage, setErrorMessage] = useState(null);
  const navigate = useNavigate()

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/signup/', formData);
      navigate("/login", { state: { successMessage: "Signup successful! You can now login with your email and password." } }); 
    } catch (error) {
      if (error.response) {
        setErrorMessage(error.response.data);
      } else if (error.request) {
        setErrorMessage('No response received');
      } else {
        setErrorMessage(error.message);
      }
    }
   };

  return (
    <div>
      <NavigationHeader />
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h1 className="text-2xl text-center font-bold mb-6">Sign Up</h1>
        {errorMessage && <ErrorMessage message={errorMessage} />}
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label htmlFor="username" className="block text-sm font-medium text-gray-600">
              Username:
            </label>
            <input
              type="text"
              id="username"
              name="username"
              value={formData.username}
              onChange={handleChange}
              className="mt-1 p-2 border rounded-md w-full"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="email" className="block text-sm font-medium text-gray-600">
              Email:
            </label>
            <input
              type="email"
              id="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="mt-1 p-2 border rounded-md w-full"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="password" className="block text-sm font-medium text-gray-600">
              Password:
            </label>
            <input
              type="password"
              id="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="mt-1 p-2 border rounded-md w-full"
              required
            />
            </div>
            {/* <div className="mb-4">
            <label htmlFor="password2" className="block text-sm font-medium text-gray-600">
              Confirm Password:
            </label>
            <input
              type="password"
              id="password2"
              name="password2"
              value={formData.password2}
              onChange={handleChange}
              className="mt-1 p-2 border rounded-md w-full"
              required
            />
            </div> */}
          <div className='mb-4'>
                <Link to="/login" className="text-blue-500 hover:underline">
                  Already have an account? <br /> Sign In
                </Link>
              </div>
          <div className="w-full text-center">
            <button
              type="submit"
              className="bg-primary text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-300"
            >
              Sign Up
            </button>
          </div>
        </form>
      </div>
    </div>
    </div>
  );
};

export default SignUp;
