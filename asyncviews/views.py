import asyncio
from time import sleep
import httpx
from django.http import HttpResponse


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    print('Operação assíncrona concluída')
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://www.example.com")
            print(response)
        except httpx.RequestError as exc:
            print(f"Erro ao fazer a requisição HTTP: {exc}")

