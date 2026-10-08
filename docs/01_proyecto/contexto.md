# Contexto: qué se analiza y por qué

Este documento explica, sin suponer conocimientos previos, cómo compra el Estado colombiano, qué es SECOP II, qué información contienen los datos que usa este proyecto y por qué vale la pena analizarlos. Los términos técnicos se explican la primera vez que aparecen y están reunidos en el [glosario](glosario.md).

---

## 1. La idea en pocas palabras

Cada año, alcaldías, gobernaciones, hospitales públicos y otras instituciones del Estado colombiano firman miles de contratos con empresas y personas para obtener bienes, obras y servicios. Todos esos contratos se pagan con dinero público.

Colombia publica buena parte de esa información en internet, en una plataforma oficial llamada **SECOP II**, y la ofrece como **datos abiertos**: cualquiera puede descargarla gratis. El problema es que son cientos de miles de registros, con nombres escritos de formas distintas y campos técnicos difíciles de interpretar. Que la información sea pública no significa que sea fácil de entender.

**Este proyecto toma los contratos firmados por entidades públicas del departamento de Antioquia desde 2022, los organiza y responde cinco preguntas concretas** sobre cuánto se contrata, con quién y de qué manera, de forma que cualquier cifra pueda verificarse contra la fuente original.

---

## 2. Cómo compra el Estado colombiano

### 2.1 Quién compra: las entidades estatales

Una **entidad estatal** es cualquier institución pública que tiene presupuesto propio y puede firmar contratos: el Ministerio de Educación, la Gobernación de Antioquia, la Alcaldía de un municipio, un hospital público, una universidad pública, entre muchas otras.

Las entidades no producen por sí mismas todo lo que necesitan. Para construir una carretera, comprar medicamentos, alimentar estudiantes o contratar a un abogado, deben **contratar** a alguien externo.

### 2.2 A quién le compra: los proveedores o contratistas

El **proveedor** (también llamado **contratista** una vez firma el contrato) es la persona o empresa que vende el bien o presta el servicio. Puede ser:

- una **persona jurídica**: una empresa, identificada con su NIT (Número de Identificación Tributaria);
- una **persona natural**: un individuo, identificado normalmente con su cédula. Es muy común, por ejemplo, cuando una alcaldía contrata a un ingeniero o a un auxiliar administrativo por un periodo determinado.

### 2.3 Cómo se elige al proveedor: el proceso de contratación

Las entidades no pueden elegir a quien quieran como lo haría un comprador particular. La ley exige seguir un **proceso de contratación**, que en términos generales tiene estas etapas:

```text
 1. Planear          2. Convocar           3. Seleccionar        4. Firmar           5. Ejecutar
 La entidad    ──►  Publica qué    ──►    Evalúa las      ──►  Se firma el   ──►  El contratista
 define qué         necesita y las        ofertas y elige      contrato.           entrega, la
 necesita y         condiciones           al proveedor                             entidad paga.
 cuánto cuesta.     para participar.      ganador.
```

Un mismo proceso puede terminar en **un contrato**, en **varios** (por ejemplo, si se dividió en lotes) o en **ninguno** (si nadie se presentó o ninguna oferta cumplió; en ese caso se dice que el proceso quedó **desierto**).

### 2.4 Las modalidades de contratación

La **modalidad** es el tipo de procedimiento que la entidad usa para elegir al proveedor. La ley (principalmente las leyes 80 de 1993 y 1150 de 2007) define cuál corresponde según el monto y el tipo de compra. Es importante porque indica **cuánta competencia hubo**: en unas modalidades compiten muchos oferentes y en otras la entidad elige directamente.

| Modalidad | En palabras sencillas | Ejemplo típico | Nivel de competencia |
|-----------|----------------------|----------------|----------------------|
| **Licitación pública** | La regla general para compras grandes. Convocatoria abierta, cualquiera que cumpla puede ofertar y gana la mejor oferta según criterios publicados. | Construcción de una vía. | Alto |
| **Selección abreviada** | Un procedimiento más corto para ciertos casos, como bienes estandarizados o compras de valor medio. | Compra de computadores o papelería. | Medio–alto |
| **Concurso de méritos** | Para consultorías. Se elige principalmente por la calidad y experiencia del equipo, no por el precio. | Estudios técnicos, interventoría de una obra. | Medio–alto |
| **Mínima cuantía** | Procedimiento simplificado para compras de valor bajo. Gana el precio más bajo que cumpla. | Mantenimiento de aires acondicionados. | Medio |
| **Contratación directa** | La entidad elige al proveedor sin convocatoria competitiva. Solo se permite en casos que la ley enumera. | Contratar a una persona por prestación de servicios, un convenio con otra entidad pública, una urgencia. | Bajo |
| **Régimen especial** | Algunas entidades (como hospitales públicos y ciertas empresas del Estado) no siguen las reglas anteriores, sino sus propios manuales de contratación. | Compras de un hospital público. | Variable |

> **Importante:** la contratación directa **es legal** cuando se usa en los casos permitidos. Una proporción alta no prueba que algo esté mal; es simplemente uno de los primeros datos que se revisan para entender cómo contrata una entidad.

