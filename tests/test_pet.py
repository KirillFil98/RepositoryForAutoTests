import allure
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Pet")
class TestPet:
    @allure.title("Попытка удалить несуществующего питомца")
    def test_delete_nonexistent_pet(self):
        with allure.step("Отправка запроса на удаление несуществующего питомца"):
            responce = requests.delete(url=f"{BASE_URL}/pet/9999")

        with allure.step("Проверка статуса ответа"):
            assert responce.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текстового ответа"):
            assert responce.text == "Pet deleted", "Текст ответа не совпал с ожидаемым"

    @allure.title("Попытка обновить несуществующего питомца")
    def test_update_nonexistent_pet(self):
        with allure.step("Отправка запроса на обновление несуществующего питомца"):
            payload = {
                "id": 9999,
                "name": "Non-existent Pet",
                "status": "available"
            }
            responce = requests.put(url=f"{BASE_URL}/pet", json=payload)

        with allure.step("Проверка статуса ответа"):
            assert responce.status_code == 404, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текстового ответа"):
            assert responce.text == "Pet not found", "Текст ответа не совпал с ожидаемым"