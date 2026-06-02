const https = require('https');
const icons = ['openai', 'shopify', 'wordpress', 'amazonwebservices', 'anthropic', 'react', 'n8n', 'nextdotjs', 'supabase', 'tailwindcss'];
const colors = ['#10a37f', '#96bf48', '#21759b', '#ff9900', '#cc785c', '#61dafb', '#ef4444', '#555555', '#3ecf8e', '#38bdf8'];
const names = ['OpenAI', 'Shopify', 'WordPress', 'AWS', 'Claude AI', 'React Native', 'n8n', 'Next.js', 'Supabase', 'Tailwind CSS'];

async function fetchIcon(icon) {
  return new Promise(resolve => {
    https.get('https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/' + icon + '.svg', res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const match = data.match(/<path d="([^"]+)"/);
        resolve(match ? match[1] : '');
      });
    });
  });
}

(async () => {
  let html = '';
  for (let i=0; i<icons.length; i++) {
    const path = await fetchIcon(icons[i]);
    const bg = colors[i] + '20';
    const c = colors[i];
    html += `      <div class="mq-item"><div class="mq-icon" style="background:${c}20;"><svg width="14" height="14" viewBox="0 0 24 24" fill="${c}"><path d="${path}"/></svg></div>${names[i]}</div>\n`;
  }
  const fs = require('fs');
  fs.writeFileSync('icons.html', html);
  console.log('done');
})();
