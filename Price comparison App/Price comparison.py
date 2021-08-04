from bs4 import BeautifulSoup
import requests
from tkinter import *

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def flipkart(name):
    try:
        global flipkart
        name1 = name.replace(" ", "+")
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(
            f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
            headers=headers)

        print("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text, 'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip() 
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()
            
            return f"Product: {flipkart_name}\nPrice : {flipkart_price}\n"
        else:
            
            flipkart_price = 'no product found'
        return flipkart_price
    except:
        
        flipkart_price = 'no product found'
    return flipkart_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
        print("\nSearching in amazon:")
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0, amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                
                return f"Product: {amazon_name}\nPrice : {amazon_price}\n"
                break
            else:
                i += 1
                i = int(i)
                if i == amazon_page_length:
                    
                    amazon_price = 'no product found'
                    break
        return amazon_price
    except:
        print("amazon: No product found!")
        print("-----------------------")
        amazon_price = '0'
    return amazon_price

def olx(name):
    try:
        global olx
        name1 = name.replace(" ", "-")
        olx = f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true', headers=headers)
        print("\nSearching in OLX......")
        soup = BeautifulSoup(res.text, 'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0, olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"

                
                return f"Product: {olx_name}\nPrice : {olx_price}\n"
                break
            else:
                i += 1
                i = int(i)
                if i == olx_page_length:
                    
                    olx_price = 'product not found'
                    break
        return olx_price
    except:
        
        olx_price = 'no product found'
    return olx_price

def convert(a):
    b = a.replace(" ", '')
    c = b.replace("INR", '')
    d = c.replace(",", '')
    f = d.replace("₹", '')
    g = int(float(f))
    return g

def search():
    t1 = flipkart(product_name.get())
    box1.insert(1.0, t1)

    t2 = amazon(product_name.get())
    box2.insert(1.0, t2)
    
    t3 = olx(product_name.get())
    box3.insert(1.0, t3)

window = Tk()
window.wm_title("Price comparison ")
window.minsize(1366, 768)

lable_one = Label(window, text="Enter Product Name :", font=("Verdana", 15 ,"bold"), bg='#6D7B8D', fg="white")
lable_one.place(relx=0.2, rely=0.1, anchor="center")

product_name =  StringVar()
product_name_entry =  Entry(window, textvariable=product_name, width=65)
product_name_entry.place(relx=0.535, rely=0.1, anchor="center")

search_button = Button(window, text="Search", width=12, command=search)
search_button.place(relx=0.53, rely=0.2, anchor="center")

l1 = Label(window, text="Flipkart", font=("Verdana", 20, "bold"), bg='#6D7B8D', fg="white")
l2 = Label(window, text="Amazon", font=("Verdana", 20 ,"bold"), bg='#6D7B8D', fg="white")
l3 = Label(window, text="Olx", font=("Verdana", 20, "bold"), bg='#6D7B8D', fg="white")

l1.place(relx=0.1, rely=0.4)
l2.place(relx=0.1, rely=0.6)
l3.place(relx=0.1, rely=0.8)

box1 = Text(window, height=4, width=50)
box2 = Text(window, height=4, width=50)
box3 = Text(window, height=4, width=50)

box1.place(relx=0.4, rely=0.4)
box2.place(relx=0.4, rely=0.6)
box3.place(relx=0.4, rely=0.8)

window.configure(bg='#6D7B8D')
window.mainloop()