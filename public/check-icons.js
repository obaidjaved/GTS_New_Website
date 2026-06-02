const https = require('https');
const urls = {
  'Tailwind': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-plain.svg',
  'Laravel': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/laravel/laravel-plain.svg',
  'Django': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg',
  'FastAPI': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/fastapi.svg',
  'Shopify': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/shopify.svg',
  'Wix': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/wix.svg',
  'OpenCart': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/opencart.svg',
  'Supabase': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/supabase.svg',
  'React Native': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/react.svg',
  'Claude': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/claude.svg',
  'Gemini': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gemini.svg',
  'GitHub Actions': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/githubactions.svg',
  'Square': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/square.svg',
  'OAuth 2.0': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/oauth.svg',
  'SSL/TLS': 'https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/ssl.svg'
};
const keys = Object.keys(urls);
let pending = keys.length;
keys.forEach(key => {
  const url = urls[key];
  https.get(url, res => {
    console.log(key, res.statusCode, url);
    res.on('data', () => {});
    res.on('end', () => {
      if (--pending === 0) process.exit(0);
    });
  }).on('error', err => {
    console.error(key, 'ERROR', err.message, url);
    if (--pending === 0) process.exit(0);
  });
});
