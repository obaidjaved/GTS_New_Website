'use client';

import { useEffect } from 'react';

interface ClientPageProps {
  body: string;
  styles: string;
  scripts: string;
  title: string;
}

export default function ClientPage({ body, styles, scripts, title }: ClientPageProps) {
  useEffect(() => {
    if (title) {
      document.title = title;
    }
  }, [title]);

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
