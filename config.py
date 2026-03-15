from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_file": ".env"}

    api_key: SecretStr = Field(alias="openai_api_key")
    model_name: str = "gpt-5.4"

    max_search_results: int = 5
    max_url_content_length: int = 5000
    output_dir: str = "output"
    max_iterations: int = 10


Settings = Settings()

SYSTEM_PROMPT = "Ти - персональний асистент з проведення досліджень. " \
                "Після отримання запиту від користувача виконай відповідне дослідження відкритих джерел в Інтернет, " \
                "зроби звіт у форматі markdown та запиши його у файл. " \
                "Якщо не вдається знайти достатньо інформації, сформуй звіт на основі вже зібраних даних. " \
                "У звіті вкажи перелік використаних джерел. " \
                "Результат формуй українською мовою (для спеціальних термінів можна використовувати англійську)."

SEARCH_ENGINE = "google"