### 2.5 Las elecciones también influyen: la Ley de Garantías

La Ley 996 de 2005, conocida como **Ley de Garantías**, restringe la contratación directa durante los meses previos a las elecciones presidenciales, con algunas excepciones. Su propósito es evitar que los contratos se usen con fines electorales. Por eso, en años de elecciones presidenciales (como **2022 y 2026**), los datos mensuales muestran patrones atípicos: menos contratación directa antes de la restricción y más contratación acumulada antes o después de ella. **Esto no es un hallazgo del proyecto, sino un contexto que hay que conocer para leer los datos correctamente.**

Algo parecido ocurre con los cambios de gobierno local: alcaldes y gobernadores elegidos en octubre de 2023 asumieron en enero de 2024, y el primer año de un gobierno suele tener un ritmo de contratación distinto.

---

## 3. Qué es SECOP

**SECOP** significa *Sistema Electrónico de Contratación Pública*. Es la plataforma oficial donde las entidades estatales colombianas publican y gestionan sus procesos de contratación. La administra **Colombia Compra Eficiente**, la Agencia Nacional de Contratación Pública. Existen dos versiones que hoy conviven:

| | SECOP I | SECOP II |
|---|---|---|
| **Qué es** | Una vitrina de **publicidad**. | Una plataforma **transaccional**: el proceso ocurre dentro de ella. |
| **Cómo funciona** | La entidad hace el proceso por fuera (en papel o por correo) y después sube los documentos. | La entidad publica la convocatoria en la plataforma, los proveedores presentan sus ofertas allí y el contrato se firma electrónicamente. |
| **Calidad de la información** | Depende de que la entidad la suba completa y a tiempo. | Se genera en el momento de cada acción, por lo que es más consistente, aunque no perfecta. |

Este proyecto usa **solo SECOP II**, porque en él el contrato es el propio documento electrónico firmado en la plataforma, lo que lo convierte en la fuente más directa disponible.

---

## 4. Los datos que usa este proyecto

### 4.1 Datos abiertos y API

El Estado publica la información de SECOP II en **datos.gov.co**, el portal de datos abiertos de Colombia. Allí cada conjunto de información se llama **dataset** (conjunto de datos) y tiene un código único.

Los datos se pueden descargar desde la página web o pedir por medio de una **API**: una dirección web a la que un programa le hace preguntas y recibe los datos en un formato estructurado. Este proyecto usa la API para que la descarga sea automática y repetible.

### 4.2 El dataset: *SECOP II – Contratos Electrónicos*

- **Código:** `jbjy-vk9h`
- **Dirección:** https://www.datos.gov.co/Estad-sticas-Nacionales/SECOP-II-Contratos-Electr-nicos/jbjy-vk9h
- **Qué registra:** **contratos**, no procesos. **Cada fila es un contrato.**

```text
Proceso de contratación  ──(puede producir 0, 1 o varios)──►  Contratos
  Está en otro dataset                                         Están en ESTE dataset:
  ("SECOP II - Procesos de Contratación"),                    una fila por contrato
  que este proyecto no usa.
```

Por esta razón, el proyecto **no puede** responder preguntas sobre los procesos en sí, por ejemplo cuántas empresas compitieron en una convocatoria o cuántos procesos quedaron desiertos.

### 4.3 Qué información trae cada contrato

| Pregunta | Información disponible | Nombre técnico de la columna |
|----------|------------------------|------------------------------|
| ¿Quién compró? | Nombre e identificación de la entidad, departamento, ciudad, nivel (nacional o territorial), sector | `nombre_entidad`, `nit_entidad`, `departamento`, `ciudad`, `orden`, `sector` |
| ¿A quién? | Nombre e identificación del proveedor, si es persona natural o empresa, si se declara MiPyme | `proveedor_adjudicado`, `documento_proveedor`, `tipodocproveedor`, `es_pyme` |
| ¿Cómo? | Modalidad de contratación y tipo de contrato | `modalidad_de_contratacion`, `tipo_de_contrato` |
| ¿Cuándo? | Fecha de firma, de inicio y de finalización | `fecha_de_firma`, `fecha_de_inicio_del_contrato`, `fecha_de_fin_del_contrato` |
| ¿Por cuánto? | Valor del contrato (también montos facturados y pagados) | `valor_del_contrato` |
| ¿En qué va? | Estado del contrato (en ejecución, terminado, cancelado, etc.) | `estado_contrato` |
| ¿Dónde verificarlo? | Identificador del contrato y enlace al proceso en SECOP | `id_contrato`, `urlproceso` |

**Ejemplo ilustrativo** (datos inventados, solo para mostrar cómo se lee una fila):

>La *Alcaldía de un municipio de Antioquia* firmó el 14 de marzo de 2024, por **contratación directa**, un contrato de **prestación de servicios** con una **persona natural** por **$18.000.000** para apoyar la gestión documental durante seis meses. El contrato está **en ejecución**.

### 4.4 Advertencias sobre estos datos

Cualquier lectura de los resultados debe tener presentes estas cuatro limitaciones:

