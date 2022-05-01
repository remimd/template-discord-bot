from django.core.management import BaseCommand, call_command

from services import logs


class Command(BaseCommand):
    help = "Initialize BDD"

    def handle(self, *args, **options):
        logs.info("Reset database")
        call_command("reset_db", "--noinput", "-c")
        logs.ok("Reset successful")

        logs.info("Apply migrations")
        call_command("migrate", interactive=False)
