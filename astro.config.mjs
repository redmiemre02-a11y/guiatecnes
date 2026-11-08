import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import AstroPWA from '@vite-pwa/astro';

export default defineConfig({
  site: 'https://guiatecnes.com',
  integrations: [
    sitemap({
      serialize(item) {
        item.lastmod = new Date();
        if (item.url === 'https://guiatecnes.com/' || item.url.includes('/herramientas/')) {
          item.priority = 1.0;
          item.changefreq = 'daily';
        } else if (item.url.includes('/blog/')) {
          item.priority = 0.8;
          item.changefreq = 'weekly';
        } else {
          item.priority = 0.5;
          item.changefreq = 'monthly';
        }
        return item;
      }
    }),
    AstroPWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'GuíaTecnes - Blog de Tecnología e IA',
        short_name: 'GuíaTecnes',
        description: 'Tu guía de herramientas digitales e IA en español',
        theme_color: '#0f172a',
        background_color: '#0f172a',
        display: 'standalone',
        icons: [
          {
            src: '/icon.svg',
            sizes: '192x192 512x512',
            type: 'image/svg+xml'
          }
        ]
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,svg,png,jpg,jpeg,gif,webp,woff,woff2}']
      }
    })
  ],
});
