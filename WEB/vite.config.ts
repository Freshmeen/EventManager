import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    allowedHosts: ['9961d56eb87ffce82a8a1b475d730ad3.serveo.net']
  }
})
