# LSTM
LSTM neural network trained on wiki markup of 400 wikipedia pages for movies, generates a new movie plot.

You can start the script with an argument like "One upon a time", and the script produces the plot from there. If you don't provide the seed for text generation, it takes a sentence at random. 

Network is trained to download wiki markup for each movie from the list ("movieList.txt"), but alternatively, you can use the getPages.py script to download pages, so you can train it locally.
