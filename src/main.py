from cli.commands import execute_command
from cli.parser import parse_input
from services.command_handle_service import CommandHandleService


def main() -> None:

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["exit", "quit", "end"]:
            print("Bye!")
            break

        execute_command(command, args)


if __name__ == "__main__":
    main()
