init python:
    gallery = Gallery()

    gallery.button("CG2") 
    gallery.unlock_image("cg2")
    gallery.unlock_image("cg2") 

    gallery.button("TACKLE") 
    gallery.unlock_image("tacklecg")
    gallery.unlock_image("tacklecg") 

    gallery.button("TIEDUP") 
    gallery.unlock_image("tiedupcg")
    gallery.unlock_image("tiedupcg") 

    gallery.button("ED1") 
    gallery.unlock_image("ed1cg2")
    gallery.unlock_image("ed1cg2") 

    gallery.button("ED2") 
    gallery.unlock_image("ed2cg")
    gallery.unlock_image("ed2cg") 

    gallery.button("ED3") 
    gallery.unlock_image("ed3cg")
    gallery.unlock_image("ed3cg") 
    
    gallery.button("COMPLETE") 
    gallery.unlock_image("completecg")
    gallery.unlock_image("completecg") 
    

screen album:
    tag menu
    add "images/CustomUI/bg gallery.png"
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        grid 3 3:
            add gallery.make_button(name="CG2",unlocked="CGs/small/cg2small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="TACKLE",unlocked="CGs/small/tacklecgsmall.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="TIEDUP",unlocked="CGs/small/tiedupcgsmall.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="ED1",unlocked="CGs/small/ed1cg2small.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="ED2",unlocked="CGs/small/ed2cgsmall.png",locked="CGs/small/locked.png") 
            add gallery.make_button(name="ED3",unlocked="CGs/small/ed3cgsmall.png",locked="CGs/small/locked.png")  
            add gallery.make_button(name="COMPLETE",unlocked="CGs/small/completecgsmall.png",locked="CGs/small/locked.png")
            spacing 30
        textbutton "Return" action Return()