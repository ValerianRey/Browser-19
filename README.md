# Browser-19
Repository for the hackathon Lauzhack Against COVID-19

This project aims to provide a visual way to browse through the papers related to the different coronaviruses. We used NLP tools to classify each paper with a topic and a subtopic, and we then built a network of the papers in each subtopic.

These networks helps the user to quickly get a visual idea of the existing papers in a field of research, and to see how close they are.
On top of that, we want to have a search engine that will allow researchers to see about which topic and subtopic the queried papers are, and where they are located withing the network of papers of the subtopic.

Our search engine is not completely linked to our visualization tool yet, but that will come soon.

### Search engine repository:
The code that we made for the search engine is in another repo: https://github.com/onefork/covid-19

Note that it's just a front end that does not do an actual search, but the connection with the back end is almost done.

### Visualization: 
Topic/Subtopic selection, graph visualizations: https://valerianrey.github.io/Covid19_Papers_V2/

Search engine: https://onefork.github.io/covid-19/

### Dataset: 
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge

### Original console browser: 
https://github.com/gsarti/covid-papers-browser

We use the idea of the search engine and some of their code (located in the scripts folder) that produces text embeddings from the abstracts of the papers.

Disclaimer: some of the work was already done before the start of the Lauzhack hackathon (this project started a week before for the CodeVsCovid19 hackathon).
