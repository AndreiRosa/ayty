from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import models, schemas
import crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/call/", response_model=schemas.Call)
def create_call(id_extension: int, call: schemas.CallCreate, db: Session = Depends(get_db)):
    return crud.create_call(db=db, call=call, id_extension=id_extension)

@app.post("/extent_event/", response_model=schemas.ExtentEvent)
def create_extent_event(id_extension: int, extent_event: schemas.CallCreate, db: Session = Depends(get_db)):
    return crud.create_extent_event(db=db, extent_event=extent_event, id_extension=id_extension)

@app.post("/extension/", response_model=schemas.Extension)
def create_extension(extension: schemas.ExtensionCreate, db: Session = Depends(get_db)):
    return crud.create_extension(db=db, extension=extension)

@app.get("/extension/{id_extension}", response_model=schemas.Extension)
def read_extension_by_id(extension_id: int, db: Session = Depends(get_db)):
    db_extension = crud.get_extension_by_id(db, extension_id=extension_id)
    if db_extension is None:
        raise HTTPException(status_code=404, detail="Extension not found")
    return db_extension

@app.get("/extension/", response_model=List[schemas.Extension])
def read_extensions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    extension = crud.get_extensions(db, skip=skip, limit=limit)
    return extension

@app.get("/call/{id_call}", response_model=schemas.Call)
def read_call_by_id(call_id: int, db: Session = Depends(get_db)):
    db_call = crud.get_call_time(db, call_id=call_id)
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call

@app.get("/call/{id_extension}", response_model=schemas.Call)
def read_call_by_id_date(extension_id: int, date: datetime, db: Session = Depends(get_db)):
    db_call = crud.get_call_by_extension_and_date(db, extension_id=extension_id, date=date)
    if db_call is None:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call

@app.get("/extent_event/{id_extension}", response_model=schemas.ExtentEvent)
def read_extentevent_by_id_date(extension_id: int, date: datetime, db: Session = Depends(get_db)):
    db_extent_event = crud.get_call_by_extension_and_date(db, extension_id=extension_id, date=date)
    if db_extent_event is None:
        raise HTTPException(status_code=404, detail="Extent event not found")
    return db_extent_event

@app.post("/extension/{id_extension}", response_model=schemas.Extension)
def update_extension(id_extension: int, extension: str, nm_extension: str, is_active: bool, must_record: bool, db: Session = Depends(get_db)):
    return crud.update_extension(db=db, extension_id=id_extension, extension=extension, nm_extension=nm_extension, is_active=is_active, must_record=must_record)

@app.post("/call/{id_call}", response_model=schemas.Call)
def update_dt_answer(id_call: int, date: datetime, db: Session = Depends(get_db)):
    return crud.update_dt_answer(db=db, call_id=id_call, date=date)

@app.post("/call/{id_call}", response_model=schemas.Call)
def update_dt_start(id_call: int, date: datetime, db: Session = Depends(get_db)):
    return crud.update_dt_start(db=db, call_id=id_call, date=date)

@app.post("/call/{id_call}", response_model=schemas.Call)
def update_dt_finish(id_call: int, date: datetime, db: Session = Depends(get_db)):
    return crud.update_dt_finish(db=db, call_id=id_call, date=date)

@app.post("/extension/{id_extension}", response_model=schemas.Extension)
def delete_extension(id_extension: int, extension: str, db: Session = Depends(get_db)):
    return crud.delete_extension(db=db, extension_id=id_extension)