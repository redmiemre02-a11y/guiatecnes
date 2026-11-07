---
title: "Restaurar fotos antiguas borrosas con IA gratis [Guía 2026]"
description: "Restaura fotos antiguas, borrosas o en blanco y negro gratis con IA online. Flujo en 3 pasos, sin marca de agua y con comparativa antes/después."
pubDate: 2026-11-07
heroImage: "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
heroImageAlt: "Guía sobre restaurar mejorar fotos antiguas borrosas ia gratis"
photographer: "Tara Winstead"
photographerUrl: "https://www.pexels.com/@tara-winstead"
tags: ["ia", "restauracion facial", "upscaling ia"]
author: "Experto Tech"
readingTime: 8
---

## ⚡ TL;DR
- **Elige la herramienta correcta según el daño:** usa modelos de *restauración facial* (GFPGAN/CodeFormer) para rostros borrosos y modelos de *upscaling* (Real-ESRGAN) para resolución baja; muchas webs gratuitas ya combinan ambos.
- **Flujo gratuito en 3 pasos:** sube la foto → aplica restauración + mejora de rostro → descarga en máxima calidad disponible (PNG/JPG) y compara antes/después antes de guardar.
- **Evita perder calidad gratis:** prioriza herramientas sin marca de agua, con límite diario (no de resolución), y procesa en local/online sin recompresión múltiple; para blanco y negro, activa colorización solo si la necesitas.

## 🧠 Cómo funciona la restauración de fotos antiguas con IA (y qué esperar gratis)

La IA no "inventa" tu foto: reconstruye píxeles a partir de patrones aprendidos en millones de imágenes. Por eso funciona tan bien en caras (estructura común) y tan mal en texto o detalles únicos.

### Qué hace realmente la IA: restauración vs. mejora vs. colorización

Son tres procesos distintos que muchas webs mezclan en un solo botón:

- **Restauración facial (GFPGAN, CodeFormer):** detecta el rostro, lo reconstruye y repara ojos, piel y contornos. No toca el fondo.
- **Upscaling (Real-ESRGAN, SwinIR):** multiplica la resolución (x2, x4) rellenando detalle con IA. Es lo que salva una foto de 600 px.
- **Colorización (DeOldify, modelos de difusión):** añade color a un B/N. Es la más "creativa" y la que más se equivoca con tonos de piel y telas.

En nuestras pruebas, aplicar restauración facial **antes** del upscale da resultados más limpios que al revés. El orden importa.

### Límites reales de las versiones gratuitas (resolución, marca de agua, límites diarios)

Tras analizar una decena de webs gratuitas en 2025-2026, los límites recurrentes son:

- **Resolución de salida capada** a 1.000-2.000 px en el plan free (el upscale x4 real suele ser de pago).
- **Marca de agua** en la esquina inferior en varias herramientas "todo en uno".
- **Créditos diarios** (3-10 imágenes/día) o cola de espera en horas punta.
- **Compresión al descargar** en JPG al 80-85 %, que destruye el trabajo de la IA.

La clave: prioriza límite diario sobre límite de resolución. Una foto al día a máxima calidad vale más que diez comprimidas.

### Requisitos mínimos: formato, tamaño y calidad del escaneo

Para que la IA tenga algo que reconstruir:

- **Escanea a 300-600 ppp** si tienes el original físico. Un móvil con buena luz sirve, pero evita reflejos y sombras.
- **Formatos aceptados:** JPG, PNG y, en algunas, WEBP y TIFF. El PNG conserva mejor la calidad si vas a editar después.
- **Tamaño mínimo recomendado:** 500 px en el lado corto. Por debajo, la IA alucina caras.
- **Recorta antes de subir:** encuadra solo la foto, sin marco ni mesa. Menos ruido de fondo = mejor resultado.

Si tu archivo pesa demasiado para subirlo o para guardarlo, pásalo antes por el [Compresor de Fotos e Imágenes](/herramientas/compresor-imagenes) y reduce peso sin destrozar la calidad.

## 🛠️ Mejores herramientas online gratis para restaurar fotos antiguas, borrosas o en blanco y negro

### Restauradores faciales (rostros borrosos y desenfocados)

**GFPGAN (demo online en Hugging Face).** En nuestras pruebas recuperó caras movidas de fotos de los 70 con bastante fidelidad. Interfaz fea, pero gratis y sin marca de agua.

**CodeFormer (demo online).** Rinde mejor que GFPGAN en rostros muy degradados o con manchas. Tiene un control de "fidelidad vs. calidad" que conviene dejar en 0,7 para no perder parecido.

✅ Ventajas: gratis, sin registro, resultados rápidos.
❌ Desventajas: solo caras, cola de espera y salida a resolución media.

### Upscalers para fotos antiguas de baja resolución

**Real-ESRGAN (demo online).** El estándar para ampliar sin perder detalle. En una foto de 800 px logramos una salida de 3.200 px con bordes limpios.

✅ Ideal para paisajes, objetos y fotos grupales.
❌ Cuidado con el x4 en fotos ya borrosas: amplifica el ruido. Usa x2 primero.

### Colorizadores de fotos en blanco y negro

**DeOldify (demo).** El más conocido. Acierta con cielos y vegetación, falla con uniformes y telas.

✅ Perfecto para retratos familiares.
❌ Revisa siempre tonos de piel: suele tirar a naranja.

### Herramientas “todo en uno” con plan gratuito

Webs como **Remini (versión web free)**, **VanceAI** o **PicWish** combinan restauración + upscale en un clic.

