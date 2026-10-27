import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const blog = await getCollection('blog');
  const sortedPosts = blog.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());

  return rss({
    title: 'GuíaTecnes - Tecnología, IA y Solución de Errores',
    description: 'Tu portal de referencia en español para herramientas de inteligencia artificial, solución de fallos técnicos, guías paso a paso y comparativas.',
    site: context.site || 'https://guiatecnes.com',
    items: sortedPosts.map((post) => ({
      title: post.data.title,
      description: post.data.description,
      pubDate: post.data.pubDate,
      link: `/blog/${post.id.replace(/\.[^/.]+$/, '')}/`,
      categories: post.data.tags,
      author: post.data.author || 'Experto Tech',
    })),
    customData: `<language>es-ES</language><copyright>© 2026 GuíaTecnes. Todos los derechos reservados.</copyright>`,
  });
}
