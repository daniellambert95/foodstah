// NavigationHeader.jsx

import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { isLoggedIn } from '../utils/authUser.js';
import { logout } from '../utils/logout.js';


const NavigationHeader = () => {
  const navigate = useNavigate();
  const handleLogout = () => {
    logout(navigate);
  };

  return (
    <header className="bg-primary p-5">
      <nav className="flex items-center justify-between">
        <Link to="/" className="text-white text-4xl font-bold">
          Foodstah
        </Link>
        {isLoggedIn() && <button className="bg-light text-dark py-2 px-4 rounded-lg hover:bg-light hover:text-dark transition duration-300" onClick={handleLogout}>Logout</button>}
      </nav>
    </header>
  );
 };
 
 export default NavigationHeader;