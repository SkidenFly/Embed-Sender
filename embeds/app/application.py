import json

import requests

from embeds.utils import *


class Application:
    
    @property
    def __get_token(self):
        with open("././secrets/token", "r") as f:
            token = f.read()
            f.close()
        
        return token

    def __init__(self):
        self.__token = self.__get_token
        self.__headers = {'Authorization': self.__token}
        
        self.__channel_id = 0

        self.__embed = {
            "embed": {
                "title": "",
                "url": "",
                "description": "",
                "color": 0,

                "image": {
                    "url": ""
                },
                
                "author": {
                    "name": "", 
                    "url": "", 
                    "icon_url": ""
                },
                
                "footer": {
                    "text": "", 
                    "icon_url": ""
                }
            }
        }

    def run(self):
        """ Application main loop """
        while True:
            options = {
                "Title": self.__embed["embed"]["title"],
                "URL": self.__embed["embed"]["url"],
                "Description": self.__embed["embed"]["description"],
                "Color": self.__embed["embed"]["color"],
                "Image": self.__embed["embed"]["image"]["url"],
                "Author": self.__embed["embed"]["author"],
                "Footer": self.__embed["embed"]["footer"],
                "Set channel": self.__channel_id,
                "Import embed": "",
                "Export embed": "",
                "Send": ""
            }

            self.banner()

            count = 1
            for key in options:
                if options[key]:
                    print(f"[{count}] - {key}: {options[key]}")
                else:
                    print(f"[{count}] - {key}")

                count += 1

            option = int(Console.get_input())

            if option == 1:
                self.title()
            elif option == 2:
                self.url()
            elif option == 3:
                self.description()
            elif option == 4:
                self.color()
            elif option == 5:
                self.image()
            elif option == 6:
                self.author()
            elif option == 7:
                self.footer()
            elif option == 8:
                self.set_channel()
            elif option == 9:
                self.import_embed()
            elif option == 10:
                self.export_embed()
            elif option == 11:
                self.send()


    def banner(self):
        Console.clear()
        Console.print_banner()
        Console.print_app_color()


    def title(self):
        """ Set embed title """
        self.banner()
        
        print("Title: ")
        self.__embed["embed"]["title"] = Console.get_input()

    def url(self):
        """ Set title url """
        while True:
            self.banner()
            
            print("URL: ")
            url = Console.get_input()

            if url.startswith("http") or url.startswith("https") or not url:
                self.__embed["embed"]["url"] = url
                return
            else:
                print("Invalid URL")
                Console.pause()
 
    def description(self):
        """ Set embed description """
        self.banner()
        
        print("Description: ")
        self.__embed["embed"]["description"] = Console.get_input()

    def color(self):
        """ Set embed color """
        self.banner()
        
        print("Color: ")
        self.__embed["embed"]["color"] = int(Console.get_input())


    def image(self):
        """ Set embed image """
        self.banner()
        
        print("Image URL: ")
        url = Console.get_input()

        if url.startswith("http") or url.startswith("https") or not url:
            self.__embed["embed"]["image"]["url"] = url
            return
        else:
            print("Invalid URL")
            Console.pause()


    def author(self):
        """ Set embed author """
        while True:
            self.banner()

            print("[1] - Author name: " + self.__embed["embed"]["author"]["name"])
            print("[2] - Author url: " + self.__embed["embed"]["author"]["url"])
            print("[3] - Author icon: " + self.__embed["embed"]["author"]["icon_url"])
            print("[4] - Ready")

            option = int(Console.get_input())

            if option == 1:
                print("Author name: ")
                self.__embed["embed"]["author"]["name"] = Console.get_input()

            elif option == 2:
                print("Author url: ")
                self.__embed["embed"]["author"]["url"] = Console.get_input()

            elif option == 3:
                print("Author icon: ")
                self.__embed["embed"]["author"]["icon_url"] = Console.get_input()

            elif option == 4:
                return


    def footer(self):
        """ Set embed footer """
        while True:
            self.banner()

            print("[1] - Footer text: " + self.__embed["embed"]["footer"]["text"])
            print("[2] - Footer icon: " + self.__embed["embed"]["footer"]["icon_url"])
            print("[3] - Ready")

            option = int(Console.get_input())

            if option == 1:
                print("Footer text: ")
                self.__embed["embed"]["footer"]["text"] = Console.get_input()

            elif option == 2:
                print("Footer icon: ")
                self.__embed["embed"]["footer"]["icon_url"] = Console.get_input()

            elif option == 3:
                return


    def set_channel(self):
        """ Set embed channel """
        self.banner()
        
        print("Channel ID: ")
        self.__channel_id = Console.get_input()

        print("Is DM? (y/n)")
        option = Console.get_input().lower()

        if option == "y":        
            res = requests.post(
                "https://discordapp.com/api/v6/users/@me/channels", 
                headers= self.__headers, 
                json= {"recipient_id": self.__channel_id}
            )

            self.__channel_id = res.json().get("id")


    def import_embed(self):
        """ Imports embed from json file """
        self.banner()
        
        print("JSON file: ")
        file = Console.get_input()

        with open(file, "r") as f:
            self.__embed = json.load(f)

    def export_embed(self):
        """ Exports current embed to json file """
        self.banner()
        
        with open("embed.json", "w") as file:
            json.dump(self.__embed, file)
            file.close()

        print("File saved as embed.json")
        return Console.pause()

    
    def send(self):
        """ Sends embed to the channel """       
        
        if not self.__channel_id:
            print("Channel ID not set")
            return Console.pause()
            
        if not self.__embed:
            print("Embed not set")
            return Console.pause()
        
        
        return requests.post(
            f"https://discordapp.com/api/v6/channels/{self.__channel_id}/messages", 
            headers= self.__headers, 
            json= self.__embed
        )
