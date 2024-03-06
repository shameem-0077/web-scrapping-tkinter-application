import os
import customtkinter
from PIL import Image



class ScrollableSelectorsFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.find = customtkinter.CTkLabel(self, text="Find:", anchor="w")
        self.find.grid(row=1, column=0, padx=(20, 10), pady=20, sticky="wn")

        self.find_entry = customtkinter.CTkEntry(self, placeholder_text="Enter base selector")
        self.find_entry.grid(row=1, column=0, rowspan=4, padx=(60, 10), pady=20, sticky="wne")
        
        self.enter_base_selector_label = customtkinter.CTkLabel(self, text="From:", anchor="w")
        self.enter_base_selector_label.grid(row=1, column=1, padx=(10, 10), pady=20, sticky="wn")

        self.enter_base_selector = customtkinter.CTkEntry(self, placeholder_text="Enter base selector")
        self.enter_base_selector.grid(row=1, column=1, rowspan=4, padx=(60, 10), pady=20, sticky="wne")

        self.enter_base_selector_label = customtkinter.CTkLabel(self, text="Scrape:", anchor="w")
        self.enter_base_selector_label.grid(row=1, column=2, padx=(0, 10), pady=20, sticky="wne")


        optionmenu_var = customtkinter.StringVar(value="text")
        self.optionmenu = customtkinter.CTkOptionMenu(self,values=["text", "src"], variable=optionmenu_var)
        
        self.optionmenu.grid(row=1, column=2, padx=(50, 20), pady=20, sticky="wne")

        current_dir = os.path.dirname(os.path.abspath(__file__))
        add_new_icon = customtkinter.CTkImage(Image.open(f"{current_dir}/test_images/plus.png"))


        self.widget_count = 1
        self.new_widgets = []
        def button_event():

            if len(self.new_widgets) > 0:
                for check in self.new_widgets:
                    print(check)
                    if check['title'] == self.find_entry.get():
                        check['from'] = self.enter_base_selector.get()
                        check['scrape'] = self.optionmenu.get()
                    else:
                        data = {
                            "title": self.find_entry.get(),
                            "from": self.enter_base_selector.get(),
                            "scrape": self.optionmenu.get()
                        }

                        self.new_widgets.append(data)
            else:
                data = {
                    "title": self.find_entry.get(),
                    "from": self.enter_base_selector.get(),
                    "scrape": self.optionmenu.get()
                }

                self.new_widgets.append(data)
            
            self.find_entry.configure(state='disabled')
            self.enter_base_selector.configure(state='disabled')
            self.optionmenu.configure(state='disabled')


            self.widget_count += 1

            self.find = customtkinter.CTkLabel(self, text="Find:", anchor="w")
            self.find.grid(row=self.widget_count, column=0, padx=(20, 10), pady=20, sticky="wn")

            self.find_entry = customtkinter.CTkEntry(self, placeholder_text="Enter base selector")
            self.find_entry.grid(row=self.widget_count, column=0, rowspan=4, padx=(60, 10), pady=20, sticky="wne")
            
            self.enter_base_selector_label = customtkinter.CTkLabel(self, text="From:", anchor="w")
            self.enter_base_selector_label.grid(row=self.widget_count, column=1, padx=20, pady=20, sticky="wn")

            self.enter_base_selector = customtkinter.CTkEntry(self, placeholder_text="Enter base selector")
            self.enter_base_selector.grid(row=self.widget_count, column=1, rowspan=4, padx=(60, 10), pady=20, sticky="wne")

            self.enter_base_selector_label = customtkinter.CTkLabel(self, text="Scrape:", anchor="w")
            self.enter_base_selector_label.grid(row=self.widget_count, column=2, padx=(0, 20), pady=20, sticky="wne")

            optionmenu_var = customtkinter.StringVar(value="text")
            self.optionmenu = customtkinter.CTkOptionMenu(self,values=["text", "src"], variable=optionmenu_var)
            self.optionmenu.grid(row=self.widget_count, column=2, padx=(50, 20), pady=20, sticky="wne")

            self.button.grid(row=self.widget_count, column=3, rowspan=4, padx=(10, 20), pady=20, sticky="wne")


        self.button = customtkinter.CTkButton(self, text=None, image=add_new_icon, command=button_event, fg_color='transparent', width=20, height=40, corner_radius=10)
        self.button.grid(row=self.widget_count, column=3, rowspan=4, padx=(10, 20), pady=20, sticky="wne")
