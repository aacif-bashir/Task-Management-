import utils.transport
import utils.session
from fastapi import FastAPI
from src.utils.db import Base, engine

Base.metadata.create_all(engine)
app = FastAPI(title="Task Management")