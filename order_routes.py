from fastapi import APIRouter

order_router = APIRouter(prefix='/order', tags=['order'])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos. Todas as rotas dos pedidos precisam de autenticação.
    """
    return {"mensagem:" "Voce acessou a rota de pedidos "}

