---
title: "Audio y vídeo desincronizados en Smart TV, PC o VLC: cómo calcular y ajustar el retraso en ms"
description: "¿El sonido va por detrás de las voces en tu Smart TV, barra de sonido o VLC? Aprende a calibrar el retraso de audio en milisegundos (ms) y resolver el desfase de inmediato."
pubDate: "2026-11-08"
heroImage: "https://images.pexels.com/photos/4009402/pexels-photo-4009402.jpeg?auto=compress&cs=tinysrgb&w=1200"
heroImageAlt: "Persona ajustando el sonido de un televisor inteligente con mando a distancia"
photographer: "Cottonbro Studio"
tags: ["Smart TV", "Audio", "Tutoriales", "VLC", "Streaming"]
author: "Experto Tech"
readingTime: 7
---

Pocas cosas resultan más frustrantes al disfrutar de una película o serie que notar que las bocas de los actores no coinciden con las palabras que escuchas: el temido efecto **lip-sync error** o desincronización de audio y vídeo. Este problema es especialmente habitual al conectar barras de sonido por Bluetooth o HDMI eARC, en aplicaciones de streaming como Netflix o HBO Max, y al reproducir archivos multimedia en VLC Media Player.

En esta guía paso a paso te explicamos por qué ocurre este desfase temporal, cómo calcular exactamente el retraso en milisegundos (ms) y los ajustes exactos que debes aplicar en tu televisor, receptor o reproductor multimedia.

> **Consejo visual:** Si estás configurando tu salón o espacio de cine en casa, te recomendamos revisar nuestra [Calculadora de Distancia y Tamaño de Pantalla de TV](/herramientas/calculadora-distancia-pantalla-tv) para garantizar una inmersión visual y acústica perfecta.

---

## ¿Por qué se desincronizan el audio y el vídeo?

La imagen y la pista de sonido viajan por canales de procesamiento distintos dentro de tus dispositivos electrónicos:

1. **Retardo por posprocesamiento de vídeo:** Las Smart TV modernas aplican algoritmos pesados de mejora de imagen (escalado 4K/8K, interpolación de movimiento MEMC, reducción de ruido digital). Todo este procesamiento toma entre **40 ms y 120 ms**. Si el audio no se retrasa deliberadamente en la misma medida, escucharás la voz antes de ver moverse los labios.
2. **Latencia Bluetooth:** El códec de audio estándar SBC introduce de **150 ms a 250 ms** de latencia. En este caso, el sonido llega bastante más tarde que el movimiento labial.
3. **Conversión de formatos multicanal (Dolby Atmos / DTS a PCM):** Si la tele intenta decodificar una pista compleja en tiempo real antes de enviarla a una barra de sonido básica por cable óptico (TOSLink), el cuello de botella provoca un desfase progresivo.

---

## Cómo calcular el retraso en milisegundos (ms)

Para ajustar el retardo sin volverte loco probando números al azar:

| Situación visual percibida | Causa habitual | Ajuste recomendado (ms) |
| :--- | :--- | :--- |
| **Escuchas la voz ANTES de que abra la boca** | La TV tarda en procesar el vídeo | Retrasar audio: **+40 ms a +100 ms** |
| **La voz se oye DESPUÉS de cerrarse la boca** | Latencia Bluetooth o receptor lento | Adelantar audio / Modo Juego: **-50 ms a -150 ms** |
| **El desfase crece a medida que avanza el vídeo** | Diferencia de fotogramas por segundo (23.976 fps vs 25 fps) | Re-sincronizar pista en VLC |

> **Prueba del aplauso:** Busca en YouTube el vídeo oficial *"Audio Video Sync Test 60fps"*. Observa el momento exacto en que la barra blanca golpea el marcador de cero con un sonido de "bip". Si el bip suena antes de tocar la línea, añade retardo al sonido; si suena después, reduce el retardo.

---

## Solución 1: Ajustar el desfase en VLC Media Player (PC y Mac)

VLC es el reproductor más versátil y cuenta con atajos de teclado instantáneos para corregir el desfase en tiempo real:

