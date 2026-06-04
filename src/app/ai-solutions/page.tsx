import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function AiSolutionsPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/ai-solutions/ai-solutions.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
