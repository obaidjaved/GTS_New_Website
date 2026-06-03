import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Web Development Services — Globotech Solutions',
  description: 'Globotech Solutions builds high-performance web apps with React, Next.js, and Node.js. Custom web development services for startups and enterprises in the USA — from MVP to production in weeks.',
  alternates: { canonical: 'https://www.globotechsolutions.com/web-development' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Web Development Services — Globotech Solutions',
    description: 'High-performance web apps with React, Next.js, and Node.js. Custom web development for startups and enterprises in the USA.',
    url: 'https://www.globotechsolutions.com/web-development',
    images: [{ url: 'https://www.globotechsolutions.com/og-web-dev.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Web Development Services — Globotech Solutions',
    description: 'High-performance web apps with React, Next.js, and Node.js. USA-based custom web development agency.',
    images: ['https://www.globotechsolutions.com/og-web-dev.jpg'],
  },
};

export default function WebDevelopmentPage() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/Web-Dev/web-development.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
