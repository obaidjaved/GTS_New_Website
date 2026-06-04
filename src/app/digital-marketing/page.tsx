import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function DigitalMarketingPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/digital-marketing/digital-marketing.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
