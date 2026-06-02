import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function WebDevelopmentPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/Web-Dev/web-development.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
