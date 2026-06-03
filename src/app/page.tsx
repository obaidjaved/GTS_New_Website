import { parseHtmlFile } from './parseHtml';
import ClientPage from './ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Globotech Solutions — AI Development Agency',
  description: 'Globotech Solutions builds AI systems, web apps, mobile apps, and e-commerce storefronts that drive measurable business growth. Custom software development agency based in the USA.',
  alternates: { canonical: 'https://www.globotechsolutions.com/' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Globotech Solutions — AI Development Agency',
    description: 'Custom AI systems, web apps, mobile apps, and e-commerce storefronts that drive measurable business growth. USA-based software development agency.',
    url: 'https://www.globotechsolutions.com/',
    images: [{ url: 'https://www.globotechsolutions.com/og-home.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Globotech Solutions — AI Development Agency',
    description: 'Custom AI systems, web apps, mobile apps, and e-commerce storefronts. USA-based software development agency.',
    images: ['https://www.globotechsolutions.com/og-home.jpg'],
  },
};

export default function Home() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/Home/homepage.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
