# pa1-webcrawler-from-scratch
 
The goal of this project is to implement a web crawler from scratch to use within the Kennesaw State University website. We will identify the following information:

1. Top 5 pages with the most incoming links
2. Top 5 pages with the most outgoing links
3. Top 5 longest pages in terms of number of words
4. Build a vocabulary of words from the crawled pages and plot a word frequency distribution to see if the distribution follows Zipf's law
5. Remove the stop words from the vocabulary and show the 30 most frequent words
6. Randomly select 5 pages, use TF-IDF to extract the top 5 keywords from each page

Program must take a seed URL as input and crawl the webpage starting from the given URL. It must be invokable from a command line interface