import pandas as pd
from airium import Airium

df_prof = pd.read_csv("test_gallery.csv", sep=";")
df_pic = pd.read_csv("test_activities.csv", sep=";")
a = Airium()

a('<!DOCTYPE html>')
with a.html(lang="en"):
    with a.head():
        a.meta(charset="UTF-8")
        a.meta(name="viewport", content="width=device-width, initial-scale=1.0")

        a.title(_t="Home")
        a.link(rel="stylesheet", href="style.css")
        a.link(rel="preconnect", href="https://fonts.googleapis.com")
        a.link(rel="preconnect", href="https://fonts.gstatic.com", tag_name="crossorigin")
        a.link(href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300;0,500;0,600;0,700;0,800;1,600&display=swap", rel="stylesheet")
    
    with a.body():
        #Header
        with a.div(klass="header"):

            with a.div(klass="hero"):
                #img
                a.img(src="images/sailboat.jpg", alt="")
                #title
                with a.div(klass="title"):
                    with a.h1():
                        a("Hello World")
                #caption
                with a.div(klass="caption"):
                    a("Lorem ipsum dolor sit amet consectetur adipisicing elit. Labore enim, quas nostrum beatae corrupti sit.")
            #navbar
            with a.div(klass="nav bottom-nav", id="navbar"):
                #home button
                with a.a(href="#", klass="nav-link"):
                    a("Beranda")
                #gallery button
                with a.a(href="anggota_kelas.html", klass="nav-link"):
                    a("Anggota Kelas")
                #activities button
                with a.a(href="galeri.html", klass="nav-link"):
                    a("Galeri")
        #Main content
        with a.div(klass="main-content"):
            #Profiles
            with a.div(klass="all-profiles"):
                #H1
                with a.h1():
                    a("Lorem Ipsum")
                #profiles
                with a.div(klass="profiles"):
                    for i in  range(3):
                        #profile
                        with a.div(klass="profile"):
                            #profile photo
                            with a.div(klass="photo", style="background: url('{}'); background-repeat: no-repeat;background-size: cover;".format(df_prof['foto diri'][i])):
                                pass
                            #profile title
                            with a.div(klass="title"):
                                with a.h2():
                                    a(str(df_prof['nama lengkap'][i]))
                            #caption
                            with a.div(klass="caption"):
                                with a.p():
                                    a(str(df_prof['kesan dan pesan'][i]))
                with a.div(klass="all-profiles-caption"):
                    with a.p():
                        a("Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit at distinctio culpa voluptate sequi itaque temporibus rem nemo deserunt atque totam quo sit, saepe omnis hic. Illo quod tenetur quia nam cupiditate cumque porro exercitationem laudantium incidunt, harum dolor magnam nemo. Sunt ab quae, assumenda dolorem magni maxime amet. Iusto!")
            #Pictures
            with a.div(klass="pictures"):
                #picture loop
                for i in range(3):
                    with a.div(klass="picture"):
                        #gambar di kiri jika genap
                        if i%2==0 or i==0:
                            #picture img
                            a.img(klass="img float-left", style="background: url('{}');background-repeat: no-repeat;background-size: cover;".format(df_pic['image link'][i]))
                            #picture title
                            with a.div(klass="title float-right"):
                                with a.h1():
                                    a(str(df_pic['title'][i]))
                            #picture caption
                            with a.div(klass="caption float-right"):
                                with a.p():
                                    a("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione, repellendus, voluptas sapiente vitae in quis aperiam necessitatibus autem nihil minima tempore officiis harum dolore soluta, nesciunt dolorem. Quidem architecto tempora a eos odit neque natus velit sint provident, nulla nihil!")
                        else:
                            #picture img
                            a.img(klass="img float-right", style="background: url('{}');background-repeat: no-repeat;background-size: cover;".format(df_pic['image link'][i]))
                            #picture title
                            with a.div(klass="title float-left"):
                                with a.h1():
                                    a(str(df_pic['title'][i]))
                            #picture caption
                            with a.div(klass="caption float-left"):
                                with a.p():
                                    a("Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ratione, repellendus, voluptas sapiente vitae in quis aperiam necessitatibus autem nihil minima tempore officiis harum dolore soluta, nesciunt dolorem. Quidem architecto tempora a eos odit neque natus velit sint provident, nulla nihil!")
        #Footer
        with a.div(klass="footer"):
            #members
            with a.div(klass="members"):
                #Members:
                with a.p():
                    a("Anggota Kelas:")
                #all members
                with a.div(klass="all-members"):
                    #4* '8members'
                    for i in range(4):
                        with a.div(klass="8members"):
                            #8* 'member'
                            for j in range(8):
                                with a.div(klass="member"):
                                    a("Lorem Ipsum")
            a.br()
            #line
            with a.div(klass="line"):pass
            a.br()
            #credit
            with a.div(klass="credit"):
                with a.pre():
                    a("Hubungi saya jika ingin melakukan perubahan:")
                    a.br()
                    a("fadlanerman6@gmail.com")
                    a.br()
                    a.br()
                    a("Link repository:")
                    a.br()
                with a.pre():
                    a("    ")
                    a("<a href=\"https://github.com/vFadlan011/album-22/\" target=\"_blank\"><ion-icon name=\"logo-github\"></ion-icon>Github</a>")
                    a.br()
            a.br()
        with a.script(src="script.js"):
            pass
        with a.script(type="module", src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"):
            pass
        with a.script(tag_name="nomodule", src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"):
            pass

# SAVE HTML
html_path = "index.html"
html = str(a)

with open(html_path, 'wb') as f:
    f.write(bytes(html, encoding='utf8'))