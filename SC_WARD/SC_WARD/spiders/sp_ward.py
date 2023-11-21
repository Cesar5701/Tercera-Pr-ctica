import scrapy
import os
from urllib.parse import urlparse
from datetime import datetime


class SpWardSpider(scrapy.Spider):
    name = 'sp_ward'
    
    def __init__(self, start_url=None, depth=None, *args, **kwargs):
        super(SpWardSpider, self).__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.depth = int(depth) if depth is not None else 1

        # Crear un identificador único para esta sesión de crawling
        self.session_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.session_path = os.path.join('paginas', self.session_id)
        if not os.path.exists(self.session_path):
            os.makedirs(self.session_path)
            
    def parse(self, response):
        # Parsea el URL para crear un nombre de archivo seguro
        parsed_url = urlparse(response.url)
        filename = f"{parsed_url.netloc}{parsed_url.path}".replace('/', '_') + '.txt'
        
        # Guarda el contenido de la página en un archivo en la subcarpeta
        with open(os.path.join(self.session_path, filename), 'wb') as f:
            f.write(response.body)

        # Sigue los enlaces de la página
        for href in response.css('a::attr(href)').getall():
            yield response.follow(href, callback=self.parse)


            
