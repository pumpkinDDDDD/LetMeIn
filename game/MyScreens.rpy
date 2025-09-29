#LETMEIN
label myscreens:

screen mapscreen1:
    add "bedroomnight.png"

    #Bed
    if not visited_bbed:
        imagebutton:
            xpos 556
            ypos 408
            idle "bedroombed_idle.png"
            hover "bedroombed (1).png"
            action [ SetVariable("visited_bbed", True), Jump("bbed") ]
    else:
        add "bedroombed_idle.png" xpos 556 ypos 408

    #Wardrobe
    if not visited_bwardrobe:
        imagebutton:
            xpos 282
            ypos 162
            idle "bedroomwardrobe_idle.png"
            hover "bedroomwardrobe (1).png"
            action [ SetVariable("visited_bwardrobe", True), Jump("bwardrobe") ]
    else:
        add "bedroomwardrobe_idle.png" xpos 282 ypos 162

    #Chest
    if not visited_bchest:
        imagebutton:
            xpos 7
            ypos 561
            idle "bedroomchest_idle.png"
            hover "bedroomchest (1).png"
            action [ SetVariable("visited_bchest", True), Jump("bchest") ]
    else:
        add "bedroomchest_idle.png" xpos 7 ypos 561

    #Carpet
    if not visited_bcarpet:
        imagebutton:
            xpos 102
            ypos 754
            idle "bedroomcarpet_idle.png"
            hover "bedroomcarpet (1).png"
            action [ SetVariable("visited_bcarpet", True), Jump("bcarpet") ]
    else:
        add "bedroomcarpet_idle.png" xpos 102 ypos 754

    #Wall
    if not visited_bwall:
        imagebutton:
            xpos 1507
            ypos 230
            idle "bedroomwall_idle.png"
            hover "bedroomwall (1).png"
            action [ SetVariable("visited_bwall", True), Jump("bwall") ]
    else:
        add "bedroomwall_idle.png" xpos 1507 ypos 230

    #Window
    if not visited_bwindow:
        imagebutton:
            xpos 657
            ypos 162
            idle "bedroomwindow_idle.png"
            hover "bedroomwindow (1).png"
            action [ SetVariable("visited_bwindow", True), Jump("bwindow") ]
    else:
        add "bedroomwindow_idle.png" xpos 657 ypos 162

    if visited_bbed and visited_bwardrobe and visited_bchest and visited_bcarpet and visited_bwall and visited_bwindow:
        timer 0.1 action Jump("bend1")




screen mapscreen2:
    add "kitchen.png"

    #SHelf 
    if not visited_kshelf:
        imagebutton:
            xpos 1
            ypos 10
            idle "kitchenshelf_idle.png"
            hover "kitchenshelf (1).png"
            action [ SetVariable("visited_kshelf", True), Jump("kshelf") ]
    else:
        add "kitchenshelf_idle.png" xpos 1 ypos 10

    #Table
    if not visited_ktable:
        imagebutton:
            xpos 427
            ypos 578
            idle "kitchentable_idle.png"
            hover "kitchentable (1).png"
            action [ SetVariable("visited_ktable", True), Jump("ktable") ]
    else:
        add "kitchentable_idle.png" xpos 427 ypos 578

    #Cupboard
    if not visited_kcupboard:
        imagebutton:
            xpos 825
            ypos 155
            idle "kitchencupboard_idle.png"
            hover "kitchencupboard (1).png"
            action [ SetVariable("visited_kcupboard", True), Jump("kcupboard") ]
    else:
        add "kitchencupboard_idle.png" xpos 825 ypos 155

    #Basket
    if not visited_kbasket:
        imagebutton:
            xpos 1567
            ypos 514
            idle "kitchenbasket_idle.png"
            hover "kitchenbasket (1).png"
            action [ SetVariable("visited_kbasket", True), Jump("kbasket") ]
    else:
        add "kitchenbasket_idle.png" xpos 1567 ypos 514

    if visited_kshelf and visited_ktable and visited_kcupboard and visited_kbasket:
        timer 0.1 action Jump("bend2")

screen mapscreen3:
    add "attic.png"

    #Wardrobe
    if not visited_awardrobe:
        imagebutton:
            xpos -1
            ypos 120
            idle "atticwardrobe_idle.png"
            hover "atticwardrobe (1).png"
            action [ SetVariable("visited_awardrobe", True), Jump("awardrobe") ]
    else:
        add "atticwardrobe_idle.png" xpos -1 ypos 120

    #Chest
    if not visited_achest:
        imagebutton:
            xpos 562
            ypos 595
            idle "atticchest_idle.png"
            hover "atticchest (1).png"
            action [ SetVariable("visited_achest", True), Jump("achest") ]
    else:
        add "atticchest_idle.png" xpos 562 ypos 595

    #Window
    if not visited_awindow:
        imagebutton:
            xpos 713
            ypos 264
            idle "atticwindow_idle.png"
            hover "atticwindow (1).png"
            action [ SetVariable("visited_awindow", True), Jump("awindow") ]
    else:
        add "atticwindow_idle.png" xpos 713 ypos 264

    #Trapdoor
    if not visited_atrap:
        imagebutton:
            xpos 666
            ypos 851
            idle "attictrapdoor_idle.png"
            hover "attictrapdoor (1).png"
            action [ SetVariable("visited_atrap", True), Jump("atrap") ]
    else:
        add "attictrapdoor_idle.png" xpos 666 ypos 851

    #Curtain
    if not visited_acurtain:
        imagebutton:
            xpos 1170
            ypos 12
            idle "atticcurtain_idle.png"
            hover "atticcurtain (1).png"
            action [ SetVariable("visited_acurtain", True), Jump("acurtain") ]
    else:
        add "atticcurtain_idle.png" xpos 1170 ypos 12

    if visited_awardrobe and visited_achest and visited_awindow and visited_atrap and visited_acurtain:
        timer 0.1 action Jump("bend3")
