from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Float, BigInteger
from sqlalchemy.orm import declarative_base
from connection import connect_DDBB
import logging

'''
Este script me permite crear las tablas con sus relaciones
'''

logging.basicConfig(filename='modelado.log',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d - %m - %Y')

engine = connect_DDBB()
Base = declarative_base()



class dim_tienda(Base):
    __tablename__ = 'dim_tienda'
    id_tienda = Column(Integer, primary_key=True)
    tipo_tienda = Column(String, nullable=False)

class dim_barrio(Base):
    __tablename__ = 'dim_barrio'
    id_barrio = Column(Integer, primary_key=True)
    nombre_barrio = Column(String, nullable=False)

class dim_codigo_tienda(Base):
    __tablename__ = 'dim_codigo_tienda'
    id_codigo_tienda = Column(Integer, primary_key=True)
    codigo_tienda = Column(Integer, nullable=False)
    id_barrio = Column(Integer, ForeignKey('dim_barrio.id_barrio'), nullable=False)
    id_tienda = Column(Integer, ForeignKey('dim_tienda.id_tienda'))

class dim_coordenada(Base):
    __tablename__ = 'dim_coordenada'
    id = Column(Integer, primary_key=True)
    latitud_tienda = Column(Float, nullable=False)
    longitud_tienda = Column(Float, nullable=False)
    id_codigo_tienda = Column(Integer, ForeignKey('dim_codigo_tienda.id_codigo_tienda'), nullable=False)



class dim_documentos(Base):
    __tablename__ = 'dim_documentos'
    id_documento = Column(Integer, primary_key=True)
    num_documento_cliente = Column(BigInteger, nullable=False)

class dim_tipo_documento(Base):
    __tablename__ = 'dim_tipo_documento'
    tipo_documento_cliente = Column(Integer, primary_key=True)
    descripcion = Column(String, nullable=False)


class Fact_table(Base):
    __tablename__ = 'fact_table'
    id_table = Column(Integer, primary_key=True)
    fecha_compra = Column(Date, nullable=False)
    id_codigo_tienda = Column(Integer, ForeignKey('dim_codigo_tienda.id_codigo_tienda'), nullable=False)
    id_documento = Column(Integer, ForeignKey('dim_documentos.id_documento'), nullable=False)
    tipo_documento_cliente = Column(Integer, ForeignKey('dim_tipo_documento.tipo_documento_cliente'), nullable=False)

try:

    Base.metadata.create_all(engine)
    logging.info('Se crearon las tablas')

except Exception as e:
    logging.error(e)