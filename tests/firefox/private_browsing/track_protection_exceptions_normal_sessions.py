# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from targets.firefox.fx_testcase import *


class Test(FirefoxTest):
    @pytest.mark.details(
        description="Tracking protection exceptions can be successfully added, "
        "remembered and removed from normal browsing session",
        test_case_id="107717",
        test_suite_id="1826",
        locales=["en-US"],
    )
    def run(self, firefox):
        remove_website_button_pattern = (
            AboutPreferences.Privacy.Exceptions.REMOVE_WEBSITE_BUTTON
        )
        privacy_page_pattern = AboutPreferences.PRIVACY_AND_SECURITY_BUTTON_SELECTED
        tracking_protection_shield_pattern = (
            LocationBar.TRACKING_PROTECTION_SHIELD_ACTIVATED
        )
        tracking_protection_shield_deactivated_pattern = Pattern(
            "tracking_protection_shield_deactivated.png"
        )

        turn_off_blocking_pattern = Pattern("turn_off_blocking_for_site_button.png")
        manage_exceptions_button_pattern = Pattern("manage_exceptions_button.png")
        privacy_strict_checkbox_unchecked_pattern = Pattern(
            "privacy_strict_checkbox_unchecked.png"
        )
        privacy_strict_checkbox_checked_pattern = Pattern(
            "privacy_strict_checkbox_checked.png"
        )
        firefox_tracker_site_content_pattern = Pattern(
            "firefox_tracker_site_content.png"
        )
        third_party_tracker_correctly_blocked_text = Pattern(
            "simulated_third_party_tracker_correctly_blocked_text.png"
        )
        first_party_tracker_correctly_blocked_text = Pattern(
            "simulated_first_party_tracker_correctly_blocked_text.png"
        )
        dnt_signal_correctly_sent_text = Pattern("dnt_signal_correctly_sent_text.png")
        third_party_tracker_incorrectly_loaded_text = Pattern(
            "simulated_third_party_tracker_incorrectly_loaded_text.png"
        )
        itstrap_site_exception_selected_pattern = Pattern(
            "itstrap_site_exception_selected.png"
        )
        tracking_content_detected_pattern = Pattern("tracking_protection_is_off.png")
        exceptions_content_blocking_panel_pattern = Pattern(
            "exceptions_content_blocking_label.png"
        )

        navigate("about:preferences#privacy")
        navigated_to_preferences = exists(
            privacy_page_pattern, FirefoxSettings.FIREFOX_TIMEOUT
        )
        assert (
            navigated_to_preferences
        ), "The about:preferences#privacy page is successfully displayed."

        privacy_strict_checkbox_unchecked_displayed = exists(
            privacy_strict_checkbox_unchecked_pattern
        )
        if privacy_strict_checkbox_unchecked_displayed:
            click(privacy_strict_checkbox_unchecked_pattern)
        else:
            raise FindError('The "Strict" content blocking option was not found')

        click(AboutPreferences.PRIVACY_AND_SECURITY_BUTTON_SELECTED)

        privacy_strict_checkbox_checked_displayed = exists(
            privacy_strict_checkbox_checked_pattern
        )
        assert privacy_strict_checkbox_checked_displayed, (
            'The "Strict" content blocking' " option was successfully saved"
        )

        navigate("https://itisatrap.org/firefox/its-a-tracker.html")

        close_content_blocking_pop_up()

        if OSHelper.is_windows():  # to prevent pop-up covering pattern
            type(Key.ESC)

        firefox_tracker_site_logo_displayed = exists(
            firefox_tracker_site_content_pattern
        )
        assert (
            firefox_tracker_site_logo_displayed
        ), "The website is successfully displayed."

        tracking_protection_shield_displayed = exists(
            tracking_protection_shield_pattern
        )
        assert tracking_protection_shield_displayed, (
            "The Tracking protection shield" " is displayed near the address bar."
        )

        third_party_tracker_correctly_blocked_displayed = exists(
            third_party_tracker_correctly_blocked_text
        )
        assert third_party_tracker_correctly_blocked_displayed, (
            "Simulated third-party tracker" " was correctly blocked is displayed."
        )

        first_party_tracker_correctly_blocked_displayed = exists(
            first_party_tracker_correctly_blocked_text
        )
        assert first_party_tracker_correctly_blocked_displayed, (
            "Simulated first-party tracker" " was correctly loaded is displayed."
        )

        dnt_signal_correctly_sent_displayed = exists(dnt_signal_correctly_sent_text)
        assert (
            dnt_signal_correctly_sent_displayed
        ), "The DNT signal was correctly sent is displayed."

        click(tracking_protection_shield_pattern)

        time.sleep(1)  # wait for the pop-up loading

        turn_off_blocking_displayed = exists(turn_off_blocking_pattern)
        assert (
            turn_off_blocking_displayed
        ), "Turn off blocking for this site is displayed."

        click(turn_off_blocking_pattern)

        if OSHelper.is_windows():  # to prevent pop-up covering pattern
            type(Key.ESC)

        if not exists(
            firefox_tracker_site_content_pattern, FirefoxSettings.FIREFOX_TIMEOUT
        ):
            if OSHelper.is_mac():
                type("r", KeyModifier.CMD)
            else:
                type("r", KeyModifier.CTRL)
        firefox_tracker_site_logo_displayed = exists(
            firefox_tracker_site_content_pattern, FirefoxSettings.FIREFOX_TIMEOUT
        )
        assert (
            firefox_tracker_site_logo_displayed
        ), "Site is reloaded after turning off content blocking"

        tracking_protection_shield_deactivated_displayed = exists(
            tracking_protection_shield_deactivated_pattern
        )
        assert tracking_protection_shield_deactivated_displayed, (
            "The tracking protection shield is displayed"
            " as deactivated (strikethrough)."
        )
        type(Key.ESC)

        move(tracking_protection_shield_deactivated_pattern)
        tracking_content_detected_pattern_displayed = exists(
            tracking_content_detected_pattern, FirefoxSettings.TINY_FIREFOX_TIMEOUT
        )
        assert tracking_content_detected_pattern_displayed, (
            "On hover, the tracking protection"
            ' shield displays a "Tracking content detected"'
            " tooltip message."
        )

        third_party_tracker_incorrectly_loaded_displayed = exists(
            third_party_tracker_incorrectly_loaded_text
        )
        assert third_party_tracker_incorrectly_loaded_displayed, (
            "Simulated third-party tracker" " was incorrectly loaded is displayed."
        )

        first_party_tracker_correctly_blocked_displayed = exists(
            first_party_tracker_correctly_blocked_text
        )
        assert first_party_tracker_correctly_blocked_displayed, (
            "Simulated first-party tracker" " was correctly loaded is displayed."
        )

        dnt_signal_correctly_sent_displayed = exists(dnt_signal_correctly_sent_text)
        assert (
            dnt_signal_correctly_sent_displayed
        ), "The DNT signal was correctly sent is displayed."

        navigate("about:preferences#privacy")

        click(manage_exceptions_button_pattern)
        exceptions_content_blocking_panel_displayed = exists(
            exceptions_content_blocking_panel_pattern
        )
        assert exceptions_content_blocking_panel_displayed, (
            "The Exceptions - Content Blocking panel" " is successfully displayed."
        )

        itstrap_site_exception_displayed = exists(
            itstrap_site_exception_selected_pattern
        )
        assert itstrap_site_exception_displayed, (
            "The previously accessed website is displayed"
            " as exception inside the panel."
        )

        click(remove_website_button_pattern)
        if OSHelper.is_mac():
            save_changes_button_pattern = Pattern("save_changes_button.png")
            click(save_changes_button_pattern)
        else:
            click(AboutPreferences.Privacy.Exceptions.SAVE_CHANGES_BUTTON)
        click(manage_exceptions_button_pattern)

        itstrap_site_exception_displayed = exists(
            itstrap_site_exception_selected_pattern
        )
        assert (
            itstrap_site_exception_displayed is False
        ), "The website is successfully removed from the panel."

        navigate("https://itisatrap.org/firefox/its-a-tracker.html")

        if OSHelper.is_windows():  # to prevent pop-up covering pattern
            type(Key.ESC)

        firefox_tracker_site_logo_displayed = exists(
            firefox_tracker_site_content_pattern
        )
        assert (
            firefox_tracker_site_logo_displayed
        ), "The website is successfully displayed."

        tracking_protection_shield_displayed = exists(
            tracking_protection_shield_pattern
        )
        assert tracking_protection_shield_displayed, (
            "The Tracking protection shield" " is displayed near the address bar."
        )

        third_party_tracker_correctly_blocked_displayed = exists(
            third_party_tracker_correctly_blocked_text
        )
        assert third_party_tracker_correctly_blocked_displayed, (
            "Simulated third-party tracker" " was correctly blocked is displayed."
        )

        first_party_tracker_correctly_blocked_displayed = exists(
            first_party_tracker_correctly_blocked_text
        )
        assert first_party_tracker_correctly_blocked_displayed, (
            "Simulated first-party tracker" " was correctly loaded is displayed."
        )

        dnt_signal_correctly_sent_displayed = exists(dnt_signal_correctly_sent_text)
        assert (
            dnt_signal_correctly_sent_displayed
        ), "The DNT signal was correctly sent is displayed."
