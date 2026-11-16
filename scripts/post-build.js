import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');
const distDir = path.join(projectRoot, 'dist');
const blogDir = path.join(projectRoot, 'src', 'content', 'blog');

// 1. Collect publication / updated dates for all blog posts
const datesMap = new Map();
if (fs.existsSync(blogDir)) {
  const files = fs.readdirSync(blogDir).filter(f => f.endsWith('.md') || f.endsWith('.mdx'));
  for (const f of files) {
    const slug = f.replace(/\.[^/.]+$/, '');
    const content = fs.readFileSync(path.join(blogDir, f), 'utf-8');
    const pubMatch = content.match(/pubDate:\s*['"]?([^\n'"]+)/);
    const updMatch = content.match(/updatedDate:\s*['"]?([^\n'"]+)/);
    const dateStr = updMatch ? updMatch[1] : (pubMatch ? pubMatch[1] : null);
    if (dateStr) {
      try {
        const d = new Date(dateStr.trim());
        if (!isNaN(d.getTime())) {
          datesMap.set(slug, d.toISOString());
        }
      } catch (e) {}
    }
  }
}
console.log(`Loaded ${datesMap.size} blog post dates for sitemap`);

// 2. Identify the urlset file: sitemap-0.xml or sitemap.xml
const sitemapZero = path.join(distDir, 'sitemap-0.xml');
const sitemapIndex = path.join(distDir, 'sitemap-index.xml');
const sitemapTarget = path.join(distDir, 'sitemap.xml');

let sourceXml = null;
if (fs.existsSync(sitemapZero)) {
  sourceXml = fs.readFileSync(sitemapZero, 'utf-8');
} else if (fs.existsSync(sitemapTarget)) {
  const content = fs.readFileSync(sitemapTarget, 'utf-8');
  if (content.includes('<urlset')) {
    sourceXml = content;
  }
}

if (sourceXml && sourceXml.includes('<urlset')) {
  // Update lastmod for blog posts with their actual date
  let updatedXml = sourceXml.replace(/<url>(.*?)<\/url>/gs, (match, inner) => {
    const locMatch = inner.match(/<loc>(.*?)<\/loc>/);
    if (!locMatch) return match;
    const url = locMatch[1];
    
    // Check if it's a blog post
    const blogMatch = url.match(/\/blog\/([^/]+)\/?$/);
    if (blogMatch) {
      const slug = blogMatch[1];
      const realDate = datesMap.get(slug);
      if (realDate) {
        if (inner.includes('<lastmod>')) {
          return match.replace(/<lastmod>.*?<\/lastmod>/, `<lastmod>${realDate}</lastmod>`);
        } else {
          return match.replace('</loc>', `</loc><lastmod>${realDate}</lastmod>`);
        }
      }
    } else if (url === 'https://guiatecnes.com/' || url.includes('/herramientas/') || url.endsWith('/blog/') || url.endsWith('/categoria/')) {
      const recentDate = new Date().toISOString();
      if (inner.includes('<lastmod>')) {
        return match.replace(/<lastmod>.*?<\/lastmod>/, `<lastmod>${recentDate}</lastmod>`);
      } else {
        return match.replace('</loc>', `</loc><lastmod>${recentDate}</lastmod>`);
      }
    }
    return match;
  });

  // Write single flat sitemap.xml
  fs.writeFileSync(sitemapTarget, updatedXml, 'utf-8');
  console.log('✅ Created dist/sitemap.xml as a SINGLE flat <urlset> with accurate lastmod dates');

  // Remove multi-sitemap files
  if (fs.existsSync(sitemapZero)) {
    fs.unlinkSync(sitemapZero);
    console.log('🗑️ Removed dist/sitemap-0.xml');
  }
  if (fs.existsSync(sitemapIndex)) {
    fs.unlinkSync(sitemapIndex);
    console.log('🗑️ Removed dist/sitemap-index.xml');
  }
} else {
  console.warn('⚠️ Could not find valid <urlset> in sitemap files');
}

// 3. Create Cloudflare Pages _redirects file
// Redirect any requests for sitemap-index.xml or sitemap-0.xml to sitemap.xml with 301
const redirectsFile = path.join(distDir, '_redirects');
const redirectsContent = `# Cloudflare Pages Redirects
/sitemap-index.xml /sitemap.xml 301
/sitemap-0.xml /sitemap.xml 301
`;
fs.writeFileSync(redirectsFile, redirectsContent, 'utf-8');
console.log('✅ Created dist/_redirects with 301 redirects to single sitemap.xml');
