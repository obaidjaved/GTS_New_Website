import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function ContactPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/Contact/contact.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
