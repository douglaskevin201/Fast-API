from fastapi import APIRouter
from models import Usuario
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.get('/')
async def home():
    """
    Essa é a rota padrão do nosso sistema
    """
    return {"Mensagem": "Você acessou a rota padrão de autenticação", "autenticação": False}


@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email==email)
    if usuario:
        return {"mensagem": "Já existe um usuario com esse email"}
    else:
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": "Usuario cadastrado com sucesso"}