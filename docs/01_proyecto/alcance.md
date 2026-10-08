# Alcance: qué incluye el análisis y qué no

Este documento define con precisión qué contratos se analizan, qué queda por fuera y por qué. También explica qué conclusiones **no** se pueden sacar de este proyecto. Los términos técnicos se explican en el [glosario](glosario.md).

---

## 1. Resumen

| Aspecto | Qué se incluye | Qué queda por fuera y por qué |
|---------|----------------|-------------------------------|
| **Fuente de datos** | El conjunto de datos *SECOP II – Contratos Electrónicos* (código `jbjy-vk9h`), publicado en datos.gov.co. | Otros conjuntos de datos relacionados: procesos de contratación, adiciones a contratos, SECOP I, Tienda Virtual del Estado y pagos. Cada uno describe algo distinto y combinarlos haría el proyecto mucho más extenso. |
| **Territorio** | Contratos firmados por entidades **ubicadas en el departamento de Antioquia**. | Otros departamentos. Tampoco se incluyen contratos que se ejecutan en Antioquia pero fueron firmados por entidades ubicadas en otro lugar, porque los datos no permiten identificarlos con fiabilidad. |
| **Periodo** | Contratos con fecha de firma desde el **1 de enero de 2022** hasta la **fecha de corte** (el día en que se descargan los datos). | Contratos sin fecha de firma registrada. No se usan en los cálculos, pero se cuentan en el reporte de calidad. |
| **Entidades** | **Todas** las entidades públicas ubicadas en Antioquia, de cualquier nivel (nacional o territorial) y de cualquier sector. | Ninguna se excluye de antemano. Dejar fuera algunas entidades distorsionaría las comparaciones entre ellas. |
| **Tipos de contrato** | **Todos** (obra, suministro, prestación de servicios, consultoría, etc.). | Ninguno se excluye. Cuando es útil, los resultados se separan por tipo. |
| **Estado del contrato** | Todos los contratos se descargan y se guardan. | En los cálculos no se cuentan los contratos que nunca llegaron a ejecutarse, como los cancelados.  |
| **Valor** | El valor registrado de cada contrato, en pesos colombianos **sin ajustar por inflación**. | El ajuste por inflación queda como mejora futura. |

---

## 2. Periodo analizado

- **Desde el 1 de enero de 2022.** Esto da cuatro años completos (2022, 2023, 2024 y 2025) y parte de 2026. Es suficiente para comparar años y abarca dos elecciones presidenciales (2022 y 2026) y un cambio de gobiernos locales (2024), situaciones que afectan cómo contratan las entidades (ver [contexto](contexto.md), sección 2.5).
- **Se usa la fecha de firma** porque es el momento en que el contrato nace. Otras fechas, como la de inicio, a veces están vacías o corresponden al futuro.
- **Fecha de corte:** todas las cifras del proyecto corresponden a los datos tal como estaban el día de la descarga. Como SECOP II se actualiza continuamente, una descarga posterior podría dar resultados distintos.
  - **Fecha de corte de esta versión:** *pendiente; se publicará al realizar la descarga definitiva.*
- **2026 es un año incompleto.** Su total no se compara con el de años completos. Para comparar años se usan los mismos meses de cada año (por ejemplo, enero a agosto) o la evolución mes a mes.

---

## 3. Entidades y tipos de contrato incluidos

**Entidades.** Se incluyen todas las entidades registradas en Antioquia: la Gobernación, el Distrito de Medellín, las alcaldías municipales, los hospitales públicos (llamados Empresas Sociales del Estado, ESE), institutos y empresas públicas, y las sedes de entidades nacionales registradas en el departamento.

**Tipos de contrato.** Un caso merece atención especial: los contratos de **prestación de servicios** con personas naturales. Las entidades los usan mucho para vincular personal por periodos determinados, por lo que son la mayoría de los contratos en **cantidad**, aunque no necesariamente en **dinero**. Por esa razón, todos los resultados del proyecto se presentan de dos formas: **por número de contratos y por valor en pesos**. Mirar solo una de las dos puede dar una imagen equivocada.

---

## 4. Cantidad de contratos que se espera analizar

Antes de descargar los datos se consulta a la plataforma cuántos contratos cumplen los criterios del alcance. Esa cifra cumple dos funciones:

- **Planear:** confirmar que el volumen se puede procesar en un computador personal.
- **Verificar:** al terminar la descarga, el número de registros obtenidos debe ser igual a esta cifra. Si no coincide, la descarga está incompleta.

| Año | Contratos | Observación |
|-----|-----------|-------------|
| 2022 | *pendiente* | Año de elecciones presidenciales (Ley de Garantías). |
| 2023 | *pendiente* | Último año de los gobiernos locales anteriores. |
| 2024 | *pendiente* | Primer año de los nuevos gobiernos locales. |
| 2025 | *pendiente* | |
| 2026 | *pendiente* | Año incompleto hasta la fecha de corte; año de elecciones presidenciales. |
| **Total** | *pendiente* | Fecha de la consulta: *pendiente* |


