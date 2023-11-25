import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";

import NavigationHeader from '../components/navigation-header';
import SuccessMessage from '../components/success-message';
import ErrorMessage from '../components/error-message';
import { isLoggedIn } from '../utils/authUser.js';


const LoginPage = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  // location is being used to catch the success message state from the signup page
  const location = useLocation();
  const successMessage = location.state ? location.state.successMessage : null;
  const [errorMessage, setErrorMessage] = useState(null);
  const navigate = useNavigate()

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/v1/auth/login/', formData);
      if (response.status === 200) {
        console.log('Login successful');
        localStorage.setItem('token', response.data.data.token);
        navigate("/");
       }
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
      {successMessage && <SuccessMessage message={successMessage} />}
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="bg-white p-8 rounded shadow-md w-96">
          <h1 className="text-2xl text-center font-bold mb-6">Log In</h1>
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
            <div className="flex justify-between items-center mb-4">
              <div >
                <Link to="/signup" className="text-blue-500 hover:underline">
                  Don't have an account? Sign Up
                </Link>
              </div>
              <div>
                <Link to="/forgot-password" className="text-blue-500 hover:underline">
                  Forgot Password?
                </Link>
              </div>
            </div>
            <div className="w-full text-center mt-4'">
              <button
                type="submit"
                className="bg-primary text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-300"
              >
                Log In
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
