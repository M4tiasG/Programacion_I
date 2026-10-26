from gui.app import create_window
from gui.views import build_views
from gui.controllers import resize_window_to_content

if __name__ == "__main__":
    create_window()
    build_views()
    resize_window_to_content()
    
    import gui.app as app
    app.window.mainloop()