---
layout: default
title: Research
description: "Only a narrow subset of possible phenotypes exists, and that subset is patterned. What organizes it, how do we measure it, and what is its geometry?"
---

<!--
  Narrative order:
    1. Darwin's endless forms is the received view. Establish the counter-claim
       first: life occupies a small, uneven region of possible phenotype space.
       This is an ARGUMENT, not an assertion. The combinatorial point does that
       work; do not weaken it back into a bare claim.
    2. Then two modest observations, framed as "worth noticing", NOT as a thesis:
       (a) the region is not uniform. Dependencies are part of what structures
           it, and structure should leave a geometry.
       (b) the phenotypes worth explaining are high-dimensional, so measurement
           and representation determine what we can say, and bear on geometry too.
    3. Those two observations lead to the three lines. End the intro on the
       question, not on a list of what I build. Question-oriented, not tool-oriented.

  Figures were removed pending better source images. The .figure styles in
  assets/css/style.css are still available when they return.

  Kept off this page on purpose: specific grant plans, and unpublished results
  from the in-progress flower colour work.
-->

# Research

<blockquote class="epigraph">
  <p>From so simple a beginning endless forms most beautiful and most wonderful
  have been, and are being, evolved.</p>
  <cite>Charles Darwin, On the Origin of Species, 1859</cite>
</blockquote>

<p class="lede">
The forms are wonderful. They are not endless.
</p>

Thirty binary characters already describe more than a billion combinations, far
more than the number of species alive today, and almost none of those
combinations has ever been built. Allow the description to include size and
shape and the gap stops being countable at all. Against a space of possibility
that really is endless, life has taken one narrow and uneven path. What
determines that path?

Two things about it are worth noticing.

The first is that the path is not uniform. Realized forms cluster, and some
regions stay empty while their neighbours fill. Traits that depend on one
another are part of the reason, since the state of one character changes which
states of another a lineage can reach. Constraint of that kind does not merely
thin the occupied region, it gives the region a shape.

The second is that the phenotypes worth explaining are high-dimensional. A form,
a spectrum, or a photograph carries far more of what an organism is than a
handful of measurements do. Describing organisms that fully raises a question
the older methods never had to answer: in a space of shapes, what does it mean
for two organisms to be close together, or for a lineage to have travelled a
long way? Questions about closeness and distance are questions about geometry,
and they return us to the shape the first observation pointed at.

The three lines below follow from those two observations.

## Modelling dependencies

Dependencies are the part of the structure we can write down. Traits are bound
to one another, to the environment, and to the genotypes that build them.
Analyses that treat characters separately miss this, and they can credit the
wrong cause for a change. I build models that state the dependencies explicitly.
[corHMM](https://github.com/thej022214/corHMM) fits
several discrete characters at once, including characters we cannot observe
directly, which reduces the false correlations that appear when traits are fitted
one at a time.

Plant life history shows what this buys. Annuals wait out bad seasons as seed, so
it is natural to ask whether climatic extremes favour that strategy. But life
history also shapes which climates a lineage can occupy, and separating the two
requires fitting them together. I wrote **hOUwie** to do this, joining an
Ornstein-Uhlenbeck process to a hidden Markov model. Across 32 angiosperm clades
and eight climate variables, the maximum temperature of the warmest month was the
most consistent predictor of annual life history. The same reasoning applies to
antibiotic resistance, where each genetic background determines which mutations
come next; with the Michigan Infectious Disease Genomics Center I used
[phyloAMR](https://github.com/kylegontjes/phyloAMR) to sample the full range of
plausible histories rather than settle on one, and found seven distinct routes to
resistance in *Klebsiella pneumoniae*.

## Measuring phenotypes at scale

Claims about which forms exist are empirical claims, and testing them takes
measurements that stay consistent across thousands of species. Museums and
citizen-science platforms have already produced the images. Measuring them is the
slow part, because it is laborious and depends on who is doing it.

I use machine learning to turn those images into standard measurements. With
support from OpenAI I built pipelines that read flower colour from tens of
millions of iNaturalist photographs, covering roughly 80,000 flowering plant
species, a trait that had been studied in only a handful of systems because
collecting it by hand was impractical. Language models handle colour and
description well, but shape needs something more exact, so I am building
landmarking tools with convolutional networks. Those now measure head, mandible,
and body length across more than 270,000 ant specimens, and intertegular distance,
which tracks foraging ecology, across 550,000 bee images. Two R packages came out
of this work: [SegmentR](https://github.com/jboyko/SegmentR) for segmenting
specimen images, and [mvh](https://github.com/tncvasconcelos/mvh) for assembling
virtual herbaria.

## Recovering geometry

Colour and length are easy to extract partly because they already suit the models
we have, in which a phenotype is a point in a low-dimensional space and evolution
moves it around. Shape, sound, and spectral reflectance do not reduce that way.
Measuring them does not tell us how to compare two of them, or how far apart they
lie. Until that question is settled, a pattern we report may belong to our
representation rather than to the organism.

The problem appears in miniature in model selection. As characters accumulate,
the number of possible models grows faster than we can search it, so I wrote
**corHMMDredge**, which borrows regularization and parameter sharing from
statistical learning to keep the search tractable. Applied to mating system and
estrus signalling in primates, the best model confined change to a
one-dimensional path through a much larger space. Over the next several years I
want to build a geometric framework for comparative biology that describes the
surface phenotypic evolution actually moves on, and asks whether estimated rates
change once we measure them on that surface. The aim across all three lines is a
comparative biology that can tell the structure we impose from the structure
evolution leaves behind.
