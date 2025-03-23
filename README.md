# EcoShape Backend

API REST desarrollada con Flask para cálculos de volúmenes y resistencia de macetas y conos.

## 🛠 Tecnologías

- Python 3.8+
- Flask
- SymPy
- NumPy

## 📋 Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/jcgmU/EcoShapeBack.git
cd EcoShapeBack
```

2. Crear y activar entorno virtual:

```bash
python3 -m venv env
source env/bin/activate  # En macOS/Linux
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Iniciar el servidor:

```bash
python app.py
```

El servidor estará disponible en [http://localhost:5001](http://localhost:5001)

## 📚 Estructura del Proyecto

```
Backend/
├── app.py            # Aplicación principal Flask
├── requirements.txt  # Dependencias del proyecto
└── README.md        # Documentación
```

## 🔗 API Endpoints

### Volumen Maceta

POST `/api/volumen-maceta`

```json
{
  "R": float,  // Radio externo (cm)
  "H": float,  // Altura (cm)
  "t": float   // Espesor (cm)
}
```

### Resistencia Maceta

POST `/api/resistencia-maceta`

```json
{
  "C": float,        // Constante (MPa·mm)
  "H_mm": float,     // Altura (mm)
  "t_mm": float,     // Espesor (mm)
  "sigma_adm": float // Resistencia admisible (MPa)
}
```

### Volumen Cono

POST `/api/volumen-cono`

```json
{
  "R": float,  // Radio (cm)
  "e": float,  // Espesor (cm)
  "H": float   // Altura (cm)
}
```

## ✉️ Contacto

Juan Carlos - [@jcgmU](https://github.com/jcgmU)

Enlace del proyecto: [https://github.com/jcgmU/EcoShapeBack](https://github.com/jcgmU/EcoShapeBack)
