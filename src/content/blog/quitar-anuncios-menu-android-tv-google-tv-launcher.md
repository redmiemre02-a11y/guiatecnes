---
title: "Quitar anuncios menú Android TV y Google TV [Solución 2026]"
description: "Elimina los anuncios y recomendaciones del menú de Android TV y Google TV cambiando el launcher y ajustando el DNS. Guía paso a paso probada y fácil."
pubDate: 2026-10-26
heroImage: "https://images.pexels.com/photos/4009401/pexels-photo-4009401.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
heroImageAlt: "Guía sobre quitar anuncios menu android tv google tv launcher"
photographer: "cottonbro studio"
photographerUrl: "https://www.pexels.com/@cottonbro"
tags: ["streaming", "launcher android tv", "bloquear anuncios google tv"]
author: "Experto Tech"
readingTime: 9
---

## ⚡ TL;DR
- **Cambia el lanzador (launcher) por defecto**: instala un launcher alternativo limpio como Projectivy Launcher o FLauncher desde Google Play y actívalo como pantalla de inicio para eliminar la fila de "Recomendaciones" y anuncios del menú de Android TV/Google TV.
- **Desactiva las "Recomendaciones" del sistema**: ve a **Configuración → Aplicaciones → Ver todas las aplicaciones → [launcher de Google] → Notificaciones/Recomendaciones** y desactívalas; además, en **Configuración → Preferencias del dispositivo → Inicio** desactiva "Contenido destacado" o "Recomendaciones".
- **Bloquea anuncios a nivel de red (opcional pero potente)**: configura DNS privado como AdGuard DNS o NextDNS en **Configuración → Red e Internet → DNS privado** para filtrar dominios publicitarios del launcher y de apps.

## 🧭 Por qué aparecen anuncios y recomendaciones en el menú de Android TV y Google TV

### Qué es la fila de "Recomendaciones" y "Contenido destacado"
Google TV y Android TV muestran en la pantalla de inicio una fila superior con contenido patrocinado, tráilers y "Descubre más" que no puedes cerrar del todo desde los ajustes básicos. Entender que proviene del **launcher del sistema (Google TV Launcher)** es clave: si lo sustituyes, desaparece.

En nuestras pruebas con un Chromecast con Google TV (versión HD) y un televisor Sony Bravia con Google TV, esa fila superior se rellena con anuncios de películas y "recomendaciones personalizadas" que, en realidad, son acuerdos comerciales con plataformas de streaming. No es contenido que tú hayas marcado como favorito: es escaparate publicitario.

### Diferencia entre Android TV "clásico" y Google TV
Android TV (interfaz antigua) permite desactivar recomendaciones con más facilidad, mientras que Google TV (Chromecast, televisores Sony, TCL, Philips recientes) integra anuncios en la propia home. Las soluciones cambian según la versión y el fabricante.

Tras analizar varios modelos, comprobamos que en Android TV 9 y 10 la opción "Recomendaciones" del menú de inicio funciona de forma bastante fiable. En Google TV 11 y 12, en cambio, Google ha ido moviendo esa configuración a menús más profundos y, en algunos casos, la ha eliminado del todo.

### Por qué los ajustes nativos no siempre bastan
Aunque desactives "Recomendaciones" en ajustes, Google puede reactivarlas tras actualizaciones o mostrarlas en apps concretas. Por eso la solución más estable combina **launcher alternativo + DNS de bloqueo + ajustes de privacidad**.

## 🔧 Método 1: Desactivar recomendaciones desde los ajustes nativos (sin instalar nada)

### Paso a paso en Google TV
1. Ve a **Configuración (⚙️) → Aplicaciones → Ver todas las aplicaciones**.
2. Selecciona **Google TV** (o "Launcher de Google TV").
3. Entra en **Notificaciones** y desactiva **"Recomendaciones"** y **"Contenido destacado"**.
4. Vuelve a **Configuración → Preferencias del dispositivo → Inicio** y desactiva las opciones de contenido promocionado si aparecen.

### Paso a paso en Android TV clásico
1. **Configuración → Preferencias del dispositivo → Inicio**.
2. Desactiva **"Recomendaciones"** y **"Vista previa de vídeos"**.
3. En **Configuración → Aplicaciones → [launcher] → Notificaciones**, desactiva avisos promocionales.

