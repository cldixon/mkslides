# MkSlides

Mkdocs for slides. Modular and re-usable slides, freed from their decks. Build with with simple config files. This tool utilizes the [marp](https://marp.app) ecosystem to create markdown-based slides built with independent, self-contained and individual markdown slides. Using a configuration file, similar to mkdocs' `mkdocs.yml`, we _build_ slide decks from specified markdown slide files. This way, multiple decks can use and re-use slides, and decks can be built on the fly to keep content up to date.

:vertical_traffic_light:, :warning: and :construction: : This is a slide project and under occasional development when I have time. I also use this project to test out new tools before bringing them to work.

### Usage

Create a new configuration file for your markdown slides.

```sh
$ mkslides init
```

The directory will look like this as a result:

```
mkslides.yml
slides/
    cover.md
```

The initialization step creates a sample slide so the following build process works out of the box.

The generated configuration file will look like this.

```yaml
name: my-slide-deck.md
description: First deck developed by mkslides.
author: Your name here, please!
output_format: html
theme: default
paginate: false
header: null
footer: null
overwrite: true
slides:
    - cover.md
```

Next, we can build our slide deck.


```sh
$ mkslides build
```

This will create a new directory `decks`, in which the output artifacts of our slide deck are stored. Currently, this command will compile the slides listed in the `mkslides.yml` into a single markdown, marp-style file, and is then converted into marp-supported output formats. HTML is the default, but you can also specify PDF or PPTX in the configurations file.
