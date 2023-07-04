import sys
import json
from string import Template

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

def bard_to_md( source: str ) -> str:
    source_json = json.loads( source )
    rounds = [
        format_round( i + 1, round['query'], round['response'] )
        for i, round in enumerate(source_json)
    ]
    return "\n".join( rounds )

if __name__ == "__main__":
    try:
        source_type = sys.argv[1]
    except IndexError:
        source_type = 'bard'

    source = "".join( sys.stdin )
    if source_type == 'bard':
        print( bard_to_md( source ) )


