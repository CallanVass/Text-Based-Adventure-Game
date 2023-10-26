# IMPORTED MODULES
from classes import *
import time
from functions import *
from colour_text import ColourText

# INTRODUCTION
draculas_castle()
time.sleep(2)
intro()
# MAIN LOOP
while True:
# CELL LOGIC
    display_stats()
    options(cell_prompt_list_1_1, cell)
    user_input = input(">>> ")
    can_write(user_input)
    # Option 1
    while user_input == "1":
        if main_character.bloodglut < 20:
            print("You walk over to the pile of bones.")
            time.sleep(0.3)
            print("Poor chap, you think. Lazily, your eyes drift over to the cell door, then back to the bones.")
            time.sleep(0.3)
            print("Hmmm... If only you were stronger...")
            break
        elif main_character.bloodglut >= 20:
            print("You examine the pile of bones")
            options(cell_prompt_list_1_2, cell)
            user_input_1_2 = input(">>> ")
            can_write(user_input_1_2)
            while user_input_1_2 == "1":
                if main_character.inv.has_item("Bone Key"):
                    print("You've already done this.")
                    time.sleep(1)
                    break
                else:
                    print("It takes some doing, but you manage to snap it in half.")
                    main_character.inv.add_item("Bone Key")
                    time.sleep(2)
                    break
            while user_input_1_2 == "2":
                if main_character.inv.has_item("Bone Pen"):
                    print("You've already done that.")
                    time.sleep(1)
                    break
                else:
                    print("Time drags on, but eventually you make a pen for... writing.")
                    time.sleep(0.3)
                    print("HINT: Type 'Write' into the terminal to carve text into your arm.")
                    time.sleep(0.3)
                    main_character.inv.add_item("Bone Pen")
                    break
            if user_input_1_2 == "3":
                print("You go back.")
                time.sleep(0.5)
                break
    # Option 2
    while user_input == "2":
        print("You check the basin. The blood is as much mud as it is blood. You revolt.")
        options(cell_prompt_list_2_1, cell)
        user_input_2_1 = input(">>> ")
        can_write(cell_prompt_list_2_1)
        while user_input_2_1 == "1":
            if main_character.bloodglut >= 20:
                print("You've already done this.")
                time.sleep(2)
                break
            else:
                main_character.add_blood_glut(20)
                break
        while user_input_2_1 == "2":
            print("You kneel down and look under the sink to see someone has engraved some text.")
            time.sleep(0.3)
            print(ct.convert("<>yellow 'Something always yearns. Don't ever accept this hell.'<>"))
            break
        while user_input_2_1 == "3":
            self_bludgeon_ending()
        if user_input_2_1 == "4":
            break
    # Option 3
    while user_input == "3":
        print("'Help me', calls one prisoner. 'Please', calls another. They're Dracula's play things.")
        time.sleep(0.3)
        print("Treated like nothing but chaffe. Your will cements. You must escape.")
        break
    # Option 4
    while user_input == "4":
        print("You reach your arms up, looking closely at the bite marks made by Dracula. You think of")
        time.sleep(0.3)
        print("the countless times you've been fed on and you seethe...")
        break
    # Option 5
    while user_input == "5":
        exit_cell_room = False
        if cell_door_open:
            print("You step through the opened cell door.")
            time.sleep(1)
        elif main_character.inv.has_item("Bone Key"):
            cell_door_open = True
            print("You jam the bone key into the cell door keyhole, breaking it but snapping the lock open at ")
            time.sleep(0.3)
            print("the same time. The door slides wide open and you step through into a hallway.")
            time.sleep(0.3)
            main_character.inv.remove_item("Bone Key")
            time.sleep(0.3)
            print("The prisoners moan and wail at you to let them out. To the left of you is a door labelled ")
            time.sleep(0.3)
            print("'Treasury'. You can hear coins clinking behind it, but no speaking.")
            time.sleep(0.3)
            print("To your right is a door named 'Armoury'. Behind it, Dracula's guards laugh and joust.")
            time.sleep(0.3)
            print("Before you is a wide, closed door that appears to lead outside. Something is carved into it.")
            cell_door_opened_once = True
        else:
            if cell_door_opened_once:
                print("You step through the cell door without needing a key.")
                time.sleep(2)
            else:
                print("It's not particularly well built. If only we had some way to open it...")
                time.sleep(2)
            break
        # CELL ROOM/JAIL LOGIC
        while cell_door_open and not exit_cell_room:
            display_stats()
            if armoury_entered is False:
                options(cell_room_prompt_list_1_1, jail)
            else:
                options(cell_room_prompt_list_1_2, jail)
            cell_room_user_input = input(">>> ")
            can_write(cell_room_user_input)
            # Option 1
            while cell_room_user_input == "1":
                if tresury_entered is False:
                    tresury_entered = True
                    print("Silently, you enter a well lit room with piles upon piles of golden coins strewn about the place.")
                    time.sleep(0.3)
                    print("A blind servant sits at a rickety table, counting coins and placing them into bags.")
                    display_stats()
                    options(treasury_prompt_list_1_1, treasury)
                    treasury_room_user_input = input(">>> ")
                    can_write(treasury_room_user_input)
                else:
                    print("You're standing in the Treasury.")
                    display_stats()
                    options(treasury_prompt_list_1_1, treasury)
                    treasury_room_user_input = input(">>> ")
                    can_write(treasury_room_user_input)
                while treasury_room_user_input == "1":
                    if servant_killed is False and servant_unconscious is False:
                        print("You sieze the servant, ripping into his neck and drinking deeply. With nobody to stop you,")
                        time.sleep(0.3)
                        print("you're able to drink your fill.")
                        time.sleep(0.3)
                        main_character.add_blood_glut(30)
                        servant_killed = True
                        break
                    elif servant_unconscious is True:
                        print("A change of heart, eh?")
                        time.sleep(0.3)
                        print("You pick the man up off the floor and tear into his neck. With nobody to stop you,")
                        time.sleep(0.3)
                        print("you're able to drink your fill.")
                        time.sleep(0.3)
                        main_character.add_blood_glut(30)
                        servant_killed = True
                        break
                    else:
                        print("He can't get any dead-er than he is.")
                        time.sleep(2)
                        break
                # Option 2
                while treasury_room_user_input == "2":
                    print("You examine the gold coins.")
                    display_stats()
                    options(treasury_prompt_list_1_2, treasury)
                    treasury_room_user_input_1 = input(">>> ")
                    can_write(treasury_room_user_input_1)
                    while treasury_room_user_input_1 == "1":
                        print("Your teeth sink straight through the metal. Yep, that's real gold alright.")
                        break
                    while treasury_room_user_input_1 == "2":
                        if main_character.inv.has_item("Gold Key"):
                            print("You've already done that.")
                            time.sleep(2)
                            break
                        else:
                            print("You grab a couple gold coins and get to work, compressing them like clay and fashioning yourself a key.")
                            time.sleep(0.3)
                            main_character.inv.add_item("Gold Key")
                            break
                    if treasury_room_user_input_1 == "3":
                        break
                # Option 3
                while treasury_room_user_input == "3":
                    if servant_unconscious is False and servant_killed is False:
                        print("With a hard backhand, you clop the servant over the head. He falls to the ground,")
                        time.sleep(0.3)
                        print("moaning for a moment before going still. His wheezing breaths fill the chamber. How annoying.")
                        servant_unconscious = True
                        break
                    elif servant_killed is True:
                        print("You've just killed the man. Doesn't get much more 'unconscious' than that, does it?")
                        time.sleep(2.5)
                        break
                    else:
                        print("He's already unconscious. Give the man a break.")
                        time.sleep(2)
                        break
                # Option 4
                while treasury_room_user_input == "4":
                    # TRESURY LOGIC
                    if servant_unconscious is False and servant_killed is False:
                        print("You can't do that yet, you'll be heard!")
                        time.sleep(2)
                        break
                    else:
                        print("You approach the door, which is mostly-obscured by piles of coins.")
                        display_stats()
                        if tunnel_door_opened:
                            options(treasury_prompt_list_1_3_1, treasury)
                        else:
                            options(treasury_prompt_list_1_3, treasury)
                        treasury_room_user_input_2 = input(">>> ")
                        can_write(treasury_room_user_input_2)
                        # Option 1
                        while treasury_room_user_input_2 == "1":
                            if dig_counter >= 3:
                                tunnel_door_opened = True
                                print("You stand before a dark tunnel with a yellow glowing light at the end of it.")
                                display_stats()
                                options(tunnel_prompt_list_1, tunnel)
                                treasury_room_user_input_3 = input(">>> ")
                                can_write(treasury_room_user_input_3)
                                while treasury_room_user_input_3 == "1":
                                    if tunnel_travelled_down is False:
                                        print(ct.convert("You venture down the tunnel, closing the distance between you and the <>yellow yellow<> light."))
                                        time.sleep(0.3)
                                        print("As you near, you realise it's not a light, but two lights. You go to turn back, but ")
                                        time.sleep(0.3)
                                        print("a voice calls to you, telling you to come closer. You take the chance, and soon find ")
                                        time.sleep(0.3)
                                        print("yourself standing before a shadowy figure with two monstrous eyes. The figure hovers ")
                                        time.sleep(0.3)
                                        print("before a tunnel.")
                                        tunnel_travelled_down = True
                                    display_stats()
                                    if asked_riddle is False:
                                        options(tunnel_prompt_list_2, tunnel)
                                    else:
                                        options(tunnel_prompt_list_2_1, tunnel)
                                    tunnel_user_input_2 = input(">>> ")
                                    can_write(tunnel_user_input_2)
                                    while tunnel_user_input_2 == "1":
                                        if bowed_before_ominous_spirit is False:
                                            print("'What is this? Get up. Bow again and rip you to shreds,' he says.")
                                            time.sleep(0.3)
                                            print("How pleasant.")
                                            bowed_before_ominous_spirit = True
                                            break
                                        else:
                                            print("'What, you thought I was joking?'")
                                            time.sleep(0.3)
                                            print("The Ominous Spirit lashes out.")
                                            main_character.lose_health(40)
                                            check_character_health()
                                            break
                                    while tunnel_user_input_2 == "2":
                                        if main_character.bloodglut >= 50:
                                            print("'Look at you - all gorged on blood. And now you want my help? I don't think so.'")
                                            break
                                        if asked_riddle is False:
                                            print("'Hmm, interesting proposition,' says the Ominous Spirit. 'I'll tell you what - ")
                                            time.sleep(0.3)
                                            print("if you can answer my riddle, I'll let you go. Here it is: ")
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow 'I'm the timeless enigma, lurking somwhere between future and past.<>"))
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow To me, a sharpened pencil is closer than an unsharpened one.<>"))
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow I was before, and I will be again.'<>"))
                                            time.sleep(0.3)
                                            print("What am I?'")
                                            asked_riddle = True
                                        else:
                                            print("'Back to make another guess? Come on then, let's hear it.'")
                                            time.sleep(0.3)
                                            print("'Here's the riddle again, in case you've forgotten. You probably have:'")
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow 'I'm the timeless enigma, lurking somwhere between future and past.<>"))
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow To me, a sharpened pencil is closer than an unsharpened one.<>"))
                                            time.sleep(0.3)
                                            print(ct.convert("<>yellow I was before, and I will be again.'<>"))
                                            time.sleep(0.3)
                                            print("What am I?'")
                                            time.sleep(7)
                                        tunnel_user_input_3 = input(">>> ")
                                        can_write(tunnel_user_input_3)
                                        if tunnel_user_input_3 == "Death" or tunnel_user_input_3 == "death":
                                            ominous_spirit_riddle_ending()
                                        else:
                                            print("Ha. Nice try, but you'll have to try harder.")
                                            time.sleep(2)
                                            break
                                    while tunnel_user_input_2 == "3":
                                        if ominous_spirit_stare_counter > 19:
                                            ominous_spirit_stare_ending()
                                        elif ominous_spirit_stare_counter < 5:
                                            print("The Ominous Spirit stares straight back at you, piercing your very soul. Something ")
                                            time.sleep(0.3)
                                            print("inside you goes cold. You shiver.")
                                            time.sleep(2.5)
                                            ominous_spirit_stare_counter += 1
                                            break
                                        elif ominous_spirit_stare_counter >= 5 and ominous_spirit_stare_counter < 10:
                                            print("'What?' the Ominous Spirit asks. 'Why are you staring?'")
                                            time.sleep(0.3)
                                            print("You smile.")
                                            time.sleep(2.5)
                                            ominous_spirit_stare_counter += 1
                                            break
                                        elif ominous_spirit_stare_counter >= 10 and ominous_spirit_stare_counter < 15:
                                            print("The Spirit appears to be losing his composition. You keep smiling.")
                                            time.sleep(2.5)
                                            ominous_spirit_stare_counter += 1
                                            break
                                        elif ominous_spirit_stare_counter >= 15 and ominous_spirit_stare_counter <= 19:
                                            print("He begins to sweat. Your smile widens.")
                                            time.sleep(2.5)
                                            ominous_spirit_stare_counter += 1
                                            break
                                    if tunnel_user_input_2 == "4":
                                        break
                                if treasury_room_user_input_3 == "2":
                                    break
                            chance_of_success(2)
                            if tunnel_door_opened is False:
                                if chance_of_success(2) == "Your attempt fails!":
                                    dig_counter += 1
                                    print("A guard stumbles into the room, sword half unsheathed, drawn in by the tinkling of coins.")
                                    attacked_by_one_guard(1.5, treasury)
                                    treasury_guard_dead = True
                                else:
                                    print("You dig some of the coins away without being heard!")
                                    # print(dig_counter) TEST ONE
                                    time.sleep(2)
                                    dig_counter += 1
                                break
                            else:
                                break
                        # Option 2
                        if treasury_room_user_input_2 == "2":
                            print("It reads: 'No bloodbag is to enter here until I've dealt with its occupant.'")
                            time.sleep(0.3)
                            print("Signed: Dracula")
                        # Option 3
                        if treasury_room_user_input_2 == "3":
                            break
                        # Option 5
                if treasury_room_user_input == "5":
                    break
            # Option 2
            while cell_room_user_input == "2":
                if prisoners_free:
                    print("You've already done that.")
                    time.sleep(1)
                    break
                elif main_character.inv.has_item("Master Key"):
                    print("With Dracula's key, you free the prisoners!")
                    time.sleep(2)
                    prisoners_free = True
                    break
                elif main_character.inv.has_item("Bone Key"):
                    print("You're resourceful, aren't you?")
                    time.sleep(0.3)
                    print("You go back and forth, forging bone-shaped keys and smashing them into the locks one by one.")
                    time.sleep(0.3)
                    print("The prisoners have been freed! They huddle around the main door, too scared to do anything else.")
                    prisoners_free = True
                    break
                elif main_character.bloodglut < 50:
                    print("You try and bend the bars, but they won't give. If only you were stronger...")
                    time.sleep(2.5)
                    break
                elif prisoners_free is True:
                    print("They're already free.")
                    time.sleep(1.5)
                else:
                    print("Strength swells within you. With your newfound might, you snap the bars off their hinges. ")
                    time.sleep(0.3)
                    print("The prisoners have been freed!")
                    time.sleep(0.3)
                    prisoners_free = True
                    break
            # Option 3
            while cell_room_user_input == "3":
                # ARMOURY LOGIC
                if main_character.inv.has_item("Gold Key"):
                    if armoury_entered is False:
                        print("You open the Armoury door to find 3 guards, all with plate armour and weapons. They drop their drinks and draw their swords.")
                        display_stats()
                        options(armoury_prompt_list_1, armoury)
                        armoury_user_input_1 = input(">>> ")
                        can_write(armoury_user_input_1)
                        # Option 1
                        while armoury_user_input_1 == "1":
                            print("You lunge at the closest one, who raises his sword in defense. You dodge.")
                            time.sleep(1.5)
                            attacked_by_one_guard(1.4, armoury)
                            print("Done with the first one, the other two charge you.")
                            display_stats()
                            options(armoury_prompt_list_2, armoury)
                            armoury_user_input_2 = input(">>> ")
                            can_write(armoury_user_input_2)
                            if armoury_user_input_2 == "1":
                                print("You edge backwards, forcing them to face you one at a time.")
                                attacked_by_one_guard(1.4, armoury)
                                display_stats()
                                print("Done with the first, the other looks hesitant to approach you. You take the fight to him.")
                                time.sleep(1)
                                attacked_by_one_guard(1.7, armoury)
                                display_stats()
                                armoury_entered = True
                                break
                            elif armoury_user_input_2 == "2":
                                print("Blindly, you rush both of them and get attacked twice in a short period.")
                                attacked_by_one_guard(1, armoury)
                                attacked_by_one_guard(1, armoury)
                                armoury_entered = True
                                break

                    else:
                        print("You stand in the armoury, surveying the carnage you've caused.")
                        display_stats()
                        options(armoury_prompt_list_3, armoury)
                        armoury_user_input_3 = input(">>> ")
                        can_write(armoury_user_input_3)
                        # DRACULA'S CHAMBERS LOGIC
                        while armoury_user_input_3 == "1":
                            if dracula_chambers_entered is False:
                                print("With a looming silence, you press forwards, inching the doors to Dracula's chamber open.")
                                time.sleep(0.3)
                                print("It's daytime, so you expect a sleeping figure hanging from the ceiling. You've never")
                                time.sleep(0.3)
                                print("been more incorrect.")
                                time.sleep(0.3)
                                print("Resting on a velvet throne is Dracula in a full set of engraved metal armour. In the")
                                time.sleep(0.3)
                                print("engravings you see a million deaths. A million lifetimes spent drinking blood. Dracula smiles,")
                                time.sleep(0.3)
                                print("her spectacularly white teeth sparkling between her frame of golden hair. She stands from her")
                                time.sleep(0.3)
                                print("throne and descends a couple steps.")
                                time.sleep(0.3)
                                print(ct.convert("<>magenta 'I can only presume you're here to kill me,'<> she says, her smirk growing wider."))
                                display_stats()
                                dracula_chambers_entered = True
                            else:
                                display_stats()
                            if dracula_killed is True:
                                options(dracula_prompt_list_3, dracula_chambers)
                                dracula_chambers_user_input_5 = input(">>> ")
                                can_write(dracula_chambers_user_input_5)
                                if dracula_chambers_user_input_5 == "1":
                                    break
                            if servant_killed is True and guard_killed_counter >= 1:
                                options(dracula_prompt_list_1, dracula_chambers)
                            else:
                                options(dracula_prompt_list_2, dracula_chambers)
                            dracula_chambers_user_input_3 = input(">>> ")
                            can_write(dracula_chambers_user_input_3)
                            # Option 1
                            if dracula_chambers_user_input_3 == "1":
                                print(ct.convert("<>magenta 'Do I really?'<> she asks. <>magenta 'People kill animals all the time. What's the difference?<>"))
                                time.sleep(0.3)
                                print("'People aren't animals, and they aren't slaves either. They want to live,' you")
                                time.sleep(0.3)
                                print("remind her. Much good it will do.")
                                time.sleep(0.3)
                                print(ct.convert("Dracula's eyes take on a faint glow. <>magenta 'I've never seen an animal that wanted to die.<>"))
                                time.sleep(0.3)
                                print(ct.convert("<>magenta Yet here you are,'<> she whispers, breaking into a tinkling laugh so violent it rattles"))
                                time.sleep(0.3)
                                print("the plates of her armour.")
                            # Option 2
                            if dracula_chambers_user_input_3 == "2":
                                print(ct.convert("<>magenta 'It's never enough. Not really. I suspect you're beginning to realise this seeing<>"))
                                time.sleep(0.3)
                                print(ct.convert("<>magenta as how you're becoming exactly like me.'<>"))
                            # Option 3
                            if dracula_chambers_user_input_3 == "3":
                                print(ct.convert("<>magenta 'Yes, you do display the explicit level of corruption that I've come to demand of my servants.'<>"))
                                time.sleep(0.3)
                                print("'I'm not corrupt,' you point out.")
                                time.sleep(0.3)
                                print("Dracula snorts, her small pale nose facing the floor as she giggles. What an odd sound.")
                                time.sleep(0.3)
                                print(ct.convert("She leans in closer and whispers. <>magenta 'Corruption is a matter of perspective.'<>"))
                            # Option 4
                            while dracula_chambers_user_input_3 == "4":
                                print(ct.convert("<>magenta 'If you insist...'<>"))
                                time.sleep(1)
                                print(ct.convert("<>magenta 'Then so do I.'<>"))
                                dracula.check_dracula_stats()
                                time.sleep(1)
                                print("In a blinding flash, she strikes out with her claws.")
                                time.sleep(3)
                                fight_with_dracula(main_character, 0.8, 40)
                                dracula.check_dracula_stats()
                                display_stats()
                                print(ct.convert("She backs up, eyes glued to you as she circles. <>magenta 'You think that was quick?'<> she asks."))
                                time.sleep(0.3)
                                print(ct.convert("<>magenta 'Then try this.'<>"))
                                time.sleep(0.3)
                                print("A blinding attack comes for you.")
                                time.sleep(7)
                                fight_with_dracula(main_character, 0.5, 40)
                                dracula.check_dracula_stats()
                                display_stats()
                                print("She smiles and a spurt of blood jumps from her throat.")
                                time.sleep(0.3)
                                print(ct.convert("<>magenta 'You're quick. Not quick enough, though.'<>"))
                                time.sleep(5)
                                fight_with_dracula(main_character, 0.5, 40)
                                dracula.check_dracula_stats()
                                display_stats()
                                print("As she crashes into her throne, a serious gasp exits her mouth.")
                                time.sleep(0.3)
                                print("You press the advantage, leaping across the room and grabbing her by the throat")
                                time.sleep(0.3)
                                print("With all your might, you smash her into the cobbled floor, sending fractures in")
                                time.sleep(0.3)
                                print("every direction. ")
                                time.sleep(0.3)
                                print("Like stray lightning, Dracula reaches for you.")
                                time.sleep(10)
                                fight_with_dracula(main_character, 0.3, 40)
                                dracula.check_dracula_stats()
                                display_stats()
                                print("You raise your hand, ready to finish the monster once and for all.")
                                time.sleep(0.3)
                                print(ct.convert("<>magenta 'Wait!'<> she shouts."))
                                time.sleep(0.3)
                                print(ct.convert("You pause. <>magenta 'You don't understand this,'<> she sputters. <>magenta 'If you kill me,<>"))
                                time.sleep(0.3)
                                print(ct.convert("<>magenta you'll never understand it. Spare me, and I'll show you things you've never<>"))
                                time.sleep(0.3)
                                print(ct.convert("<>magenta imagined. Worlds - completely seperate from this one.'<>"))
                                time.sleep(7)
                                dracula.check_dracula_stats()
                                display_stats()
                                options(dracula_prompt_list_2_1, dracula_chambers)
                                dracula_chambers_user_input_4 = input(">>> ")
                                can_write(dracula_chambers_user_input_4)
                                while dracula_chambers_user_input_4 == "1":
                                    print("'Sorry. Once a monster, always a monster.'")
                                    time.sleep(0.3)
                                    print("You bring a clawed hand down, severing her head from her shoulders.")
                                    time.sleep(0.3)
                                    dracula.dracula_health_loss(20)
                                    time.sleep(0.3)
                                    dracula.check_dracula_stats()
                                    print("Finally... she's dead. You stand up, still shaking from the fight.")
                                    time.sleep(5)
                                    main_character.inv.add_item("Master Key")
                                    time.sleep(2)
                                    dracula_killed = True
                                    break
                                if dracula_chambers_user_input_4 == "2":
                                    dracula_spared_ending()
                                break
                            if dracula_chambers_user_input_3 == "5":
                                if dracula_killed is False:
                                    print("There is no going back. One way or another, this ends now.")
                                    time.sleep(2)
                                else:
                                    break
                        # Option 2
                        if armoury_user_input_3 == "2":
                            print("With thoughts of facing Dracula armed, you reach for their weapons and armour,")
                            time.sleep(0.3)
                            print("only to find they're made of silver and hot to the touch.")
                            time.sleep(0.3)
                            main_character.lose_health(5)
                            time.sleep(0.3)
                            print("'Curse this affliction,' you murmur.")
                            time.sleep(0.3)
                            check_character_health()
                        # Option 3
                        if armoury_user_input_3 == "3":
                            break
                else:
                    print("It appears you need some sort of metal key to do that. Maybe you can make one?")
                    time.sleep(2.5)
                    break
            # Option 4
            while cell_room_user_input == "4":
                if main_character.inv.has_item("Master Key") and main_character.bloodglut <= 65:
                    main_door_ending_with_key()
                elif main_character.bloodglut < 65:
                    print("You need either the Master Key or the strength to brute force it.")
                    time.sleep(2.5)
                    break
                elif main_character.bloodglut > 99:
                    main_door_full_blood_glut_ending()
                elif main_character.bloodglut > 65 and main_character.bloodglut < 99:
                    main_door_ending_without_key()
            # Option 5
            while cell_room_user_input == "5":
                print("You step closer, reading the carving plainly with your improved vision.")
                time.sleep(0.3)
                print(ct.convert("<>yellow 'I'll tear spleens, defeat everything and this hell to get what I want.'<>"))
                break
            # Option 6
            if cell_room_user_input == "6":
                exit_cell_room = True
        if exit_cell_room:
            break