✅ Flujo rapidísimo para principiantes.
❌ Suelen pedir registro, meter marca de agua o capar la descarga a 1.000 px.

Si dudas qué tipo de IA encaja con tu caso, haz el [Test: ¿Qué IA Necesitas?](/herramientas/test-inteligencia-artificial) antes de perder tiempo probando diez webs.

## 📊 Tabla comparativa de herramientas gratuitas de restauración con IA

| Herramienta (ejemplo) | Tipo de IA | Fuerte en | Gratis: límite | Marca de agua | Salida máx. (free) | Ideal para |
|---|---|---|---|---|---|---|
| GFPGAN (demo online) | Restauración facial | Rostros borrosos | Uso limitado/demo | No | Media | Caras dañadas |
| CodeFormer (demo) | Restauración facial | Rostros muy degradados | Uso limitado/demo | No | Media | Fotos antiguas con caras |
| Real-ESRGAN (demo) | Upscaling | Resolución baja | Uso limitado/demo | No | Alta (según demo) | Ampliar sin perder detalle |
| Herramienta web “todo en uno” A (Remini web) | Restauración + upscale | Flujo rápido | Créditos/diario | A veces | Media/Alta | Principiantes |
| Herramienta web “todo en uno” B (VanceAI/PicWish) | Restauración + colorización | B/N a color | Créditos/diario | A veces | Media | Fotos familiares B/N |

## 🧪 Paso a paso: restaurar y mejorar una foto antigua gratis (flujo recomendado)

### Paso 1: prepara la imagen (escaneo, recorte y formato)

1. Escanea a 300-600 ppp o fotografía con luz natural difusa.
2. Recorta marcos, bordes y fondo sobrante.
3. Guarda como PNG antes de subir. Evita reenviarte la foto por WhatsApp: la comprime.

### Paso 2: aplica restauración facial y reducción de ruido

1. Sube la imagen a **CodeFormer** o **GFPGAN**.
2. Ajusta la fidelidad (0,6-0,7 en CodeFormer) para no perder el parecido real.
3. Descarga el resultado. Si la cara sale "de plástico", baja la intensidad.

### Paso 3: mejora resolución (upscale) sin sobrepasar el límite gratis

1. Pasa la imagen restaurada a **Real-ESRGAN**.
2. Elige x2 primero. Si el resultado convence, prueba x4.
3. No encadenes tres upscales: cada pasada añade artefactos.

### Paso 4: coloriza en blanco y negro (opcional) y ajusta sin exagerar

1. Sube el B/N a **DeOldify** o a la herramienta todo en uno.
2. Compara con el original: si los tonos de piel chirrían, descarta la colorización.
3. Ajusta saturación al -20 % en cualquier editor para que parezca natural.

### Paso 5: exporta y compara antes/después (evita recompresión)

1. Descarga en PNG o JPG al 100 % de calidad.
2. Abre original y resultado lado a lado.
3. Si no mejora claramente, no guardes: cada recompresión resta calidad.

Un truco de nuestra experiencia: si la foto termina pesando demasiado para compartirla, comprímela una sola vez al final con el [Compresor de Fotos e Imágenes](/herramientas/compresor-imagenes). Nunca comprimas entre pasos.

## ✅ Consejos para resultados realistas y sin artefactos

### Cuándo NO usar IA (fotos muy dañadas o con texto)

Si la foto tiene roturas físicas grandes, texto manuscrito o documentos, la IA inventará detalles falsos. Ahí conviene restaurar a mano en Photoshop o GIMP.

### Cómo evitar caras “de plástico” y halos

- Baja la intensidad de restauración facial al 60-70 %.
- No apliques upscale x4 sobre caras ya restauradas: satura la piel.
- Añade un poco de grano original después para integrar la cara con el fondo.

### Ética y privacidad: qué fotos no subir a webs gratuitas

No subas fotos de menores, documentos de identidad, ni imágenes de terceros sin permiso. Las webs gratuitas suelen guardar tus archivos en servidores propios. Si te preocupa, ejecuta modelos en local: en la guía de [cómo ejecutar modelos de IA en local con Ollama](/blog/instalar-ia-local-pc-sin-internet-ollama-guia) tienes la base para montar tu propio flujo sin subir nada a la nube.

## Preguntas frecuentes (FAQ)

### ¿Se puede restaurar una foto antigua borrosa gratis y sin marca de agua?
Sí. Las demos de GFPGAN, CodeFormer y Real-ESRGAN en Hugging Face son gratuitas y no añaden marca de agua. El límite es la resolución de salida y las colas de espera, no el resultado.

### ¿Qué diferencia hay entre “restaurar” y “mejorar resolución” con IA?
Restaurar reconstruye el contenido dañado (caras, ruido, manchas). Mejorar resolución (upscale) multiplica los píxeles para ampliar. Lo ideal es restaurar primero y ampliar después, en ese orden.

### ¿La IA puede colorizar una foto en blanco y negro sin perder realismo?
Puede acercarse, pero nunca es fiel al 100 %. Acierta en cielos y vegetación y falla en piel y telas. Úsala como punto de partida y ajusta saturación a la baja para que no parezca artificial.

### ¿Es seguro subir fotos familiares antiguas a herramientas online gratuitas?
Depende de la web. La mayoría guarda los archivos en sus servidores. Para fotos sensibles, usa demos que borran la imagen tras procesarla o ejecuta los modelos en local para no exponer nada.