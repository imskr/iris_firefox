# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *


class Test(FirefoxTest):

    @pytest.mark.details(
        description='Firefox can be set to display a blank page on launch',
        locale=['en-US'],
        test_case_id='2241',
        test_suite_id='143544'
    )
    def run(self, firefox):
        homepage_preferences_pattern = Pattern('homepage_preferences.png')
        default_setting_home_pattern = Pattern('default_new_tab_setting_home.png')
        blank_page_option_pattern = Pattern('blank_page_option.png')
        mozilla_tab_not_focused_pattern = Pattern('mozilla_tab_not_focused.png')
        wiki_logo_unactive_tab_pattern = Pattern('wiki_logo_unactive_tab.png')

        navigate(LocalWeb.MOZILLA_TEST_SITE)

        mozilla_test_opened = exists(LocalWeb.MOZILLA_LOGO, FirefoxSettings.SHORT_FIREFOX_TIMEOUT)
        assert mozilla_test_opened, 'Mozilla test site opened'

        new_tab()
        navigate(LocalWeb.SOAP_WIKI_TEST_SITE)

        mozilla_test_opened = exists(LocalWeb.SOAP_WIKI_SOAP_LABEL, FirefoxSettings.SHORT_FIREFOX_TIMEOUT)
        assert mozilla_test_opened, 'Wiki test site opened'

        new_tab()

        navigate('about:preferences#home')

        preferences_page_opened = exists(homepage_preferences_pattern, FirefoxSettings.FIREFOX_TIMEOUT)
        assert preferences_page_opened, 'The about:preferences page is successfully loaded.'

        homepage_preferences_location = find(homepage_preferences_pattern)
        homepage_preferences_width, homepage_preferences_height = homepage_preferences_pattern.get_size()
        homepage_section_region = Region(homepage_preferences_location.x, homepage_preferences_location.y,
                                         homepage_preferences_width*3, int(homepage_preferences_height*1.5))

        home_option_displayed = exists(default_setting_home_pattern, FirefoxSettings.FIREFOX_TIMEOUT,
                                       homepage_section_region)
        assert home_option_displayed, 'The options for "Home" section are displayed.'

        click(default_setting_home_pattern, region=homepage_section_region)

        blank_page_option_displayed = exists(blank_page_option_pattern, FirefoxSettings.FIREFOX_TIMEOUT)
        assert blank_page_option_displayed, 'The \'Blank Page\' option for "Home" section is displayed.'

        click(blank_page_option_pattern)

        quit_firefox()

        firefox.start(url='', image=NavBar.HOME_BUTTON)

        time.sleep(Settings.DEFAULT_UI_DELAY_LONG)

        home_page_displayed = not exists(Utils.TOP_SITES, FirefoxSettings.FIREFOX_TIMEOUT) and \
                              not exists(Tabs.NEW_TAB_HIGHLIGHTED)

        no_other_tabs_displayed = not exists(mozilla_tab_not_focused_pattern) and \
                                  not exists(wiki_logo_unactive_tab_pattern)

        assert home_page_displayed and no_other_tabs_displayed,\
            'The browser opens successfully and the blank page is the only one loaded.'
