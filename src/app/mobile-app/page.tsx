import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function MobileAppPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/mobile-app/mobile-app.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
