function cell_import_txt(~)
% Multi-import_txt using cell

% % The argument of this function is added, using the imput function, by the 
% user. You have to indicate the name of the txt files that the folder 
% contain with the follow sintaxis: 'nameoffile*'. 

clear, clc;
a=input('Add the name of the .txt file: ');
d=dir(a);
l_d = length(d)-1;
super_psit = cell(1, l_d);

for k = 1:l_d
  psit = sprintf('psit%d.txt', k);
  super_psit{k} = importdata(psit);
end
save('super_psit.mat','super_psit');