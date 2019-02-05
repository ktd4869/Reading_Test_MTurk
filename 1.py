import re
if __name__ == "__main__":
    for i in range(2,19):
        with open("article/article_1.txt") as file:
            text = file.read()
            out = re.sub('1',str(i),text)
            with open("article/article"+str(i)+".html",'w') as output:
                output.write(out)