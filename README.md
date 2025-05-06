# 🏦 Banco ICARO – Proyecto de Ingeniería de Datos

**Banco ICARO** es un proyecto en desarrollo que simula un sistema bancario real y evoluciona progresivamente hacia una solución completa de **Ingeniería de Datos**. Comienza con una base de datos relacional y operaciones básicas implementadas en Python, y está diseñado para escalar con herramientas modernas del ecosistema Data Engineering.

## 🎯 Objetivos

- Modelar entidades bancarias como clientes, cuentas y transacciones.
- Automatizar operaciones como transferencias y depósitos desde backend en Python.
- Registrar, consultar y analizar transacciones financieras.
- Escalar hacia arquitectura de procesamiento de datos moderna: ETL, nube y análisis con PySpark.

---

## 🧰 Tecnologías utilizadas

### 🗄️ **Base de datos**
- **MySQL** – Sistema de gestión relacional para almacenar los datos bancarios.

### 🐍 **Backend y scripts**
- **Python 3.11**
- `mysql-connector-python` – Conexión a base de datos.
- `pandas` – Exploración y análisis de datos.
- `dotenv` – Manejo de variables de entorno seguras.

### 📦 **Organización de código**
- Estructura modular con carpetas `db/`, `scripts/` y `notebooks/`.
- Separación clara entre lógica de conexión, operaciones y análisis.

### 🧪 **(Fase futura)**
- **Jupyter Notebooks** – Para análisis de transacciones y visualizaciones.
- **MongoDB** – Almacenamiento NoSQL para logs o auditoría.
- **Azure Data Factory** – Ingesta y orquestación de datos desde múltiples fuentes.
- **Databricks + PySpark** – Procesamiento distribuido y creación de Delta Tables.
- **Arquitectura Medallion** – Organización eficiente de datos en capas Bronce, Silver y Gold.

---

## 🔄 Funcionalidades actuales

- Crear clientes y cuentas desde scripts en Python.
- Realizar transferencias con validación de saldo.
- Consultar el historial de transacciones por cuenta.
- Conexión directa con MySQL usando `.env` para seguridad.

---

## 📈 Próximos pasos

- Análisis de datos con Pandas y Jupyter. (hecho)
- Exportación de transacciones a CSV.
- Integración con Azure para simular pipelines reales.
- Enriquecimiento y limpieza de datos con PySpark en Databricks.

---


## 📁 Estructura del proyecto

bancoIcaro/
├── db/ # Lógica de conexión a la base de datos
├── scripts/ # Scripts para operaciones (insertar, transferir, consultar)
├── notebooks/ # Análisis exploratorios con Pandas (próximo paso)
├── .env # Variables de entorno (no versionado)
├── requirements.txt # Dependencias
└── README.md

# activar entorno
.\env\Scripts\activate
