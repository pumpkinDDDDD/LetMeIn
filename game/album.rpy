image CG2 = im.FactorScale("images/cg2.png", 0.25)
image TACKLE = im.FactorScale("images/tacklecg.png", 0.25)
image TIEDUP = im.FactorScale("images/tiedupcg.png", 0.25)
image ED1 = im.FactorScale("images/ed1cg2.png", 0.25)
image ED2 = im.FactorScale("images/ed2cg.png", 0.25)
image ED3 = im.FactorScale("images/ed3cg.png", 0.25)
image COMPLETE = im.FactorScale("images/completecg.png", 0.25)
image bglock_button = "images/locked.png"

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

    gallery.button("ENDING1") 
    gallery.unlock_image("ed1cg2")
    gallery.unlock_image("ed1cg2") 

    gallery.button("ENDING2") 
    gallery.unlock_image("ed2cg")
    gallery.unlock_image("ed2cg") 

    gallery.button("ENDING3") 
    gallery.unlock_image("ed3cg")
    gallery.unlock_image("ed3cg")

    gallery.button("COMPLETE") 
    gallery.unlock_image("completecg")
    gallery.unlock_image("completecg") 
    

screen album:
    tag menu
    add "images/game_menu.png"
    
    hbox:
        xalign 0.5
        yalign 0.5
        spacing 20
        grid 3 2:
            add gallery.make_button(name="CG2",unlocked="images/cg2.png",locked="images/locked.png") 
            add gallery.make_button(name="TACKLE",unlocked="images/tacklecg.png",locked="images/locked.png") 
            add gallery.make_button(name="TIEDUP",unlocked="images/tiedupcg.png",locked="images/locked.png") 
            add gallery.make_button(name="ED1",unlocked="images/ed1cg2.png",locked="images/locked.png") 
            add gallery.make_button(name="ED2",unlocked="images/ed2cg.png",locked="images/locked.png") 
            add gallery.make_button(name="ED3",unlocked= "images/ed3cg.png",locked="images/locked.png")  
            spacing 30
        textbutton "Return" action Return()