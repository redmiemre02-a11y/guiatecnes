---
title: "Cómo solucionar el error DNS_PROBE_FINISHED_NXDOMAIN en Google Chrome, Windows 11 y Android"
description: "¿Te aparece el error DNS_PROBE_FINISHED_NXDOMAIN al abrir páginas web? Descubre los métodos definitivos para limpiar la caché DNS y restaurar tu conexión a internet."
pubDate: "2026-11-08"
heroImage: "https://images.pexels.com/photos/5380642/pexels-photo-5380642.jpeg?auto=compress&cs=tinysrgb&w=1200"
heroImageAlt: "Pantalla de portátil con mensaje de error de conexión a internet"
photographer: "Karolina Grabowska"
tags: ["Redes", "Windows 11", "Android", "Chrome", "Solución de Errores"]
author: "Experto Tech"
readingTime: 6
---

El código de error **DNS_PROBE_FINISHED_NXDOMAIN** es uno de los fallos de red más habituales en Google Chrome, Microsoft Edge y navegadores móviles. En términos técnicos, *NXDOMAIN* significa *"Non-Existent Domain"* (dominio inexistente): el sistema DNS (Domain Name System) de tu dispositivo o de tu operador de telecomunicaciones no ha podido traducir la dirección web que escribiste (por ejemplo, `google.com`) a su dirección IP numérica correspondiente.

Si la página web está operativa para otras personas pero a ti te arroja este error en bucle, el problema reside en la caché DNS corrupta de tu sistema o en los servidores DNS asignados por tu router. A continuación te presentamos las 5 soluciones definitivas comprobadas paso a paso.

---

## 1. Vaciar la caché DNS en Windows 11 / Windows 10

La memoria caché local almacena las direcciones IP temporales para acelerar la carga. Si la dirección de un servidor cambió o la tabla local se corrompió, Windows continuará intentando conectarse a un destino erróneo:

1. Presiona la combinación de teclas **Windows + S** y escribe `cmd`.
2. Haz clic derecho sobre **Símbolo del sistema** y selecciona **Ejecutar como administrador**.
3. Escribe el siguiente comando y pulsa **Enter**:
   ```bash
   ipconfig /flushdns
   ```
4. Aparecerá el mensaje: *"Se vació correctamente la caché del solucionador de DNS"*.
5. A continuación, renueva la concesión de red ejecutando estos dos comandos seguidos:
   ```bash
   ipconfig /release
   ipconfig /renew
   ```
6. Reinicia tu navegador y vuelve a cargar la web.

---

## 2. Limpiar la caché interna de Google Chrome

Google Chrome cuenta con su propia caché interna de nombres de dominio independiente del sistema operativo. Si vaciar Windows no fue suficiente:

1. Copia y pega esta dirección en la barra de búsqueda de Chrome:
   ```text
   chrome://net-internals/#dns
   ```
2. Pulsa en el botón gris que dice **"Clear host cache"** (Limpiar caché de hosts).
3. Luego, introduce esta otra URL:
   ```text
   chrome://net-internals/#sockets
   ```
4. Haz clic en **"Flush socket pools"** para cerrar todas las conexiones TCP abiertas.

---

## 3. Cambiar a los servidores DNS públicos de Cloudflare o Google

En la mayoría de hogares, el router utiliza los servidores DNS asignados por la compañía proveedora de internet (Movistar, Vodafone, Claro, Telmex, etc.), los cuales sufren caídas periódicas o bloqueos preventivos erróneos. Cambiar a servidores globales ultra rápidos resuelve el 95% de los fallos:

| Proveedor DNS | Dirección Primaria (IPv4) | Dirección Secundaria (IPv4) | Seguridad y Privacidad |
| :--- | :--- | :--- | :--- |
| **Cloudflare** | `1.1.1.1` | `1.0.0.1` | Máxima velocidad mundial y sin registro de IPs |
| **Google Public DNS** | `8.8.8.8` | `8.8.4.4` | Máxima estabilidad y compatibilidad |
| **Quad9** | `9.9.9.9` | `149.112.112.112` | Bloqueo activo de malware y phishing |

### Cómo cambiarlos en Windows 11:
1. Abre **Configuración > Red e internet > Wi-Fi** (o Ethernet).
2. Haz clic en las propiedades de tu conexión actual.
3. En la sección **Asignación de servidor DNS**, haz clic en **Editar**.
4. Selecciona **Manual**, activa el interruptor **IPv4** e introduce `1.1.1.1` en DNS preferido y `1.0.0.1` en alternativo.
5. Haz clic en Guardar.

---

## 4. Solución en teléfonos móviles Android

En Android el error suele producirse cuando el servicio de DNS Privado entra en conflicto con una red Wi-Fi pública o el operador móvil:

1. Entra en **Ajustes > Conexión y compartir > DNS Privado**.
2. Si está en *Automático*, cámbialo temporalmente a **Desactivado** para comprobar si el error desaparece.
3. Si prefieres una conexión blindada contra publicidad y fallos, selecciona **Nombre de host del proveedor de DNS privado** e introduce `dns.google` o `1dot1dot1dot1.cloudflare-dns.com`.
4. En Chrome para Android, entra en **Ajustes > Privacidad y seguridad > Borrar datos de navegación** y marca "Archivos e imágenes en caché".

---

## 5. Restablecer el catálogo Winsock en el PC

Si ninguna de las soluciones anteriores funcionó, los protocolos de red TCP/IP de Windows pueden tener una clave de registro dañada por software de terceros o programas VPN:

1. Abre el **Símbolo del sistema (CMD)** como Administrador.
2. Ejecuta:
   ```bash
   netsh winsock reset
   ```
3. Reinicia tu ordenador obligatoriamente para aplicar los cambios del socket de red.

---

## Preguntas Frecuentes (FAQ)

### ¿El error DNS_PROBE_FINISHED_NXDOMAIN es culpa de mi conexión o de la página?

**Respuesta**: Puede ser de ambos. Para averiguarlo al instante, intenta abrir esa misma dirección URL desde tu teléfono móvil conectado con datos móviles (4G/5G). Si en datos móviles carga correctamente, el problema está en tu router, PC o Wi-Fi. Si tampoco carga en datos móviles, el nombre de dominio ha expirado, está mal configurado en su hosting o el sitio web ha dejado de existir.

### ¿Cambiar mis DNS a 1.1.1.1 aumenta la velocidad de descarga?

**Respuesta**: Los servidores DNS no aumentan el ancho de banda contratado de tu fibra (tus megas de descarga siguen siendo los mismos), pero reducen drásticamente el tiempo de respuesta (latencia) al hacer clic en cualquier enlace, haciendo que las páginas web comiencen a cargar de forma instantánea.

### ¿Afecta una VPN al error NXDOMAIN?

**Respuesta**: Sí. Las extensiones de navegador y programas VPN modifican los adaptadores de red virtuales. Si el servidor de la VPN se desconecta de forma anómala, el navegador continuará buscando servidores que ya no responden. Desactivar o reinstalar el cliente VPN suele solucionar de inmediato la incidencia.
