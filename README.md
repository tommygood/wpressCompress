<h1>Background</h1>

As the wordpress plugin - all-in-one migration have a functionality that it will auto backup the wordpress site to .wpress in a time interval(ex. 2 weeks), but
the .wpress file is too large.

<h1>Introduction</h1>

compress all the `.wpress` files(wordpress backup files) in the path of backups file(default is in `/wordpress/wp-content/ai1wm-backups`) to tar file, and remove the origin `.wpress` when successfully compress.

<h1>Configuration</h1>

change the `directory` to your wordpress path in `passWpress.py`

<h1>Usage</h1>

- use crontab to auto execute in a time interval depend on your time interval of backup the wordpress
  - `crontab -e`
  
     `0 0 * * 0 python3 /path/to/wpressCompress/passWpress.py`
      - this will execute the script each week
