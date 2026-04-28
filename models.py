from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from database import Base


class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    status = Column(Boolean, nullable=True)
    descricao = Column(String(150))
    produto = relationship("Produto", back_populates="categorias")

    def __repr__(self):
        return f"Categoria: id: {self.id} - nome: {self.nome} - status: {self.status} - descricao: {self.descricao}"
    


class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    estoque = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto = id: {self.id} - nome: {self.nome} - Estoque: {self.estoque} - Preco: {self.preco}"