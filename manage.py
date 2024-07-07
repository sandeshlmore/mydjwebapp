#!/usr/bin/env python

#Labour’s victory was seismic. It was very nearly unprecedented; only Tony Blair’s Labour Party has ever won more seats in an election.

#Addressing the nation before entering 10 Downing Street on Friday afternoon, Starmer pledged a return to the politics of public service, vowing to heal the “weariness at the heart of the nation” with “action not words.”

#But Labour’s win was also fragile. The vote breakdown made clear that the election was as much, if not more, about the public’s anger towards the Conservatives as it was about excitement for Labour’s offer.

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
