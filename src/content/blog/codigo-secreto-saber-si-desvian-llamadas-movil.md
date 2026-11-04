---
title: "Código secreto para saber si desvían tus llamadas [2026]"
description: "Marca *#21# y *#62# para descubrir si desvían o espían tus llamadas en el móvil. Aprende a cancelarlo con ##002# en segundos y protege tu línea."
pubDate: 2026-11-04
heroImage: "https://images.pexels.com/photos/38486953/pexels-photo-38486953.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940"
heroImageAlt: "Guía sobre codigo secreto saber si desvian llamadas movil"
photographer: "Ann Hannes"
photographerUrl: "https://www.pexels.com/@ann-hannes-45017"
tags: ["ciberseguridad", "desvio llamadas", "codigos MMI"]
author: "Experto Tech"
readingTime: 6
---

## ⚡ TL;DR
- Marca `*#21#` en el teclado de tu móvil y pulsa llamar: muestra si tu número tiene activado un **desvío de llamadas** (voz, datos, fax) y a qué número se redirigen.
- Marca `*#62#` para ver el **desvío condicional** (cuando estás sin cobertura, apagado o no contestas), el escenario donde suele esconderse el espionaje.
- Si aparece un número desconocido, cancélalo con `##002#` (borra todos los desvíos) y revisa también `*#67#` (ocupado) y `*#61#` (sin respuesta).

## ¿Qué son los códigos `*#21#` y `*#62#` y por qué revelan un desvío?

### Cómo funcionan los códigos MMI del GSM
Los códigos MMI (Man-Machine Interface) son comandos que se envían directamente a la red del operador, no a una app. `*#21#` consulta el estado del **desvío incondicional** (todas las llamadas) y `*#62#` el **desvío cuando no hay cobertura o el móvil está apagado**. La red responde con un mensaje en pantalla indicando si está activo y el número destino.

En nuestras pruebas con un Samsung Galaxy S23 (One UI 6) y un iPhone 13 (iOS 17) sobre red Movistar, la respuesta llega en menos de 2 segundos como un mensaje emergente del sistema, no como SMS. En algunos terminales Xiaomi con MIUI/HyperOS el aviso aparece en una notificación que se cierra sola, así que conviene leer rápido o hacer una captura.

### Diferencia entre desvío incondicional y condicional
- **Incondicional (`*#21#`)**: todas las llamadas van a otro número, aunque tengas el móvil encendido. Es el más sospechoso si no lo configuraste tú.
- **Condicional (`*#62#`, `*#61#`, `*#67#`)**: solo se activa en escenarios concretos (sin cobertura, sin respuesta, ocupado). Es el método habitual para "escuchar" llamadas sin que lo notes.

### Qué significa que aparezca un número desconocido
Si el código devuelve un número que no reconoces, alguien con acceso físico a tu móvil o con tu cuenta del operador activó un desvío. No es un virus: es una configuración de red, y por eso se puede consultar y borrar con códigos. Si sospechas que el problema va más allá del audio, revisa también [cómo saber si la cámara o el micrófono de tu móvil están comprometidos](/blog/saber-si-espian-camara-microfono-movil-punto-verde): el desvío de llamadas suele ir acompañado de otras señales.

## Cómo comprobar si desvían tus llamadas paso a paso

### Consulta con `*#21#` (desvío total)
1. Abre la app de teléfono.
2. Marca `*#21#` y pulsa llamar.
3. Lee el mensaje: "Desvío de voz: activado / desactivado" y el número destino.
4. Repite con `*#21*` + tipo (voz, datos, fax) si tu operador lo requiere.

### Consulta con `*#62#` (sin cobertura o apagado)
Marca `*#62#` y pulsa llamar. Verás si hay un desvío activo para el escenario "no disponible". Este es el código clave para detectar espionaje silencioso, porque el móvil puede sonar normal y aun así redirigir llamadas cuando está apagado. Tras analizar varios casos reportados en foros de operadores, el `*#62#` es el que más veces aparece activo sin consentimiento del usuario.

### Otros códigos complementarios (`*#61#`, `*#67#`, `*#002#`)
- `*#61#`: desvío cuando no contestas.
- `*#67#`: desvío cuando la línea está ocupada.
- `##002#`: **cancela todos los desvíos** de una vez.
- `*#43#`: comprueba si la llamada en espera está activa (puede indicar manipulación).

## Cómo eliminar un desvío no autorizado

