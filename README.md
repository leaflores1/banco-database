# 🏦 Banco ICARO – Proyecto de Ingeniería de Datos

**Banco ICARO** es un sistema bancario educativo y progresivo que simula operaciones reales de una entidad financiera, combinando desarrollo backend con análisis de datos. Comienza con una base relacional y crece hacia una arquitectura moderna de procesamiento de datos, integrando los contenidos de la **Diplomatura Universitaria en Data Engineering (ICARO - UNC)**.

---

## 🎯 Objetivos

- Modelar entidades como clientes, cuentas y transacciones en una base MySQL.
- Automatizar operaciones bancarias básicas en Python (depósitos, extracciones, transferencias).
- Incorporar lógica de validación y trazabilidad de movimientos financieros.
- Analizar datos reales con Pandas y proyectar integración futura con herramientas Big Data.

---

## 🧰 Tecnologías utilizadas

### 🗄️ **Base de datos**
- **MySQL** – Motor relacional con vistas, procedimientos y llaves foráneas.

### 🐍 **Backend en Python**
- `mysql-connector-python` – Conector de Python a MySQL
- `pandas` – Análisis y manipulación de datos
- `python-dotenv` – Variables de entorno seguras
- Scripts interactivos tipo CLI

### 📦 **Estructura del proyecto**
- `db/` – Conexión a la base de datos
- `scripts/` – Scripts interactivos (crear clientes, cuentas, transferencias, login, cajero)
- `notebooks/` – Análisis exploratorios (en progreso)
- `sql/` – Archivos separados por responsabilidad (`schema.sql`, `views.sql`, `data.sql`)
- `.env` – Configuración segura de credenciales

---

## 🔄 Funcionalidades actuales

- ✅ Crear clientes y cuentas bancarias
- ✅ Validar usuarios con login (DNI + email)
- ✅ Depositar, extraer y transferir dinero entre cuentas
- ✅ Ver historial de transacciones por cuenta
- ✅ Menú interactivo tipo *cajero automático* para operar en consola
- ✅ Análisis de transacciones reales con Pandas en notebooks

---

## 🧪 Análisis de datos

- Conexión desde Jupyter Notebook
- Extracción de transacciones en DataFrame
- Agrupamiento por tipo de operación
- Visualización de saldos y actividad

---

## 🚧 Próximos pasos

- Exportar extractos y reportes a CSV
- Implementar módulo de auditoría con MongoDB
- Orquestar carga y transformación de datos con Azure Data Factory
- Aplicar limpieza y enriquecimiento de datos con PySpark en Databricks
- Diseñar un esquema medallion con capas Bronce, Silver y Gold

---

## 📁 Estructura del proyecto

bancoIcaro/
├── db/ # Conexión y configuración de base de datos
├── scripts/ # Scripts funcionales de backend bancario
├── auth/ # Módulo de login de clientes
├── notebooks/ # Notebooks de análisis con Pandas
├── sql/ # Scripts SQL para schema, vistas, inserts y queries
├── .env # Variables de entorno (no versionado)
├── requirements.txt # Dependencias del proyecto
└── README.md

## 📎 Requisitos

- Python 3.11
- MySQL Server (Workbench o DBeaver)
- Entorno virtual (`python -m venv env`)
- Instalar dependencias:
  ```bash
  pip install -r requirements.txt
