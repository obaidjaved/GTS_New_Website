'use client';

import { useEffect } from 'react';

interface ClientPageProps {
  body: string;
  styles: string;
  scripts: string;
  title: string;
  jsonLd?: string[];
}

export default function ClientPage({ body, styles, scripts, title, jsonLd }: ClientPageProps) {
  useEffect(() => {
    if (title) {
      document.title = title;
    }
  }, [title]);

  useEffect(() => {
    if (!jsonLd || jsonLd.length === 0) return;
    const injected: HTMLScriptElement[] = [];
    jsonLd.forEach((json, i) => {
      const existing = document.getElementById(`page-jsonld-${i}`);
      if (existing) existing.remove();
      const el = document.createElement('script');
      el.id = `page-jsonld-${i}`;
      el.type = 'application/ld+json';
      el.textContent = json;
      document.head.appendChild(el);
      injected.push(el);
    });
    return () => { injected.forEach(el => el.remove()); };
  }, [jsonLd]);

  useEffect(() => {
    if (!scripts) return;

    // Use a small timeout to ensure React has fully rendered and flushed the HTML content to the DOM
    const timer = setTimeout(() => {
      try {
        // Clean up any previously existing script element to prevent duplication
        const existingScript = document.getElementById('page-inline-script');
        if (existingScript) {
          existingScript.remove();
        }

        const scriptEl = document.createElement('script');
        scriptEl.id = 'page-inline-script';
        scriptEl.textContent = scripts;
        document.body.appendChild(scriptEl);
      } catch (err) {
        console.error('Error executing page inline script:', err);
      }
    }, 100);

    return () => {
      clearTimeout(timer);
      const scriptEl = document.getElementById('page-inline-script');
      if (scriptEl) {
        scriptEl.remove();
      }
    };
  }, [scripts]);

  return (
    <>
      <style dangerouslySetInnerHTML={{ __html: styles }} suppressHydrationWarning />
      <div dangerouslySetInnerHTML={{ __html: body }} suppressHydrationWarning />
    </>
  );
}
