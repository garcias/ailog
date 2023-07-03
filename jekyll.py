import yaml
from dataclasses import dataclass
from typing import Dict

@dataclass
class JekyllPage:
    front_matter: Dict[ str, str ]
    content: str

    def write_file( self, path ):
        with open( path, 'w' ) as f:
            f.write( self.page() )

    def page( self ):
        p = f"---\n{ yaml.safe_dump( self.front_matter ) }\n---\n"
        p += self.content + "\n"
        return p
    
if __name__ == "__main__":
    fm = { 'title': "Welcome", 'layout': "default" }
    content = "Hello, World!"
    jp = JekyllPage( fm, )
    print( "Demonstration:" )
    print( jp.page() )
