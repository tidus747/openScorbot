import os, platform, logging
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
import logging.handlers as handlers
import time

if platform.platform().startswith('Windows'):
    fichero_log = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'openscorbot.log')
else:
    fichero_log = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'openscorbot.log')

logger = logging.getLogger('main')
logger.setLevel(logging.INFO) #Limitamos a INFO como el log de menor nivel
                              #Filtramos los DEBUG y NOTSET

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s - [%(filename)s] %(message)s',
                    datefmt='%d/%m/%y %H:%M:%S',
                    filename = fichero_log,
                    filemode = 'a')

logHandler = handlers.TimedRotatingFileHandler(filename ='openscorbot.log',
                                                when='midnight')
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

#logging.debug('Comienza el programa')
#logging.info('Procesando con normalidad')
#logging.error('',exc_info=True) #exc_info a TRUE incluye la ruta y linea del error
#logging.warning('Advertencia')
