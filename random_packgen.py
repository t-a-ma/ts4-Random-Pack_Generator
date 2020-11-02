import random

stuffPacks = ['Luxury Party', 'Perfect Patio', 'Cool Kitchen', 'Spooky Stuff', 'Movie Hangout', 'Romantic Garden', 'Kids Room', 'Backyard Stuff',
'Vintage Glamour', 'Bowling Night', 'Fitness Stuff', 'Toddler Stuff', 'Laundry Day', 'My First Pet', 'Moschino', 'Tiny Living', 'Nifty Knitting']
gamePacks = ['Outdoor Retreat', 'Spa Day', 'Dine Out', 'Vampires', 'Parenthood', 'Jungle Adventure', 'Strangerville', 
'Realm of Magic', 'Journey to Batuu' ]
expansionPacks = ['Get to Work', 'Get Together', 'City Living', 'Cats and Dogs', 'Seasons', 'Get Famous', 'Island Living', 
'Discover University','Eco Lifestyle','Snowy Escape']


def main():
    pack_type = random.randint(1, 12946801) % 4
    if pack_type == 0:
        pack_type += random.randint(1,3)
    # maybe u should test how random this really is 

    if pack_type == 1:
        pack = random.randint(1, 38583621) % len(expansionPacks)
        return expansionPacks[pack]
    elif pack_type == 2:
        pack = random.randint(1, 38583621) % len(gamePacks)
        return gamePacks[pack]
    else:
        pack = random.randint(1, 38583621) % len(stuffPacks)
        return stuffPacks[pack]


print(main())