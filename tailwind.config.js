/** @type {import('tailwindcss').Config} */
const { addDynamicIconSelectors } = require('@iconify/tailwind');
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui"), addDynamicIconSelectors()],
  daisyui: {
    themes: [
      {
        'light': {
           'primary' : '#ff3548',
           'primary-focus' : '#ed1d31',
           'primary-content' : '#ffffff',

           'secondary' : '#3e44f9',
           'secondary-focus' : '#3338cc',
           'secondary-content' : '#fff',

           'accent' : '#1ed9aa',
           'accent-focus' : '#02b185',
           'accent-content' : '#ffffff',

           'neutral' : '#262626',
           'neutral-focus' : '#3d3d3d',
           'neutral-content' : '#ffffff',

           'base-100' : '#FAFAFA',
           'base-200' : '#F2F0F1',
           'base-300' : '#E4DDE0',
           'base-content' : '#1e2734',

           'info' : '#1c92f2',
           'success' : '#009485',
           'warning' : '#ff9900',
           'error' : '#f41f43',

          '--rounded-box': '1rem',          
          '--rounded-btn': '.5rem',        
          '--rounded-badge': '.5rem',      

          '--animation-btn': '.25s',       
          '--animation-input': '.2s',       

          '--btn-text-case': 'capitalize',   
          '--navbar-padding': '.5rem',      
          '--border-btn': '1px',            
        },
      },
    ],
  },
}

