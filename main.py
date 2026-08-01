from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)




# Para executar o nosso codigo roda isso no terminal > uvicorn main:app --reload

# endpoints:
# dominio.com/pedidos/lista

# Rest APIs
# GET -> leitura/pegar
# Post -> Enviar/criar
# Put/Patch -> edição
# Delete -> deletar

