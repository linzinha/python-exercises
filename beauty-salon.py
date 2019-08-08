import random
import time

salonServices = ["shampoo", "cut", "color", "treatment", "style", "nails", "facial hair", "body hair", "facial treatments", "body treatments"]

nails = ["basic manicure", "gel manicure", "basic pedicure", "gel pedicure"]

facialHair = ["lip wax", "eyebrow wax", "full face wax", "shave", "facial hair trim", "facial hair conditioning treatment"]

bodyHair = ["bikini", "brazilian", "underarm", "shoulders", "stomach", "buttocks", "half legs", "full legs", "half arms", "full arms", "chest", "back", "stomach strip", "chest and stomach", "back and shoulders", "full body"]

facialTreatment = ["deep pore cleansing facial", "brightening facial", "clarity complexion treatment", "red carpet facial", "advanced hydrafacial", "rejuvenation treatment", "opulence treatment"]

facialTreatmentEnhancements = ["healing jade treatment"]

lightTherapies = ["micro photo treatment", "lhe photo rejuvenation", "lhe acne", "lhe lifting and tightening"]

peels = ["vi peel", "vi acne peel", "modified jessner peel", "cosmederm 50% glycolic peel"]

spaRituals = ["signature clarifying spa ritual", "organic euphoria spa ritual", "head to toe spa ritual", "transformational spa ritual"]

bodyCocktail = ["cucumber honey body cocktail", "mineral mud body cocktail", "warm lavender body cocktail", "organic moroccan earth body cocktail"]

saltSugarSctubs = ["exotic rose + jasmine", "the greek", "the Moroccan", "traditional sea salt scrub"]

massage = ["return to nature", "manly-sage", "four handed", "ultimate relax", "hot stone", "herbal heat", "craniosacral", "thai", "shiatsu", "swedish", ]

bodyTreatmentEnhancements = ["eco-hin heat therapy", "detoxifying foot soak", "reflexology", "hot stone enhancement"]

skinTypes = ["dry", "oily", "combination"]
skinConcerns = ["redness", "acne", "oiliness", "dryness", "wrinkles and fine lines", "uneven skin tone", "uneven texture"]

dayIncome = 0
tipPool = 0



# prices = [30, 25, 40, 20, 20, 35, 50, 35]
#
# last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#
# total_price = 0

# for price in prices:
#     total_price += price
# print(total_price)
#
# average_price = total_price / len(hairstyles)
# print("Average Haircut Price: $" + str(average_price))
#
# new_prices = [price - 5 for price in prices]
# print(new_prices)
#
# total_revenue = 0
#
# for i in range(len(hairstyles)):
#     total_revenue += prices[i] * last_week[i]
#
# print("Total Revenue: $" + str(total_revenue))
# average_daily_revenue = total_revenue / 7
# print(average_daily_revenue)
#
# cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
#
# print(cuts_under_30)

# sources: http://www.olehenriksenspa.com/services/
# https://www.bareskindetroit.com/facials
# https://www.csalons.com/services/
# https://globalwellnesssummit.com/wp-content/uploads/Industry-Research/Asia-Pacific/2014-colliers-international-uae-spa-market.pdf

firstFancyNames = {
    1: "Andre", 2: "Michael", 3: "Jermaine", 4: "Susan", 5: "Stacey", 6: "Dominique", 7: "Alejandro", 8: "Ali", 9: "Fatima", 10: "Camila"
}

lastFancyNames = {
    1: "Lauder", 2: "Beauregard", 3: "Beaudelaire", 4: "Astor", 5: "Urbinati", 6: "Canalé", 7: "Lecompte", 8: "Hatzis", 9: "Atelier", 10: "Galván"
}

firstNames = {
    1: "Tim", 2: "Michael", 3: "Jermaine", 4: "Susan", 5: "Stacey", 6: "Dominique", 7: "Alejandro", 8: "Ali", 9: "Fatima", 10: "Camila", 11: "Mohammed", 12: "Liam", 13: "Noah", 14: "Francesco", 15: "Jose", 16: "Maryam", 17: "Ximena", 18: "Emma", 19: "Eleni", 20: "Isabella"
}

lastNames = {
    1: "Smith", 2: "Wang", 3: "Johnson", 4: "Li", 5: "Garcia", 6: "Patel", 7: "Miller", 8: "Nguyen", 9: "Atelier", 10: "Galván", 11: "Lauder", 12: "Astor", 13: "Lecompte", 14: "Stevenson", 15: "Lauren", 16: "Jones", 17: "Brings", 18: "Sarra", 19: "Reda", 20: "Summ"
}

gender = {
    1: 'Mr.', 2: 'Mrs.', 3: 'Ms.', 4: 'Miss', 5: 'Mx.'
}

genderOwner = {
    1: 'man', 2: 'woman', 3: 'person'
}

