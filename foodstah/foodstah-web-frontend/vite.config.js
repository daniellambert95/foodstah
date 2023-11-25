import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  build: {

    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `@import "./src/styles/tailwind.css";`, 
        },
      },
    },
  },
});