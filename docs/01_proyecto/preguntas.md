# Las cinco preguntas del proyecto

Todo el proyecto existe para responder estas cinco preguntas. Cada cálculo de la base de datos, cada gráfico del tablero y cada hallazgo publicado sale de alguna de ellas. No se agregan preguntas nuevas mientras estas cinco no estén respondidas.



Los términos técnicos se explican en el [glosario](glosario.md).


---

## Pregunta A — ¿Cuánto contratan las entidades de Antioquia y cómo cambia mes a mes?

| | |
|---|--|
| **Por qué importa** | Da la dimensión del fenómeno: cuántos contratos y cuánto dinero hay en juego. Es la referencia para leer las demás preguntas. También muestra los ritmos del año, como los picos de diciembre o los efectos de la Ley de Garantías en 2022 y 2026. |
| **Cómo se mide** | Para cada mes: **número de contratos**, **valor total**, **valor promedio** y **valor mediano** (el valor del contrato que queda justo en la mitad al ordenarlos de menor a mayor; a diferencia del promedio, no lo alteran unos pocos contratos gigantes). Además, la **variación frente al mismo mes del año anterior**. |
| **Qué datos usa** | Identificador del contrato (`id_contrato`), fecha de firma (`fecha_de_firma`), valor (`valor_del_contrato`) y estado (`estado_contrato`). | 

---

## Pregunta B ★ — ¿Qué tan concentrado está el gasto de cada entidad en pocos proveedores?

**Es la pregunta principal del proyecto.**

### En qué consiste

Una entidad puede repartir su dinero entre muchos proveedores o concentrarlo en unos pocos. Esta pregunta mide, para cada entidad, **qué parte de todo lo que contrató se la llevaron sus diez proveedores más grandes**.

### Ejemplo ilustrativo (cifras inventadas)

> La Entidad X contrató 10.000 millones entre 2022 y 2026 con 150 proveedores distintos. Si se ordenan los proveedores de mayor a menor según cuánto recibieron, los diez primeros suman 7.200 millones.
>
> **Concentración en los 10 principales = 7.200 / 10.000 = 72 %.**
>
> Dicho de otra forma: 10 de sus 150 proveedores (el 7 %) recibieron casi tres cuartas partes del dinero.

Si en la Entidad Y ese mismo indicador es 25 %, su gasto está mucho más repartido. Como el resultado es un porcentaje, se pueden comparar entidades de tamaños muy distintos, como una alcaldía pequeña y la Gobernación.

### Por qué importa

Es lo primero que preguntaría un periodista: *¿a cuántos proveedores le entrega esta entidad la mayor parte de su dinero?* Una concentración alta puede indicar poca competencia y señala dónde vale la pena mirar con más detalle, **aunque no prueba ninguna irregularidad** (ver [alcance](alcance.md), sección 5).

### Cómo se mide

| Indicador | Qué significa | Cálculo |
|-----------|---------------|---------|
| **Concentración en los 10 principales** (indicador principal) | Porcentaje del dinero de la entidad que recibieron sus 10 proveedores más grandes. | Valor de los 10 proveedores con más valor ÷ valor total de la entidad |
| **Número de proveedores** | Cuántos proveedores distintos tuvo la entidad. | Conteo de proveedores distintos |
| **Proveedores que suman el 80 %** | Cuántos proveedores, empezando por los más grandes, hacen falta para llegar al 80 % del dinero. Cuanto menor el número, más concentrado el gasto. | Conteo acumulado de mayor a menor |
| **Índice Herfindahl-Hirschman (IHH)** | Medida estándar de concentración de mercados. Va de casi 0 (dinero muy repartido) a 10.000 (todo el dinero en un solo proveedor). | Suma de los cuadrados de la participación porcentual de cada proveedor |

### Qué datos usa

Identificación y nombre de la entidad (`nit_entidad`, `nombre_entidad`), identificación y nombre del proveedor (`documento_proveedor`, `proveedor_adjudicado`), valor (`valor_del_contrato`) y fecha de firma (`fecha_de_firma`).


### Cómo leer correctamente el resultado

- ✔ **Correcto:** *"En la Entidad X, diez proveedores recibieron el 72 % del valor contratado entre 2022 y 2026."*
- ✘ **Incorrecto:** *"La Entidad X favorece a diez proveedores."* Esta frase atribuye una intención que los datos no muestran.

### Por qué es la pregunta principal

1. Responde la primera inquietud del público del proyecto.
2. Al ser un porcentaje, permite comparar entidades de cualquier tamaño.
3. Se puede cruzar con las preguntas D y E para obtener el hallazgo central: *¿las entidades con el gasto más concentrado son también las que más contratan de forma directa?*
4. Es la más exigente técnicamente, por lo que demuestra el dominio de consultas analíticas.






---

## Pregunta C — ¿Qué entidades y qué proveedores manejan más dinero en el departamento?

