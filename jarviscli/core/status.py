from plugin import Platform, plugin, require


@plugin("status")
def status(jarvis, s):
    count_enabled = jarvis.plugin_manager.get_number_plugins_loaded()
    count_disabled = len(jarvis.plugin_manager.get_disabled())
    jarvis.say(
        "{} Plugins enabled, {} Plugins disabled.".format(
            count_enabled,
            count_disabled))

    if "short" not in s and count_disabled > 0:
        jarvis.say("")
        for disabled, reason in jarvis.plugin_manager.get_disabled().items():
            jarvis.say("{:<20}: {}".format(disabled, " OR ".join(reason)))
