# 1. Create songs set of 3 songs

songs = {"Rockstar", "Fall Apart", "Broken Whiskey Glass"}
print(songs)

# 2. Use the .add() method to add the title "Treehouse Hula" to songs

songs.add("Treehouse Hula")
print(songs)

# 3. Use .update() to add the following two sets to your songs
#{"Python Two-Step", "Ruby Rhumba"}
#{"My PDF Files"}

songs.update({"Python Two-Step", "Ruby Rhumba"},{"My PDF Files"})
print(songs)
