alias:: 火狐, FF
description:: ff

- [[Backup]]
  - **Profile**: `%APPDATA%\Mozilla\Firefox\Profiles\`
    collapsed:: true
    - ```shell
      .
      ├── AlternateServices.txt
      ├── ClientAuthRememberList.txt
      ├── SecurityPreloadState.txt
      ├── SiteSecurityServiceState.txt
      ├── Telemetry.FailedProfileLocks.txt
      ├── addonStartup.json.lz4
      ├── addons.json
      ├── autofill-profiles.json
      ├── blocklist.xml
      ├── bookmarkbackups           # This folder stores bookmark backup files,
      |                   # which can be used to restore your bookmarks.
      ├── broadcast-listeners.json
      ├── browser-extension-data
      ├── cert9.db              # all your security certificate settings and
      |                   # any SSL certificates you have imported into
      |                                       # Firefox.
      ├── cert_override.txt
      ├── compatibility.ini
      ├── containers.json           # the details of containers used by the Container
      |                   # Tabs feature, including those created by extensions
      |                                       # such as Facebook Container.
      ├── content-prefs.sqlite        # Site-specific preferences:
      ├── cookies.sqlite            # a bit of information stored on your computer
      |                   # by a website you’ve visited
      ├── crashes
      ├── datareporting
      ├── enumerate_devices.txt
      ├── extension-preferences.json
      ├── extension-settings.json
      ├── extensions              # stores files for any extensions you have installed
      ├── extensions.json
      ├── favicons.sqlite           # all of the favicons for your Firefox bookmarks.
      ├── features
      ├── formhistory.sqlite          # This file remembers what you have searched
      |                   # for in the Firefox search bar and what
      |                                       # information you’ve entered into forms on websites.
      ├── gmp
      ├── gmp-gmpopenh264
      ├── gmp-widevinecdm
      ├── handlers.json           # preferences that tell Firefox what to do when
      |                   # it comes across a particular type of file.
      ├── key4.db               # Passwords
      ├── logins-backup.json
      ├── logins.json             # Passwords
      ├── mediacapabilities
      ├── memory-report.json.gz
      ├── minidumps
      ├── notificationstore.json
      ├── parent.lock
      ├── permissions.sqlite          # Site-specific preferences
      ├── pkcs11.txt              # security module configuration.
      ├── places.sqlite             # This file contains all your Firefox bookmarks
      |                   # and lists of all the files you've downloaded
      |                   # and websites you’ve visited.
      ├── pluginreg.dat
      ├── prefs.js              # customized user preference settings, such as
      |                   # changes you make in Firefox Settings dialogs.
      |                                       # The optional user.js file, if one exists,
      |                                       # will override any modified preferences.
      ├── protections.sqlite
      ├── saved-telemetry-pings
      ├── search.json.mozlz4          # This file stores user-installed search engines
      ├── security_state
      ├── serviceworker.txt
      ├── sessionCheckpoints.json
      ├── sessionstore-backups
      ├── sessionstore.jsonlz4        # the currently open tabs and windows
      ├── shader-cache
      ├── shield-preference-experiments.json
      ├── signedInUser.json
      ├── storage
      ├── storage-sync-v2.sqlite
      ├── storage-sync-v2.sqlite-shm
      ├── storage-sync-v2.sqlite-wal
      ├── storage-sync.sqlite
      ├── storage.sqlite
      ├── times.json
      ├── weave
      ├── webappsstore.sqlite         # DOM storage,  provide a larger, more secure,
      |                   # and easier-to-use alternative to storing
      |                   # information in cookies.
      └── xulstore.json           # toolbar and window size/position settings
      ```
      via: [MZHistoryView: View the list of visited web sites in Firefox / Mozilla browsers](http://www.nirsoft.net/utils/mozilla_history_view.html) & https://support.mozilla.org/bm/questions/754699