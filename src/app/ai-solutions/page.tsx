import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'AI Solutions & Intelligent Automation — Globotech Solutions',
  description: 'Globotech Solutions builds custom AI systems — chatbots, RAG pipelines, workflow automation, and LLM integrations — that cut costs and accelerate growth for businesses in the USA.',
  alternates: { canonical: 'https://www.globotechsolutions.com/ai-solutions' },
  openGraph: {
    type: 'website',
    siteName: 'Globotech Solutions',
    title: 'AI Solutions & Intelligent Automation — Globotech Solutions',
    description: 'Custom AI systems — chatbots, RAG pipelines, workflow automation, and LLM integrations — that cut costs and accelerate growth.',
    url: 'https://www.globotechsolutions.com/ai-solutions',
    images: [{ url: 'https://www.globotechsolutions.com/og-ai.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'AI Solutions & Intelligent Automation — Globotech Solutions',
    description: 'Custom AI systems — chatbots, RAG pipelines, workflow automation, and LLM integrations.',
    images: ['https://www.globotechsolutions.com/og-ai.jpg'],
  },
};

export default function AiSolutionsPage() {
  const { body, styles, scripts, title, jsonLd } = parseHtmlFile('src/ai-solutions/ai-solutions.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} jsonLd={jsonLd} />;
}