1. Mientras reproduces el vídeo, presiona la tecla **`J`** para adelantar el sonido (reducir retardo en bloques de 50 ms).
2. Presiona la tecla **`K`** para retrasar el sonido (añadir retardo en bloques de 50 ms).
3. Verás en la esquina superior derecha un mensaje flotante con el valor: ej. `Retraso de audio: 150 ms`.
4. Si necesitas guardarlo de forma fija para ese archivo, ve a **Herramientas > Efectos y filtros > Sincronización** y ajusta la *Sincronización de pistas de audio*.

---

## Solución 2: Calibración en Smart TV (Samsung, LG, Google TV)

Todos los sistemas operativos actuales cuentan con una función nativa de sincronización labial (*Audio Delay* o *Lip Sync*):

### En Smart TV Samsung (Tizen)
1. Abre el menú **Ajustes > Sonido > Ajustes para expertos**.
2. Selecciona **Retardo de audio digital (Audio Delay)**.
3. El valor viene por defecto en `100`. Si el audio va adelantado, súbelo a `140 - 180`. Si el audio va atrasado, bájalo hacia `0 - 50`.
4. Asegúrate de configurar la salida digital en **Paso a través (Pass-Through)** en lugar de Auto o PCM para que tu barra decodifique sin demoras.

### En Smart TV LG (webOS)
1. Pulsa el botón de engranaje y ve a **Todos los ajustes > Sonido > Ajustes avanzados**.
2. Entra en **Ajustar sincronización de audio (Match Screen and Sound)**.
3. Activa la opción y mueve la barra deslizante hacia la izquierda (adelantar) o hacia la derecha (retrasar) hasta calibrar la voz con la boca.
4. Si tienes una barra conectada por eARC, activa la opción **Bypass** (derivación sin procesar).

### En Google TV y Android TV (Sony, Philips, Xiaomi, TCL)
1. Ve a **Ajustes > Pantalla y sonido > Salida de audio**.
2. Busca la opción **A/V Sync** (Sincronización de audio y vídeo).
3. Cámbiala de *Desactivado* a *Activado* o *Automático*.

---

## Solución 3: Eliminar la latencia al usar auriculares Bluetooth

Si el desfase ocurre únicamente cuando escuchas con auriculares inalámbricos:

- **Activa el "Modo Juego" en tus auriculares:** La gran mayoría de marcas (Xiaomi, Soundcore, Razer, Realme) cuentan con un modo de baja latencia que reduce el buffer de 200 ms a tan solo 45-60 ms, haciendo el retraso imperceptible para el ojo humano.
- **Usa un transmisor Bluetooth con códec aptX Low Latency (aptX-LL):** Los televisores antiguos solo admiten SBC. Un pequeño adaptador conectado a la salida óptica o jack de 3.5 mm resolverá la latencia para siempre.

---

## Preguntas Frecuentes (FAQ)

### ¿Por qué el retardo de audio solo ocurre en Netflix pero no en YouTube?

**Respuesta**: Porque Netflix transmite pistas envolventes de alta compresión como Dolby Digital Plus 5.1 o Atmos, mientras que YouTube transmite en audio estéreo PCM simple de 2 canales. El procesador de tu TV tarda más milisegundos en decodificar el audio de 6 canales. Activar el modo "Pass-Through" en los ajustes de sonido de la TV soluciona este desfase en plataformas de streaming.

### ¿Qué conexión de barra de sonido tiene menos retraso: HDMI eARC u óptico?

**Respuesta**: HDMI eARC (Enhanced Audio Return Channel) es infinitamente superior al cable óptico clásico. El estándar eARC incluye un canal de datos dedicado que realiza sincronización labial automática (Auto Lip-Sync Correction) entre la pantalla y el receptor en tiempo real.

### ¿Poner la TV en Modo Juego soluciona el desfase de sonido?

**Respuesta**: Sí, en muchos casos. El Modo Juego desactiva los procesadores pesados de reducción de ruido y suavizado de movimiento de la pantalla, reduciendo el retardo de entrada (input lag) de 100 ms a menos de 10 ms, lo que hace que la imagen se muestre de inmediato sin desfasarse respecto al sonido.
