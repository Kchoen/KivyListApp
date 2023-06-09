from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import random

class RestaurantList(BoxLayout):
    default_list = ['BurgerKing','McDonald\'s']
    def add_restaurant(self):
        for idx,restaurant in enumerate(self.ids.restaurant_list.children):
            if(restaurant.id[0]=='D'):
                restaurant.disabled=True
                restaurant.opacity=0
        restaurant_name = self.ids.restaurant_name.text
        if(len(restaurant_name)>0):
            self.default_list.append(restaurant_name)
            l = Label(text=restaurant_name,font_size= 20,bold=True)
            self.ids.restaurant_list.add_widget(l)
            l.id="L"+str(len(self.default_list))
            btn = Button(size_hint=(0.3,1),text="Delete", background_color=(1, 0, 0, 1),disabled=True,opacity=0,on_press=self.delete_item)
            btn.id = "D"+str(len(self.default_list))
            self.ids.restaurant_list.add_widget(btn)
        self.ids.restaurant_name.text = ''


    def select_restaurant(self):
        selected_restaurant = random.choice(self.default_list)
        self.ids.selected_restaurant.text = selected_restaurant
        for idx,restaurant in enumerate(self.ids.restaurant_list.children):
            if(restaurant.id[0]=='D'):
                restaurant.disabled=True
                restaurant.opacity=0

    def delete_restaurants(self):
        for idx,restaurant in enumerate(self.ids.restaurant_list.children):
            if(restaurant.id[0]=='D'):
                restaurant.opacity = int(restaurant.disabled==True)
                restaurant.disabled= restaurant.disabled==False
        
    def delete_item(self,button):
        dnum,lnum = button.id,'L'+button.id[1:]
        del_list=[]
        parent = button.parent
        for child in button.parent.children:
            if child.id==dnum or child.id==lnum:
                del_list.append(child)
        for item in del_list:
            parent.remove_widget(item)


class RestaurantListApp(App):
    def build(self):
        rest_list = RestaurantList()
        for idx,rest_name in enumerate(rest_list.default_list):
            old = Label(text=rest_name,font_size= 20,bold=True)
            rest_list.ids.restaurant_list.add_widget(old)
            old.id = "L"+str(idx+1)
            btn = Button(size_hint=(0.3,1),text="Delete", background_color=(1, 0, 0, 1),disabled=True,opacity=0,on_press=rest_list.delete_item)
            btn.id = "D"+str(idx+1)
            rest_list.ids.restaurant_list.add_widget(btn)
        return rest_list

if __name__ == '__main__':
    RestaurantListApp().run()
