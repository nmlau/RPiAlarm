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