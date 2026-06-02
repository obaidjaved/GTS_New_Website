import { parseHtmlFile } from '../parseHtml';
import ClientPage from '../ClientPage';

export default function ECommerceSolutionsPage() {
  const { body, styles, scripts, title } = parseHtmlFile('src/e-commerce-solutions/e-commerce-solutions.html');
  return <ClientPage body={body} styles={styles} scripts={scripts} title={title} />;
}
