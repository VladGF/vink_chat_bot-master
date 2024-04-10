import requests


def yandex_gpt(question):
    FOLDER_ID = "b1gm7s7g99jm6hpbg6p0"
    IAM_TOKEN = "AQVN2OKYYRKGFRB8lsFXc5yiJwwxKS1VpLEcOnZu"
    prompt = {
        "modelUri": f"gpt://{FOLDER_ID}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
            },
        "messages": [
            {
                "role": "system",
                "text": (
                    "Ты консультант по имени Виктор чата поддержки в"
                    " магазине материалов и оборудования для рынка "
                    "визуальных офлайн-коммуникаций 'Vink'. "
                    "Компания 'Vink' предоставляет полный спектр услуг "
                    "по ремонту и обслуживанию широкоформатного печатного "
                    "и режущего оборудования. Номер телефона "
                    "службы поддержки: 8 800 550 7888"),
            },
            {
                "role": "user",
                "text": question
            }
        ]}
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {IAM_TOKEN}",
        "x-folder-id": "b1gm7s7g99jm6hpbg6p0"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    return result["result"]["alternatives"][0]["message"]["text"]
