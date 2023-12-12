# alembic/env.py

from alembic import context
from sqlalchemy import engine_from_config, pool, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from models import Base  

# Load the SQLAlchemy URL from the config
config = context.config
engine = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix='sqlalchemy.',
)
Session = scoped_session(sessionmaker(bind=engine))


target_metadata = Base.metadata
