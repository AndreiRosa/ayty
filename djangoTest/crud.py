import django
from datetime import datetime
from django.db import connection
from pydantic import BaseModel
import modells


def create_extension(extension: str, nm_extension: str, is_active: bool, must_record: bool, number_transfer: str, was_exported: str) :
    cursor = connection.cursor()
    cursor.execute("INSERT INTO extension (extension, nm_extension, is_active, mustmodels.Boolean_record, number_transfer, was_exported) VALUES (%s, %s, %s, %s, %s, %s,)", [extension, nm_extension, is_active, must_record, number_transfer, was_exported])
    row = cursor.fetchone()
    return row

def create_extent_event(extension: str, status: str, dt_event: datetime, id_extension: int):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO exten_event (extension, status, dt_event, id_extension) VALUES (%s, %s, %s, %s)", [extension, status, dt_event, id_extension])
    row = cursor.fetchone()
    return row

def create_call( extension: str, nu_ddd: str, nu_phone: str, dt_start: datetime, dt_answer: datetime, dt_finish: datetime, id_extension: int):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO call (extension, nu_ddd, nu_phone, dt_start, dt_answer, dt_finish, id_extension) VALUES (%s, %s, %s, %s, %s, %s, %s)", [extension, nu_ddd, nu_phone, dt_start, dt_answer, dt_finish, id_extension])
    row = cursor.fetchone()
    return row

def update_dt_start(id_call: int, date: datetime):  
    cursor = connection.cursor()
    cursor.execute("UPDATE call SET dt_start = %s WHERE id_call = %s", [date, id_call])
    row = cursor.fetchone()
    return row

def update_dt_answer(id_call: int, date: datetime):  
    cursor = connection.cursor()
    cursor.execute("UPDATE call SET dt_answer = %s WHERE id_call = %s", [date, id_call])
    row = cursor.fetchone()
    return row

def update_dt_finish(id_call: int, date: datetime):  
    cursor = connection.cursor()
    cursor.execute("UPDATE call SET dt_finish = %s WHERE id_call = %s", [date, id_call])
    row = cursor.fetchone()
    return row

def update_extension(id_extension: int, extension: str, nm_extension: str, is_active: bool, must_record: bool, number_transfer: str):  
    cursor = connection.cursor()
    cursor.execute("UPDATE extension SET nm_extension = %s, is_active = %s, must_record = %s, number_transfer = %s, was_exported = 0, WHERE id_extension = %s", [nm_extension, is_active, must_record, number_transfer, id_extension])
    row = cursor.fetchone()
    return row

def delete_extension(id_extension: int):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM extension WHERE id_extension = ", [id_extension])
    row = cursor.fetchone()
    return row

def get_extension_by_id(id_extension: int):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM extension WHERE id_extension = ", [id_extension])
    row = cursor.fetchone()
    return row

def get_extensions():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM extension")
    row = cursor.fetchone()
    return row

def get_call_time(id_call: int):
    cursor = connection.cursor()
    cursor.execute("SELECT dt_answer, dt_finish, DATEDIFF (minute, dt_answer, dt_finish) as call_duration FROM call WHERE id_call = ", [id_call])
    row = cursor.fetchone()
    return row

def get_call_by_extension_and_date(id_extension: int, date: datetime):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM call WHERE (id_extension LIKE %s) AND (dt_start LIKE %s)", [id_extension, date])
    row = cursor.fetchone()
    return row

def get_extentevent_by_extension_and_date(id_extension: int, dt_event: datetime):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM exten_event WHERE (id_extension LIKE %s) AND (dt_event LIKE %s)", [id_extension, dt_event])
    row = cursor.fetchone()
    return row