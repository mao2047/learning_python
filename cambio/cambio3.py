import re
import json
from bs4 import BeautifulSoup


html_doc = """
<script type="text/javascript">
        var modelData = {
            name: 'somename',
            thumbnailUrl: 'https://website.com/blob/bG9uZ2RhbjovL0ZPVVIvbGRwcm9kLWRlL3ljb3B6YTY4N0pnQ2Nfc3JYcVV3VXc9PQ',
            account: '5LH7J44IYPAGEZEYA9KIL',
            Id: 'someid'
        };
        store.initOmlib({"ClusterEndpoints":{"ONE":["http://us.site.me"],"TWO":["http://sg.site.me"],"FOUR":["http://de.site.me"],"FIVE":["http://in.site.me"],"SIX":["http://ja.site.me"],"SEVEN":["http://br.site.me"]},"ClusterEndpointsInternal":{"ONE":["http://usi.site.me"],"TWO":["http://sgi.site.me"],"FOUR":["http://dei.site.me"],"FIVE":["http://ini.site.me"],"SIX":["http://jai.site.me"],"SEVEN":["http://bri.site.me"]},"ClusterKeys":{"FIVE":"Cf0Mw0I2/cZf6alwfMhelEEOb6xq23IhPvC9E4eoaXU=","SIX":"bfYXVkWhs/gv+TCJ3EeeEE3oxiZRDpJO0fecUGdq2Qg=","ONE":"xkkzyNJmZ1DmNPxGwrykZ2O91f10KNXQvspa15nKKGs=","FOUR":"xMRCvh1eki9JEceBcV7Bx49uaQYpX8FdD0eZ+LCGqCc=","TWO":"XaG4I7b7wDOZ+lGHSPwbJ2HLkIFf0UGYAWz9c9LkiQk=","SEVEN":"LuSOGA/u5PL7rP8PG3cr6bqgQy7jXEv65iuHUX9ePQY="},"DefaultCluster":"ONE","IdpEndpoints":["http://idp.site.me"],"IdpKey":"MIOC9PS8KIwXOXSHtplBZLSpIqcifns0jzExtkHXw1g=","ReadOnlyEndpoints":["http://site.gg"],"ReadOnlyKey":"QKxHfdLVgbn+VYpnUiCFLMq/hhUpkpx7occEY3Z0Wnk="}, {"Id":"001026a1c1064a1b9305400814783c2385e2a978f13a","Secret":"0110de13b2187fe3078e13d9f6ad4e7567fdc143e915c9cb4df67ca"});

        if (store.renderArc) {
            store.renderArc(document.getElementById('root'), modelData, translateTable);
        } else {
            store.renderUser(document.getElementById('root'), modelData, translateTable);
        }
    </script>
"""

soup = BeautifulSoup(html_doc, "html.parser")
# locate the script, get the contents
script_text = soup.select_one("script").contents[0]

# get javascript object inside the script
model_data = re.search(r"modelData = ({.*?});", script_text, flags=re.S)
model_data = model_data.group(1)

# "convert" the javascript object to json-valid object
model_data = re.sub(
    r"^\s*([^:\s]+):", r'"\1":', model_data.replace("'", '"'), flags=re.M
)

# json decode the object
model_data = json.loads(model_data)

# print the data
print(model_data["name"])
print(model_data["thumbnailUrl"])
print(model_data["account"])
