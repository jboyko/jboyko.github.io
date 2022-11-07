---
title: "Research"
layout: splash
permalink: /research/
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: /assets/images/meltingphy.png
  caption: "Markov Condition"
excerpt: "The past and the future are dependent only through the present."
intro: 
  - excerpt: "'It is abundantly evident that rates of evolution vary. They vary greatly from group to group, and even among closely related lineages there may be strikingly different rates. Differences in rates of evolution [...] are among the reasons for the great diversity of organisms on the earth.' '
  -    Simpson (1953)"
feature_row:
  - image_path: assets/images/corhmm.png
    title: "Generalized hidden Markov models"
    excerpt: "I have extended discrete character models to allow for any number of characters with any number of observed or hidden states. This addresses the issue that phenotypic evolution, even when simplified to a discrete character, is better understood as the confluence of several characters evolving together, rather than a single character evolving independently. Furthermore, I demonstrate the some of the advantages of increasing state space from an information theoretic view."
    
  - image_path: /assets/images/maddfitz.png
    title: "False correlations in PCMs"
    excerpt: "I have applied hidden Markov models to the issue of false correlation between discrete character evolution. Comparative biologists are often interested in whether to discrete characters are correlated with each other as a significant and repeated dependent relationship may give insight into the underlying evolutionary process. However, it has been shown that several commonly used comparative methods are susceptible to false correlations. In this work, I demonstrated that allowing for character independent rate heterogeneity through the application of hidden Markov models, is one way to account for this statistical bias."
    
  - image_path: /assets/images/houwie.png
    title: "Jointly modeling discrete and continuous characters"
    excerpt: "I have developed a new model for linking discrete and continuous character evolution. The model called hOUwie, attempts to detect correlation between discrete and continuous characters and estimates their joint evolution. Furthermore, this model is developed with the issues of false correlations in mind and therefore allows for character independent rate heterogeneity as an alternative explanation."
---
There are two main themes in my research. First, most phenotypic evolution is not independent of other phenotypes. Changes in a particular character may influence changes in another and modeling these characters in isolation can mislead our inferences. Second, evolutionary change is heterogeneous. Not all species are going to change the same way at all times and failing to account for that, may again, mislead our inferences. The intersection of these two themes, character dependence and rate heterogeneity, is more natural than it may first appear. This claim is particularly true in the context of phylogenetic comparative methods (PCMs).

{% include feature_row id="intro" type="center" %}

{% include feature_row %}

