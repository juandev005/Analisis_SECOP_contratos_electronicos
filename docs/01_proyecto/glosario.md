# Glosario

Definiciones en lenguaje sencillo de los términos usados en la documentación del proyecto. Están agrupadas por tema y ordenadas alfabéticamente dentro de cada grupo.

---

## Contratación pública

**Adición.** Ampliación del valor o del plazo de un contrato ya firmado. En SECOP II se registra en un conjunto de datos distinto del que usa este proyecto.

**Colombia Compra Eficiente.** Nombre con el que se conoce a la Agencia Nacional de Contratación Pública, la entidad del Gobierno colombiano que define políticas de contratación y administra SECOP.

**Concurso de méritos.** Modalidad de contratación para consultorías (estudios, diseños, interventorías), en la que se elige principalmente por la calidad y experiencia del oferente y no por el precio.

**Contratación directa.** Modalidad en la que la entidad elige al proveedor sin una convocatoria competitiva. Solo está permitida en los casos que la ley enumera, por ejemplo para contratar servicios profesionales de una persona, para convenios entre entidades públicas o ante una urgencia. Es legal cuando se usa en esos casos.

**Contratista.** El proveedor que firmó un contrato con una entidad estatal.

**Contrato.** Acuerdo firmado entre una entidad estatal y un proveedor, en el que este se compromete a entregar un bien, construir una obra o prestar un servicio a cambio de un pago.

**Contrato electrónico.** Contrato que se elabora y se firma dentro de la plataforma SECOP II.

**Entidad estatal.** Institución pública con presupuesto propio y capacidad para firmar contratos: ministerios, gobernaciones, alcaldías, hospitales públicos, universidades públicas, entre otras.

**ESE (Empresa Social del Estado).** Nombre que reciben los hospitales y centros de salud públicos en Colombia. Contratan con un régimen especial.

**Ley de Garantías.** Ley 996 de 2005. Restringe la contratación directa durante los meses previos a las elecciones presidenciales, con algunas excepciones, para evitar que los contratos se usen con fines electorales.

**Licitación pública.** Modalidad general de contratación para compras de mayor valor. La convocatoria es abierta, cualquier interesado que cumpla los requisitos puede presentar una oferta y se elige la mejor según criterios publicados de antemano.

**MiPyme.** Micro, pequeña o mediana empresa.

**Mínima cuantía.** Modalidad simplificada para compras de valor bajo. Se elige la oferta de menor precio que cumpla los requisitos.

**Modalidad de contratación.** Procedimiento que la entidad usa para elegir al proveedor. Indica cuánta competencia hubo.

**NIT (Número de Identificación Tributaria).** Número con el que se identifica a empresas y entidades ante la autoridad tributaria colombiana. Suele incluir al final un dígito de verificación.

**Orden (nacional o territorial).** Nivel del Estado al que pertenece una entidad. Las del orden nacional dependen del Gobierno nacional (por ejemplo, un ministerio); las del orden territorial dependen de un departamento o municipio (por ejemplo, una alcaldía).

**Persona jurídica.** Una empresa u organización con identidad legal propia, identificada con NIT.

**Persona natural.** Un individuo, identificado normalmente con su cédula de ciudadanía.

**Prestación de servicios.** Tipo de contrato con el que una entidad contrata a una persona o empresa para realizar una tarea durante un tiempo determinado. Es muy frecuente con personas naturales.

**Proceso de contratación.** Conjunto de pasos (planear, convocar, seleccionar, firmar) que una entidad sigue para elegir a un proveedor. Puede terminar en uno, varios o ningún contrato.

**Proceso desierto.** Proceso de contratación que termina sin contrato porque nadie se presentó o ninguna oferta cumplió los requisitos.

**Proveedor.** Persona o empresa que vende un bien o presta un servicio a una entidad estatal.

**Régimen especial.** Situación de algunas entidades (como hospitales públicos y ciertas empresas del Estado) que no siguen las modalidades generales de contratación, sino sus propios manuales.

**SECOP (Sistema Electrónico de Contratación Pública).** Plataforma oficial donde las entidades estatales colombianas publican y gestionan su contratación.

**SECOP I.** Versión de SECOP que funciona como vitrina de publicidad: la entidad realiza el proceso por fuera y luego sube los documentos.

**SECOP II.** Versión transaccional de SECOP: el proceso completo ocurre dentro de la plataforma, desde la convocatoria hasta la firma electrónica del contrato.

**Selección abreviada.** Modalidad de contratación más ágil que la licitación, usada en casos como la compra de bienes estandarizados o de valor medio.

**Tienda Virtual del Estado Colombiano.** Plataforma donde las entidades compran productos y servicios estandarizados a precios previamente negociados. Sus compras no están completas en el conjunto de datos de este proyecto.

---

## Datos y análisis

**API.** Dirección web a la que un programa le hace consultas y recibe datos en un formato estructurado. Permite descargar información de forma automática.

**Base de datos.** Sistema para guardar y consultar grandes cantidades de información de forma organizada. Este proyecto usa PostgreSQL.

**Concentración del gasto.** Medida de qué tanto del dinero de una entidad se reparte entre pocos proveedores. En este proyecto se mide principalmente como el porcentaje que reciben los 10 proveedores más grandes.

**Conjunto de datos (dataset).** Colección de información publicada como una tabla, con un código que la identifica. En este proyecto, cada fila del conjunto de datos es un contrato.

**Datos abiertos.** Información pública que cualquier persona puede descargar, usar y compartir gratuitamente. En Colombia se publican en datos.gov.co.

**Duplicado.** Registro que aparece más de una vez. Si no se elimina, el mismo contrato se cuenta varias veces.

**Fecha de corte.** Día en que se descargaron los datos. Todas las cifras del proyecto describen la situación de ese día.

**Índice Herfindahl-Hirschman (IHH).** Medida estándar de concentración. Se calcula sumando el cuadrado de la participación porcentual de cada proveedor. Va de casi 0 (dinero muy repartido) a 10.000 (todo el dinero en un solo proveedor).

**Mediana.** Valor que queda en la mitad cuando se ordenan los datos de menor a mayor. A diferencia del promedio, no se altera por unos pocos valores extremos; por eso es útil cuando hay contratos muy grandes.

**Reglas de calidad.** Comprobaciones automáticas que detectan registros con problemas, como valores en cero, fechas imposibles o proveedores sin identificación.

**SQL.** Lenguaje estándar para consultar bases de datos.

**Tablero (dashboard).** Conjunto de gráficos y tablas interactivos que resume los resultados del análisis. Este proyecto usa Power BI.

**Valor nominal.** Valor en pesos tal como se registró, sin ajustar por inflación.

**Vista.** Consulta guardada en la base de datos que produce una tabla de resultados. Cada pregunta del proyecto se responde con una vista.
