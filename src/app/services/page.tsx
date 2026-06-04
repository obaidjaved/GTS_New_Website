import fs from 'fs';
import path from 'path';
import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function ServicesPage() {
  const parsed = parseHtmlFile('src/Services/services.html');

  // Read services.css to bundle it directly with the page, ensuring styling loads reliably
  const cssPath = path.join(process.cwd(), 'src/app/services.css');
  const servicesCss = fs.readFileSync(cssPath, 'utf-8');

  // Combine services.css styling with any inline styles in services.html
  const combinedStyles = servicesCss + '\n' + parsed.styles;

  return (
    <ClientPage
      body={parsed.body}
      styles={combinedStyles}
      scripts={parsed.scripts}
      title={parsed.title}
    />
  );
}
