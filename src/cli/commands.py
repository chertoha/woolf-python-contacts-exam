from typing import List
from cli.config import Commands
from decorators.catch import catch
from exceptions.wrong_command_exception import WrongCommandException
from services.command_handle_service import CommandHandleService


commands = {
    Commands.ADD: CommandHandleService.add,
    Commands.FIND: CommandHandleService.find,
    Commands.UPDATE: CommandHandleService.update,
    Commands.BIRTHDAY: CommandHandleService.birthday,
}


@catch
def execute_command(command: str, args: List[str]):
    if any(cmd.value == command for cmd in Commands):
        handler = commands[Commands(command)]
        handler(args)
    else:
        raise WrongCommandException()