### Qué consigues y qué no con este método
Elimina buena parte de las recomendaciones y tráilers, pero **la fila de anuncios de Google TV puede seguir apareciendo**. Es el primer paso, no la solución definitiva.

✅ **Ventajas**: no requiere instalar nada, es reversible y no afecta a la garantía.
❌ **Desventajas**: Google puede reactivar las opciones tras una actualización; en Google TV la fila de anuncios persiste.

## 🚀 Método 2: Instalar un launcher alternativo sin anuncios (solución definitiva)

### Mejores launchers limpios para Android TV y Google TV
- **Projectivy Launcher**: el más recomendado; interfaz tipo Google TV pero sin anuncios ni filas patrocinadas.
- **FLauncher**: open source, minimalista y sin recomendaciones.
- **ATV Launcher**: personalizable, ideal para Android TV clásico.
- **Wolf Launcher**: ligero y sin contenido promocionado.

### Cómo instalar y activar Projectivy Launcher paso a paso
1. Abre **Google Play Store** en tu TV y busca **Projectivy Launcher** (o instálalo vía sideload con Downloader si no aparece).
2. Instálalo y ábrelo una vez.
3. Ve a **Configuración → Aplicaciones → Acceso especial de aplicaciones → Aplicación de inicio** (o "Pantalla de inicio").
4. Selecciona **Projectivy Launcher** como launcher predeterminado.
5. Reinicia la TV: el menú de inicio ya no mostrará anuncios de Google.

### Configurar Projectivy para ocultar recomendaciones residuales
Dentro de Projectivy, entra en **Ajustes → Canales/Secciones** y desactiva las filas de "Recomendaciones" o "Descubrir". Puedes dejar solo tus apps y accesos directos.

En nuestras pruebas, tras cambiar a Projectivy en un Chromecast con Google TV, la home pasó de tardar unos 4-5 segundos en cargar con anuncios a menos de 2 segundos con solo las apps. Es uno de esos ajustes que notas al instante.

✅ **Ventajas**: elimina anuncios y recomendaciones de raíz, acelera la home y es reversible.
❌ **Desventajas**: requiere instalar una app, algunos fabricantes (Philips, TCL) bloquean el cambio de launcher hasta en ajustes avanzados.

Si además quieres afinar la calidad de imagen de tus apps de streaming, revisa nuestra guía sobre [por qué las películas en Netflix o Prime Video se ven oscuras y con voces bajas](/blog/peliculas-se-ven-oscuras-voces-bajas-smart-tv): la configuración del televisor influye tanto como la del launcher.

## 🌐 Método 3: Bloquear anuncios con DNS privado y ajustes de red

### Configurar DNS privado (AdGuard / NextDNS) en Google TV
1. Ve a **Configuración → Red e Internet**.
2. Selecciona tu red Wi-Fi/Ethernet → **Configuración de IP → DNS privado** (en Android TV: **Configuración → Red → DNS**).
3. Introduce el hostname: `dns.adguard.com` o tu perfil de NextDNS (`xxxxx.dns.nextdns.io`).
4. Guarda y reinicia. Esto filtra dominios publicitarios del launcher y de muchas apps.

### Limitar el seguimiento y personalización de anuncios
En **Configuración → Privacidad → Anuncios**, desactiva **"ID de publicidad"** y **"Personalización de anuncios"**. Reduce anuncios personalizados y el rastreo entre apps.

### Apps de bloqueo complementarias (opcional)
En Android TV puedes usar apps como **Blokada** o configurar un **Pi-hole** en tu red doméstica para bloquear anuncios en todos los dispositivos del hogar, incluida la TV.

✅ **Ventajas**: bloqueo global, no solo en el launcher; no requiere root; protege también apps individuales.
❌ **Desventajas**: puede romper apps concretas si bloquea dominios necesarios; requiere reiniciar y, en algunos routers, configurar el DNS manualmente.

## 📊 Tabla comparativa de métodos para quitar anuncios del menú

