html = """
<script>
    var id = \"5010\";
    var id2 = \"8888\";
    var idX = \"XoX\";
</script>"""

varlist = {}
vars  = html.split("var ")[1:]  # get each var entry
for v in vars:
    name = v.split("=")[0].strip()  # first part is the var [name = "]
    value = v.split("\"")[1]        # second part is the value [ = "..."]
    varlist[name] = value           # store it for printing below

print("Varlist - " + str(varlist))
