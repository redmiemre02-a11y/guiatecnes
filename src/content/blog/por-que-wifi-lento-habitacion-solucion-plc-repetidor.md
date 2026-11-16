---
title: "Por qué el WiFi va lento en una habitación y cómo solucionarlo con PLC o repetidor barato"
description: "Averigua por qué pierdes velocidad de internet en habitaciones lejanas. Comparativa técnica entre repetidores WiFi, adaptadores PLC de enchufe y redes Mesh sin gastar de más."
pubDate: 2026-11-16
updatedDate: 2026-11-16
heroImage: "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&fit=crop&w=1200&q=80"
heroImageAlt: "Router WiFi moderno con luces LED azules en una vivienda"
tags: ["tecnologia", "errores", "hogar", "guias"]
author: "Experto Tech"
readingTime: 6
---

## ⚡ En Resumen (TL;DR)

- **La trampa del 5 GHz**: La banda de 5 GHz ofrece hasta 800 Mbps junto al router, pero se debilita drásticamente al atravesar dos paredes o un tabique con azulejos (baños y cocinas).
- **El error de los repetidores baratos de 15€**: Un repetidor WiFi convencional reduce automáticamente la velocidad a la mitad (50% de pérdida por retransmisión dúplex) y añade latencia severa (ping alto).
- **La solución estrella para casas antiguas (PLC)**: Los adaptadores PLC transmiten los datos a través de los cables eléctricos de las paredes, logrando una conexión estable sin obras ni cables a la vista.
- **Redes Mesh para pisos grandes**: Si tienes más de 100 m² o varias plantas, una red en malla con soporte WiFi 6 o WiFi 7 es la única forma de moverte de habitación sin cortes de llamada o streaming.

---

Contratas 600 Mbps o 1 Gbps de fibra óptica con tu operadora, te colocas al lado del router en el salón y la velocidad vuela. Sin embargo, caminas 10 metros hasta el dormitorio o el despacho de teletrabajo y la conexión cae a unos míseros 15 Mbps, con cortes continuos en videollamadas de Zoom y vídeos de YouTube que se quedan en búfer.

¿Por qué ocurre este fenómeno físico y cuál es la solución más económica y eficaz para resolverlo?

---

## 1. Los 4 enemigos físicos que destruyen tu señal WiFi

Las ondas de radiofrecuencia (microondas) no viajan en el vacío dentro de casa. Se enfrentan a obstáculos materiales invisibles:

1. **Agua y tuberías (Atenuación extrema)**: El agua absorbe con voracidad las ondas de 2.4 GHz y 5 GHz. Si entre el router y tu habitación se interpone la cocina (frigorífico con agua, lavavajillas) o un cuarto de baño, la señal llega pulverizada.
2. **Espejos y cristales gruesos**: Los espejos llevan una fina lámina de plata o aluminio en el reverso que actúa como un escudo reflector bloqueando la señal.
3. **Muros de carga y hormigón armado**: Las varillas de hierro encofrado dentro de los pilares crean el efecto de una *Jaula de Faraday*.
4. **Saturación vecinal de canales**: En bloques de pisos, decenas de routers emitiendo en el mismo canal se interfieren mutuamente creando colisiones de paquetes.

---

## 2. La gran comparativa: ¿Repetidor WiFi, Adaptador PLC o Red Mesh?

Ante el problema de cobertura, la mayoría de personas comete el error de comprar el repetidor más barato de Amazon. Analicemos técnicamente qué opción te conviene según tu caso particular:

| Dispositivo | Precio Orientativo | Velocidad Real Típica | Latencia (Ping) | Cuándo Elegirlo |
| :--- | :---: | :---: | :---: | :--- |
| **Repetidor WiFi Básico (N300/AC1200)** | 15 € - 30 € | 25 - 60 Mbps | Alta (40-80 ms) | Presupuestos mínimos; pisos pequeños de 1 sola planta sin paredes gruesas. |
| **Adaptadores PLC por cable eléctrico** | 40 € - 75 € | 150 - 450 Mbps | Muy Baja (8-15 ms) | Ideal para teletrabajo, gaming y habitaciones alejadas con instalación eléctrica moderna. |
| **Sistema WiFi Mesh (2-3 nodos)** | 80 € - 180 € | 400 - 800 Mbps | Baja (10-20 ms) | Casas de 2 o más plantas, chalets o pisos grandes de más de 110 m². |

---

## 3. Por qué el PLC suele ser el gran vencedor en casas individuales

Un kit de **PLC (Powerline Communications)** incluye dos pequeños adaptadores de enchufe:
1. Enchufas el primero junto a tu router y lo conectas mediante un cable Ethernet corto.
2. Enchufas el segundo en la habitación donde no llega el WiFi.
3. La señal de internet se modula a alta frecuencia a través del cobre del tendido eléctrico de tu hogar.
4. El adaptador de destino emite su propia red WiFi limpia o te permite conectar el ordenador por cable de red directo.

> 💡 **Consejo clave**: Nunca conectes un PLC a una regleta de enchufes con interruptor o protección contra sobretensiones; conéctalo siempre directamente a la toma de la pared para evitar ruidos parásitos en la señal.

---

## 4. Medir antes y después de instalar tu solución

No confíes en las "rayitas" de cobertura del móvil; las barras solo indican la intensidad de la señal portadora (RSSI), no la calidad ni la velocidad real de transferencia de paquetes de datos.

> ⚡ **Comprobación en tiempo real**: Mide tu latencia y ancho de banda en segundos con nuestro [Test de Velocidad de Conexión WiFi en vivo](/herramientas/test-velocidad/). Haz una prueba antes de mover nada y otra tras aplicar las mejoras para verificar la ganancia exacta en megabits.
