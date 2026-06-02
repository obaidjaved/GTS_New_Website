import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function AboutUsPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/About/aboutus.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