| | |
|---|---|
| **Por qué importa** | Pone nombres propios a los resultados: quiénes son los mayores compradores públicos de Antioquia y quiénes sus mayores contratistas. Complementa la pregunta B con una mirada de todo el departamento. |
| **Cómo se mide** | Dos rankings (entidades y proveedores) ordenados por valor total y, por separado, por número de contratos. Para cada posición se indica su porcentaje del total departamental y el porcentaje acumulado (por ejemplo: "las 5 primeras entidades suman el 40 % del dinero"). |
| **Qué datos usa** | Identificación y nombre de la entidad (`nit_entidad`, `nombre_entidad`), identificación, nombre y tipo de documento del proveedor (`documento_proveedor`, `proveedor_adjudicado`, `tipodocproveedor`) y valor (`valor_del_contrato`). |
| **Dónde se calcula** | `mart.v_ranking_entidades` y `mart.v_ranking_proveedores`  |
---

## Pregunta D — ¿Qué modalidades de contratación se usan más, en número y en valor?

| | |
|---|---|
| **Por qué importa** | La modalidad indica cuánta competencia hubo para obtener el contrato (ver [contexto](contexto.md), sección 2.4). Una proporción alta de contratación directa no es ilegal, pero es uno de los primeros datos que se revisan. |
| **Cómo se mide** | Para cada modalidad: su **porcentaje del número de contratos** y su **porcentaje del valor total**. Para cada entidad: **qué porcentaje de su dinero contrató de forma directa**. |
| **Qué datos usa** | Modalidad (`modalidad_de_contratacion`), justificación registrada para usar esa modalidad (`justificacion_modalidad_de`), identificador del contrato (`id_contrato`), valor (`valor_del_contrato`) e identificación de la entidad (`nit_entidad`). | 

---

## Pregunta E — ¿Qué parte del dinero llega a micro, pequeñas y medianas empresas (MiPymes)?

| | |
|---|---|
| **Por qué importa** | Indica si la contratación pública abre oportunidades a las empresas pequeñas o si se concentra en las grandes. |
| **Cómo se mide** | **Porcentaje del valor que recibieron empresas que se declaran MiPyme**, calculado solo sobre los contratos con empresas (personas jurídicas) en los que esa información está registrada. El porcentaje de valor **sin información** sobre si el proveedor es MiPyme se informa aparte, para no ocultarlo. |
| **Qué datos usa** | Indicador MiPyme (`es_pyme`), tipo de documento del proveedor (`tipodocproveedor`), valor (`valor_del_contrato`) y fecha de firma (`fecha_de_firma`).  |
| **Precaución** | La condición de MiPyme la declara el propio proveedor. Las personas naturales no son empresas, por lo que se excluyen de este cálculo para no distorsionarlo. |
---

## Datos necesarios para responder las cinco preguntas

Esta tabla resume qué columnas del conjunto de datos se descargan y para qué pregunta sirve cada una. **Las columnas que no aparecen aquí no se descargan.** Los nombres técnicos se confirmarán contra el diccionario oficial del conjunto de datos antes de la descarga.

| Columna (nombre técnico) | Qué contiene | A | B | C | D | E |
|--------------------------|--------------|---|---|---|---|---|
| `id_contrato` | Identificador único del contrato | ● | ● | ● | ● | ● |
| `fecha_de_firma` | Fecha en que se firmó el contrato | ● | ● | ● | ● | ● |
| `valor_del_contrato` | Valor registrado del contrato | ● | ● | ● | ● | ● |
| `estado_contrato` | Situación actual del contrato | ● | ● | ● | ● | ● |
| `departamento` | Departamento donde está ubicada la entidad | ● | ● | ● | ● | ● |
| `nit_entidad` | Identificación de la entidad | | ● | ● | ● | |
| `nombre_entidad`, `ciudad`, `orden`, `sector` | Nombre, municipio, nivel y sector de la entidad | | ● | ● | ● | |
| `documento_proveedor`, `tipodocproveedor` | Número y tipo de documento del proveedor | | ● | ● | | ● |
| `proveedor_adjudicado` | Nombre del proveedor | | ● | ● | | |
| `es_pyme` | Si el proveedor se declara MiPyme | | | | | ● |
| `modalidad_de_contratacion` | Procedimiento usado para elegir al proveedor | | | | ● | |
| `justificacion_modalidad_de` | Motivo registrado para usar esa modalidad | | | | ● | |
| `tipo_de_contrato` | Obra, suministro, prestación de servicios, etc. | ● | | ● | ● | |
| `fecha_de_inicio_del_contrato`, `fecha_de_fin_del_contrato` | Duración del contrato; también se usan para detectar fechas imposibles | | | | | |
| `proceso_de_compra`, `urlproceso` | Identificador del proceso y enlace a su página en SECOP, para verificar | | ● | ● | | |
