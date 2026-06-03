import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Mobile App Development — Globotech Solutions',
  description: 'Globotech Solutions builds iOS and Android apps with React Native and Flutter. Full-cycle mobile development — from UX design to App Store launch — for startups and enterprises in the USA.',
  alternates: { canonical: 'https://www.globotechsolutions.com/mobile-app' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Mobile App Development — Globotech Solutions',
    description: 'iOS and Android apps with React Native and Flutter. Full-cycle mobile development from UX design to App Store launch.',
    url: 'https://www.globotechsolutions.com/mobile-app',
    images: [{ url: 'https://www.globotechsolutions.com/og-mobile.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mobile App Development — Globotech Solutions',
    description: 'iOS and Android apps with React Native and Flutter. Full-cycle mobile app development in the USA.',
    images: ['https://www.globotechsolutions.com/og-mobile.jpg'],
  },
};

export default function MobileAppPage() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/mobile-app/mobile-app.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
