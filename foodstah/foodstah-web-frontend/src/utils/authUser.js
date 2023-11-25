// src/utils/auth.js

// Returns a Boolean value for if User is logged in
export function isLoggedIn() {
    return !!localStorage.getItem('token');
   }
   
// Returns the users auth token. Used for requests.
export const getToken = () => {
    return localStorage.getItem('token');
};