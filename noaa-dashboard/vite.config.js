import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // Binds to all interfaces, allowing access from other devices
    port: 5179, // Default port, can be changed if needed
  },
})
