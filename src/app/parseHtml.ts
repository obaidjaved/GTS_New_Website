import fs from 'fs';
import path from 'path';

export interface ParsedHtml {
  body: string;
  styles: string;
  scripts: string;
  title: string;
}

export function parseHtmlFile(relativeFilePath: string): ParsedHtml {
  const filePath = path.join(/*turbopackIgnore: true*/ process.cwd(), relativeFilePath);
  // Normalize all CRLF newlines to LF to prevent hydration mismatch errors in Next.js
  const html = fs.readFileSync(filePath, 'utf-8').replace(/\r\n/g, '\n');

  // Extract body content
  const bodyMatch = html.match(/<body[\s\S]*?>([\s\S]*?)<\/body>/i);
  let body = bodyMatch ? bodyMatch[1] : html;

  // Extract all inline style blocks
  const styleMatches = [...html.matchAll(/<style[\s\S]*?>([\s\S]*?)<\/style>/gi)];
  let styles = styleMatches.map(m => m[1]).join('\n');

  // Rewrite asset paths from relative (file-friendly) to absolute (Next.js public folder root)
  body = body.replace(/\.\.\/\.\.\/public\/assets\//g, '/assets/');
  styles = styles.replace(/\.\.\/\.\.\/public\/assets\//g, '/assets/');

  // Rewrite page link paths from relative HTML files to clean Next.js routes
  body = body.replace(/href="\.\.\/Home\/homepage\.html"/g, 'href="/"');
  body = body.replace(/href="homepage\.html"/g, 'href="/"');

  body = body.replace(/href="\.\.\/Home\/homepage\.html#cta"/g, 'href="/#cta"');
  body = body.replace(/href="\.\.\/Home\/homepage\.html#cases"/g, 'href="/#cases"');

  body = body.replace(/href="\.\.\/Services\/services\.html"/g, 'href="/services"');
  body = body.replace(/href="services\.html"/g, 'href="/services"');

  body = body.replace(/href="\.\.\/About\/aboutus\.html"/g, 'href="/about"');
  body = body.replace(/href="aboutus\.html"/g, 'href="/about"');

  body = body.replace(/href="\.\.\/Blog\/blog\.html"/g, 'href="/blog"');
  body = body.replace(/href="blog\.html"/g, 'href="/blog"');

  body = body.replace(/href="\.\.\/Contact\/contact\.html"/g, 'href="/contact-us"');
  body = body.replace(/href="contact\.html"/g, 'href="/contact-us"');

  body = body.replace(/href="\.\.\/Web-Dev\/web-development\.html"/g, 'href="/web-development"');
  body = body.replace(/href="web-development\.html"/g, 'href="/web-development"');

  body = body.replace(/href="\.\.\/mobile-app\/mobile-app\.html"/g, 'href="/mobile-app"');
  body = body.replace(/href="mobile-app\.html"/g, 'href="/mobile-app"');

  body = body.replace(/href="\.\.\/ai-solutions\/ai-solutions\.html"/g, 'href="/ai-solutions"');
  body = body.replace(/href="ai-solutions\.html"/g, 'href="/ai-solutions"');

  body = body.replace(/href="\.\.\/e-commerce-solutions\/e-commerce-solutions\.html"/g, 'href="/e-commerce-solutions"');
  body = body.replace(/href="e-commerce-solutions\.html"/g, 'href="/e-commerce-solutions"');

  body = body.replace(/href="\.\.\/digital-marketing\/digital-marketing\.html"/g, 'href="/digital-marketing"');
  body = body.replace(/href="digital-marketing\.html"/g, 'href="/digital-marketing"');

  // Extract all inline script blocks and wrap each in an IIFE scope with try-catch.
  // This prevents variable collision / "Identifier already declared" syntax errors.
  const scriptMatches = [...html.matchAll(/<script(?![^>]*src)[\s\S]*?>([\s\S]*?)<\/script>/gi)];
  const scripts = scriptMatches.map(m => `(function(){\ntry{\n${m[1]}\n}catch(e){console.error("Script error:", e);}\n})();`).join('\n');

  // Extract title
  const titleMatch = html.match(/<title>([\s\S]*?)<\/title>/i);
  const title = titleMatch ? titleMatch[1].trim() : '';

  return { body, styles, scripts, title };
}
