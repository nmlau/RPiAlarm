#!/usr/bin/env python

from datetime import datetime
import pytz

def get_current_time(timezone):
    # same format as google event time
    localFormat = "%Y-%m-%dT%H:%M" 

    utcmoment_unaware = datetime.utcnow()
    utcmoment = utcmoment_unaware.replace(tzinfo=pytz.utc)
    
    if timezone == 'PST':
      localDatetime = utcmoment.astimezone(pytz.timezone('America/Los_Angeles'))
    else:
      localDatetime = utcmoment.astimezone(pytz.utc)
        
    return localDatetime.strftime(localFormat)