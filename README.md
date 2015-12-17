Notes:
* Don't know if time handles DST properly
* add disable flag that constantly checks for button press, stops alarm for several hours, then switches back to enable
* My naming conventions are inconsistent
* Should play music in background so it can still access OS to shut music off

Great python libraries, http://goo.gl/2SWw1G
-Arrow for datetime
-Maybe invoker if I have trouble with os
-Could use for RPI (add to notes for it)

==================== Todo ====================

* Create backup for if internet goes down
  * Check what happens when it's running and you pull the internet (I expect error in get_events http or service)

* Turn config tuple into map
* Change to arrow for datetime?
* IR to turn off, then switch to running pyfeed messages (weather, news, etc)

==================== Done ====================

* Globals should go in config file, using (safe)configparser
* Fix fullday events by checking for datetime, look for events by query (add query to config)
* Check for OS when calling mpg (since python library is different) (use platform library)
* Modularize Keyboard interrupt response
* Add shutdown interval to config

==================== Learned ====================

platform.system() is op, http://goo.gl/HMCge3

==================== saved from log ====================

No upcoming events found.
Traceback (most recent call last):
  File "rpi_alarm.py", line 51, in <module>
    alarm.run()
  File "rpi_alarm.py", line 36, in run
    events = googlecalendar.get_events(self.credentials, self.query)
  File "/Users/nicholaslau/Dropbox/Dev/RPiAlarm/modules/googlecalendar.py", line 61, in get_events
    calendarId='primary', q=query, timeMin=now, maxResults=100, singleEvents=True, orderBy='startTime').execute()
  File "/Library/Python/2.7/site-packages/oauth2client/util.py", line 142, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "/Library/Python/2.7/site-packages/googleapiclient/http.py", line 722, in execute
    body=self.body, headers=self.headers)
  File "/Library/Python/2.7/site-packages/oauth2client/client.py", line 589, in new_request
    redirections, connection_type)
  File "/Library/Python/2.7/site-packages/httplib2/__init__.py", line 1609, in request
    (response, content) = self._request(conn, authority, uri, request_uri, method, body, headers, redirections, cachekey)
  File "/Library/Python/2.7/site-packages/httplib2/__init__.py", line 1351, in _request
    (response, content) = self._conn_request(conn, request_uri, method, body, headers)
  File "/Library/Python/2.7/site-packages/httplib2/__init__.py", line 1278, in _conn_request
    raise ServerNotFoundError("Unable to find the server at %s" % conn.host)
httplib2.ServerNotFoundError: Unable to find the server at www.googleapis.com