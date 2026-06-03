import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Custom E-Commerce Storefronts & Integrations — Globotech Solutions',
  description: 'Globotech Solutions builds headless e-commerce storefronts on Shopify, Next.js Commerce, and WooCommerce. Custom payment, ERP, and inventory integrations for fast-growing brands in the USA.',
  alternates: { canonical: 'https://www.globotechsolutions.com/e-commerce-solutions' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'Custom E-Commerce Storefronts & Integrations — Globotech Solutions',
    description: 'Headless e-commerce storefronts on Shopify, Next.js Commerce, and WooCommerce with payment, ERP, and inventory integrations.',
    url: 'https://www.globotechsolutions.com/e-commerce-solutions',
    images: [{ url: 'https://www.globotechsolutions.com/og-ecommerce.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Custom E-Commerce Storefronts — Globotech Solutions',
    description: 'Headless e-commerce storefronts on Shopify, Next.js Commerce, and WooCommerce with full payment integrations.',
    images: ['https://www.globotechsolutions.com/og-ecommerce.jpg'],
  },
};

export default function ECommerceSolutionsPage() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/e-commerce-solutions/e-commerce-solutions.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
