import gi
import webview
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    #show the page
webview.create_window('Innatical Cloud', 'https://dashboard.innatical.cloud/')
webview.start()

#kill the app when x is pressed
def on_window1_destroy(self, *args):    
    webview.end()
    exit()
    #Fuck me raw Python won't do the python things

# Create a new application
app = Gtk.Application(application_id='cloud.innatical')
app.connect('activate', on_activate)

# Run the application
app.run(None)
