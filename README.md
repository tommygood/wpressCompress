<h1>Background</h1>

As the wordpress plugin - all-in-one migration have a functionality that it will auto backup the wordpress site to .wpress in a time interval(ex. 2 weeks), but
the .wpress file is too large.

<h1>Introduce</h1>

compress the wordpress backup file(.wpress) to tar file when using the all-in-one migration to backup, and remove the origin .wpress when successfully compress.

<h1>Usage</h1>

- use crontab to auto execute in a time interval depend on your time interval of backup the wordpress
  - `crontab -e`
  
     `0 0 * * 0 python3 /path/to/wpressCompress/passWpress.py`
      - this will execute the script each week
