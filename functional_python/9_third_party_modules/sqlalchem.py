import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.dialects.mysql import DOUBLE, INTEGER, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


DB_URI = "mysql+mysqlconnector://appyens:Gpa$$i0n@localhost:3306/threatdb"
DB_URI2 = 'sqlite:///:memory:'
ENGINE = create_engine(DB_URI, echo=True)
# conn = ENGINE.connect()
Base = declarative_base()


class BlockedIPs(Base):
    __tablename__ = 'blocked_ips'
    id = Column('id', INTEGER, primary_key=True)
    ip_address = Column('ip_address', String(50), nullable=False)
    reliability = Column('reliability', INTEGER, nullable=True)
    priority = Column('priority', INTEGER, nullable=True)
    activity = Column('activity', String(128), nullable=True)
    sub_category = Column('sub_category', String(128), nullable=True)
    country = Column('country', String(128), nullable=True)
    city = Column('city', String(128), nullable=True)
    latitude = Column('latitude', DOUBLE, nullable=True)
    longitude = Column('longitude', DOUBLE, nullable=True)
    source = Column('source', String(128), nullable=True)
    target = Column('target', String(128), nullable=True)
    dest_port = Column('dest_port', INTEGER, nullable=True)
    last_online = Column('last_online', String(128), nullable=True)
    first_seen = Column('first_seen', String(128), nullable=True)
    used_by = Column('used_by', String(128), nullable=True)
    reference_link = Column('reference_link', String(128), nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=False,  server_default=func.now())
    updated_at = Column('updated_at', TIMESTAMP, nullable=False, server_default=func.now())
    revision = Column('revision', Integer, nullable=False)


class MalwareURLs(Base):
    __tablename__ = 'malware_urls'
    id = Column('id', INTEGER, primary_key=True)
    url = Column('url', String(256), nullable=False)
    domain = Column('domain', String(256), nullable=True)
    filename = Column('filename', String(256), nullable=True)
    priority = Column('priority', String(256), nullable=True)
    file_type = Column('file_type', String(256), nullable=True)
    country = Column('country', String(256), nullable=True)
    url_status = Column('url_status', String(256), nullable=True)
    date_added = Column('date_added', String(256), nullable=True)
    threat_type = Column('threat_type', String(256), nullable=True)
    threat_tag = Column('threat_tag', String(256), nullable=True)
    created_at = Column('created_at', TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = Column('updated_at', TIMESTAMP, nullable=False, server_default=func.now())


Base.metadata.create_all(bind=ENGINE)
session = sessionmaker(bind=ENGINE)()
ips = BlockedIPs()
urls = MalwareURLs()
session.add()
session.commit()

