# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
# Author: Patrick Galbraith <patg@hp.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# should this be in schema.py?
from uuid import uuid4
from migrate import *
from sqlalchemy import ForeignKey
from sqlalchemy import (Enum)
from sqlalchemy.schema import (Column, MetaData)
from sqlalchemy.orm import relationship, backref
from moniker.database.sqlalchemy.migrate_repo.schema import (
    Table, Integer, String, Text, create_tables, 
    UUID, drop_tables, DateTime, RECORD_TYPES)
from moniker.database.sqlalchemy.types import (
    Inet)
from moniker.openstack.common import timeutils

meta = MetaData()

domains = Table('domains', meta,
                Column('id', UUID(), default=uuid4, primary_key=True),
                Column('created_at', DateTime(), default=timeutils.utcnow),
                Column('updated_at', DateTime(), onupdate=timeutils.utcnow),
                Column('version', Integer(), default=1, nullable=False),
                Column('tenant_id', String(36), default=None, nullable=True),
                Column('name', String(255), nullable=False, unique=True),
                Column('email', String(36), nullable=False),
                Column('ttl', Integer(), default=3600, nullable=False),
                Column('refresh', Integer(), default=3600, nullable=False),
                Column('retry', Integer(), default=3600, nullable=False),
                Column('expire', Integer(), default=3600, nullable=False),
                Column('minimum', Integer(), default=3600, nullable=False),
                useexisting=True)

servers = Table('servers', meta,
                Column('id', UUID(), default=uuid4, primary_key=True),
                Column('created_at', DateTime(), default=timeutils.utcnow),
                Column('updated_at', DateTime(), onupdate=timeutils.utcnow),
                Column('version', Integer(), default=1, nullable=False),
                Column('name', String(255), nullable=False, unique=True),
                Column('ipv4', Inet(), nullable=False, unique=True),
                Column('ipv6', Inet(), default=None, unique=True),
                useexisting=True)

records = Table('records', meta,
                Column('id', UUID(), default=uuid4, primary_key=True),
                Column('created_at', DateTime(), default=timeutils.utcnow),
                Column('updated_at', DateTime(), onupdate=timeutils.utcnow),
                Column('version', Integer(), default=1, nullable=False),
                Column('type', Enum(name='record_types', *RECORD_TYPES),
                       nullable=False),
                Column('name', String(255), nullable=False),
                Column('data', Text(), nullable=False),
                Column('priority', Integer(), default=None),
                Column('ttl', Integer(), default=3600, nullable=False),
                Column('domain_id', UUID(), ForeignKey('domains.id'),
                       nullable=False),
                useexisting=True)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tables = [domains, servers, records, ]
    create_tables(tables)


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    tables = [domains, servers, records, ]
    drop_tables(tables)
