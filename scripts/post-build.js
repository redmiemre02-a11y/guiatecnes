import fs from 'fs';
import path from 'path';

const distDir = path.resolve('dist');

// 1. Ensure sitemap.xml exists by copying sitemap-index.xml (or sitemap-0.xml)
const sitemapIndex = path.join(distDir, 'sitemap-index.xml');
const sitemapTarget = path.join(distDir, 'sitemap.xml');

if (fs.existsSync(sitemapIndex)) {
  fs.copyFileSync(sitemapIndex, sitemapTarget);
  console.log('✅ Created dist/sitemap.xml from sitemap-index.xml');
} else {
  const sitemapZero = path.join(distDir, 'sitemap-0.xml');
  if (fs.existsSync(sitemapZero)) {
    fs.copyFileSync(sitemapZero, sitemapTarget);
    console.log('✅ Created dist/sitemap.xml from sitemap-0.xml');
  }
}

// 2. Create Cloudflare Pages _redirects file
const redirectsFile = path.join(distDir, '_redirects');
const redirectsContent = `# Cloudflare Pages Redirects
/sitemap.xml /sitemap-index.xml 200
`;
fs.writeFileSync(redirectsFile, redirectsContent, 'utf-8');
console.log('✅ Created dist/_redirects for Cloudflare Pages');
