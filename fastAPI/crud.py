from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def create_call(db: Session, call: schemas.CallCreate, id_extension = int):
    db_call = models.Call(extension=call.extension, nu_ddd=call.nu_ddd, nu_phone=call.nu_phone, dt_start=call.dt_start, dt_answer=call.dt_answer, dt_finish=call.dt_finish, owner_id=id_extension)
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call

def create_extent_event(db: Session, extent_event: schemas.ExtentEventCreate, id_extension = int):
    db_extent_event = models.Extent_event(extension=extent_event.extension, status=extent_event.status, dt_event=extent_event.dt_event, owner_id=id_extension)
    db.add(db_extent_event)
    db.commit()
    db.refresh(db_extent_event)
    return db_extent_event

def create_extension(db: Session, extension: schemas.ExtensionCreate):
    db_extension = models.Extension(extension=extension.extension,nm_extension=extension.nm_extension, is_active=extension.is_active, must_record=extension.must_record, number_transfer=extension.number_transfer, was_exported=extension.was_exported)
    db.add(db_extension)
    db.commit()
    db.refresh(db_extension)
    return db_extension


def get_extension_by_id(db: Session, extension_id: int):
    return db.query(models.Extension).filter(models.Extension.id_extension == extension_id).first()

def get_extensions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Extension).offset(skip).limit(limit).all()

def get_call_time(db: Session, call_id: int):
    return db.query(models.Call).filter(models.Call.id_call == call_id).first()

def get_call_by_extension_and_date(db: Session, extension_id: int, date: datetime):
    return db.query(models.Call).filter(models.Call.dt_start == date and models.Extension.id == extension_id).first()

def get_extentevent_by_extension_and_date(db: Session, extension_id: int, date: datetime):
    return db.query(models.Extent_event).filter(models.Extent_event.dt_event == date and models.Extension.id == extension_id).first()

def update_dt_answer(db: Session, call_id: int, date: datetime):  
    db.query(models.Call).filter(models.Call.id_call == call_id).update({"dt_answer":date}, synchronize_session='fetch')
    db.commit()

def update_dt_start(db: Session, call_id: int, date: datetime):  
    db.query(models.Call).filter(models.Call.id_call == call_id).update({"dt_start":date}, synchronize_session='fetch')
    db.commit()

def update_dt_finish(db: Session, call_id: int, date: datetime):  
    db.query(models.Call).filter(models.Call.id_call == call_id).update({"dt_finish":date}, synchronize_session='fetch')
    db.commit()

def update_extension(db: Session, extension_id: int, extension: str, nm_extension: str, is_active: bool, must_record: bool):  
    db.query(models.Extension).filter(models.Extension.id_extension == extension_id).update({"extension":extension}, {"was_exported":0}, {"nm_extension": nm_extension}, {"is_active": is_active}, {"must_record": must_record}, synchronize_session='fetch')
    db.commit()

def delete_extension(db: Session, extension_id: int):
    db.query(models.Extension).filter(models.Extension.id_extension == extension_id).delete(synchronize_session='fetch')
    db.commit()
