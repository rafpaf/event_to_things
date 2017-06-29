#!/usr/bin/env python

from subprocess import call
import pytz
import os

import datetime
from dateutil.relativedelta import relativedelta

from icalendar import Calendar, vDatetime

from localsettings import *

notice_options = {
    'one day before': datetime.timedelta(days=-1),
    'three days before': datetime.timedelta(days=-3),
    'one week before': datetime.timedelta(days=-7),
    'two weeks before': datetime.timedelta(days=-14),
    'one month before': relativedelta(months=-1)
}

call([WGET, URL, "-O", FILENAME])

with open(FILENAME,'rb') as calfile:
    cal = Calendar.from_ical(calfile.read())

    today = pytz.UTC.localize(datetime.datetime.today())

    # Create log if it doesn't exist
    if not os.path.exists(LOG):
        call(['touch',LOG]) # obviously not the canonical method

    with open(LOG,'rb') as log:
        already_logged = [line.decode('utf-8') for line in log.read().splitlines()]

    with open(LOG,'a') as log:
        for component in cal.walk():
            for row in data:
                if component.name == "VEVENT":
                    event_name = component['SUMMARY']
                    if component['UID'] in already_logged:
                        print("Already logged: %s" % event_name)
                        continue
                    # If at least one string matches:
                    if True in [(s.lower() in event_name.lower())
                                for s in row['if_event_matches']]:
                        date = component['DTSTART'].dt
                        if isinstance(date, datetime.datetime):
                            if date.tzinfo is None or date.tzinfo.utcoffset(date) is None:
                                # Note that this assumes the events are in UTC. Really doesn't matter.
                                date = pytz.UTC.localize(date)
                            in_future = (date > today)
                        elif isinstance(date, datetime.date):
                            in_future = (date > today.date())
                        else:
                            raise

                        if in_future:
                            reminder_dates = [] # initial value
                            for when in row['when']:
                                reminder_dates.append(date + notice_options[when])
                            for rd in reminder_dates:
                                todo_name = "%s [for event: %s]" % (
                                    row['remind_me_to'], event_name)
                                call([NEWTODO,
                                    todo_name,
                                    rd.strftime('%m %d, %Y'),
                                    row['notes']
                                    ])
                            # Append a new line containing the event ID to the log,
                            # so we don't create another reminder for this event
                            # next time we run the program.
                            log.write('%s%s' % (component['UID'], os.linesep))
