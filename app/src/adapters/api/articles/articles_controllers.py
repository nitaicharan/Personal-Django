from fastapi import APIRouter
from fastapi_injector import Injected


import abc
from abc import abstractmethod


class SomeInterface(abc.ABC):
    @abstractmethod
    async def create_some_entity(self) -> str:
        pass


class SomeSavePort(abc.ABC):
    @abc.abstractmethod
    async def save_something(self) -> None:
        pass


class SomeService(SomeInterface):
    def __init__(self, save_port=Injected(SomeSavePort)):
        self.save_port = save_port

    async def create_some_entity(self) -> str:
        return "test 0"


class SomeRepository(SomeSavePort):
    async def save_something(self) -> str:
        return "test 1"


router = APIRouter()


@router.get("")
def list(useCase: SomeInterface = Injected(SomeInterface)):
    return useCase.create_some_entity()
