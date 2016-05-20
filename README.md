# LSTM
LSTM neural network trained on wiki markup of 400 wikipedia pages for movies, generates a new movie plot, also written in wiki markup.
Network model has two lstm layers, and it generates 800 characters for a plot.

You can start the script with an argument like "One upon a time", and the script produces the plot from there. If you don't provide the seed for text generation, it takes a sentence at random.
Network downloads wiki markup for each movie from the list ("movieList.txt"), so you need internet connection to train it. 
