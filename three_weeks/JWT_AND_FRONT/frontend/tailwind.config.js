/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f3fbf4",
          100: "#d9f3de",
          200: "#bae7c4",
          300: "#8fd3a0",
          400: "#5eb67a",
          500: "#3a995f",
          600: "#2d7b4b",
          700: "#255f3c",
          800: "#214d33",
          900: "#1c402b"
        }
      },
      boxShadow: {
        soft: "0 18px 45px rgba(46, 91, 62, 0.12)"
      }
    }
  },
  plugins: []
};
