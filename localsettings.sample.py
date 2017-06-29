# Settings for event_to_things

# URL of your iCal calendar
URL = "https://calendar.google.com/calendar/ical/yourgmail/private-blahblahblah/basic.ics"

# Where to store your calendar on your local computer.
FILENAME = "/tmp/calendar.ics"

# Where to keep a log of events for which todos have already been made.
LOG = "/Users/you/repos/event_to_things/log"

# Where is wget?
WGET="/usr/local/bin/wget"

# Where is the newtodo.sh script?
NEWTODO="/Users/you/repos/event_to_things/newtodo.sh"

data = (
    {
        'if_event_matches': ['wedding', 'marriage', 'marries', 'weds', 'hitched'],

        'remind_me_to': "Review wedding checklist",

        # This will be added to the 'notes' section of the todo.
        'notes': 'https://docs.google.com/document/d/blahblahblah/edit',

        # Options are in event_to_things.py in the `notice_options` dictionary.
        'when': ['one day before', 'one week before']
    },
    {
        'if_event_matches': ['flight', 'travel', 'fly'],
        'remind_me_to': "Review travel checklist",
        'notes': 'https://docs.google.com/document/d/yaddayaddayadda/edit',
        'when': ['one day before', 'one week before']
    },
    # Add more stuff here. Don't forget to put commas between the dictionaries,
    # and between the items in each dictionary.
)
