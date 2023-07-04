import sys
import json
from string import Template

round_template = Template("""\
{: prompt }
${prompt}

{: response }
${response}\
""")

def format_round( index: int, prompt: str, response: str ) -> str :
    round = round_template.substitute( prompt = prompt, response = response )
    return f"#### {index}\n\n{blockquote( round )}"

def blockquote( text:str ) -> str:
        lines = text.split('\n')
        lines = [ f"> {line}\n" for line in lines ]
        return "".join( lines )

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


