# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.nightly.firefox_app.fx_browser import Profiles, FirefoxUtils
from targets.nightly.firefox_ui.bookmarks import Bookmarks
from targets.nightly.firefox_ui.helpers.history_test_utils import open_clear_recent_history_window
from targets.nightly.firefox_ui.helpers.keyboard_shortcuts import *
from targets.nightly.firefox_ui.helpers.update_rules import is_update_required, get_rule_for_channel, get_update_rules
from targets.nightly.firefox_ui.history import History
from targets.nightly.firefox_ui.library import Library
from targets.nightly.firefox_ui.library_menu import LibraryMenu
from targets.nightly.firefox_ui.sidebar import Sidebar
from targets.nightly.firefox_ui.test_utils import restore_firefox_focus, open_clear_recent_history_window
from targets.nightly.local_web.web_links.local_web import LocalWeb
from targets.nightly.firefox_ui.utils import Utils
from targets.nightly.firefox_ui.helpers.general import *
from targets.nightly.firefox_ui.helpers.history_test_utils import *
from targets.nightly.firefox_ui.tabs import Tabs
from targets.nightly.firefox_ui.download_dialog import DownloadDialog
from targets.nightly.firefox_ui.about_preferences import AboutPreferences
from targets.nightly.firefox_ui.about_addons import *
from targets.nightly.firefox_ui.private_window import *
from targets.nightly.firefox_ui.find_toolbar import *
from targets.nightly.firefox_ui.hamburger import *
from targets.nightly.firefox_ui.nav_bar import *
from targets.nightly.firefox_ui.menu_bar import *
from targets.nightly.firefox_ui.find_toolbar import *
from targets.nightly.firefox_ui.location_bar import *
from targets.nightly.firefox_ui.private_window import *
from targets.nightly.firefox_ui.content_blocking import *
from targets.nightly.firefox_ui.content_blocking_tour import *
from targets.nightly.firefox_ui.docker import *
from targets.nightly.firefox_ui.helpers.file_picker_utils import *
from targets.nightly.firefox_ui.download_manager import *
from targets.nightly.settings import FirefoxSettings
from targets.nightly.firefox_ui.customize import Customize
