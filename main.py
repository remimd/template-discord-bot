import sys

from services.environment import set_environment


def main():
    set_environment()

    from django.core.management import execute_from_command_line

    execute_from_command_line(argv=sys.argv)


if __name__ == "__main__":
    main()
