from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
Window.size = (300, 700)
import random

class RestaurantList(BoxLayout):
    f = open("text.txt",'r')
    default_list = f.read().split('\n')
    f.close()
    curr_idx = 0
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
            l.id="L"+str(self.curr_idx+1)
            btn = Button(size_hint=(0.3,1),text="Delete", background_color=(1, 0, 0, 1),disabled=True,opacity=0,on_press=self.delete_item)
            btn.id = "D"+str(self.curr_idx+1)
            self.ids.restaurant_list.add_widget(btn)
            self.curr_idx+=1
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
                if(child.id==lnum):
                    self.default_list.remove(child.text)
        for item in del_list:
            parent.remove_widget(item)


class RestaurantListApp(App):
    def build(self):
        rest_list = RestaurantList()
        for idx,rest_name in enumerate(rest_list.default_list):
            old = Label(text=rest_name,font_size= 20,bold=True)
            rest_list.ids.restaurant_list.add_widget(old)
            old.id = "L"+str(rest_list.curr_idx+1)
            btn = Button(size_hint=(0.3,1),text="Delete", background_color=(1, 0, 0, 1),disabled=True,opacity=0,on_press=rest_list.delete_item)
            btn.id = "D"+str(rest_list.curr_idx+1)
            rest_list.ids.restaurant_list.add_widget(btn)
            rest_list.curr_idx+=1
        return rest_list

if __name__ == '__main__':
    RestaurantListApp().run()
