#60
# hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
# hitsTitles.append('CHILD IN TIME')
# hitsTitles.append('AGAIN')
# print(hitsTitles)
# hitsTitles.insert(2,"HOTEL CALIFORNIA")
# print(hitsTitles)
# hitsTitles.insert(0,'THE SOUND OF SILENCE')
# print(hitsTitles)
# hitsTitles.remove("HOTEL CALIFORNIA")
# print(hitsTitles)

# hitsToRead = hitsTitles.copy()
# print(hitsTitles)
# print(hitsToRead)

# hitsToRead.reverse()
# print(hitsTitles)
# print(hitsToRead)

# hitsToRead.sort()
# print(hitsToRead)

# print(hitsToRead.pop(0))
# print(hitsToRead.pop(0))
# print(hitsToRead)

# additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
# print(additionalSongs)
# hitsToRead.extend(additionalSongs)
# print(hitsToRead)
#
# print(hitsToRead.count('WISH YOU WERE HERE'))
# print(hitsToRead.count('RIDERS ON THE STORM'))
#
# hitsToRead.clear()
# print(hitsToRead)

#63
# marketing = ['loyality program', 'client promotion', 'market research']
# print(marketing)
#
# print(marketing[2])
#
# marketing.insert(1,'investor relations')
#
# emailMarketing = marketing.copy()
#
# emailMarketing.sort()
#
# internalEmails = ['internal communication']
#
# emailMarketing.extend(internalEmails)
#
# emailTuple = tuple(emailMarketing)
# print('tupla: ', emailTuple)

#66
chanels = {'Google':'1480', 'Email':'300', 'Natural Traffic':'440', 'TV Spot':'700'}
print(chanels)
print(chanels['Email'])

chanelsUpdate = {'Natural Traffic':'520', 'News':'600'}
print(chanelsUpdate)

chanels.update(chanelsUpdate)
print(chanels)

print(chanels.keys())

chanels.pop('Email')
print(chanels)





