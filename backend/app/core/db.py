import logging
from sqlmodel import Session, create_engine, select

from app.core.config import settings
import app.models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-template/issues/28
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next lines
    from sqlmodel import SQLModel

    # from app.core.engine import engine
    # This works because the models are already imported and registered from app.models
    SQLModel.metadata.create_all(engine)

    person = session.exec(select(app.models.Person)).first()
    if not person:
        logger.info("No one is in the DB. Creating a person.")
        new_person = app.models.PersonCreate(name="Richard Paredes", age=25)
        person = app.models.Person.model_validate(new_person)
        session.add(person)
        session.commit()
        session.refresh(person)
    else:
        logger.info("Person is already created!")
    logger.info(f"Person: {person}")
