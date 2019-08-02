salonServices = ["shampoo", "cut", "color", "treatment", "style", "nails", "facial hair", "body hair", "facial treatments", "body treatments"]

haircuts = ["pixie", "crew", "asymmetric", "bangs", "bob", "mohawk", "fade", "feathered", "hime", "hi-top fade", "ivy league", "long layers", "lob", "mullet", "fashion mullett", "pageboy", "shag", "undercut"]

color = ["partial highlight", "all over color", "root touch up", "full highlight", "base color + partial highlight", "base color + full highlight", "partial baylage", "root melt + lowlights", "ombre", "baylage"]

treatment = ["keratin", "brazilian blowout", "permanent wave", "relaxer", "olaplex", "toner", ]

hairstyles = ["bouffant", "afro", "beehive", "box braids", "updo", "chignon", "cornrows", "crown braid", "locs", "extensions", "finger waves", "french twist", "jheri curl", "liberty spikes", "natural", "pompadour"]

nails = ["basic manicure", "gel manicure", "basic pedicure", "gel pedicure"]

facialHair = ["lip wax", "eyebrow wax", "full face wax", "shave", "facial hair trim", "facial hair conditioning treatment"]

bodyHair = ["bikini", "brazilian", "underarm", "shoulders", "stomach", "buttocks", "half legs", "full legs", "half arms", "full arms", "chest", "back", "stomach strip", "chest and stomach", "back and shoulders", "full body"]


prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
    total_price += price
print(total_price)

average_price = total_price / len(hairstyles)
print("Average Haircut Price: $" + str(average_price))

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: $" + str(total_revenue))
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print(cuts_under_30)




