import asyncio
from fastapi import FastAPI, Body
import uvicorn
from app import *
from checks import check_if_text_in_docx, check_item_quantity

# from transformers import pipeline
# from ruclip_check_photo import check_photo_function

app = FastAPI()


@app.get("/api/")
async def default_endpoint():
    return "Hello, i'm python web app"


@app.post("/api/check_title")
async def check_title(data=Body()):
    """Проверка наименования"""
    try:
        input_title = str(data["title"])
        file_bytes = data["file"]["buffer"]["data"]
        return check_if_text_in_docx(input_title, file_bytes)
    except Exception as ex:
        print(ex)


@app.post("/api/check_quantity")
async def check_quantity(data=Body()):
    """
    Проверка того, что количество товаров в КС
    соответствует количеству в ТЗ
    """
    try:
        product_items = data['specifications']
        file_bytes = data["file"]["buffer"]["data"]
        return check_item_quantity(product_items, file_bytes, "Проверка количества товаров выполнена успешно")
    except Exception as ex:
        print(ex)


@app.post("/api/check_contract_enforced")
async def check_contract_enforced(data=Body()):
    """Проверка обеспечения исполнения контракта"""
    try:
        contract_enforced = str(data["contractEnforced"])
        return check_contract_enforced_function(contract_enforced)
    except Exception as ex:
        print(ex)


@app.post("/api/check_photo")
async def check_photo(data=Body()):
    """Проверка фото"""
    try:
        specifications = data["specifications"]
        photos = [{'photo_url': item['image'], 'name': item['title']} for item in specifications]
        ret
        # return check_photo_function(photos)
    except Exception as ex:
        print(ex)


async def run():
    config = uvicorn.Config("main:app", host="127.0.0.1", port=5300, log_level="info", loop="none")
    server = uvicorn.Server(config)
    await server.serve()


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run())
    loop.close()


if __name__ == '__main__':
    main()
