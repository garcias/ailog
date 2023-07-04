# ailog

Website to publicly disclose and log my interactions with public AI agents, for transparency and attribution. Also disclose ethical principles I try to follow in these interactions.

Uses Jekyll (and theme [Just the Docs](https://just-the-docs.com)) to build from Markdown files. [build.sh](build.sh) contains functions to install helpful gems and to build and serve the site, for testing in a devcontainer.

```sh
source serve.sh
install
serve
```

## Generate posts from interaction data

Python script [convert.py](convert.py) will read a JSON file of an interaction (it must have the structure in the example below), generate a Jekyll Markdown file with proper front matter in `_posts/`, and move the JSON to `archive/`. To process a file named `test.json`, first activate Pipenv (or install `pyyaml` and `python-slugify`), and then invoke the script below. The resulting .md and .json files will be named using the date and slugified title.

```sh
python3 -m convert bard test.json
```

For example, running the script on the interaction file below ...

```json
{
    "metadata": { 
        "title": "Getting to know each other",
        "date": "2023-05-29",
        "agent": "bard"
    },
    "rounds": [
        {
            "query": "Hello", 
            "response": "Hello! How can I help you?"
        },{
            "query": "My name is Simon",
            "response": "Hi Simon, it's nice to meet you! How can I help you today?"            
        }, 
        ...
    ]
}
```

... will generate the following files:

- `_posts/2023-05-29-getting-to-know-each-other.md`
- `archive/2023-05-29-getting-to-know-each-other.json`