**Cómo verificar estas cifras.** Cualquier persona puede obtenerlas abriendo estas direcciones en un navegador. Son consultas directas a la API oficial de datos.gov.co.

Cómo aparece escrito "Antioquia" en los datos, y cuántos contratos tiene cada departamento:

```text
https://www.datos.gov.co/resource/jbjy-vk9h.json?$select=departamento,count(*)&$where=fecha_de_firma >= '2022-01-01T00:00:00.000'&$group=departamento&$order=count(*) DESC
```

Total de contratos dentro del alcance:

```text
https://www.datos.gov.co/resource/jbjy-vk9h.json?$select=count(*)&$where=departamento='Antioquia' AND fecha_de_firma >= '2022-01-01T00:00:00.000'
```

Contratos por año:

```text
https://www.datos.gov.co/resource/jbjy-vk9h.json?$select=date_extract_y(fecha_de_firma),count(*)&$where=departamento='Antioquia' AND fecha_de_firma >= '2022-01-01T00:00:00.000'&$group=date_extract_y(fecha_de_firma)&$order=date_extract_y(fecha_de_firma)
```

---

## 5. Qué NO afirma este proyecto

Estas limitaciones aparecen también en el tablero y en la presentación del proyecto. Cualquier uso de los resultados debe tenerlas en cuenta.

1. **No detecta corrupción ni irregularidades.** Que una entidad concentre su gasto en pocos proveedores, contrate mucho de forma directa o repita contratistas puede tener explicaciones legítimas: que solo exista un proveedor capaz de hacer el trabajo, una emergencia, convenios entre entidades públicas o la necesidad de conocimientos muy especializados. El proyecto muestra **dónde** mirar, no **qué** pasó.
2. **No mide todo el gasto público de Antioquia.** Solo incluye lo registrado en SECOP II. Quedan por fuera, total o parcialmente, las compras de la Tienda Virtual del Estado, los contratos que aún se publican en SECOP I y parte de la contratación de entidades con régimen especial.
3. **2026 es un año incompleto.** Sus totales no se pueden comparar con los de años completos.
4. **El valor analizado no es el valor final ni lo efectivamente pagado.** Es el valor registrado del contrato, que puede no incluir ampliaciones posteriores (adiciones).
5. **La ubicación es la de la entidad,** no la del lugar donde se ejecuta el contrato.
6. **La condición de MiPyme la declara el propio proveedor** al registrarse en SECOP II. El proyecto no verifica el tamaño real de las empresas.
7. **Los valores no están ajustados por inflación.** Parte del aumento del valor contratado entre un año y otro puede deberse solo al aumento general de precios.
8. **No explica causas.** El proyecto describe patrones; no determina por qué ocurren.
9. **Los resultados corresponden a una fecha de corte.** Como la fuente se actualiza, otra descarga puede dar cifras diferentes.

---

## 6. Supuestos y riesgos

| Supuesto o riesgo | Qué podría pasar | Cómo se controla |
|-------------------|------------------|------------------|
| Cada contrato tiene un identificador único. | Un mismo contrato podría aparecer dos veces y contarse doble. | Se revisa si hay identificadores repetidos. Si los hay, se conserva el registro más reciente y se documenta. |
| El número de identificación del proveedor lo identifica correctamente. | Un mismo proveedor puede aparecer con su nombre escrito de varias formas o con su número en distintos formatos (con puntos, guiones o dígito de verificación). | Se agrupa por número de identificación unificado, no por nombre. |
| Los valores están bien digitados. | Contratos con valor cero o con cifras absurdamente altas por errores de digitación. | Reglas de calidad que los detectan y uso de la **mediana** (que no se ve afectada por valores extremos) junto al promedio. |
| La plataforma responde de forma estable. | Interrupciones o límites en la descarga. | Descarga por partes, con reintentos automáticos y una clave de acceso oficial de la plataforma. |
| El volumen está dentro de lo previsto. | Demasiados datos para procesar en un computador personal. | Consulta previa del total y el criterio de la sección 4. |

---

## 7. Mejoras futuras (fuera de esta versión)

Ordenadas de mayor a menor valor para el análisis:

1. **Incorporar los procesos de contratación** para saber cuántos proveedores compitieron en cada convocatoria y cuántas tuvieron un único oferente. Es la extensión natural de la pregunta principal.
2. **Incorporar las adiciones** para comparar el valor inicial de los contratos con su valor final.
3. **Ajustar los valores por inflación.**
4. **Ampliar a otros departamentos** y mostrar los resultados en un mapa.
5. **Actualizar los datos de forma automática y periódica.**
6. **Ampliar las pruebas automáticas** del código.
7. **Analizar el texto de los objetos de los contratos** para clasificar en qué se gasta el dinero.
