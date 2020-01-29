#15. Utwórz skrypt, w którym zamiescisz 3 listy danych,
# zawierajace po 14 temperatur dla 3 wybranych miast na kolejne 14 dni oraz utwórz wykres z tych danych. Twój wykres powinien miec 3 linie z zaznaczonymi punktami danych za pomoca różnych znaczników, tytul, opisane osie oraz legende

from pylab import plot, show, xticks, yticks, title, xlabel, ylabel, legend, savefig
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
y = [14,16,12,8,6,5,4,4,10,14,12,11,12,11]
q = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
w = [16,17,10,9,5,4,3,6,11,11,9,10,14,10]
o = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
p = [16,16,16,7,6,3,2,3,8,15,11,9,13,10]
y4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14],fontsize='7',color = "r",style = 'oblique')
yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],fontsize="7")
plot(x,y4,'--k', x, y, q,w,o,p)
title("Temperatura dzienna dla 3 róznych miast na przestrzeni 14 dni",fontsize='10')
xlabel("dni",fontsize='10')
ylabel("temperatura",fontsize='10')
legend(["A","Warszawa","Poznań","Karków"])
savefig("mojwykres.png")