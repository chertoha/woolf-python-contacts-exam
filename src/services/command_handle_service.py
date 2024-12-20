from typing import List
from decorators.catch import catch


class CommandHandleService:

    @staticmethod
    @catch
    def add(args: List[str]):
        print("add")

    @staticmethod
    @catch
    def find(args: List[str]):
        print("find")

    @staticmethod
    @catch
    def update(args: List[str]):
        print("update")

    @staticmethod
    @catch
    def birthday(args: List[str]):
        print("birthday")
