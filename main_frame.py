import customtkinter
from selectors_frame import ScrollableSelectorsFrame


class MainFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.enter_base_url_label = customtkinter.CTkLabel(self, text="Enter base URL:", anchor="w")
        self.enter_base_url_label.grid(row=0, column=0, padx=20, pady=20, sticky="wn")

        self.enter_base_url_entry = customtkinter.CTkEntry(self, placeholder_text="Enter website url for scrapping", width=350)
        self.enter_base_url_entry.grid(row=0, column=0, padx=(120, 20), pady=(20, 20), sticky="wne")

        self.enter_base_url_selector = customtkinter.CTkLabel(self, text="Enter base selector:", anchor="w")
        self.enter_base_url_selector.grid(row=1, column=0, padx=20, pady=20, sticky="wn")

        self.enter_base_url_selector = customtkinter.CTkEntry(self, placeholder_text="Enter base selector")
        self.enter_base_url_selector.grid(row=1, column=0, rowspan=4, padx=(150, 20), pady=20, sticky="wne")

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)
            selected_option = choice

            if selected_option == "elements":
                self.scrollable_checkbox_frame.grid(row=1, column=0, rowspan=4, padx=10, pady=(100, 0), sticky="nsew")
                self.scrape_label.grid_forget()
                self.optionmenu_for_single_element.grid_forget()
            elif selected_option == 'element':
                self.scrollable_checkbox_frame.grid_forget()
                self.scrape_label.grid(row=1, column=3, padx=(0, 20), pady=20, sticky="wne")
                self.optionmenu_for_single_element.grid(row=1, column=3, padx=(50, 20), pady=20, sticky="wne")

        optionmenu_var = customtkinter.StringVar(value="element")
        self.optionmenu = customtkinter.CTkOptionMenu(self,values=["element", "elements"], command=optionmenu_callback, variable=optionmenu_var)
        
        self.optionmenu.grid(row=1, column=1, padx=(50, 20), pady=20, sticky="wne")

        
        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = ScrollableSelectorsFrame(self, title="Add new selectors", values=values)
        self.scrollable_checkbox_frame.grid(row=1, column=0, rowspan=2, columnspan=4, padx=10, pady=(100, 0), sticky="nsew")

        if self.optionmenu.get() == "element":
            self.scrollable_checkbox_frame.grid_forget()
            self.scrape_label = customtkinter.CTkLabel(self, text="Scrape:", anchor="w")
            self.scrape_label.grid(row=1, column=3, padx=(0, 20), pady=20, sticky="wne")

            optionmenu_var = customtkinter.StringVar(value="text")
            self.optionmenu_for_single_element = customtkinter.CTkOptionMenu(self,values=["text", "src"], command=optionmenu_callback, variable=optionmenu_var)
            self.optionmenu_for_single_element.grid(row=1, column=3, padx=(50, 20), pady=20, sticky="wne")
