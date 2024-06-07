import flet as ft
import mysql.connector
import time
from flet import View



db = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = "Minh_17102004",
    database = "mellia"
)
mycursor = db.cursor()

def main(page: ft.Page):
    #SET UP ALL FIELD AND FUNCTIONAL BUTTON LAYOUT
    def Authentication(e):
        Authenticated = "SELECT username,password FROM mellia_user WHERE id = 1"
        try:
            mycursor.execute(Authenticated)
            for obj in mycursor:
                user = obj[0]
                #Username
                password = obj[1]
                #Password
            if UsernameField.value == user and PasswordField.value == password:
                print("Login succcessfully")
                CautionText.visible = False
                page.go("/Home")
                UsernameField.value = user
                PasswordField.value = password
            else:
                CautionText.visible = True
                print("Denied !!!")
        except Exception as error :
            print(error)

        db.commit()
        page.update()
        
    def ConfirmednandSaveLogs(e):
        logs = "SELECT username, password FROM mellia_user WHERE id = 1"
        try:
            mycursor.execute(logs)
            for log_obj in mycursor:
                obj_usrname = log_obj[0]
                obj_pwd = log_obj[1]
            UsernameField.value = obj_usrname
            PasswordField.value = obj_pwd

        except Exception as error:
            print(error)
        page.update()



    # logs = "SELECT username, password FROM mellia_user WHERE id = 1"
    # try:
    #     mycursor.execute(logs)
    #     for log_obj in mycursor:
    #         obj_usrname = log_obj[0]
    #         obj_pwd = log_obj[1]
    #     # UsernameField.value = obj_usrname
    #     # PasswordField.value = obj_pwd

    # except Exception as error:
    #     print(error)



    Greeting = ft.Text("Welcome back, Thai Thu", size=20,color="white",text_align='center')
    CautionText = ft.Text("Wrong username or password, try again",color="red",visible=False,size=15)
    UsernameField = ft.TextField(width=300,border=ft.InputBorder.UNDERLINE,color="white",label="Username",label_style=ft.TextStyle(color="white",))
    PasswordField = ft.TextField(width=300,border=ft.InputBorder.UNDERLINE,can_reveal_password=True,password=True,color="white",label="password",label_style=ft.TextStyle(color="white",))
    ForgotPWD = ft.TextButton(text="Forgot password ?",style=ft.ButtonStyle(color="white"))
    CopyrightBrand = ft.Text("Copyright by @mtranquoc77 Inc",size=10,color="white",text_align="center")
    rememberUSR = ft.Checkbox(label="Remember me",label_style=ft.TextStyle(color="white"),fill_color="white",check_color="black",on_change=None,tristate=False)
    LoginButton = ft.ElevatedButton(text="Login",color="black",width=300,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),bgcolor="white",on_click=Authentication)
    Avatar = ft.Container(
        image_src="images/baothu.png",
        image_fit=ft.ImageFit.FILL,
        height=130,
        width=130,
        border_radius=100,
        border=ft.border.all(1.5,"white")
    )
    #SET UP LAYOUT
    Screen_layout = ft.Container(
            ft.Stack(
                [
                    ft.Image(
                        src="images/Cafeteria.png",
                        fit=ft.ImageFit.FILL,
                        width=2000,
                        
                        
                    ),
                    ft.Container(
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            # 
                                            Avatar,
                                            
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Row(
                                        [
                                            Greeting
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    ft.Row(
                                        [
                                            
                                            ft.Column(
                                                [
                                                    
                                                    UsernameField,
                                                    PasswordField,
                                                    CautionText,
                                                    ft.Row(
                                                        [
                                                            ForgotPWD,
                                                            ft.Row(width=5),
                                                            rememberUSR
                                                        ],
                                                        
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                    ),
                                                    LoginButton,
                                                    ft.Row(
                                                        [
                                                            CopyrightBrand
                                                        ],
                                                        width=300,
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                    )
                                                ]
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    )
                                ]
                            ),
                            width=500,
                            height=600,
                            margin=ft.margin.only(top=50),
                            blur=ft.Blur(5,7, ft.BlurTileMode.CLAMP),
                            alignment=ft.alignment.center,
                            border_radius=20,
                            border=ft.border.all(1.5,"white"),
                            padding=ft.padding.only(top=70,left=50,right=50)
                        ),
                        alignment=ft.alignment.center
                    )
                ]
            ),
            margin=ft.margin.only(bottom=100),
            
        )
    






    #Add new Order 
    Banner_title = ft.AppBar(
        title=ft.Text("MELLIA COFFEE & BAKERY",color="white"),
        center_title=True,
        bgcolor="black"
    )

    def selected_page(e):
        for index, page_nav in enumerate(page_stack):
           page_nav.visible = True if index == Menu.selected_index else False
        page.update()
    #Banner customize

    Menu = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.ADD),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.MENU_BOOK),
                label='Menu'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.CHAIR),
                label='Slot & status'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.CHECK_BOX),
                label='Bill'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.ACCOUNT_BALANCE),
                label='Income'
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.SETTINGS),
                label='Settings'
            ),
            
        ],
        on_change=selected_page,
        
    )
    #Menu Rail Selection
    #-----------------
    #SETTINGS

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            ChangeThemeSwitch.label = "Dark"
            page.theme_mode == ft.ThemeMode.DARK
        else:
            ChangeThemeSwitch.label = "Light"
            page.theme_mode == ft.ThemeMode.LIGHT
        #CHANGE THEME COLOR "DARK" TO "LIGHT"
        page.update()
    ChangeThemeSwitch = ft.Switch(label="Light", on_change=change_theme)

    #-----------------
    #Customize size for image and container

    ctn_width = 200
    ctn_height = 350
    

    #-----------------
    #category's Banner

    Coffee_banner = ft.Container(
        ft.Row(
            controls=[
                ft.Text('Coffee & tea',size=30),
            ],
            
        ),
        height=50,
        padding=ft.padding.only(right=100)
    )
    Dessert_banner = ft.Container(
        ft.Row(
            controls=[
                ft.Text('Dessert & side dishes',size=30)
            ],
            
        ),
        height=50,
        padding=ft.padding.only(right=100)
    )
    #-----------------
    #Set up daytime 
    Time = ft.Text(size=15)
    settimetoday = time.strftime("%d%m%Y")
    Time.value = settimetoday

    

    



    #-----------------
    #Coffeee & Tea Image custom
    img1 = ft.Image(
        src="images\Bac-xiu.png",
        width=200,
        height=200,
        border_radius=20
    )
    img2 = ft.Image(
        src="images\caphesuasaigonpng.png",
        width=150,
        height=140,
        border_radius=20
    )
    img3 = ft.Image(
        src="images\caphedenda.png",
        width=170,
        height=170,
        border_radius=20
    )
    img4 = ft.Image(
        src="images\caphemuoi.png",
        width=150,
        height=150,
        border_radius=20
    )
    img5 = ft.Image(
        src="images\lemontea.png",
        width=150,
        height=150,
        border_radius=20
    )
    img6 = ft.Image(
        src="images\peachtea.png",
        width=150,
        height=150,
        border_radius=20
    )
    img7 = ft.Image(
        src="images\orangejuice.png",
        width=250,
        height=150,
        border_radius=20
    )
    #-----------------
    #Dessert & side dishes
    img8 = ft.Image(
        src="images\Croissant.png",
        width=200,
        height=200,
        border_radius=20
    )
    img9 = ft.Image(
        src="images\pancake.png",
        width=150,
        height=200,
        border_radius=20
    )
    img10 = ft.Image(
        src="images\custad.png",
        width=150,
        height=200,
        border_radius=20
    )
    img11 = ft.Image(
        src="images\Sandwich.png",
        width=150,
        height=200,
        border_radius=20
    )
    img12 = ft.Image(
        src="images\strawberry.png",
        width=150,
        height=200,
        border_radius=20
    )
    img13 = ft.Image(
        src="images\Oliu.png",
        width=150,
        height=200,
        border_radius=20
    )



    #---------------------
    #Custome layout for Coffee & Tea Layout
    bacxiu = ft.Container(
        ft.Column(
            controls=[
                img1,
                ft.Row(
                    controls=[
                        
                        ft.Text("Bạc xĩu",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Row(
                    controls=[
                        
                        ft.Text("30.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
      
    )
    #This is "Bac xiu" layout


    milkcoffee = ft.Container(
        ft.Column(
            controls=[
                img2,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Cà phê sữa",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("25.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=70,left=10)
    )
    #This is 'Ca phe sua' Layout


    

    coffenden =  ft.Container(
        ft.Column(
            controls=[
                img3,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Cà phê đen",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("20.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=15,left=10)
    )
    #This is 'Ca phe den ' Layout

    saltcoffee = ft.Container(
        ft.Column(
            controls=[
                img4,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Cà phê muối",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("30.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=50,left=10)
      
    )
    #This is 'ca phe muoi' layout

    lemontea = ft.Container(
        ft.Column(
            controls=[
                img5,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Nước Chanh",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("25.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=50,left=10)
    )
    peachtea = ft.Container(
        ft.Column(
            controls=[
                img6,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Trà đào",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("15.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=50,left=10)
    )

    orangejuice = ft.Container(
        ft.Column(
            controls=[
                img7,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Nước Cam",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("15.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(top=50,left=10)
    )
    #------------------------------
    #Customize Layout for Dessert & side Dishes
    croissant = ft.Container(
        ft.Column(
            controls=[
                img8,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Bánh Sừng Bò",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("25.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=350,left=10)
    )
    pancake = ft.Container(
        ft.Column(
            controls=[
                img9,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Bánh Kếp mật ong",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("27.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=100,left=10)
    )

    custard = ft.Container(
        ft.Column(
            controls=[
                img10,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Bánh bông lan",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("27.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=100,left=10)
    )
    sandwich= ft.Container(
        ft.Column(
            controls=[
                img11,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Bánh Sandwich",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("30.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=100,left=10)
    )
    strawberry= ft.Container(
        ft.Column(
            controls=[
                img12,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Dâu Tây Dà Lạt",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("31.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=100,left=10)
    )
    Oliwe= ft.Container(
        ft.Column(
            controls=[
                img13,
                ft.Row(height=15),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("Mứt Ô liu",size=20),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                
                ft.Row(
                    controls=[
                        
                        ft.Text("31.000 VNĐ",size=15),
                        
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
            ]
        ),
        height=ctn_height,
        width=ctn_width,
        margin= ft.margin.only(bottom=100,left=10)
    )
    #-----------------------------------------------------------------------------------
    
    

    

    #----------------------------------------------------------------------------------
    #LOGIC FUNCTION
    Total_order = ft.Text(size=20)
    total_payment = ft.Text(size=20)

    def TotalOrder(e):
        total = "SELECT COUNT(id) FROM mellia_orders"
        mycursor.execute(total)
        Total_order.value = f"{mycursor.fetchall()[0][0]}"

        page.update()
    def PriceCategories(e):
        if product.value == "Ca phe sua":
            Price_summary.value = 25000 * int(Order_field.value)
        elif product.value == "Bac xiu":
            Price_summary.value = 30000 * int(Order_field.value)
        elif product.value == "Ca phe den":
            Price_summary.value = 20000 * int(Order_field.value)
        elif product.value == "Ca phe muoi":
            Price_summary.value = 30000 * int(Order_field.value)
        elif product.value == "Nuoc chanh":
            Price_summary.value = 25000 * int(Order_field.value)
        elif product.value == "Nuoc cam":
            Price_summary.value = 15000 * int(Order_field.value)
        elif product.value == "Tra dao":
            Price_summary.value = 15000 * int(Order_field.value)
        page.update()
    
    
    
    product = ft.Dropdown(
        label="Product",
        width=200,
        options=[
            ft.dropdown.Option("Ca phe sua"),
            ft.dropdown.Option("Bac xiu"),
            ft.dropdown.Option("Ca phe den"),
            ft.dropdown.Option("Ca phe muoi"),
            ft.dropdown.Option("Nuoc chanh"),
            ft.dropdown.Option("Nuoc cam"),
            ft.dropdown.Option("Tra dao"),
        ],
        on_change=PriceCategories,
        # border_color="white",
        border_color="grey",
        bgcolor="grey"
    )
    StatementOrders = ft.Dropdown(
        label="Order method",
        width=200,
        options=[
            ft.dropdown.Option("Take away"),
            ft.dropdown.Option("on place")
            
        ],
        # border_color="white",
        
    )

    #SET UP ALL FIELD
    name = ft.TextField(label="Slot's ID",width=300, border_color="grey",bgcolor="white")
    table = ft.TextField(label="Slot's Number ",width=200, border_color="grey",bgcolor="white")
    Quantity_choose = ft.TextField(label="Quantity",width=300,border_color="grey",bgcolor="white")
    Order_field = ft.TextField(label="Order",width=300,border_color="grey",bgcolor="white")
    Price_summary = ft.TextField(label="Total",width=300,border_color="grey",read_only=True,on_change=PriceCategories,bgcolor="white")
    Staff_name = ft.TextField(label="Waiter's name",width=200,border_color="grey",bgcolor="white")
    
    
    #LOGIC FUNCTION FOR USER
    def Show(e):
        #CREATE RELEASE ITEM FROM SCHEMAS - 'ORDERS'
        show_command = "SELECT id, tb, quantity, order_slot, product, price, staffname, status FROM mellia_orders "
        mycursor.execute(show_command)

        Order_list.rows.clear()

        for obj in mycursor.fetchall():
            obj_id = obj[0]
            obj_tb = obj[1]
            obj_quantity = obj[2]
            obj_order = obj[3]
            obj_product = obj[4]
            obj_price = obj[5]
            obj_staff = obj[6]
            obj_status = obj[7]
            Order_list.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(int(obj_id),size=20)),
                    ft.DataCell(ft.Text(int(obj_tb),size=20)),
                    ft.DataCell(ft.Text(int(obj_quantity),size=20)),
                    ft.DataCell(ft.Text(int(obj_order),size=20)),
                    ft.DataCell(ft.Text(obj_product,size=20)),
                    ft.DataCell(ft.Text(obj_price,size=20)),
                    ft.DataCell(ft.Text(obj_staff,size=20)),
                    ft.DataCell(ft.Text(obj_status,size=20)),
                    ft.DataCell(option)
                ],
                on_select_changed=lambda e: Edit(e.control.cells[0].content.value,e.control.cells[1].content.value,
                                                        e.control.cells[2].content.value,e.control.cells[3].content.value,
                                                        e.control.cells[4].content.value,e.control.cells[5].content.value,
                                                        e.control.cells[6].content.value,e.control.cells[7].content.value),
                
                #ON SELECTED CONTENT NEED TO BE CLICKED ON BEFORE USE EDIT,REMOVE
            )
        )
        
        db.commit()
        page.update()


    def Order(e):
        Order_list.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(int(name.value),size=20)),
                    ft.DataCell(ft.Text(int(table.value),size=20)),
                    ft.DataCell(ft.Text(int(Quantity_choose.value),size=20)),
                    ft.DataCell(ft.Text(int(Order_field.value),size=20)),
                    ft.DataCell(ft.Text(product.value,size=20)),
                    ft.DataCell(ft.Text(Price_summary.value,size=20)),
                    ft.DataCell(ft.Text(Staff_name.value,size=20)),
                    ft.DataCell(ft.Text(StatementOrders.value,size=20)),
                    ft.DataCell(option)
                ]
            )
        )
        add_item = "INSERT INTO mellia_orders (id, tb, quantity, order_slot, product, price, staffname, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        items = (int(name.value),int(table.value),int(Quantity_choose.value),
                 int(Order_field.value),str(product.value),int(Price_summary.value),
                 str(Staff_name.value),str(StatementOrders.value))
        try:
            mycursor.execute(add_item,items)
            db.commit()
        except Exception as error:
            print("Error - ",error)
        # TotalBill(e)
        TotalOrder(e)
        page.update()

    #GET INFORMATION FROM THE ROW
    def Edit(e,t,q,o,p,pr,s,st):

        name.value = int(e)
        table.value = int(t)
        Quantity_choose.value = int(q)
        Order_field.value = int(o)
        product.value = str(p)
        Price_summary.value = int(pr)
        Staff_name.value = str(s)
        StatementOrders.value = str(st)
        page.update()

    def Edit_Save(e):
        # AFTER CLICKED THE ROW, ALL RECORD FROEM TABLE WILL BE DISPLAY ON THE GUI, EDIT INTO THE FIELD , DROPDOWN SELECTION
        Edit_command = f"UPDATE mellia_orders SET tb = {table.value}, quantity = {Quantity_choose.value}, order_slot = {Order_field.value}, product = '{product.value}', price = {Price_summary.value}, staffname = '{Staff_name.value}', status = '{StatementOrders.value}'  WHERE id = {name.value}"
        try:
            mycursor.execute(Edit_command)
            db.commit()
        except Exception as error:
            print("Error - ",error)
        Order_list.rows.clear()
        PriceCategories(e)
        TotalOrder(e)
        Show(e)
        page.update()


    def Remove_data(e):
        Delete_command = f"DELETE FROM mellia_orders WHERE tb = {table.value} AND quantity = {Quantity_choose.value} AND order_slot = {Order_field.value} AND product = '{product.value}' AND price = {Price_summary.value} AND staffname = '{Staff_name.value}' AND status = '{StatementOrders.value}' AND id = {name.value}"
        try:
            mycursor.execute(Delete_command)
            # del Order_list.rows[name.value, table.value, Quantity_choose.value, Order_field.value, product.value,Price_summary.value, Staff_name.value]
            Order_list.rows.clear()
            Show(e)
        except Exception as error:
            print("Error - ",error)
        page.update()

    def ClearRow(e):
        Order_list.rows.clear()
        page.update()


    def DeleteAll(e):
        Delete_command = "TRUNCATE TABLE mellia_orders"
        mycursor.execute(Delete_command)
        Order_list.rows.clear()
        page.update()


    #BILL CUSTOM FUNCTIONS

    #CLEAR BILL PAYMENT LIST
    def ClearBillList(e):
        Bill_list.rows.clear()
        page.update()
    #SOLVE VOUCHER
    def VoucherSolved(e):
        total_payment.value = int(total_payment.value) - int(Coupon.value)
        page.update()
    #SOLVE CHANGE
    def ResolvedChange(e):
        Change.value = int(CashGiven.value) - int(total_payment.value)
        page.update()

    #CLEAR SCREEN OF BILL
    def ClearBill(e):
        SlotID.value = ""
        Date.value = ""
        Month.value = ""
        Year.value = ""
        Coupon.value = ""
        CashGiven.value = ""
        Change.value = ""
        PaymentMethod.value = ""
        Bill_list.rows.clear()
        SlotIDrelease.value = "Slot.ID: "
        paymentmethodrelease.value = "Payment method: "
        Cashgivenrelease.value = "Guest payment: "
        changerelease.value = "Change: "
        Couponrelease.value = "Voucher: "
        total_payment.value = ""
        page.update()

    #SOLVE TOTAL
    def TotalPayment(e):
        SumPrice = f"SELECT SUM(price) FROM mellia_orders WHERE tb = {SlotID.value}"
        mycursor.execute(SumPrice)
        sum_rs = mycursor.fetchall()
        total_payment.value = int(sum_rs[0][0])
        ResolvedChange(e)
        
        page.update()
    #UPDATE BILL'S INFORMATION
    def UpdateBill(e):
        SetdatetTime = f"{Year.value}-{Month.value}-{Month.value}"
        updatedchanged = f"UPDATE mellia_bill SET total = {total_payment.value}, settime = '{SetdatetTime}' , method = '{PaymentMethod.value}', coupon = {Coupon.value} WHERE tb = {SlotID.value}"
        try:
            mycursor.execute(updatedchanged)
            db.commit()
        except Exception as error:
            print("Error - ",error)



    #CREATE VALUE RECIEVED FROM FIELD
    def BillID(e):
        BillIDvalue = SlotID.value
        SlotIDrelease.value = f"Slot.ID: {BillIDvalue}"
        page.update()
    def Method(e):
        methodvalue = PaymentMethod.value
        paymentmethodrelease.value = f"Payment method: {methodvalue}"
        page.update()
    def Cashgiven(e):
        Cashgivenvalue = CashGiven.value
        Cashgivenrelease.value = f"Guest payment: {Cashgivenvalue}"
        page.update()

    def ChangedCost(e):
        changevalue = Change.value
        changerelease.value = f"Change: {changevalue}"
        page.update()
    def CouponSolved(e):
        couponvalue = Coupon.value
        Couponrelease.value = f"Voucher: {couponvalue}"
        page.update()

    def BillRelease(e):
        BillID(e)
        Method(e)
        Cashgiven(e)
        ChangedCost(e)
        CouponSolved(e)
        page.update()

    def SaveBill(e):
        SaveChanged = "INSERT INTO mellia_bill (tb, total, settime, method, coupon) VALUES (%s, %s, %s, %s, %s)"
        SetdatetTime = f"{Year.value}-{Month.value}-{Month.value}"
        insertedChanged = (int(SlotID.value),int(total_payment.value), SetdatetTime, str(PaymentMethod.value), int(Coupon.value))
        try:
            mycursor.execute(SaveChanged,insertedChanged)
            db.commit()
        except Exception as error:
            print("Error - ",error)
        page.update()


    #Show off list of products and total payment of quantity
    def SetupBill(e):
        ClearBillList(e)
        TotalOrder = f"SELECT tb, product, order_slot, price FROM Mellia_orders WHERE tb = {SlotID.value} "
        try:
            mycursor.execute(TotalOrder)
            for obj in mycursor.fetchall():
                obj_slot = obj[0]
                obj_prdct = obj[1]
                obj_order = obj[2]
                obj_price = obj[3]
                Bill_list.rows.append(ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(int(obj_slot),size=20)),
                        ft.DataCell(ft.Text(str(obj_prdct),size=20)),
                        ft.DataCell(ft.Text(int(obj_order),size=20)),
                        ft.DataCell(ft.Text(int(obj_price),size=20))
                    ],
                
                )
            )
            TotalPayment(e)
            VoucherSolved(e)
            BillRelease(e)
            
            
            
        except Exception as error:
            print("Error - ",error)
        page.update()

    
    #----------------------------------------------------------------------------------
    #Order and Payment

    ClearButton = ft.ElevatedButton("Clear",on_click=ClearRow,bgcolor="Red",color="white")
    RemoveDataButton = ft.ElevatedButton("Remove History",on_click=DeleteAll,bgcolor="Red",color="white")
    Addbutton = ft.ElevatedButton("Order",on_click=Order,bgcolor="green",color="white")
    Deletebutton = ft.IconButton(ft.icons.DELETE,on_click=Remove_data,icon_color="red")
    Editbutton = ft.ElevatedButton("Edit & Save",on_click=Edit_Save,bgcolor="blue",color="white")
    Refreshbutton = ft.ElevatedButton("History",on_click=Show,bgcolor="lightblue",color="white",)
    option = ft.Row(
        [
            Deletebutton
        ],
        
    )
    TableTitle = ft.Container(
        
        ft.Row([ft.Text("ORDER & PAYMENT",color="black")],alignment=ft.MainAxisAlignment.CENTER),
        
        height=60,
        width=1370,
        border_radius=ft.border_radius.only(top_left=15,top_right=15),
        border=ft.border.all(1,"grey")
        
    )

    Order_list = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("No.ID",size=20)),
            ft.DataColumn(ft.Text("No.Table",size=20)),
            ft.DataColumn(ft.Text("Quantity",size=20)),
            ft.DataColumn(ft.Text("Order",size=20)),
            ft.DataColumn(ft.Text("Product",size=20)),
            ft.DataColumn(ft.Text("Total",size=20)),
            ft.DataColumn(ft.Text("Waiter",size=20)),
            ft.DataColumn(ft.Text("Status",size=20)),
            ft.DataColumn(ft.Text("",size=20))
            
        ],
        rows=[],
        
    )
    
    Order_layout = ft.Container(
        ft.Column(
            [
                Order_list
            ]
        ),
        margin=ft.margin.only(bottom=500),
        padding=ft.padding.only(left=10)
    )
    

    option_layout_order = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        name,
                        Order_field,
                        table,
                        Staff_name
                    ]
                ),
                ft.Row(
                    controls=[
                        Quantity_choose,
                        Price_summary,
                        product,
                        StatementOrders
                        
                        
                    ]
                ),
                ft.Row(
                    controls=[
                        Addbutton,
                        Refreshbutton,
                        RemoveDataButton,
                        ClearButton,
                        Editbutton
                    ]
                ),
                
                
                
            ]
        ),
        width=1370,
        height=250,
        border=ft.border.all(1,"grey"),
        padding=20,
        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
    )



    #----------------------------------------------------------------------------------
    #Bill Layout 






    QRcode = ft.Image(
        src="images\Vcb.png",
        width=220,
        height=220,
        border_radius=20
    )

    PaymentLayout = ft.Container(

        ft.Row(
            [
                ft.Text("BILL & PAYMENT")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=60,
        width=1370,
        border_radius=30,
        border=ft.border.all(1,"grey")

    )

    PaymentMethod = ft.Dropdown(
        label="Payment method",
        width=200,
        options=[
            ft.dropdown.Option("Cash Payment"),
            ft.dropdown.Option("Online Banking"),
            
            
        ],
        # border_color="white",
        
    )
    #Field's Form 
    SlotID = ft.TextField(label="Slot.ID",width=320)
    Date = ft.TextField(label="Date",width=100)
    Month = ft.TextField(label="Month",width=100)
    Year = ft.TextField(label="Year",width=100)
    Coupon = ft.TextField(label="Voucher",value=0,width=200)
    CashGiven = ft.TextField(label="Guest's Payment",width=320)
    Change = ft.TextField(label="Change",width=200)
    BankID = ft.TextField(label="Banking's ID",value="1029713023",width=320,color="black")
    Bank = ft.TextField(label="Bank",width=200,value="Vietcombank")

    #Button's layout
    SubmitBillbutton = ft.ElevatedButton("Submit",width=200,bgcolor="green",color="white",on_click=SetupBill)
    ClearBillbutton = ft.ElevatedButton("Clear",width=200,bgcolor="red",color="white",on_click=ClearBill)
    EditSaveBillbutton = ft.ElevatedButton("Edit & Save",width=200,bgcolor="blue",color="white",on_click = UpdateBill)
    SaveBillbutton = ft.ElevatedButton("Save Form",width=300,bgcolor="orange",color="white",on_click=SaveBill)


    #CUSTOM BILL RELEASE
    SlotIDrelease = ft.Text("Slot.ID: ",size=20)
    paymentmethodrelease = ft.Text("Payment method: ",size=20)
    Cashgivenrelease = ft.Text("Guest payment: ",size=20)
    changerelease = ft.Text("Change: ",size=20)
    Couponrelease = ft.Text("Voucher: ",size=20)
    

    #CUSTOM LAYOUT FOR BUTTON WITH BILL

    OptionLayoutButton = ft.Container(
        ft.Row(
            [
                SubmitBillbutton,
                ClearBillbutton,
                EditSaveBillbutton
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=1370,
        height=70,
    )


    #Custom Container for Field & input-Selection
    CustomBillLayout = ft.Container(

        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        SlotID,
                        ft.Row(
                            controls=[
                                Date,Month,Year
                            ]
                        ),
                        CashGiven,
                        BankID
                        
                    ]
                ),
                ft.Column(
                    controls=[
                        PaymentMethod,
                        Coupon,
                        Change,
                        Bank
                    ]
                ),
                ft.Column(
                    controls=[
                        QRcode,

                    ]
                ),
                
            
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=1370,
        height=300,
        border=ft.border.all(1,"grey"),
        padding=20,
        border_radius=20,
       
    )

    #Bill Payment
    Bill_list = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Table Slot",size=20)),
            ft.DataColumn(ft.Text("Description",size=20)),
            ft.DataColumn(ft.Text("Quantity",size=20)),
            ft.DataColumn(ft.Text("Price",size=20))

        ],
        rows=[],
        
    )
    #Custom Bill

    Bill_title = ft.Container(
        ft.Row(
            [
                ft.Text("Bill Transfer information")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=1370,
        height=50,
        border=ft.border.all(1,"grey"),
        
    )

    


    Bill_table_summary = ft.Container(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Row(
                            [
                                SlotIDrelease
                                
                            ]
                        ),
                        ft.Divider(color=None),
                        ft.Row(
                            [
                                
                               paymentmethodrelease
                                 
                            ]
                        ),
                        ft.Divider(color=None),
                        ft.Row(
                            [
                                
                                Cashgivenrelease
                            ]
                        ),
                        ft.Divider(color=None),
                        ft.Row(
                            [
                                
                                changerelease
                                
                            ]
                        ),
                        ft.Divider(color=None),
                        ft.Row(
                            [
                                
                                Couponrelease

                            ]
                        ),
                        ft.Divider(color=None),
                        ft.Row(
                            [
                                ft.Text("Total: ",size=20),
                                total_payment
                            ]
                        ),
                        ft.Divider(color=None),
                    ]
                )
            ]
        ),
        width=680,
        height=400,
        border=ft.border.all(1,"grey"),
        margin=ft.margin.only(bottom=10),
        padding=20
    )
    Bill_table_list = ft.Container(
        ft.Row(
            [
                ft.Column(
                    [
                      
                       Bill_list
                    ],
                    scroll=ft.ScrollMode.ALWAYS,
                    height=500
                )
            ]
        ),
        width=680,
        height=400,
        border=ft.border.all(1,"grey"),
        margin=ft.margin.only(bottom=10),
        padding=50
    )




    #----------------------------------------------------------------------------------

    #PAGE SET UP
    #----------------------------------------------------------------------------------
    #Menu

    page_1 = ft.Column(
        controls=[
            Coffee_banner,
            ft.Row(
                controls=[
                    bacxiu,
                    milkcoffee,
                    coffenden,
                    saltcoffee,
                    lemontea,
                    peachtea,
                    orangejuice,
                    
                ],
                scroll= ft.ScrollMode.ALWAYS,
                height=400
            ),
            ft.Divider(color="grey"),
            Dessert_banner,
            ft.Row(
                controls=[
                    croissant,
                    pancake,
                    custard,
                    sandwich,
                    strawberry,
                    Oliwe
                ],
                scroll= ft.ScrollMode.ALWAYS,
                height=400
            )
        ],

        alignment=ft.MainAxisAlignment.START,
        expand=True,
        scroll=ft.ScrollMode.ALWAYS,
        height=1000,
        
    
    )

    #Order & Payment
    page_2 = ft.Column(
        controls=[
            TableTitle,
            option_layout_order,
            ft.Divider(color="grey"),
            Order_layout,
            

        ]
        
    )  

    #Bills and Payment
    page_3 = ft.Column(
        controls=[
            PaymentLayout,
            CustomBillLayout,
            OptionLayoutButton,
            ft.Divider(color="grey"),
            Bill_title,
            ft.Column(
                [
                    ft.Row(
                        [
                            Bill_table_summary,
                            Bill_table_list

                        ]
                    ),
                    ft.Row(
                        [
                            SaveBillbutton
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=50

                    )
                ]
            )
            
        ]
    )
    #----------------------------------------------------------------------------------
    #PAGE STACK LIST 
    #Set up Page stack for route change
    page_stack = [
        ft.Container(page_1,visible=True),
        ft.Container(page_2,visible=False),
        ft.Container(page_3,visible=False)
    ]

    #----------------------------------------------------------------------------------

    def route_change(e):
        page.views.clear
        page.views.append(
            View(
                "/Login",
                [
                    
                    Screen_layout
                ],
                padding=0
                # scroll=ft.ScrollMode.ALWAYS
                
            ),
                
        )
        if page.route == "/Home":
            page.views.append(
                View(
                    "/Home",
                    [
                        Banner_title,
                        ft.Row(
                            [
                                Menu,
                                ft.VerticalDivider(width=1,color="grey"),
                                ft.Column(page_stack,scroll=ft.ScrollMode.ALWAYS, expand=True)
                            ],
                            expand=True
                        ),
                    ]
                )
            )
        
        page.update()

    def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.theme_mode = ft.ThemeMode.LIGHT
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)



    
    page.bgcolor = "black"
    page.update()
if __name__ == "__main__":

    ft.app(target=main,assets_dir='assets')