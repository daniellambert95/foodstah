import React from 'react';
import { Link } from 'react-router-dom';
import NavigationHeader from '../components/navigation-header';


const HomePage = () => {
  return (
    <div>
       <NavigationHeader />
    <div className="min-h-screen flex items-center justify-center bg-light text-white">
      <div className="text-center">
        <h1 className="text-primary text-4xl font-bold mb-4">Welcome to Foodstah</h1>
        <p className="text-dark text-lg mb-8">Share your culinary creations with the world!</p>
        <div className="flex justify-center space-x-4">
          <Link to="/login">
            <button className="bg-light text-dark py-2 px-4 rounded-lg hover:bg-dark hover:text-light transition duration-300">
              Log In
            </button>
          </Link>
          <Link to="/signup">
            <button className="bg-primary text-light py-2 px-4 rounded-lg hover:bg-light hover:text-dark transition duration-300">
              Sign Up
            </button>
          </Link>
        </div>
      </div>
    </div>
    </div>
  );
};

export default HomePage;