1. **El departamento es el de la entidad, no el del lugar donde se ejecuta el contrato.** Una entidad nacional con sede en Bogotá que contrata una obra en Antioquia aparece como "Bogotá".
2. **Los datos cambian con el tiempo.** SECOP II se actualiza continuamente: un contrato puede cambiar de estado o de valor. Por eso todas las cifras del proyecto indican una **fecha de corte**, es decir, el día en que se descargaron los datos.
3. **El valor registrado puede no ser el valor final.** Cuando un contrato se amplía (lo que se llama una **adición**), esa información se registra en otro dataset que este proyecto no usa.
4. **No todo el gasto público está aquí.** Las compras por la Tienda Virtual del Estado Colombiano, los contratos que algunas entidades todavía registran en SECOP I y parte de los contratos de entidades con régimen especial pueden faltar o estar incompletos.

---

## 5. Por qué importa analizar la contratación pública

- **Es donde el presupuesto se vuelve realidad.** Las obras, la alimentación escolar, los servicios de salud y buena parte del personal que trabaja para el Estado llegan a través de contratos.
- **Transparencia.** La Ley 1712 de 2014 establece que la información pública debe ser accesible para todos. SECOP II cumple con publicarla, pero su volumen y complejidad hacen que, en la práctica, pocas personas puedan analizarla. Este proyecto busca reducir esa barrera para una región concreta.
- **Buen uso del dinero.** Cuando varios proveedores compiten, el Estado tiende a obtener mejores precios y mejor calidad. Por eso existen indicadores que se usan en Colombia y en otros países para observar la contratación: cuánto se contrata de forma directa, cuánto dinero se concentra en pocos proveedores y cuánto llega a empresas pequeñas. **Ninguno de ellos demuestra irregularidades**, pero ayudan a saber dónde vale la pena mirar con más detalle.

---

## 6. Por qué Antioquia

El análisis se limita a un departamento para que el proyecto sea manejable y sus resultados se puedan revisar con cuidado. Se eligió **Antioquia** por cuatro razones:

| Criterio | Explicación |
|----------|-------------|
| **Conocimiento del territorio** | El autor estudia en Medellín, la capital del departamento. Conocer la región permite detectar cuándo un resultado no tiene sentido y probablemente se debe a un error en los datos. |
| **Variedad de entidades** | Antioquia tiene la Gobernación, el Distrito de Medellín, 125 municipios, numerosos hospitales públicos y otras entidades. La pregunta principal del proyecto compara entidades entre sí, y para eso necesita muchas. |
| **Volumen de datos** | Es alto, pero se puede procesar en un computador personal si se descargan solo las columnas necesarias. El número exacto de contratos se confirma antes de la descarga (ver [alcance](alcance.md), sección 4). |
| **Calidad esperada** | Las entidades grandes llevan años usando SECOP II y suelen registrar mejor la información. Si los municipios pequeños la registran peor, eso también es un resultado que se documenta. |

---

## 7. Para quién es este análisis

El análisis está pensado para **periodistas de datos o de investigación**, en particular de medios regionales.

**Perfil de referencia:** *una periodista de un medio regional de Medellín. Usa hojas de cálculo con soltura, pero no sabe programar ni consultar bases de datos. Tiene una tarde para encontrar una historia y necesita verificar cada cifra antes de publicarla.*

**Por qué este público y no otro:**

| Público posible | Por qué no es el público principal |
|-----------------|------------------------------------|
| Ciudadano en general | Necesita respuestas más simples que un análisis de concentración del gasto; las herramientas del proyecto le resultarían demasiado técnicas. |
| Ente de control (Contraloría, Procuraduría) | Necesita cobertura total (SECOP I, adiciones, pagos) y rigor jurídico, algo que excede lo que un solo dataset permite. |
| Reclutador o evaluador técnico | Lee el proyecto para conocer las habilidades del autor, pero no usa el análisis. Lo que mejor demuestra esas habilidades es un análisis diseñado para un usuario real. |

**Qué implica este público para el diseño del proyecto:**

| La periodista necesita… | Por eso el proyecto… |
|-------------------------|----------------------|
| Saber dónde mirar, no un veredicto | Presenta indicadores descriptivos y rankings, sin calificar a nadie como "riesgoso". |
| Comparar una alcaldía pequeña con la Gobernación | Usa porcentajes y medianas, no solo totales en pesos. |
| Verificar antes de publicar | Muestra el identificador de cada contrato y el enlace a su página en SECOP. |
| No equivocarse al interpretar | Incluye una nota metodológica visible con las limitaciones del análisis. |

---

## 8. Normas citadas

| Norma | Qué establece, en resumen |
|-------|---------------------------|
| Ley 80 de 1993 | Estatuto General de Contratación de la Administración Pública: las reglas básicas con las que contratan las entidades estatales. |
| Ley 1150 de 2007 | Define las modalidades de contratación (licitación, selección abreviada, concurso de méritos, contratación directa, mínima cuantía) y crea el SECOP. |
| Ley 996 de 2005 | Ley de Garantías: restringe la contratación en periodos electorales. |
| Ley 1712 de 2014 | Ley de Transparencia y del Derecho de Acceso a la Información Pública. |
