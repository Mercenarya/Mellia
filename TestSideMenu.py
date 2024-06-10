import flet as ft
import base64
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    username = 'root',
    password = 'Minh_17102004',
    database = 'Mellia'
)
cursoritem = db.cursor()

def main(page: ft.Page):
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
        SaveItems = "INSERT INTO producttb (id, name, price, content, image) VALUES (%s, %s, %s, %s, %s)"
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
                FROM producttb"""
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
        


    page.add(
        ft.Row(
            [
                CustomLayut,
                ft.ElevatedButton("show",on_click=ListItems),
                
            ],
            scroll=ft.ScrollMode.ALWAYS
        ),
        ft.Row(
            [
                List_product
            ],
            scroll=ft.ScrollMode.ALWAYS
        )
    )
    page.scroll = ft.ScrollMode.ALWAYS
    page.update()
if __name__ == "__main__":
    ft.app(target=main,assets_dir='assets')