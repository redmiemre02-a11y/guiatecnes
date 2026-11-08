---
title: "Cómo ejecutar Inteligencia Artificial en local en tu PC sin tarjeta gráfica (Ollama y DeepSeek)"
description: "Aprende a instalar modelos de IA como DeepSeek y Llama 3 en tu ordenador de forma 100% gratuita, privada y sin tarjeta gráfica dedicada usando Ollama y cuantización CPU."
pubDate: "2026-11-08"
heroImage: "https://images.pexels.com/photos/8386440/pexels-photo-8386440.jpeg?auto=compress&cs=tinysrgb&w=1200"
heroImageAlt: "Concepto de inteligencia artificial y tecnología de computación moderna"
photographer: "Tara Winstead"
tags: ["Inteligencia Artificial", "Ollama", "DeepSeek", "Software Libre", "Tutoriales"]
author: "Experto Tech"
readingTime: 8
---

Muchos usuarios creen erróneamente que para ejecutar modelos de Inteligencia Artificial en su propio ordenador necesitan comprar una costosa tarjeta gráfica para videojuegos con 16 GB o 24 GB de memoria VRAM (como las NVIDIA RTX 4080 o 4090).

La realidad en 2026 es muy diferente: gracias a los avances en técnicas de **cuantización de pesos matemáticos (formato GGUF)** y a herramientas de código abierto como **Ollama**, hoy es totalmente posible ejecutar modelos punteros como **DeepSeek R1**, **Llama 3** o **Mistral** utilizando únicamente el procesador principal (CPU) y la memoria RAM estándar (8 GB o 16 GB) de cualquier ordenador portátil o sobremesa convencional.

Todo esto con una ventaja insustituible: **100% privacidad**. Tus documentos, códigos y preguntas jamás salen de tu disco duro ni viajan a servidores de OpenAI o Microsoft.

---

## Requisitos mínimos de hardware para correr IA en CPU

Para obtener una velocidad de respuesta fluida (entre 12 y 25 palabras por segundo):

| Componente | Requisito Mínimo (Modelos 1.5B - 3B) | Requisito Recomendado (Modelos 7B - 8B) |
| :--- | :--- | :--- |
| **Procesador (CPU)** | Intel Core i5 / AMD Ryzen 5 (últimos 5 años) | Intel Core i7 / Ryzen 7 o Apple Silicon (M1/M2/M3/M4) |
| **Memoria RAM** | 8 GB DDR4 / DDR5 | 16 GB DDR4 / DDR5 |
| **Almacenamiento** | 10 GB libres en disco SSD | 20 GB libres en disco SSD NVMe |
| **Tarjeta Gráfica (GPU)** | Ninguna (usa gráficos integrados Intel/AMD) | Opcional (si tienes una GPU modesta acelerará el proceso) |

> **Nota sobre el almacenamiento:** Es fundamental que el modelo esté instalado en una unidad de estado sólido (SSD) y no en un disco duro mecánico antiguo (HDD), para que la carga en memoria sea instantánea.

---

## Paso 1: Descargar e instalar Ollama

Ollama es el motor más ligero y eficiente del mundo para correr grandes modelos de lenguaje (LLMs):

1. Visita la página web oficial gratuita: `ollama.com`.
2. Descarga el instalador correspondiente a tu sistema: **Windows**, **macOS** o **Linux**.
3. Ejecuta el archivo descargado e instala la aplicación con las opciones por defecto.
4. Una vez completado, verás el icono de una simpática alpaca en tu barra de tareas de Windows, indicando que el servicio local está listo para recibir instrucciones.

---

## Paso 2: Elegir el modelo de IA adecuado para tu memoria RAM

Los modelos se identifican por sus "parámetros" (el número de conexiones neuronales calculadas). Cuantos más parámetros, más inteligente es el modelo pero más memoria RAM requiere:

### Si tienes 8 GB de RAM:
- **`deepseek-r1:1.5b`**: Modelo de razonamiento ultra rápido, ideal para resúmenes y preguntas directas.
- **`llama3.2:3b`**: Excelente comprensión del español y fluidez conversacional consumiendo menos de 3 GB de RAM.

### Si tienes 16 GB de RAM:
- **`deepseek-r1:8b`**: Razonamiento de nivel matemático avanzado y análisis de documentos extensos.
- **`mistral:7b`** o **`llama3.1:8b`**: La mejor combinación calidad-rendimiento para programar y redactar artículos técnicos.

---

## Paso 3: Descargar y chatear con el modelo desde la terminal

1. Abre la **Terminal de Windows** (PowerShell o CMD).
2. Para descargar y poner en marcha DeepSeek de razonamiento ligero, simplemente escribe este comando y pulsa **Enter**:
   ```bash
   ollama run deepseek-r1:1.5b
   ```
3. Ollama descargará automáticamente el archivo cuantizado (apenas 1.1 GB).
4. En cuestión de segundos verás el cursor parpadeando con el mensaje `>>> Send a message`.
5. Escribe cualquier pregunta en español:
   ```text
   >>> Escribe un contrato de confidencialidad simple entre dos empresas en España
   ```
6. El modelo generará el texto en tiempo real utilizando el 100% de la potencia de los núcleos de tu procesador.
7. Para salir de la conversación, escribe `/bye` y pulsa Enter.

---

## Paso 4 (Opcional): Añadir una interfaz gráfica visual idéntica a ChatGPT

Si no quieres interactuar por la consola de texto, puedes instalar una interfaz visual web limpia:

- **Chatbox AI** o **Page Assistant**: Aplicaciones gratuitas de escritorio que se conectan automáticamente a `http://localhost:11434` (el puerto local de Ollama) permitiéndote chatear con burbujas de colores, cargar archivos PDF y guardar conversaciones organizadas por carpetas.

---

## Preguntas Frecuentes (FAQ)

### ¿El uso de Ollama consume internet mientras estoy chateando?

**Respuesta**: No. Solo necesitas conexión a internet durante el minuto que dura la descarga inicial del modelo a tu disco duro. Una vez descargado, puedes desconectar el cable de red o apagar el Wi-Fi por completo; el modelo seguirá respondiendo a máxima velocidad sin emitir ni un solo paquete de datos al exterior.

### ¿Se calienta mucho el procesador de mi portátil al procesar respuestas?

**Respuesta**: Durante los segundos en que la IA está generando la respuesta, los núcleos de la CPU trabajarán al 70-90% de su capacidad y los ventiladores pueden acelerar temporalmente. Una vez termina de redactar el párrafo, el consumo cae de nuevo al 0%. Es un comportamiento completamente normal y seguro para el hardware.

### ¿Puedo utilizar Ollama para resumir documentos confidenciales de mi empresa?

**Respuesta**: Sí, es precisamente uno de sus casos de uso corporativos más valorados. Al ejecutarse en un entorno local aislado (on-premise), ningún tercero ni proveedor en la nube tiene acceso a tus datos financieros, códigos fuente o secretos industriales, cumpliendo al 100% con la normativa europea RGPD.
