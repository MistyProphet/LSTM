# LSTM
LSTM neural network trained on wiki markup of 400 wikipedia pages for movies, generates a new movie plot, also written in wiki markup.
Network model has two lstm layers, and it generates 800 characters for a plot.

You can start the script with an argument like "One upon a time", and the script produces the plot from there. If you don't provide the seed for text generation, it takes a sentence from train set at random.
Network downloads wiki markup for each movie from the list ("movieList.txt"), so you need internet connection to train it. 

Example output after 33 training iterations:
--------------------------------------------------
----- diversity: 0.2
----- Generating with seed: " the season, the athletics fare poorly, "
 the season, the athletics fare poorly, later learning that he is now called but personal sees the various change and beat up in finding his death. the night learn the family is still unconscious.the man is roger with a party. the next day, priest, and the blast call of sam into the united states in the face of a series of visiting her of the desert, during a victory and the house of porson saying the sort beat unender for his creatures. anderson gets a trip to visit jamie to the driver's room, in the [[forerand calls]]'s money and drack sexually escape.she suddenly proves that he was alien to wait harry and calls his daughter and encounters another classmate, mary wants to attend and he leaves to be a subleede. eucy refuses, saying that she not the baral into the warlion before george of [[metachites]] has a true for another ti

----- diversity: 0.5
----- Generating with seed: " the season, the athletics fare poorly, "
 the season, the athletics fare poorly, later learning that he is now called ball. meanwhile, molly in a streather has had getting matt in order to stay in the search for the aunity and confronts laulably delivers a thene is on his mother and she sees a mission to [[rogar's president]], and he and several occuer from [[massah hamphhhon]], and a conversation beau confronts him, causing him to prove with his sep of another time service, remy's concile as a child, revealing that he is recording him as a major pawel. he sees a girl, and that he may be have a fallen for door which causes him to meet her for her dead.attern with the dad on her and they become a support who has no ine-putal devis alerticing his craig, and starts a surprise and invites him to make his pecicion. after his parents are a struggling creature and learns for 

----- diversity: 1.0
----- Generating with seed: " the season, the athletics fare poorly, "
 the season, the athletics fare poorly, later learn from the truck and dreams him in the work to kill her and he believes her in a station service, and as an ipportation of her son, but is surprised with and part of the following the car of leaving, he and nico male young him on the [[sing-share]]. soul is commanical life and land to be in the uncown. %end%

----- diversity: 1.2
----- Generating with seed: " the season, the athletics fare poorly, "
 the season, the athletics fare poorly, later visits jason that he joins her mother, survived that greene can the only with which they ded until the martians not rebeck to john by her love, his house, rushes on fire fuel. in the ccurse in on her, which malcolm realies hos.emily shows up and tricks them but can only as the late fighter. they su¥poved it back and morting and punches the garage for a singhel -[[brodutes]] containing a superizencer ([[ante-statito]]) tries to feel sara for him and has never supporting and rebuild him, he is diagned by angela and he sees up with garden and informs zim store gone to a provering call and shows her in the restaurant to new york and discover that sara is missing carl ends auntha, who is now no one with upset mexican in jack home and seek up while the cash of the brother is visiting him a

--------------------------------------------------
