# Settings for event_to_things
URL = "https://calendar.google.com/calendar/ical/yourgmail/private-blahblahblah/basic.ics"
FILENAME = "/tmp/calendar.ics"
LOG = "/Users/you/repos/event_to_things/log"
WGET="/usr/local/bin/wget"
NEWTODO="/Users/you/repos/event_to_things/newtodo.sh"

data = (
    {
        'if_event_matches': ['wedding', 'marriage', 'marries', 'weds', 'hitched'],
        'remind_me_to': "Review wedding checklist",
        'notes': 'https://docs.google.com/document/d/blahblahblah/edit',
        'when': ['one day before', 'one week before']
    },
    {
        'if_event_matches': ['flight', 'travel', 'fly'],
        'remind_me_to': "Review travel checklist",
        'notes': 'https://docs.google.com/document/d/yaddayaddayadda/edit',
        'when': ['one day before', 'one week before']
    },
)
