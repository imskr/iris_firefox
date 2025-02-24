# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from moziris.api.finder.pattern import Pattern


class ContentBlocking(object):
    POP_UP_ENABLED = Pattern('cb_pop_up_enabled.png')
    CLOSE_CB_POP_UP = Pattern('close_cb_pop_up.png')