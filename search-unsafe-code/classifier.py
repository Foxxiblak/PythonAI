from dataclasses import dataclass
from enum import Enum
from typing import List

class Severity(str, Enum):
    CRITICAL = "critical"
    MEDIUM = "medium"
    LOW = "low"

@dataclass(frozen=True)
class Vulnerability:
    class_id: str
    name: str
    level: Severity
    keyword: str


vulnerabilities: List[Vulnerability] = [
    Vulnerability("A1", "SQL-инъекция", Severity.CRITICAL, "SELECT * FROM"),
    Vulnerability("A2", "Выполнение команд оболочки", Severity.CRITICAL, "Runtime.getRuntime().exec"),
    Vulnerability("A3", "XSS (Межсайтовый скриптинг)", Severity.CRITICAL, 'echo $_GET'),
    Vulnerability("A4", "Жестко закодированные учетные данные", Severity.CRITICAL, 'api_key'),
    Vulnerability("A5", "Отсутствие проверки вводимых данных", Severity.CRITICAL, 'request.GET['),

    Vulnerability("B1", "CSRF", Severity.MEDIUM, "POST"),
    Vulnerability("B2", "Неправильное управление сессиями", Severity.MEDIUM, 'session_id'),
    Vulnerability("B3", "Уязвимости при работе с файлами", Severity.MEDIUM, 'move_uploaded_file($_FILES'),
    Vulnerability("B4", "Отсутствие шифрования данных", Severity.MEDIUM, 'http://'),

    Vulnerability("C1", "Использование уязвимых библиотек", Severity.LOW, 'requests==2.18'),
    Vulnerability("C2", "Ошибки конфигурации", Severity.LOW, 'DEBUG = True'),
    Vulnerability("C3", "Необработанные исключения", Severity.LOW, 'catch(Exception e) { e.printStackTrace() }'),
]