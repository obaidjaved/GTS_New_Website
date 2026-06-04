import { parseHtmlFile } from './parseHtml';
import ClientPage from './ClientPage';

export default function Home() {
  const { body, styles, scripts, title } = parseHtmlFile('src/Home/homepage.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
