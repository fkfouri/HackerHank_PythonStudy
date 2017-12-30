import sys

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def up(self):
        self.canal +=1
    def down(self):
        self.canal -=1


tv = Televisao()
tv.up()


print(tv.canal)
#dir(tv)

SELECT RPAD('*',21-LEVEL,'*')
FROM DUAL 
CONNECT BY LEVEL BETWEEN 0 AND 20;


Declare
    p :=20;
begin
    while p >= 1 loop
        DBMS_OUTPUT.PUT_LINE(RPAD('*',p,'*') ); 
        p := p - 1;
    end loop;   

end;

********************

    