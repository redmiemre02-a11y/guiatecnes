---
title: "Passkeys vs Contraseñas: qué son y cómo activarlas en Google, WhatsApp y Amazon"
description: "¿Qué son las llaves de acceso o Passkeys? Descubre cómo sustituir las contraseñas por huella dactilar o Face ID en Google, WhatsApp y Amazon de forma 100% segura."
pubDate: "2026-11-08"
heroImage: "https://images.pexels.com/photos/5473955/pexels-photo-5473955.jpeg?auto=compress&cs=tinysrgb&w=1200"
heroImageAlt: "Primer plano de un usuario desbloqueando su móvil con huella dactilar de forma segura"
photographer: "Mikael Blomkvist"
tags: ["Seguridad", "Passkeys", "Ciberseguridad", "WhatsApp", "Google"]
author: "Experto Tech"
readingTime: 7
---

Durante décadas, las contraseñas alfanuméricas tradicionales han sido la principal puerta de entrada a nuestras cuentas en internet, y también su mayor debilidad. Millones de credenciales se filtran a diario en ataques de denegación, bases de datos hackeadas y campañas masivas de phishing mediante enlaces falsos por SMS o correo electrónico.

Para erradicar definitivamente este problema de raíz, las grandes tecnológicas (Apple, Google, Microsoft y la alianza FIDO) han estandarizado las **Passkeys (Llaves de Acceso)**. Con este nuevo sistema criptográfico, ya no necesitas memorizar complejas combinaciones de letras ni esperar códigos SMS de dos factores: inicias sesión de forma instantánea usando tu huella dactilar, Face ID o el PIN de tu propio teléfono móvil.

A continuación te mostramos por qué son inmunes a los ciberataques y cómo activarlas hoy mismo en tus servicios principales.

---

## ¿Por qué las Passkeys son inmunes al phishing?

A diferencia de una contraseña clásica, una Passkey se basa en un sistema de **criptografía asimétrica de clave pública y privada**:

- **Clave Privada:** Se genera dentro del chip de seguridad ultraseguro de tu propio dispositivo (Secure Enclave en iPhone, Titan M en Pixel o Knox en Samsung). Esta clave **nunca sale de tu teléfono** y jamás se transmite por internet.
- **Clave Pública:** Se almacena en los servidores de la empresa (Google, Amazon, etc.).

Cuando inicias sesión, el servidor envía un reto matemático firmado que solo puede resolver tu clave privada tras confirmar tu identidad biométrica (tu huella o tu rostro). 

> **Inmunidad al phishing:** Aunque un estafador te envíe un enlace idéntico a la página de inicio de sesión de tu banco o de Google, la Passkey simplemente no funcionará en el sitio falso, porque el protocolo comprueba que el dominio web del navegador coincida al 100% con el certificado oficial antes de firmar la clave.

---

## Comparativa: Passkey vs Contraseña Tradicional

| Factor | Contraseña Tradicional + 2FA SMS | Llave de Acceso (Passkey) |
| :--- | :--- | :--- |
| **Vulnerable a hackeos de servidores** | **Sí** (si roban la base de datos) | **No** (solo tienen la clave pública) |
| **Vulnerable al Phishing** | **Sí** (el usuario puede regalar el código) | **No** (protegida por dominio web) |
| **Tiempo de inicio de sesión** | 15 - 30 segundos (escribir y esperar SMS) | **Menos de 2 segundos** (un toque con el dedo) |
| **Sincronización en la nube** | Requiere gestor de contraseñas | Sincronización cifrada (iCloud / Google Password) |

---

## Cómo activar las Passkeys paso a paso

### 1. Activar Passkey en tu cuenta de Google
1. Entra desde tu navegador en `myaccount.google.com/security`.
2. En la sección *"Cómo inicias sesión en Google"*, pulsa en **Llaves de acceso y llaves de seguridad**.
3. Inicia sesión para confirmar tu identidad.
4. Pulsa en el botón azul **"Crear una llave de acceso"**.
5. Tu navegador te pedirá confirmar mediante el sensor de huella de tu móvil o el lector biométrico de tu ordenador. ¡Listo! A partir de ahora podrás acceder sin contraseña.

### 2. Activar Passkey en WhatsApp
1. Abre WhatsApp en tu smartphone (Android o iPhone).
2. Entra en **Ajustes > Cuenta**.
3. Selecciona la opción **Llaves de acceso (Passkeys)**.
4. Pulsa en **"Crear llave de acceso"**.
5. Vincula tu huella dactilar. Si cambias de teléfono o reinstalas la app, ya no tendrás que esperar el código de 6 dígitos por SMS.

### 3. Activar Passkey en Amazon
1. Abre la app de Amazon o visita su web e inicia sesión.
2. Ve a **Mi cuenta > Inicio de sesión y seguridad**.
3. Al lado de **Llaves de acceso**, haz clic en **Configurar**.
4. Sigue la ventana emergente de tu navegador para registrar tu teléfono como dispositivo de confianza mediante biometría.

---

## ¿Qué ocurre si pierdo o me roban el teléfono móvil?

Esta es la duda más frecuente entre los usuarios primerizos. Las Passkeys se sincronizan automáticamente en tu nube de credenciales cifrada de extremo a extremo:

- Si usas **Apple**, se sincronizan de forma segura a través del **Llavero de iCloud** (iCloud Keychain).
- Si usas **Android**, se sincronizan con el **Administrador de contraseñas de Google**.
- Si cambias a un teléfono nuevo, basta con iniciar sesión con tu cuenta de Apple ID o Google principal para que todas tus llaves de acceso se restauren de forma inmediata en el nuevo terminal.

---

## Preguntas Frecuentes (FAQ)

### ¿Las empresas pueden ver mi huella dactilar o mi rostro al usar una Passkey?

**Respuesta**: No, en absoluto. Tu huella dactilar o escaneo facial nunca salen del chip de seguridad físico de tu teléfono móvil. El sistema operativo solo envía a la web una confirmación criptográfica binaria (verdadero o falso) indicando que el propietario legítimo autorizó el acceso biométrico.

### ¿Puedo seguir usando mi contraseña tradicional si no tengo mi teléfono a mano?

**Respuesta**: Sí. Durante el periodo de transición actual, la mayoría de los servicios mantienen las contraseñas como método de respaldo. Si intentas iniciar sesión desde un ordenador ajeno que no tiene tu huella, puedes elegir *"Iniciar sesión con otro método"* e introducir tu contraseña manual de siempre.

### ¿Funcionan las Passkeys en navegadores como Firefox o Chrome en Windows?

**Respuesta**: Sí, Windows Hello en Windows 11 admite Passkeys de forma nativa a través de PIN, sensor de huellas o cámara infrarroja compatible. Si tu PC no tiene lector biométrico, el navegador mostrará un código QR para que lo escanees con la cámara de tu móvil y apruebes el acceso en pantalla.
