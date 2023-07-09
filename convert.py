import sys
import json
from string import Template
from jekyll import JekyllPage
from pathlib import Path
from slugify import slugify

round_template = Template("""
#### ${index}

{: .prompt }
${prompt}

{: .response }
${response}
""")

def format_round( index: int, prompt: str, response: str ) -> str :
    return round_template.substitute( 
        index = index,
        prompt = blockquote( prompt ),
        response = blockquote( response ),
    )

def blockquote( text:str ) -> str:
        lines = text.split('\n')
        lines = [ f"> {line}" for line in lines ]
        return "\n".join( lines )

def bard_to_md( source_json: dict ) -> str:
    rounds = source_json['rounds']
    rounds = [
        format_round( i + 1, round['prompt'], round['response'] )
        for i, round in enumerate( rounds )
    ]
    rounds_str = "\n".join( rounds )
    title = source_json['metadata']['title']
    date = source_json['metadata']['date']
    agent = source_json['metadata']['agent']
    front_matter = { 'title': title, 'layout': "post" }
    content = f"# {title}\n\n_date:_ {date}\n\n_agent_: {agent}\n\n{rounds_str}"
    jp = JekyllPage( front_matter=front_matter, content=content )
    return jp.page()

if __name__ == "__main__":
    try:
        source_type = sys.argv[1]
    except IndexError:
        print( 'First parameter is model for parsing file content, e.g., "bard"' )

    try:
        source_path = Path( sys.argv[2] )
        with source_path.open() as f:
            source = "".join( f.read() )
            source = json.loads( source )
    except IndexError:
        print( 'Second parameter is filename with structure consistent with model' )

    if source_type == 'bard':
        date = source['metadata']['date']
        slug = slugify( source['metadata']['title'] )
        post_name = f'{date}-{slug}.md'
        archive_name = f'{date}-{slug}.json'
        post_path = Path('_posts') / Path(post_name)
        archive_path = Path('archive') / Path(archive_name)
        with post_path.open( mode='w' ) as f:
            f.write( bard_to_md( source ) )
        source_path.replace( archive_path )
