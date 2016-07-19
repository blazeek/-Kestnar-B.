 -*- coding: utf-8 -*-

print ("Dobrodošli v igri NAJDI SKRITO ŠTEVILO,na voljo imate 1 poiskus, da odkrijete skrito šetvilo, ki je večje od 0 in manjše od 100")

secrect = "30"
guess = raw_input("Vpišite Vaše število:")

if guess == secrect :
    print ("Čestitke, vase število se ujema s skritim!")
    print ( "Prislužili ste si 150$ ki jih lahko prevzamete pri vhodu, priporočamo pa Vam se kaksno igro saj danes zares blestite")

else:
    print ("Več sreče prihodnjič, morda Vam je sreča naklonjena na sosednjem igralnem avtomatu.")
