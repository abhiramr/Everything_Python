from gi.repository import WebKit, Gtk, Gdk, Gio, GLib
import signal, os
import gi
gi.require_version('WebKit', '3.0')
class MainWin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, skip_pager_hint=True, skip_taskbar_hint=True)
        self.set_wmclass("sildesktopwidget","sildesktopwidget")
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_size_request(400,20)
        self.set_keep_below(True)

        #Set transparency
        screen = self.get_screen()
        rgba = screen.get_rgba_visual()
        self.set_visual(rgba)
        self.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255,0,0,1))

        #Add all the parts
        self.view = WebKit.WebView()
        self.view.set_transparent(True)
        self.view.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(0,255,0,0))
        self.view.props.settings.props.enable_default_context_menu = False
        pa= os.path.dirname(os.path.abspath(__file__))
        self.view.load_uri("file:///"+pa+"/memory.html")

        box = Gtk.Box(spacing=6)
        self.add(box)
        box.pack_start(self.view, True, True, 0)
        self.set_decorated(False)
        self.connect("destroy", lambda q: Gtk.main_quit())

        #Show all the parts
        self.show_all()
        self.move(100,100)

def refresh_file(*args):
    #print(args)
    mainwin.view.reload()

def file_changed(monitor, file, unknown, event):
    # reload
    GLib.timeout_add_seconds(2, refresh_file)

if __name__ == '__main__':
    pa = os.path.dirname(os.path.abspath(__file__))
    gio_file = Gio.File.new_for_path(pa+"/memory.html")
    monitor = gio_file.monitor_file(Gio.FileMonitorFlags.NONE, None)
    monitor.connect("changed", file_changed)

    mainwin = MainWin()
    signal.signal(signal.SIGINT, signal.SIG_DFL) # make ^c work
    Gtk.main()
