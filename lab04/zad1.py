import math

def forwardPass(wiek, waga, wzrost):
    hidden1 = wiek*-0.46122 + waga*0.97314 + wzrost*-0.39203 + 0.80109
    hidden1_po_aktywacji = funkcja_aktywacji(hidden1)

    hidden2 = wiek*0.78548 + waga*2.10584 + wzrost*-0.57847 + 0.43529
    hidden2_po_aktywacji = funkcja_aktywacji(hidden2)

    output = hidden1_po_aktywacji*-0.81546 + hidden2_po_aktywacji*1.03775 + -0.2368
    return output

def funkcja_aktywacji(x):
    return 1 / (1 + math.exp(-x))

rekord_1 = forwardPass(23, 75, 176) #TRUE
print(f"Rekord 1: {rekord_1}") #0.7985341880063129 TRUE

rekord_2 = forwardPass(25, 67, 180) #TRUE
print(f"Rekord 2: {rekord_2}") #0.8009499165011525 TRUE

rekord_3 = forwardPass(28, 120, 175) #FALSE
print(f"Rekord 3: {rekord_3}") #-0.0145099999999998 FALSE

rekord_4 = forwardPass(22, 65, 165) #TRUE
print(f"Rekord 4: {rekord_4}") #0.8009329715279782 TRUE

rekord_5 = forwardPass(46, 70, 187) #TRUE
print(f"Rekord 5: {rekord_5}") #0.8009499999938147 TRUE

rekord_6 = forwardPass(50, 68, 180) #FALSE
print(f"Rekord 6: {rekord_6}") #0.8009499999978288 TRUE

rekord_7 = forwardPass(48, 97, 178) #FALSE
print(f"Rekord 7: {rekord_7}") #0.01518239867249338 FALSE