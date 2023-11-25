/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.html', './src/**/*.js', './src/**/*.jsx'],
  theme: {
    extend: {
      fontFamily: {
        poppins: ['Poppins', 'sans-serif'],
      },
      colors: {
        primary: '#4B3FD8',
        secondary: '#FFF278',
        dark: '#0E101C',
        light: '#E5E5E5',
        info: '#FFA8D4',
        success: '#50D400',
        warning: '#FFB53A',
        danger: '#FE1151'
      },
    },
  },
  plugins: [],
}