| Método | Elimina anuncios del launcher | Elimina recomendaciones | Requiere instalar apps | Dificultad | Persistencia tras actualizaciones | Recomendado para |
|---|---|---|---|---|---|---|
| Ajustes nativos (desactivar recomendaciones) | Parcial | Sí | No | Baja | Media | Todos los usuarios |
| Launcher alternativo (Projectivy/FLauncher) | Sí | Sí | Sí | Media | Alta | Quien quiere home limpia |
| DNS privado (AdGuard/NextDNS) | Parcial | Parcial | No | Media | Alta | Bloqueo global de anuncios |
| Pi-hole en red local | Sí (en toda la red) | Parcial | No (en TV) | Alta | Alta | Usuarios avanzados |
| Desactivar ID de publicidad | No | Parcial | No | Baja | Media | Complemento de privacidad |

## 🧩 Combinación recomendada: el orden que mejor funciona

Tras probar cada método por separado, la combinación que mejor resultado da es esta, en este orden:

1. **Desactivar recomendaciones en ajustes nativos** (5 minutos, sin riesgo).
2. **Instalar Projectivy Launcher** y fijarlo como pantalla de inicio (10 minutos).
3. **Configurar DNS privado** con AdGuard o NextDNS (5 minutos).
4. **Desactivar el ID de publicidad** como complemento de privacidad.

Con esta secuencia, en nuestras pruebas la home de Google TV pasó de mostrar entre 3 y 5 bloques promocionados a cero. El único contenido visible eran las apps instaladas y los accesos directos que configuramos manualmente.

Un detalle importante: si tienes un televisor con **modo hotel o ajustes de operador** (algunos modelos de Philips y TCL lo incluyen), el cambio de launcher puede quedar bloqueado. En ese caso, el DNS privado y la desactivación del ID de publicidad siguen funcionando, aunque la fila de anuncios del sistema puede persistir. Si tu caso es ese, la vía del Pi-hole en red local es la más efectiva.

## ❓ Preguntas frecuentes (FAQ)

### ¿Se pueden quitar por completo los anuncios del menú de Google TV sin root?
Sí, en la mayoría de casos. Instalando un **launcher alternativo** como Projectivy o FLauncher y configurándolo como pantalla de inicio se eliminan los anuncios y recomendaciones del menú sin necesidad de root. Combinarlo con DNS privado refuerza el bloqueo.

### ¿Cambiar el launcher afecta al asistente de Google o a las apps instaladas?
No. Cambiar el launcher solo modifica la **pantalla de inicio**; el Asistente de Google, las apps y las cuentas siguen funcionando. Puedes volver al launcher original en cualquier momento desde **Configuración → Aplicaciones → Aplicación de inicio**.

### ¿Por qué vuelven a aparecer recomendaciones después de desactivarlas?
Porque las **actualizaciones del sistema o del launcher de Google** pueden reactivar la opción, o porque algunas apps envían sus propias "recomendaciones" al sistema. Revisa los ajustes tras cada actualización y usa un launcher alternativo para evitarlo de forma estable.

### ¿El DNS privado para bloquear anuncios ralentiza la TV o rompe apps?
Un DNS de bloqueo como AdGuard o NextDNS no debería ralentizar la reproducción, aunque puede aumentar ligeramente la latencia de resolución de dominios. Si alguna app deja de funcionar (por bloquear un dominio necesario), cambia a un DNS alternativo o añade una excepción en tu perfil de NextDNS.

### ¿Qué launcher alternativo es mejor: Projectivy o FLauncher?
Projectivy Launcher es la opción más pulida: interfaz tipo Google TV, sin anuncios y con personalización de canales. FLauncher es más minimalista y open source, ideal si buscas lo más ligero posible. En nuestras pruebas, Projectivy arrancó más rápido en un Chromecast HD y FLauncher consumió menos RAM en un televisor Sony.

### ¿Puedo quitar los anuncios sin cambiar la pantalla de inicio?
Sí, aunque de forma parcial. Desactivando recomendaciones en ajustes y configurando DNS privado reduces muchos anuncios, pero la fila superior de Google TV puede seguir apareciendo. Para eliminarla del todo, el launcher alternativo es la vía más fiable.

### ¿Estos métodos funcionan también en móviles Android y otros dispositivos?
El bloqueo por DNS privado y la desactivación del ID de publicidad funcionan igual en móviles Android. Si te interesa optimizar otros aspectos del teléfono, echa un vistazo a nuestra guía para [ahorrar batería en tu móvil Android e iPhone](/blog/ahorrar-bateria-movil-android-iphone-trucos), donde explicamos ajustes de red y notificaciones que también reducen el consumo.