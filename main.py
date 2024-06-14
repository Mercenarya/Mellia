import flet as ft
import mysql.connector
import time
from flet import View
import base64



db = mysql.connector.connect(
    host="localhost",
    username = "root",
    password = "Minh_17102004",
    database = "mellia"
)
mycursor = db.cursor()

def main(page: ft.Page):
    #DISPLAY PRODUCT'S LIST ON MAIN PAGE
    TitleIMG = ft.TextField(label="Name",width=210,border_color="black",color="white")
    SetPrice = ft.TextField(label="Price",width=210,border_color="black",color="white")
    ContentProduct = ft.TextField(label="Comment",width=210,border_color="black",color="white")
    IDproduct = ft.TextField(label="ID",width=210,border_color="black",color="white")


    TitleProduct = ft.Text(size=40,weight=ft.FontWeight.BOLD,color="white")
    PriceProduct = ft.Text(value=str(SetPrice.value),size=50,weight=ft.FontWeight.BOLD,color="white")
    NoteProduct = ft.Text(size=15)


    #CREATE CUSTOMIZE'S LAYOUT
    def ImageDiscline(e):
        IMGScale.image_src_base64 = None
        TestImgcontainer.image_src_base64 = None
        page.update()
    def Handle_loaded_file(e: ft.FilePickerResultEvent):
        if e.files and len(e.files):
            with open(e.files[0].path, 'rb') as r:
                IMGScale.image_src_base64 = base64.b64encode(r.read()).decode('utf-8')
                TestImgcontainer.image_src = str(e.files[0].path)
                print(e.files[0].path)
                page.update()
    def ViewProduct(e):
        ViewProductList = """ SELECT name FROM producttb
                              UNION
                              SELECT name FROM productsb
                            """
        try:
            mycursor.execute(ViewProductList)
            for obj in mycursor.fetchall():


                product.options.append(
                    ft.dropdown.Option(str(obj[0])),
                )
            db.commit()
        except Exception as error:
            print(error)
        page.update()

    def CategoriesCustomize(e):
        
        product.options.append(
            ft.dropdown.Option(str(TitleIMG.value)),
        )

        
        if CategoriesSelection.value == "Drink & Coffee":
            SaveItems = "INSERT INTO producttb (id, name, price, content, image) VALUES (%s, %s, %s, %s, %s)"
            Items = (int(IDproduct.value),str(TitleIMG.value),int(SetPrice.value),str(ContentProduct.value),TestImgcontainer.image_src)
            PriceProduct.value = str(SetPrice.value)+" $"
            TitleProduct.value = TitleIMG.value
            NoteProduct.value = ContentProduct.value
            try:
                mycursor.execute(SaveItems,Items)
                List_product.controls.append(Layout_IMG_1)
                List_product.controls.clear()
                List_product_2.controls.clear()
                ListItems(e)
                print("Saved")
            except Exception as error:
                print(error)
        elif CategoriesSelection.value == "Desserts & Sidedishes":
            SaveItems = "INSERT INTO productsb (id, name, price, content, image) VALUES (%s, %s, %s, %s, %s)"
            Items = (int(IDproduct.value),str(TitleIMG.value),int(SetPrice.value),str(ContentProduct.value),TestImgcontainer.image_src)
            PriceProduct.value = SetPrice.value
            TitleProduct.value = TitleIMG.value
            NoteProduct.value = ContentProduct.value
            try:
                mycursor.execute(SaveItems,Items)
                List_product_2.controls.append(Layout_IMG_1)
                List_product.controls.clear()
                List_product_2.controls.clear()
                ListItems(e)
                print("Saved")
            except Exception as error:
                print(error)
        db.commit()
        
        page.update()

    file_picked = ft.FilePicker(on_result=Handle_loaded_file)
    page.overlay.append(file_picked)

    CategoriesSelection = ft.Dropdown(
        label="Categories",
        width=400,
        options=[
            ft.dropdown.Option("Drink & Coffee"),
            ft.dropdown.Option("Desserts & Sidedishes")
        ],
        color="white",
        border_color="white"
        
    )

    
    TitleIMG = ft.TextField(label="Name",width=400,border_color="white",color="white")
    SetPrice = ft.TextField(label="Price",width=400,border_color="white",color="white")
    ContentProduct = ft.TextField(label="Comment",width=400,border_color="white",color="white")
    IDproduct = ft.TextField(label="ID",width=400,border_color="white",color="white")


    TitleProduct = ft.Text(size=20,weight=ft.FontWeight.BOLD,color="white")
    PriceProduct = ft.Text(value=str(SetPrice.value)+"$",weight=ft.FontWeight.BOLD,size=20,color="white")
    NoteProduct = ft.Text(color="white")
    
    
    def ClearItemChanges(e):
        SetPrice.value = None
        TitleIMG.value = None
        IDproduct.value = None
        ContentProduct.value = None
        CategoriesSelection.value = None
        page.update()
    
    IMGupload = ft.IconButton(icon=ft.icons.UPLOAD,icon_color="black",bgcolor="white",on_click= lambda _:file_picked.pick_files(
                                    allow_multiple=False, allowed_extensions=['png']),icon_size=20)
    IMGdiscilne = ft.IconButton(icon=ft.icons.DELETE,icon_color="black",bgcolor="white",on_click=ImageDiscline,icon_size=20)
    SaveItemButton = ft.ElevatedButton("Add new product",color="white",bgcolor="Blue",width=400,on_click=CategoriesCustomize)
    ClearItemButton = ft.ElevatedButton("Clear all changes",color="white",bgcolor="red",width=400,on_click=ClearItemChanges)

    IMGScale = ft.Container(
        image_src=None,
        bgcolor="white",
        width=650,
        height=670,
        border_radius=20,
        border=ft.border.all(1, "black")
    )

    CustomizeInput = ft.Container(

        ft.Column(
            [
                IDproduct,
                TitleIMG,
                ContentProduct,
                SetPrice,
                CategoriesSelection,
                SaveItemButton,
                ClearItemButton
            ],
            
        ),
        width=500,
        height=670,
        padding=ft.padding.only(left=50,top=30),
        margin=ft.margin.only(bottom=55),
        bgcolor="brown",
        border_radius= 20
            

    )
    CustomLayut = ft.Container(
        ft.Row(
            [
               
               ft.Column(
                   [
                        IMGScale,
                        ft.Row(
                            [
                                IMGupload,
                                IMGdiscilne,
                                
                                # TestUpload
                            ],
                            width=650,
                            alignment=ft.MainAxisAlignment.START
                        )
                   ]
               ),
               
               ft.Column(
                   [
                       CustomizeInput     
                   ]
               )
            ]
        ),
        padding=ft.padding.only(left=100,top=50),
        
    )






    def ListItems(e):
        ViewAlltb = """ SELECT name,price,content,image
                FROM producttb"""
        mycursor.execute(ViewAlltb)
        for obj in mycursor.fetchall():
            obj_name = obj[0]
            obj_price = obj[1]
            obj_note = obj[2]
            obj_img = obj[3]
            List_product.controls.append(
                ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    image_src=obj_img,
                                    bgcolor="#E5E5E5",
                                    width=250,
                                    height=150,
                                    padding=50,
                                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                                ),
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Column(
                                                        [
                                                            ft.Text(value=obj_name,size=20,weight=ft.FontWeight.BOLD,color="white"),
                                                            ft.Text(value=obj_note,color="white"),
                                                            ft.Text(value=str(obj_price)+"$",size=20,weight="bold",color="white"),
                                                        ],
                                                        width=150
                                                    ),
                                                    
                                                    AddIconButton
                                                    
                                                ]
                                            ),

                                        ]
                                    ),
                                    padding=ft.padding.only(left=20)
                                )
                            ]
                        ),
                        shadow = ft.BoxShadow(
                            blur_radius = 5,
                            color = ft.colors.BLACK,
                            blur_style = ft.ShadowBlurStyle.OUTER,
                        ),
                        width=250,
                        height=340,
                        padding=ft.padding.only(bottom=100),
                        bgcolor="#6F4E37",
                        margin=ft.margin.only(left=10,top=10),
                        border_radius=20,
                        border=ft.border.BorderSide(2,"#6F4E37")
                    )
            )
        ViewAlltsb = """ SELECT name,price,content,image
            FROM productsb"""
        mycursor.execute(ViewAlltsb)
        for obj in mycursor.fetchall():
            obj_name = obj[0]
            obj_price = obj[1]
            obj_note = obj[2]
            obj_img = obj[3]
            List_product_2.controls.append(
                ft.Container(
                        ft.Column(
                            [
                                ft.Container(
                                    image_src=obj_img,
                                    bgcolor="#E5E5E5",
                                    width=250,
                                    height=150,
                                    padding=50,
                                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                                ),
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Column(
                                                        [
                                                            ft.Text(value=obj_name,size=20,weight=ft.FontWeight.BOLD,color="white"),
                                                            ft.Text(value=obj_note,color="white"),
                                                            ft.Text(value=str(obj_price)+"$",size=20,weight="bold",color="white"),
                                                        ],
                                                        width=150
                                                    ),
                                                    
                                                    AddIconButton
                                                    
                                                ]
                                            ),

                                        ]
                                    ),
                                    padding=ft.padding.only(left=20)
                                )
                            ]
                        ),
                        shadow = ft.BoxShadow(
                            blur_radius = 5,
                            color = ft.colors.BLACK,
                            blur_style = ft.ShadowBlurStyle.OUTER,
                        ),
                        width=250,
                        height=340,
                        padding=ft.padding.only(bottom=100),
                        bgcolor="#6F4E37",
                        margin=ft.margin.only(left=10,top=10),
                        border_radius=20,
                        border=ft.border.BorderSide(2,"#6F4E37")
                    )
                )
            db.commit()
        page.update()
    AddIconButton = ft.IconButton(icon=ft.icons.ARROW_RIGHT,bgcolor="#e1f6f4",icon_color="#6F4E37",on_click=None,icon_size=40)
    ButtonLayout = ft.Container(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Column(
                            [
                                TitleProduct,                                
                                NoteProduct,
                                PriceProduct
                                
                            ],
                            width=150
                        ),
                        
                        AddIconButton
                        
                    ]
                ),

            ]
        ),
        padding=ft.padding.only(left=20)
    )
    TestImgcontainer = ft.Container(
        image_src=None,
        bgcolor="#E5E5E5",
        width=250,
        height=150,
        padding=50,
        border_radius=ft.border_radius.only(top_left=15,top_right=15),
    )
    Layout_IMG_1 = ft.Container(
        
        ft.Column(
            [
                TestImgcontainer,
                ButtonLayout
            ]
        ),
        shadow = ft.BoxShadow(
            blur_radius = 20,
            color = ft.colors.BLACK,
            blur_style = ft.ShadowBlurStyle.OUTER,
        ),
        width=250,
        height=340,
        padding=ft.padding.only(bottom=100),
        bgcolor="#6F4E37",
        margin=ft.margin.only(left=10,top=10),
        border_radius=20,
        border=ft.border.BorderSide(2,"#6F4E37")
        
    )
    List_product = ft.Row(
        [
            
            
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
    List_product_2 = ft.Row(
        [
            
            
        ],
        scroll=ft.ScrollMode.ALWAYS
    )














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
                ConfirmednandSaveLogs(e)
                # UsernameField.value = user
                # PasswordField.value = password
                ListItems(e)
                Show(e)
                ViewProduct(e)
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




    Greeting = ft.Text("Welcome back, Thai Thu", size=20,color="white",text_align='center')
    CautionText = ft.Text("Wrong username or password, try again",color="red",visible=False,size=15)
    UsernameField = ft.TextField(width=300,border=ft.InputBorder.UNDERLINE,color="white",label="Username",label_style=ft.TextStyle(color="white",))
    PasswordField = ft.TextField(width=300,border=ft.InputBorder.UNDERLINE,can_reveal_password=True,password=True,color="white",label="password",label_style=ft.TextStyle(color="white",))
    ForgotPWD = ft.TextButton(text="Forgot password ?",style=ft.ButtonStyle(color="white"))
    CopyrightBrand = ft.Text("Copyright by @mtranquoc77 Inc",size=10,color="white",text_align="center")
    rememberUSR = ft.Checkbox(label="Remember me",label_style=ft.TextStyle(color="white"),fill_color="white",check_color="black",on_change=None,tristate=False)
    LoginButton = ft.ElevatedButton(text="Login",color="black",width=300,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),bgcolor="white",on_click=Authentication)
    Avatar = ft.Container(
        image_src="images/AVT.png",
        image_fit=ft.ImageFit.FILL,
        height=130,
        width=130,
        border_radius=100,
        border=ft.border.all(1,"white")
    )
    #SET UP LAYOUT
    Screen_layout = ft.Container(
            ft.Stack(
                [
                    ft.Image(
                        src="images/Cafeteria.png",
                        fit=ft.ImageFit.FILL,
                        width=2000,
                        height=1000,
                        expand= True,
                        opacity=0.9
                        
                        
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
                            blur=ft.Blur(5,10, ft.BlurTileMode.CLAMP),
                            alignment=ft.alignment.center,
                            border_radius=20,
                            border=ft.border.all(1,"white"),
                            padding=ft.padding.only(top=70,left=50,right=50)
                        ),
                        alignment=ft.alignment.center
                    )
                ]
            ),
            margin=ft.margin.only(bottom=100),
            
        )
    






    #Add new Order 

    SearchTool = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Search",
        view_hint_text="Choose a product from the suggestions...",
        bar_bgcolor="white",
        width=1000
        
    )

    Banner_title = ft.Container(
        ft.Stack(
            [
                ft.Image(
                    src="images/cafeteria.png",
                    fit="cover",
                    width=2000
                ),
                ft.Container(
                    ft.Row(
                        [
                            ft.Column(
                                
                                [
                                    
                                    ft.Text("Welcome to Mellia Coffee",size=50,weight="bold",color="white"),
                                    ft.Text("Select and enjoy our product, have a nice day",size=20,color="white")
                                
                                ]
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                        
                    ),
                    width=1000,
                    padding=ft.padding.only(top=150,left=400)
                )
            ]
        ),
        height=400,
        margin=ft.margin.only(bottom=5)
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
                icon_content=ft.Icon(ft.icons.DASHBOARD_CUSTOMIZE),
                label='Customize'
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
        
        
        bgcolor="#6F4E37",
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

   
    #-----------------
    #category's Banner

    Coffee_banner = ft.Container(
        ft.Row(
            controls=[
                ft.Text('Coffee & tea',size=30,color="black",weight="bold"),
            ],
            width=2000,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=100,
        width=1350,
        

        padding=ft.padding.only(right=50),
        border_radius=20
    )
    Dessert_banner = ft.Container(
       ft.Row(
            controls=[
                ft.Text('Desserts & Side dishes',size=30,color="black",weight="bold"),
            ],
            width=2000,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=100,
        width=1350,
        

        padding=ft.padding.only(right=50),
        border_radius=20
    )
    #-----------------
    #Set up daytime 
    Time = ft.Text(size=15)
    settimetoday = time.strftime("%d%m%Y")
    Time.value = settimetoday
    
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

        SolvedPriceCommand = f""" SELECT price FROM producttb WHERE name = '{product.value}'
                                UNION 
                                SELECT price FROM productsb WHERE name = '{product.value}'
                            """
        

        try:
            mycursor.execute(SolvedPriceCommand)
            for price in mycursor.fetchall():
                Obj_price = price[0]
            total = int(Obj_price)*int(Order_field.value)
            Price_summary.value = total
            db.commit()    
        except Exception as error:
            print(error)
        
        # if product.value == "Ca phe sua":
        #     Price_summary.value = 25000 * int(Order_field.value)
        
        page.update()
    
    
    
    product = ft.Dropdown(
       
        label="Product",
        width=200,
        options=[
        
            
        ],
        on_change=PriceCategories,
        # border_color="white",
        border_color="white",
        color="white"
    )
    StatementOrders = ft.Dropdown(
        label="Order method",
        width=200,
        options=[
            ft.dropdown.Option("Take away"),
            ft.dropdown.Option("on place")
            
        ],
        border_color="white",
        color="white"
        
    )

    #SET UP ALL FIELD
    name = ft.TextField(label="Slot's ID",width=300, border_color="white",color="white")
    table = ft.TextField(label="Slot's Number ",width=200, border_color="white",color="white")
    Quantity_choose = ft.TextField(label="Quantity",width=300,border_color="white",color="white")
    Order_field = ft.TextField(label="Order",width=300,border_color="white",color="white")
    Price_summary = ft.TextField(label="Total",width=300,border_color="white",color="white",read_only=True,on_change=PriceCategories)
    Staff_name = ft.TextField(label="Waiter's name",width=200,border_color="white",color="white")
    
    
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
                    ft.DataCell(ft.Text(int(obj_id),size=20,color="black")),
                    ft.DataCell(ft.Text(int(obj_tb),size=20,color="black")),
                    ft.DataCell(ft.Text(int(obj_quantity),size=20,color="black")),
                    ft.DataCell(ft.Text(int(obj_order),size=20,color="black")),
                    ft.DataCell(ft.Text(obj_product,size=20,color="black")),
                    ft.DataCell(ft.Text(obj_price,size=20,color="black")),
                    ft.DataCell(ft.Text(obj_staff,size=20,color="black")),
                    ft.DataCell(ft.Text(obj_status,size=20,color="black")),
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
                    ft.DataCell(ft.Text(int(name.value),size=20,color="black")),
                    ft.DataCell(ft.Text(int(table.value),size=20,color="black")),
                    ft.DataCell(ft.Text(int(Quantity_choose.value),size=20,color="black")),
                    ft.DataCell(ft.Text(int(Order_field.value),size=20,color="black")),
                    ft.DataCell(ft.Text(product.value,size=20,color="black")),
                    ft.DataCell(ft.Text(Price_summary.value,size=20,color="black")),
                    ft.DataCell(ft.Text(Staff_name.value,size=20,color="black")),
                    ft.DataCell(ft.Text(StatementOrders.value,size=20,color="black")),
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
                        ft.DataCell(ft.Text(int(obj_slot),size=20,color="white")),
                        ft.DataCell(ft.Text(str(obj_prdct),size=20,color="white")),
                        ft.DataCell(ft.Text(int(obj_order),size=20,color="white")),
                        ft.DataCell(ft.Text(int(obj_price),size=20,color="white"))
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
        
        ft.Row([ft.Text("ORDER & PAYMENT",color="white",weight="bold")],alignment=ft.MainAxisAlignment.CENTER),
        bgcolor="brown",
        height=60,
        width=1370,
        border_radius=ft.border_radius.only(top_left=15,top_right=15),
        border=ft.border.all(1,"grey")
        
    )

    Order_list = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("No.ID",size=20,color="black")),
            ft.DataColumn(ft.Text("No.Table",size=20,color="black")),
            ft.DataColumn(ft.Text("Quantity",size=20,color="black")),
            ft.DataColumn(ft.Text("Order",size=20,color="black")),
            ft.DataColumn(ft.Text("Product",size=20,color="black")),
            ft.DataColumn(ft.Text("Total",size=20,color="black")),
            ft.DataColumn(ft.Text("Waiter",size=20,color="black")),
            ft.DataColumn(ft.Text("Status",size=20,color="black")),
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
        margin=ft.margin.only(bottom=500,left=100),
        padding=ft.padding.only(left=50),
        bgcolor="",
        shadow = ft.BoxShadow(
            blur_radius = 5,
            color = ft.colors.BLACK,
            blur_style = ft.ShadowBlurStyle.OUTER,
        ),
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
                    ],
                    
                ),
                
                
                
            ]
        ),
        bgcolor="brown",
        width=1370,
        height=250,
        border=ft.border.all(1,"brown"),
        padding=20,
        border_radius=ft.border_radius.only(bottom_left=15,bottom_right=15),
        shadow = ft.BoxShadow(
            blur_radius = 5,
            color = ft.colors.BLACK,
            blur_style = ft.ShadowBlurStyle.OUTER,
        ),
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
                ft.Text("BILL & PAYMENT",color="white",weight="bold")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=60,
        width=1370,
        border_radius=30,
        bgcolor="brown",
        border=ft.border.all(1,"brown")

    )

    PaymentMethod = ft.Dropdown(
        label="Payment method",
        width=200,
        options=[
            ft.dropdown.Option("Cash Payment"),
            ft.dropdown.Option("Online Banking"),
        
            
        ],
        color="white",
        bgcolor="white",
        border_color="white",
        
    )
    #Field's Form 
    SlotID = ft.TextField(label="Slot.ID",width=320,color="white",border_color="white")
    Date = ft.TextField(label="Date",width=100,color="white",border_color="white")
    Month = ft.TextField(label="Month",width=100,color="white",border_color="white")
    Year = ft.TextField(label="Year",width=100,color="white",border_color="white")
    Coupon = ft.TextField(label="Voucher",value=0,width=200,color="white",border_color="white")
    CashGiven = ft.TextField(label="Guest's Payment",width=320,color="white",border_color="white")
    Change = ft.TextField(label="Change",width=200,color="white",border_color="white")
    BankID = ft.TextField(label="Banking's ID",value="1029713023",width=320,color="white",border_color="white")
    Bank = ft.TextField(label="Bank",width=200,value="Vietcombank",color="white",border_color="white")

    #Button's layout
    SubmitBillbutton = ft.ElevatedButton("Submit",width=200,bgcolor="green",color="white",on_click=SetupBill)
    ClearBillbutton = ft.ElevatedButton("Clear",width=200,bgcolor="red",color="white",on_click=ClearBill)
    EditSaveBillbutton = ft.ElevatedButton("Edit & Save",width=200,bgcolor="blue",color="white",on_click = UpdateBill)
    SaveBillbutton = ft.ElevatedButton("Save Form",width=300,bgcolor="orange",color="white",on_click=SaveBill)


    #CUSTOM BILL RELEASE
    SlotIDrelease = ft.Text("Slot.ID: ",size=20,color="white")
    paymentmethodrelease = ft.Text("Payment method: ",size=20,color="white")
    Cashgivenrelease = ft.Text("Guest payment: ",size=20,color="white")
    changerelease = ft.Text("Change: ",size=20,color="white")
    Couponrelease = ft.Text("Voucher: ",size=20,color="white")
    

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
        border=ft.border.all(1,"brown"),
        padding=20,
        border_radius=20,
        bgcolor="brown"
       
    )

    #Bill Payment
    Bill_list = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Table Slot",size=20,color="white")),
            ft.DataColumn(ft.Text("Description",size=20,color="white")),
            ft.DataColumn(ft.Text("Quantity",size=20,color="white")),
            ft.DataColumn(ft.Text("Price",size=20,color="white"))

        ],
        rows=[],
        
    )
    #Custom Bill

    Bill_title = ft.Container(
        ft.Row(
            [
                ft.Text("Bill Transfer information",color="white",weight="bold")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        width=1370,
        height=50,
        border=ft.border.all(1,"brown"),
        bgcolor="brown"
        
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
                                ft.Text("Total: ",size=20,color="white"),
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
        border=ft.border.all(1,"brown"),
        margin=ft.margin.only(bottom=10),
        padding=20,
        bgcolor="brown"
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
        border=ft.border.all(1,"brown"),
        margin=ft.margin.only(bottom=10),
        padding=50,
        bgcolor="brown"
    )


    PromotionBanner = ft.Container(
        ft.Row(
            controls=[
                ft.Text('Our Promotion',size=30,color="black",weight="bold"),
            ],
            width=2000,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        height=100,
        width=1350,
        

        padding=ft.padding.only(right=50),
        border_radius=20
    )


    PromotionImage = ft.Container(
        image_src="images/capuchino.png",
        width=350,
        height=350,
    )

    PromotionBar = ft.Container(

        ft.Row(
            [
                PromotionImage,
                ft.Container(
            
                    ft.Column(
                        [
                            ft.Text("Today offer",weight="bold",size=50,color="black"),
                            ft.Text("Buy 2 products and rate us to recieve our voucher",size=20,color="black"),
                            ft.Text("Follow our page to see more information about us",size=20,color="black")
                        ]
                    ),
                    margin=ft.margin.only(left=50,top=50,bottom=100)
                        
                    
                ),
            ]
        ),
        
        width=1350,
        height=300,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                "brown",
                "white"
            ]
        ),
        padding=ft.padding.only(left=100),
        border_radius=40
    )


    #----------------------------------------------------------------------------------

    #PAGE SET UP
    #----------------------------------------------------------------------------------
    #Menu

    page_1 = ft.Column(
        controls=[ 
            Banner_title,
            ft.Container(
                ft.Row(
                    [
                        SearchTool,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                margin=ft.margin.only(top=20)
                
            ),
            ft.Row(
                [
                    Coffee_banner,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    List_product
                    
                ],
                scroll= ft.ScrollMode.ALWAYS,
                height=400
            ),
            
            ft.Row(
                [
                    Dessert_banner,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                controls=[
                    List_product_2
                ],
                scroll= ft.ScrollMode.ALWAYS,
                height=400
            ),
            ft.Row(
                [
                    PromotionBanner,
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    PromotionBar
                ],
                alignment=ft.MainAxisAlignment.CENTER
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
    page_4 = ft.Column(
        controls=[
            CustomLayut
        ]
    )
    #----------------------------------------------------------------------------------
    #PAGE STACK LIST 
    #Set up Page stack for route change
    page_stack = [
        ft.Container(page_1,visible=True,bgcolor="#F5DEB3",height=1000,width=2000),
        ft.Container(page_2,visible=False),
        ft.Container(page_3,visible=False),
        ft.Container(page_4,visible=False)
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
                        
                        ft.Row(
                            [
                                ft.Container(
                                    Menu,
                                    width=100,
                                    height=1000,
                                    padding=-20,
                                    margin=ft.margin.only(right=20)
                                ),
                                ft.Column(page_stack,scroll=ft.ScrollMode.ALWAYS, expand=True)
                            ],
                            expand=True
                        ),
                    ],
                    bgcolor="#F5DEB3"
                )
            )
        
        
        page.update()

    def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)




    
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.bgcolor = ft.colors.BLUE
    page.padding = 0
   


    
    
    page.update()
if __name__ == "__main__":

    ft.app(target=main,assets_dir='assets')