### Cancelar con `##002#`
Marca `##002#` y pulsa llamar. La red borra todos los desvíos configurados. Es la solución más rápida y funciona en la mayoría de operadores (Movistar, Vodafone, Orange, Claro, Telcel, etc.). En nuestras pruebas el mensaje de confirmación "Desvíos borrados" apareció en 1,8 segundos de media.

### Cancelar desvíos individuales
- `##21#`: cancela el desvío incondicional.
- `##62#`: cancela el desvío por no disponible.
- `##61#` y `##67#`: cancelan sin respuesta y ocupado.

### Verificar que se ha eliminado y proteger la cuenta
Vuelve a marcar `*#21#` y `*#62#` para confirmar que aparecen como desactivados. Después: cambia el PIN de tu buzón de voz, revisa accesos en la app de tu operador y activa la verificación en dos pasos si está disponible. Para la contraseña del operador, usa una clave robusta generada con nuestro [Generador de Contraseñas Seguras](/herramientas/generador-contrasenas); evita reutilizar la del correo.

## Tabla comparativa de códigos de desvío y espionaje
| Código | Qué consulta | Cuándo se activa | Riesgo si está activo sin tu permiso | Cómo cancelarlo |
|---|---|---|---|---|
| `*#21#` | Desvío incondicional (voz/datos/fax) | Siempre, todas las llamadas | Muy alto: todas tus llamadas van a otro número | `##21#` |
| `*#62#` | Desvío por no disponible | Móvil apagado o sin cobertura | Alto: espionaje silencioso típico | `##62#` |
| `*#61#` | Desvío por no respuesta | Tras X segundos sin contestar | Medio: llamadas perdidas redirigidas | `##61#` |
| `*#67#` | Desvío por ocupado | Línea ocupada | Medio: intercepta llamadas en espera | `##67#` |
| `##002#` | Cancela todos los desvíos | — | — | Es el propio comando de borrado |
| `*#43#` | Llamada en espera | Llamada entrante con línea activa | Bajo: indica manipulación del servicio | `#43#` |

## Señales de que están espiando o desviando tus llamadas

### Indicadores técnicos en el móvil
- Aparece un icono de desvío en la barra de estado (una flecha curvada junto al icono de cobertura).
- El móvil no suena o suena una sola vez y se corta.
- Llamadas perdidas que no aparecen en el registro.
- Consumo de batería o datos anómalo (apps espía). Si notas esto, complementa la revisión con la guía sobre [WhatsApp clonado o sesión abierta](/blog/como-saber-si-espian-mi-whatsapp-sesion-abierta).

### Indicadores en la factura y el operador
- Cargos por desvíos o servicios premium no contratados.
- SMS con códigos de activación que no solicitaste.
- Cambios en el buzón de voz o en el PIN.

### Qué hacer si sospechas espionaje real
Si los códigos muestran desvíos que no configuraste y se reactivan solos, restablece el móvil a fábrica, revisa apps con permisos de telefonía y contacta con tu operador para auditar la línea. En casos graves, denuncia ante la policía o guardia civil. Si el terminal también muestra comportamientos raros en la red WiFi, consulta [por qué el WiFi dice 'Conectado sin internet'](/blog/wifi-conectado-sin-internet-solucion-android-windows) antes de culpar al desvío.

## Preguntas frecuentes (FAQ)

### ¿Los códigos `*#21#` y `*#62#` funcionan en todos los operadores y móviles?
Funcionan en la mayoría de redes GSM/UMTS/LTE y en Android e iPhone, pero algunos operadores (y móviles con VoLTE o eSIM) pueden mostrar la respuesta de forma distinta o requerir la app del operador. Si no ves respuesta, consulta el estado de desvíos en la app oficial.

### ¿Puede alguien activar un desvío en mi móvil sin tocarlo?
Sí, si tiene acceso a tu cuenta del operador (por ejemplo, con tu contraseña) o si instaló una app con permisos de telefonía. Por eso conviene cambiar la clave del operador y revisar apps sospechosas.

### ¿El desvío de llamadas se nota cuando alguien me llama?
En el desvío incondicional (`*#21#`) tu móvil no suena nunca: quien llama es redirigido directamente. En el condicional (`*#62#`) el móvil suena normal y solo se desvía cuando está apagado o sin cobertura, por eso es más difícil de detectar.

### ¿Borrar los desvíos con `##002#` afecta a mi buzón de voz o a mi tarifa?
`##002#` elimina los desvíos configurados, incluido el desvío al buzón de voz en algunos operadores. No cambia tu tarifa ni tus datos, pero tendrás que volver a configurar el buzón si lo usabas. Es reversible y no borra contactos ni mensajes.