import flet as ft
import base64
import mysql.connector
from flet import View

db = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Minh_17102004',
    database = 'Mellia'
)
cursoritem = db.cursor()

def main(page: ft.Page):
    def Authentication(e):
        Authenticated = "SELECT username,password FROM mellia_user WHERE id = 1"
        try:
            cursoritem.execute(Authenticated)
            for obj in cursoritem:
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
            cursoritem.execute(logs)
            for log_obj in cursoritem:
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
    
    def Click(e):
        print("ok")
        page.update()
    AddIconButton = ft.IconButton(icon=ft.icons.ARROW_RIGHT,bgcolor="#e1f6f4",icon_color="pink",on_click=Click,icon_size=70)
    Textbtn = ft.TextButton("View",on_click=Click)
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


    file_picked = ft.FilePicker(on_result=Handle_loaded_file)
    page.overlay.append(file_picked)



    


        


    CategoriesSelection = ft.Dropdown(
        label="Categories",
        width=210,
        options=[
            ft.dropdown.Option("Drink & Coffee"),
            ft.dropdown.Option("Desserts & Sidedishes")
        ]
    )

    
    TitleIMG = ft.TextField(label="Name",width=210,border_color="black",color="white")
    SetPrice = ft.TextField(label="Price",width=210,border_color="black",color="white")
    ContentProduct = ft.TextField(label="Comment",width=210,border_color="black",color="white")
    IDproduct = ft.TextField(label="ID",width=210,border_color="black",color="white")


    TitleProduct = ft.Text(size=40,weight=ft.FontWeight.BOLD,color="white")
    PriceProduct = ft.Text(value=str(SetPrice.value),size=40,color="white")
    NoteProduct = ft.Text(size=15)
    
    

    def Converted(e):
        SaveItems = "INSERT INTO productsb (id, name, price, content, image) VALUES (%s, %s, %s, %s, %s)"
        Items = (int(IDproduct.value),str(TitleIMG.value),int(SetPrice.value),str(ContentProduct.value),TestImgcontainer.image_src)
        PriceProduct.value = SetPrice.value+" $"
        TitleProduct.value = TitleIMG.value
        NoteProduct.value = ContentProduct.value

        try:
            cursoritem.execute(SaveItems,Items)
            print("Saved")
        except Exception as error:
            print(error)
        db.commit()


        List_product.controls.append(Layout_IMG_1)
        page.update()
    def ListItems(e):
        ViewAll = """ SELECT name,price,content,image
                FROM productsb"""
        cursoritem.execute(ViewAll)
        for obj in cursoritem.fetchall():
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
                                    bgcolor="white",
                                    width=450,
                                    height=350,
                                    padding=100,
                                    border_radius=ft.border_radius.only(top_left=15,top_right=15),
                                ),
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    ft.Column(
                                                        [
                                                            ft.Text(value=obj_name,size=40,weight=ft.FontWeight.BOLD,color="white"),
                                                            ft.Text(value=obj_note,size=15,color="white"),
                                                            ft.Text(value=obj_price,size=40,color="white"),
                                                        ],
                                                        width=300
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
                        width=450,
                        height=540,
                        padding=ft.padding.only(bottom=100),
                        bgcolor="pink",
                        margin=ft.margin.only(left=100,top=100),
                        border_radius=20,
                    )
            )
            db.commit()
        page.update()



    IMGupload = ft.IconButton(icon=ft.icons.UPLOAD,icon_color="black",bgcolor="white",on_click= lambda _:file_picked.pick_files(
                                    allow_multiple=False, allowed_extensions=['png']),icon_size=20)
    IMGdiscilne = ft.IconButton(icon=ft.icons.CANCEL,icon_color="black",bgcolor="white",on_click=ImageDiscline,icon_size=20)
    
    TestUpload = ft.ElevatedButton("Test",width=150,
                                   on_click= lambda _:file_picked.pick_files(
                                       allow_multiple=False, allowed_extensions=['png']
                                   )
                                )

    SaveButton = ft.ElevatedButton("Save",color="white",bgcolor="Blue",width=100,on_click=Converted)


    IMGScale = ft.Container(
        image_src=None,
        bgcolor="white",
        width=250,
        height=270,
        border_radius=15,
        border=ft.border.all(1, "black")
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
                                SaveButton
                                # TestUpload
                            ],
                            width=250,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                   ]
               ),
               
               ft.Column(
                   [
                       IDproduct,
                       TitleIMG,
                       ContentProduct,
                       SetPrice,
                       CategoriesSelection,
                       
                   ]
               )
            ]
        ),
        height=450,
        width=700,
        bgcolor="pink",
        border_radius=ft.border_radius.only(top_left=30,top_right=30,bottom_left=30,bottom_right=30),
        padding=ft.padding.only(left=100,top=50),
        margin=100,
        blur=ft.Blur(10,12,ft.BlurTileMode.MIRROR)
    )


    #CREATE PRODUCT LAYOUT 
    AddIconButton = ft.IconButton(icon=ft.icons.ARROW_RIGHT,bgcolor="#e1f6f4",icon_color="pink",on_click=Click,icon_size=70)
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
                            width=300
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
        bgcolor="white",
        width=450,
        height=350,
        padding=100,
        border_radius=ft.border_radius.only(top_left=15,top_right=15),
    )
    Layout_IMG_1 = ft.Container(
        
        ft.Column(
            [
                TestImgcontainer,
                ButtonLayout
            ]
        ),

        width=450,
        height=540,
        padding=ft.padding.only(bottom=100),
        bgcolor="pink",
        margin=ft.margin.only(left=100,top=100),
        border_radius=20,
        
    )
    

    List_product = ft.Row(
        [
            
            
        ],
        scroll=ft.ScrollMode.ALWAYS
    )
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
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        CustomLayut,
                                    ]
                                ),
                                ft.Row(
                                    [
                                        List_product
                                    ],
                                    scroll=ft.ScrollMode.ALWAYS
                                )
                            ],
                            scroll=ft.ScrollMode.ALWAYS
                        )
                    ],
                    scroll=ft.ScrollMode.ALWAYS
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
    
    page.padding = 0



    page.update()
if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')