---
title: "Cómo saber si tu móvil tiene virus o está intervenido: 7 señales reales y solución sin apps"
description: "Descubre cómo saber si tu móvil Android o iPhone tiene virus, spyware o está intervenido. Códigos secretos MMI, comprobación de batería y desinfección paso a paso sin descargar aplicaciones dudosas."
pubDate: 2026-11-16
updatedDate: 2026-11-16
heroImage: "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80"
heroImageAlt: "Pantalla de teléfono móvil con candado de seguridad y ciberseguridad"
tags: ["ciberseguridad", "errores", "movil", "guias"]
author: "Experto Tech"
readingTime: 7
---

## ⚡ En Resumen (TL;DR)

- **No instales "antivirus milagrosos"**: La inmensa mayoría de apps de limpieza en Play Store o App Store son publicidad agresiva o falso software de seguridad (scareware).
- **Las 3 alertas rojas**: Sobrecalentamiento en reposo, consumo desmedido de datos móviles en segundo plano y aparición de anuncios flotantes fuera del navegador.
- **Códigos MMI oficiales**: Marca `*#21#` y `*#62#` en la app de teléfono para verificar si tus llamadas o mensajes se están desviando en secreto a otro número.
- **Solución definitiva**: Revocar permisos de "Administrador de Dispositivos", limpiar perfiles de configuración en iOS y, en caso crítico, restablecer de fábrica.

---

La sensación de que alguien puede estar espiando tus conversaciones, leyendo tus chats de WhatsApp o robando tus claves bancarias a través del teléfono móvil es una de las mayores preocupaciones de los usuarios. En la red abunda la desinformación con titulares alarmistas que intentan convencerte de pagar por suscripciones innecesarias. 

En este análisis técnico comprobamos **cómo diagnosticar realmente la integridad de tu dispositivo (Android o iOS)** utilizando exclusivamente las herramientas nativas del sistema operativo.

---

## 1. Las 7 señales inequívocas de infección o intervención

Un troyano bancario, un keylogger o un spyware (como stalkerware) necesitan recursos de hardware para operar. Por muy sigiloso que sea el código malicioso, siempre deja huellas en el rendimiento:

### A. La batería se agota el doble de rápido sin uso intensivo
Si dejas el móvil con 80% al acostarte y despiertas con 20%, o notas la parte trasera tibia mientras está bloqueado sobre la mesa, hay procesos transmitiendo datos o minando en segundo plano.

### B. Consumo fantasma de datos móviles
Entra en **Ajustes > Red móvil / Datos móviles > Uso de datos**. Si ves aplicaciones desconocidas (a menudo con iconos genéricos como un engranaje o nombres como "System Service" o "Download Manager") consumiendo cientos de megabytes o gigabytes en segundo plano, investiga de inmediato.

### C. Anuncios pop-up que saltan en la pantalla de inicio
Si estás en el escritorio del móvil o usando WhatsApp y de repente se abre un anuncio a pantalla completa, tienes un **Adware**. Suele colarse a través de falsas apps de linterna, calculadoras gratuitas descargadas en APK o editores de fotos no verificados.

### D. La pantalla se enciende sola o parpadea en reposo
Los troyanos que intentan tomar capturas de pantalla o registrar toques automáticos suelen activar brevemente la retroiluminación del panel.

### E. Mensajes SMS enviados que tú no has escrito
Muchos troyanos SMS envían mensajes a números de tarificación adicional para vaciar el saldo prepago o inflar la factura telefónica mensual.

### F. Rendimiento extremadamente lento y reinicios espontáneos
El choque constante entre el sistema operativo y el software malicioso para acceder a permisos raíz suele provocar cierres forzados del sistema (*crash* del Kernel).

### G. Cambios inesperados en tu navegador
Si al abrir Chrome o Safari tu buscador predeterminado ha cambiado a motores extraños llenos de enlaces patrocinados, tu navegador ha sido secuestrado (*browser hijacker*).

---

## 2. Los códigos secretos de verificación de llamadas (Códigos MMI)

Existen códigos de red estandarizados por la GSMA que consultan directamente a la antena de tu operadora si existe algún desvío configurado en tu tarjeta SIM:

