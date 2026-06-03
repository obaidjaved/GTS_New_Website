import fs from 'fs';
import path from 'path';
import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Globotech Solutions — Enterprise AI & Web Engineering Services',
  description: 'Explore Globotech Solutions\' full service catalogue — AI development, web apps, mobile apps, digital marketing, and e-commerce. USA-based engineering teams delivering measurable results.',
  alternates: { canonical: 'https://www.globotechsolutions.com/services' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Services — Enterprise AI & Web Engineering — Globotech Solutions',
    description: 'Full service catalogue — AI development, web apps, mobile apps, digital marketing, and e-commerce. USA-based engineering teams.',
    url: 'https://www.globotechsolutions.com/services',
    images: [{ url: 'https://www.globotechsolutions.com/og-services.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Services — Globotech Solutions',
    description: 'AI development, web apps, mobile apps, digital marketing, and e-commerce from a USA-based engineering team.',
    images: ['https://www.globotechsolutions.com/og-services.jpg'],
  },
};

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
      jsonLd={parsed.jsonLd}
    />
  );
}
