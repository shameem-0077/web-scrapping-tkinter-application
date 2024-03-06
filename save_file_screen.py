import os
import customtkinter
from tkinter import filedialog
from PIL import Image

import requests
from urllib import request
import json
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By


class SaveFileScreen(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Web-scrapper by mr.robot")
        self.geometry(f"{500}x{250}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.mainframe = customtkinter.CTkFrame(self, width=140, corner_radius=10)
        self.mainframe.grid(row=0, column=0, rowspan=4, columnspan=4, pady=10, padx=10,  sticky="nsew")
        self.mainframe.grid_rowconfigure(4, weight=1)
        self.mainframe.grid_columnconfigure(4, weight=1)

        self.file_name_label = customtkinter.CTkLabel(self.mainframe, text="File name:", anchor="w")
        self.file_name_label.grid(row=0, column=0, padx=20, pady=20, sticky='wne')

        self.file_name_entry = customtkinter.CTkEntry(self.mainframe, placeholder_text="Please enter a file name", width=200)
        self.file_name_entry.grid(row=0, column=0, columnspan=2, padx=(90, 0), pady=20, sticky='wne')

        self.location = customtkinter.CTkLabel(self.mainframe, text="Location:", anchor="w")
        self.location.grid(row=1, column=0, padx=20, pady=20, sticky='wne')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_icon = customtkinter.CTkImage(Image.open(f"{current_dir}/test_images/plus.png"))

        self.given_location = ""
        def ask_location():
            ask_location = filedialog.askdirectory(initialdir='~/Downloads', mustexist=True, title="Please select a directory", parent=self)

            if ask_location:
                ask_location = customtkinter.StringVar(value=ask_location)
                ask_location_entry = customtkinter.CTkEntry(self.mainframe, width=250, textvariable=ask_location, state='disabled')
                ask_location_entry.grid(row=1, column=0, padx=(90, 0), pady=20, sticky='wne')

                self.given_location = ask_location_entry.get()

                self.file_location_button.grid(row=1, column=1)
            

        self.file_location_button = customtkinter.CTkButton(self.mainframe, text=None, image=file_icon, command=ask_location, fg_color='transparent', width=50)
        self.file_location_button.grid(row=1, column=0, padx=(90, 0), pady=20, sticky='wn')

        def confirm_button():
            driver = webdriver.Chrome()

            main_url = master.main_frame.enter_base_url_entry.get()
            base_selector = master.main_frame.enter_base_url_selector.get()

            driver.get(main_url)

            if master.main_frame.optionmenu.get() == "elements":
                elements = driver.find_elements(By.CSS_SELECTOR, base_selector)
                new_selectors = master.main_frame.scrollable_checkbox_frame.new_widgets
                
                count = 0
                filename = f"{self.given_location}/{self.file_name_entry.get()}.csv"
                with open(filename, 'w', newline='') as file:
                    header = ['sl_no']

                    for field_name in new_selectors:
                        header.append(field_name['title'])

                    writer = csv.writer(file)

                    writer.writerow(header)
                    data = []
                    for e in elements:
                        count += 1
                        new_data = []
                        new_data.append(count)
                        for i in new_selectors:
                            if i['scrape'] == 'text':
                                title = e.find_element(By.CSS_SELECTOR, i['from']).text
                            else:
                                title = e.find_element(By.CSS_SELECTOR, i['from']).get_attribute(name=i['scrape'])
                            
                            new_data.append(title)
                        
                        data.append(new_data)
                        new_data = []

                    writer.writerows(data)

            else:
                scrape_attribute = master.main_frame.optionmenu_for_single_element.get()
                if scrape_attribute == 'text':
                    element = driver.find_element(By.CSS_SELECTOR, base_selector).text

                    print(element)
                else:
                    element = driver.find_element(By.CSS_SELECTOR, base_selector).get_attribute(name=scrape_attribute)

                    print(element)


        self.confirm_button = customtkinter.CTkButton(self.mainframe, text="Confirm", command=confirm_button)
        self.confirm_button.grid(row=4, column=0, padx=(20, 20), pady=20, sticky='wse')