eyeColor = {
    1: 'green', 2: 'blue', 3: 'brown', 4: 'hazel', 5: 'gray'
}

eyeAdjectives = {
    1: 'sparkling', 2: 'warm', 3: 'shining', 4: 'deep', 5:'bright'
}

traits = {1: 'a young', 2: 'a middle-aged', 3: 'a tall', 4: 'a stylish', 5: 'an avant-garde', 6: 'a kind', 7: 'a well-dressed', 8: 'a brassy'}

howRU = {1: '"Oh just lovely! Thank you for asking. It\'s a beautiful day."', 2: '"Busy busy! I wasn\'t sure if I\'d have time for my appointment today."', 3: '"Oh a bit worn down if I\'m being honest, work has been a nightmare'
         }

owner = random.randint(1, 10)
customer = random.randint(1, 20)
salutation = random.randint(1, 5)
eyes = random.randint(1, 5)
adj = random.randint(1, 5)
genderO = random.randint(1, 3)
type = random.randint(1, 8)

if gender[salutation] == "Mr.":
    pronoun = "his"
elif gender[salutation] == "Mx.":
    pronoun = "their"
else:
    pronoun = "her"

if gender[salutation] == "Mr.":
    pronoun2 = "him"
elif gender[salutation] == "Mx.":
    pronoun2 = "them"
else:
    pronoun2 = "her"

if gender[salutation] == "Mr.":
    pronoun3 = "he"
elif gender[salutation] == "Mx.":
    pronoun3 = "they"
else:
    pronoun3 = "she"

if gender[salutation] == "Mr.":
    pronoun4 = "the man"
elif gender[salutation] == "Mx.":
    pronoun4 = "the customer"
else:
    pronoun4 = "the woman"


# print('\nAs you walk into Luxe; ' + (lastFancyNames[owner]) + ' ' + traits[type] +  ' ' + genderOwner[genderO] + ' with ' + eyeAdjectives[adj] + ' '+ eyeColor[eyes] + ' eyes greets you at the door.\n')
# print('"Hi, you must be the new receptionist!"\n')
# print('"My name is ' + (firstFancyNames[owner]) + ' ' + (lastFancyNames[owner]) + ', and this is my spa and salon"')
# print('"Since it\'s your first day, I\'ll be showing you the ropes."')
# receptionist = input('"Tell me, what was your name again?" ')
# print('"So lovely to meet you, ' + receptionist + '."')
# print('"Ok, so it\'s just about 10 am, why don\'t you go turn on the sign?"')
# print('"Ah, right on time! ' + gender[salutation] + ' ' + lastNames[customer] + ' has arrived for ' + pronoun + ' Ten O\'Clock!"')
# if lastFancyNames[owner] == lastNames[customer]:
#     print('"Oh, ' + pronoun3 + ' is my cousin! Treat ' + pronoun2 + ' well."')
#     time.sleep(1)
#
#
# def firstGreeting():
#     greeting = input('"Why don\'t you greet ' + pronoun2 + '?"').lower()
#     if 'hello' in greeting or 'hi' in greeting or 'greetings' in greeting or 'ola' in greeting:
#         print('You smile nervously as ' + pronoun3 + ' approaches you.')
#         time.sleep(1)
#         print('"Hello, ' + gender[salutation] + ' ' + lastNames[customer] + ', welcome to Luxe; ' + (lastFancyNames[owner]) + '."')
#     else:
#         print('"That\'s no way to greet a customer! Try again"')
#         firstGreeting()
#
# def firstCustomer():
#     print((firstFancyNames[owner]) + ' leans over and kisses ' + pronoun4 + ' on each cheek.')
#     print('"' + firstNames[customer] + ' darling! And how are you this lovely day?"')
#     print('"')
#     firstAppt = input('"' + receptionist + ', I believe ' + gender[salutation] + ' ' + lastNames[customer] + ' is here for a hair appointment, would you doublecheck the book?').lower()
#     if 'check' in firstAppt:
#         print('You take a look at the appointment book on what is now your desk, and sure enough, next to ' + gender[salutation] + ' ' + lastNames[customer] + '\'s name is a check in the box indicating ' + pronoun + ' appointment is for the hair salon.')
#     else:
#         print('You fumble around with the book for a moment, perplexed, before ' + (firstFancyNames[owner]) + ' snatches it from your hands.')
#         print('"Don\'t worry, ' + receptionist + '. You\'ll get the hang of it. Do you see here where there is a check mark next to salon? That means ' + gender[salutation] + ' ' + lastNames[customer] + ' is here for a hair appointment!"')
#

