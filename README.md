# MkSlides

Mkdocs for slides. Modular and re-usable slides, freed from their decks. Build with with simple config files.

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