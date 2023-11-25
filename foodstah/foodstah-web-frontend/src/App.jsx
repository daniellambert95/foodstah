import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/home-page.jsx'
import LogIn from './pages/login-page.jsx';
import SignUp from './pages/signup-page.jsx'; 

   function App() {
     return (
       <div className="font-poppins">

         <BrowserRouter>
           <Routes>
             <Route path="/" element={<HomePage />} />
             <Route path="/signup" element={<SignUp />} />
             <Route path="/login" element={<LogIn />} />
           </Routes>
         </BrowserRouter>
       </div>
     );
   }

export default App