def hairAppointment():
    treatment = ["keratin", "brazilian blowout", "permanent wave", "relaxer", "olaplex", "toner"]
    hairstyles = ["bouffant", "afro", "beehive", "box braids", "updo", "chignon", "cornrows", "crown braid", "locs",
                  "extensions", "finger waves", "french twist", "jheri curl", "liberty spikes", "natural", "pompadour"]
    cstChoice = random.randint(0, 2)
    # haircut = random.randint(1, 2)
    # treatments = random.randint(0, 2)
    # styles = random.randint(0, 2)
    # hairOptions = [[haircut, haircuts, 'haircut'], [colour, color, 'color'], [treatments, treatment, 'treatment'], [styles, hairstyles, 'style']]
    # hairCustomers = 0
    # services = 0
    # selected = []
    # selectedList = []
    print("Which of our services are you interested in today?")
    if cstChoice == 0:
        print("I'd like a haircut please!")
    elif cstChoice == 1:
        print('I\'m here for a treatment')
    else:
        print("I'm here to be styled")
    print("What about color? You'd look great as a blonde")


def hairCuts(currentTab = 0, services = []):
    haircuts = ["pixie", "crew", "asymmetric", "bangs", "bob", "mohawk", "fade", "feathered", "hime", "hi-top fade",
                "ivy league", "long layers", "lob", "mullet", "fashion mullet", "pageboy", "shag", "undercut"]
    cutPrices = [25, 25, 30, 20, 30, 20, 35, 40, 40, 35, 40, 40, 30, 25, 40, 30, 40, 25]
    options = random.randint(0, len(haircuts)-1)
    colour = random.randint(0, 2)
    print("Just a cut today? You'd look really great as a blonde.")
    if colour == 2:
        print('"Yes, I\'ll do a color treatment as well"')
    else:
        print('"Not today, just the cut"')
    print('"Ok, what kind of cut would you like?')
    print('"I\'d like a ' + haircuts[options] + ', please')
    print('"Ok great! That will be ' + str(cutPrices[options]) + '!"')
    currentTab = cutPrices[options] + currentTab
    print(currentTab)
    services.append("a haircut")
    checkout(currentTab, services)

def hairColors(currentTab = 0, services = []):
    color = ["partial highlight", "all over color", "root touch up", "full highlight", "base color + partial highlight",
             "base color + full highlight", "partial baylage", "root melt + lowlights", "ombre", "baylage"]


def checkout (currentTab, services):
    allServices = ', '.join(services)
    print('"Ok great! For ' + allServices + ' your total will be ' + str(currentTab) + '!"')

    # for options in hairOptions:
    #     if options[0] == 2:
    #         services += 1
    #         selected.append(options[2])
    #         selectedList.append(options[1])
    # if services == 0:
    #     services += 1
    #     selected.append('haircut')
    #     selectedList.append(haircuts)
    # newList = zip(selected, selectedList)
    # print(selectedList)
    # print(selected)
    # print(services)
    # if services == 1:
    #     print('I would like a ' + selected[0])
    # if services == 2:
    #     print('I would like a ' + selected[0] + ' and a ' + selected[1])
    # if services == 3:
    #     print('I would like a ' + selected[0] + ', a ' + selected[1] + ' and a ' + selected[2])
    # if services == 4:
    #     print('I would like a ' + selected[0] + ', a ' + selected[1] + ', a ' + selected[2] + ' and a ' + selected[3])
    # for items in newList:
    #     if hairCustomers == 0:
    #         ask = input('"Now would be a good time to ask the customer what kind of ' + items[0] + ' they would like." ')
    #     if hairCustomers > 0:
    #         ask = input('ask about ' + items[0])
    #     if items[0] in ask:
    #         print('"What kind of ' + items[0] + ' would you like?"')
    #     selections = items[1]
    #     choice = random.randint(0, (len(selections)-1))
    #     print(selections[choice])
    #     if items[0] == 'color':
    #         colorTypes = ['black', 'brown', 'blonde', 'white', 'red', 'unnatural']
    #         colors = [('black', ['Jet Black', 'Natural Black', 'Blue-Black']), ('brown', ['Dark Brown', 'Chocolate Brown', 'Medium Brown', 'Light Brown', 'Medium Ash Brown']), ('blonde', ['Light Ash Brown', 'Medium Blonde', 'Honey Blonde', 'Sandy Blonde', 'Butterscotch Blonde']), ('white', ['Ash Blonde', 'Vanilla Creme Blonde', 'Rosa Rosa']), ('red', ['Copper Red', 'Rich Copper Red', 'Dark Red Copper', 'Strawberry Blonde']), ('unnatural', ['Plum Dark Purple', 'Blue Steel', 'Green Grape', 'Mystic Turquoise', 'Pink Pearl', 'Purple Passion', 'Ruby Red', 'Ultraviolet'])]
    #         print("And what color would you like today?")
    #         colorFam = random.randint(0, 5)
    #         print(colorTypes[colorFam])
    #         colorSelect = colors[colorFam]
    #         print(colorSelect)


        # print(items[1])














# firstGreeting()
# firstCustomer()

# hairAppointment()
hairCuts()
