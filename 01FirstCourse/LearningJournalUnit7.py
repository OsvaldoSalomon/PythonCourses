band_members = {"Oliver": ["vocalist", 34], "Jordan": ["keyboard", 33], "Lee": ["guitarist", 34],
                "Mat": ["drummer", 34], "Matt": ["bassist", 33]}
band_members
# {'Oliver': ['vocalist', 34], 'Jordan': ['keyboard', 33], 'Lee': ['guitarist', 34], 'Mat': ['drummer', 34],
#  'Matt': ['bassist', 33]}


def invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)
    return inverse


inverted_band = invert(band_members)
print(inverted_band)
# {'vocalist': ['Oliver'], 34: ['Oliver', 'Lee', 'Mat'], 'keyboard': ['Jordan'], 33: ['Jordan', 'Matt'],
#  'guitarist': ['Lee'], 'drummer': ['Mat'], 'bassist': ['Matt']}
