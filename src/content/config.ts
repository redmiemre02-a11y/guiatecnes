import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    heroImageAlt: z.string().optional(),
    photographer: z.string().optional(),
    photographerUrl: z.string().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string().default('Experto Tech'),
    readingTime: z.number().optional(),
  }),
});

export const collections = { blog };
