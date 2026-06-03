import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Digital Marketing, SEO, & Conversion Rate Optimization — Globotech Solutions',
  description: 'Globotech Solutions delivers data-driven SEO, paid media, and conversion rate optimisation that grows organic traffic and revenue for businesses across the USA.',
  alternates: { canonical: 'https://www.globotechsolutions.com/digital-marketing' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Digital Marketing, SEO & CRO — Globotech Solutions',
    description: 'Data-driven SEO, paid media, and CRO that grows organic traffic and revenue for businesses across the USA.',
    url: 'https://www.globotechsolutions.com/digital-marketing',
    images: [{ url: 'https://www.globotechsolutions.com/og-marketing.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Digital Marketing, SEO & CRO — Globotech Solutions',
    description: 'Data-driven SEO, paid media, and CRO that grows organic traffic and revenue.',
    images: ['https://www.globotechsolutions.com/og-marketing.jpg'],
  },
};

export default function DigitalMarketingPage() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/digital-marketing/digital-marketing.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
