import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function BlogPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/Blog/blog.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