1. **`*#21#` + Tecla de llamada**: Comprueba si las llamadas de voz, datos o mensajes SMS se están reenviando de forma incondicional a otro terminal. En pantalla debe indicar *"No desviado"* o *"Desactivado"* en todos los apartados.
2. **`*#62#` + Tecla de llamada**: Muestra a qué número se desvían las llamadas cuando tienes el móvil apagado o fuera de cobertura. (Normalmente debe coincidir con el buzón de voz oficial de tu operadora: Vodafone, Movistar, Orange, etc. Si ves un número móvil privado desconocido, anótalo).
3. **`##002#` + Tecla de llamada**: Es el comando maestro de reseteo. Borra instantáneamente todos los desvíos de llamada activos en tu línea.

---

## 3. Comprobación en Android: La trampa de los Administradores de Dispositivo

Los virus más peligrosos en Android consiguen privilegios especiales para evitar que puedas desinstalarlos normalmente desde el menú de aplicaciones:

1. Ve a **Ajustes > Seguridad y Privacidad > Administradores de dispositivos** (en algunos móviles: *Aplicaciones > Acceso especial*).
2. Aquí solo deberían figurar servicios oficiales y confiables, como **Encontrar mi dispositivo** de Google o la app de tu smartwatch (Samsung SmartThings, etc.).
3. Si observas alguna aplicación con nombre sospechoso marcada con permisos de administrador:
   - Desmarca la casilla.
   - Entra en *Ajustes > Aplicaciones*.
   - Pulsa en la app y elige **Desinstalar**.

### Cómo iniciar en Modo Seguro para borrar virus resistentes
Si una app infectada bloquea la pantalla cada vez que intentas borrarla:
1. Mantén pulsado el botón físico de encendido.
2. Mantén pulsado el icono táctil de **Apagar** hasta que aparezca el mensaje *"Reiniciar en Modo Seguro"*.
3. En modo seguro, ninguna app de terceros se ejecuta al arrancar. Ve a Ajustes y elimina la aplicación conflictiva sin resistencia.

---

## 4. Comprobación en iPhone: Perfiles MDM no autorizados

Aunque iOS cuenta con un entorno aislado (Sandbox) muy robusto, los atacantes suelen engañar a usuarios instalando **Perfiles de Gestión Empresarial (MDM)** a través de Safari o falsas tiendas de apps:

1. Ve a **Ajustes > General > VPN y gestión de dispositivos**.
2. En un iPhone personal, esta sección debería estar **completamente vacía** (salvo que uses una VPN legítima que hayas instalado conscientemente).
3. Si aparece un perfil de gestión desconocido que no pertenece a tu empresa de trabajo ni a tu centro educativo:
   - Toca sobre él y pulsa **Eliminar perfil**.
   - Introduce tu código de desbloqueo para revocar su acceso.

---

## 5. Prevención: Blindando tu identidad digital

El 95% de las infecciones móviles no proceden de sofisticados ataques gubernamentales, sino de **contraseñas débiles reutilizadas** y enlaces de phishing recibidos por SMS o correo electrónico.

> 🔒 **Pon a prueba tu seguridad**: Comprueba si las claves que protegen tu cuenta de Google, Apple ID o WhatsApp son vulnerables con nuestro [Comprobador de Seguridad y Entropía de Contraseñas](/herramientas/comprobador-seguridad-contrasenas/). Es 100% privado y calcula la resistencia real frente a ataques por fuerza bruta.

### Reglas de oro para no volver a infectarte:
- **Descarga solo de fuentes oficiales**: Evita instalar archivos `.APK` descargados de canales de Telegram o foros dudosos.
- **Revisa los permisos de cámara y micrófono**: En Android e iOS, un punto verde en la esquina superior de la pantalla indica que un sensor está activo. Si ninguna app abierta lo justifica, revisa los permisos concedidos.
- **Mantén el software al día**: Las actualizaciones mensuales de seguridad corrigen vulnerabilidades de día cero (*Zero-Day*) antes de que los ciberdelincuentes puedan explotarlas.
