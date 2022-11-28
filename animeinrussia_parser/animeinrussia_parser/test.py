#!/usr/bin/env python3

import datetime
from sqlalchemy.sql import select
from animeinrussia_parser.db import engine, shows

with engine.connect() as conn:

    t = datetime.datetime.now()

    stmt = shows.select()

    stmt = shows.select().where(shows.c.source_url == "test")

    # stmt = shows.insert().values(created_at=t, updated_at=t, source_url='test')
    res = conn.execute(stmt).first()
    print(dict(res))

    # stmt = select(shows).where(())
