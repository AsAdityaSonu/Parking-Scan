import customtkinter as ctk


def Dashboard(app):
    app.title("Dashboard")

    main_frame = ctk.CTkFrame(
        master=app,
        width=app.winfo_screenwidth(),
        height=app.winfo_screenheight(),
        fg_color="#020833"
    )
    main_frame.pack(expand=True, fill='both')

    label = ctk.CTkLabel(
        master=main_frame,
        text="Welcome to the New Page",
        font=("Helvetica", 24, "bold"),
        text_color="white"
    )
    label.pack(pady=50)

    message_label = ctk.CTkLabel(
        master=main_frame,
        text="You have successfully logged in.",
        font=("Helvetica", 16),
        text_color="white"
    )
    message_label.pack(pady=20)
