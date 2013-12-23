
#!/usr/bin/env python

import sys
import gtk
import appindicator

PING_FREQUENCY = 10     # seconds


class TimeTriggerIndicator:
    def __init__(self):
        self.ind = appindicator.Indicator(
            "new-gmail-indicator",
            "indicator-messages",
            appindicator.CATEGORY_APPLICATION_STATUS
        )
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("new-messages-red")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

        self.toggle_item = gtk.MenuItem("Toggle")
        self.toggle_item.connect("activate", self.toggle)
        self.toggle_item.show()
        self.menu.append(self.toggle_item)

    def main(self):
        self.repeated_task()
        gtk.timeout_add(PING_FREQUENCY * 1000, self.repeated_task)
        gtk.main()

    def quit(self, widget):
        sys.exit(0)

    def toggle(self, widget):
        if appindicator.STATUS_ATTENTION == self.ind.get_status():
            self.ind.set_status(appindicator.STATUS_ACTIVE)
        elif appindicator.STATUS_ACTIVE == self.ind.get_status():
            self.ind.set_status(appindicator.STATUS_ATTENTION)

        print(self.menu.get_children()[0])

    def repeated_task(self):
        status = self.repeated_task_helper()
        if status == 0:
            self.ind.set_status(appindicator.STATUS_ATTENTION)
        else:
            self.ind.set_status(appindicator.STATUS_ACTIVE)
        return True

    def repeated_task_helper(self):
    	return 1;

if __name__ == "__main__":
    indicator = TimeTriggerIndicator()
    indicator.main()
