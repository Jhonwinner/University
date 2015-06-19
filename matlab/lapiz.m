y=[]; x=[]; n_aleatorios = 100000;r = 8 ;contador = 0; 

tic  % inicio de contar cuanto tiempo demora la Simulación 
for i = 1 : n_aleatorios
y(i)=((40)*rand()); x(i)=((40)*rand()); %Cordenadas aleatorias 0 a 40cm
end
%cordenadas para dibujar el cuadrado 
b = linspace(-10,50,1000);
% Graficando  las  lineas del cuadrado 
plot(40,b,'black'); hold on; plot(0,b,'black'); hold on;
plot(b,40,'black');hold on; plot(b,0,'black'); hold on;
% --------------------------------------- Algoritmo
for i = 1 : n_aleatorios 
     ale = ((360) * rand()); % Agulo Aleatorio de 0 a 360
     xC = sin(ale).*r + x(i); %cordenada x2  
     yC = cos(ale).*r + y(i); %cordenada y2      
     %condicion de de estar Fuera del Cuadrado
     if (xC > 40 || xC < 0) || (yC  > 40 || yC <0)
     contador = contador+ 1 ;      
     end
     %Grafica del Segmento 
     m = (yC - y(i)) / (xC - x(i)); corX = linspace(x(i),xC,100);
     corY = (corX - x(i)).*m + y(i); plot(corX, corY ,'blue'); hold on;      
end
R = contador / n_aleatorios; %Resultado y Descripción del Gráfico
disp('Resultado de La simulacion es: ');disp(R);
title('GRÁFICO DE LAS CAIDAS DEL LAPIZ EN EL MOSAICO');
xlabel('Anchor de la ceramica ');ylabel('Altura de la ceramica'); hold off;
toc % fin de conteo de TieMpo
