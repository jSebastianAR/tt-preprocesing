FROM python:3.7.7

#Carpeta que contendrá todo lo necesario para el proceso
RUN mkdir /home/preprocessing
#Carpeta para almacenar los archivos de la nueva etapa
RUN mkdir /home/Archivos_Etapa_4/
#Carpeta donde se comparte el key.pickle
RUN mkdir /home/shared_container/
#Carpeta creada para almacenar los archivos a usar para etapa 3(los archivos de la etapa anterior, la 2)
RUN mkdir -p /home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/Archivos_Etapa_3/
COPY Archivos_Etapa_3/ /home/jsebastian-ar/Documentos/git-repos/tt-preprocesing/WheaterScript/Archivos_Etapa_3/
#Se establece el working directory donde está el automatizer.py
WORKDIR /home/preprocessing
#Copia todos los .py y resto de dependencias
COPY project_data/ ./
#Copia el archivo que tiene todas las dependencias del ambiente de python 3.7.7
COPY py3_dependences.txt /home/preprocessing
#Instala las dependencias de python
RUN pip install -r py3_dependences.txt
#Comando para iniciar el automatizador de llenado
CMD [ "python", "automatizer.py" ]
