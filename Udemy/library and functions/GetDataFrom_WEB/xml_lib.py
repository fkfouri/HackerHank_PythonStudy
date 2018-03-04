'''
Entendendo como ler um XML.

O XML e muito mais complexo que um Json. 
'''


data_string = """
<Bookstore>
   <Book ISBN="ISBN-13:978-1599620787" Price="15.23" Weight="1.5">
      <Title>New York Deco</Title>
      <Authors>
         <Author Residence="New York City">
            <First_Name>Richard</First_Name>
            <Last_Name>Berenholtz</Last_Name>
         </Author>
      </Authors>
   </Book>
   <Book ISBN="ISBN-13:978-1579128562" Price="15.80">
      <Remark>
      Five Hundred Buildings of New York and over one million other books are available for Amazon Kindle.
      </Remark>
      <Title>Five Hundred Buildings of New York</Title>
      <Authors>
         <Author Residence="Beijing">
            <First_Name>Bill</First_Name>
            <Last_Name>Harris</Last_Name>
         </Author>
         <Author Residence="New York City">
            <First_Name>Jorg</First_Name>
            <Last_Name>Brockmann</Last_Name>
         </Author>
      </Authors>
   </Book>
</Bookstore>
"""


#Neste exemplo vamos ler um XML con formato de arvore (TREE), segue importacao da biblioteca
from lxml import etree 
root = etree.XML(data_string) #faz um parse de uma string
print(root.tag)
print(type(root))


print('=' * 40)
for t in root:
    print(t.tag)
    for u in t:
        print(t.tag, u.tag)
        for v in u:
             print(t.tag, u.tag, v.tag)

#print(etree.tostring(root, pretty_print=True).decode("utf-8"))

print('=' * 40)
#iterator sobre cada elemento do XML
for element in root.iter():
    print(element)


print('=' * 40)
# uma maneira de fazer a iteracao em cima de uma tag especifica
for element in root.iter("Author"):
    print(element.find('First_Name').text,element.find('Last_Name').text)

print('=' * 40, 'XPATH')
for element in root.findall("Book/Title"):
    print(element.text)

print('=' * 40, 'XPATH')
for element in root.findall("Book/Authors/Author/Last_Name"):
    print(element.text)


print('=' * 40, 'Tipo Where')
print(root.find('Book[@Weight="1.5"]/Authors/Author/First_Name').text)


for element in root.findall('Book/Authors/Author[@Residence="New York City"]'):
    print(element.find('First_Name').text,element.find('Last_Name').text)