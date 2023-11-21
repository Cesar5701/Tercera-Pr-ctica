
# Web Scraping y Procesamiento de Texto con Clustering Aglomerativo

Este proyecto implementa un proceso de extracción de datos web (web scraping) usando Scrapy, seguido por un análisis y procesamiento de texto en Python. El objetivo es extraer contenido de páginas web, procesarlo y luego aplicar un clustering aglomerativo para agrupar textos basándose en su similitud.

## Descripción

El flujo de trabajo del proyecto es el siguiente:

1. **Web Scraping**: Se usa Scrapy para extraer contenido de páginas web especificadas.
2. **Procesamiento de Texto**: Se procesan los textos scrapeados para eliminar HTML, tokenizar, normalizar y eliminar stopwords.
3. **Creación de Diccionario de Términos**: Se crea un diccionario con términos únicos a partir de los textos procesados.
4. **Clustering Aglomerativo**: Se usa el método de Ward para agrupar los textos según su similitud.

## Configuración

### Requisitos

- Python 3.x
- NLTK
- Scrapy
- BeautifulSoup
- NumPy
- Scikit-Learn

### Instalación

Para instalar las dependencias necesarias, ejecute el siguiente comando:

```bash
pip install scrapy nltk beautifulsoup4 numpy scikit-learn
```

Asegúrese de tener instalado Python 3 y pip en su sistema.

### Descarga de recursos NLTK

Para descargar los recursos necesarios de NLTK, ejecute los siguientes comandos en Python:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Ejecución

Para ejecutar el proyecto, siga estos pasos:

1. Inicie el proceso de web scraping con el comando adecuado (ajuste la ruta y los parámetros según sea necesario):

    ```bash
    scrapy crawl sp_ward -a start_url=<URL> -a depth=<DEPTH>
    ```

2. Ejecute el script de Python que contiene el código de procesamiento de texto y clustering.

## Contribuir

Las contribuciones al proyecto son bienvenidas. Por favor, asegúrese de actualizar los tests según corresponda.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
