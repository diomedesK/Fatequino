import json
import os
from src.database.sqlite.models.classes import Classes

CURRENT_DIR, _ = os.path.split(os.path.abspath(__file__))


class ClassService:
    def __init__(self) -> None:
        self.classes = Classes()

    def create(self) -> list:
        data = []
        try:
            data = self.classes.find_all({})
            if len(data) > 0:
                return data

            classes = json.loads(open(os.path.join(CURRENT_DIR, '../database/static/aulas.json'), 'r').read())
            for _class in classes:
                row = self.classes.create(self.__to_database_dict(_class))
                data.append(row)
            return data
        except Exception as e:
            raise e

    def __to_database_dict(self, data: dict) -> dict:
        _class = {
            "class": data['Disciplina'],
            "course": data['Curso'],
            "period": data['Turno'],
            "semester": data['Ciclo'],
            "week_day": data['Dia'],
            "start_time": data['Horario'],
            "professor": data['Professor'],
            "room_number": data['Sala'],
            "class_per_day": data['Aulas']
        }
        return _class
