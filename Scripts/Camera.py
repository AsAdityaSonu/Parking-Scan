bgColor = "#0e1017"


def Camera(app, cameraNo):
    for widget in app.winfo_children():
        widget.destroy()

    app.title(cameraNo)
