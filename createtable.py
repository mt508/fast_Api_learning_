from database import Base, engine
import model   # IMPORTANT

Base.metadata.create_all(bind=engine)