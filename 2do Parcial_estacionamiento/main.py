from gui.app import create_window
from gui.views import build_views

if __name__ == "__main__":
    create_window()
    build_views()
    
    import gui.app as app
    app.window.mainloop()