#!/usr/bin/env python3
from sqlalchemy import create_engine, MetaData
from sqlalchemy.schema import Table
from scrapy.utils.project import get_project_settings

metadata_obj = MetaData()

def db_connect():
    engine = create_engine(
        get_project_settings().get("DB_CONNECTION"),
        connect_args={"connect_timeout": 5},
    )
    return engine

engine = db_connect()

shows = Table('air_show', metadata_obj, autoload_with=engine)
