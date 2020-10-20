function color_map2D(name_of_cell,dx,dy,D)
% Plotting a colormap2D
% Arguments:
%  1) name of cell: this is the name of the cell matrix created by the function
%  cell_import_txt.
% 2) dx,dy: minimum size between coordinates of simulation set.
% 3) D: total seze of set .
matrix_cell=struct2cell(load(name_of_cell)); %convert a struct to a cell
spsit=matrix_cell{1,1};
x=dx*((-D-1)/2:(D+1)/2);
y=dy*((-D-1)/2:(D+1)/2);
color_map_folder='color_map_img';
if ~exist(color_map_folder, 'dir')
       mkdir(color_map_folder) %create a new directory if do not exist
end
%mkdir(color_map_folder) 
for i=1:50
    %figure(i);
    imagesc(x,y,spsit{1,i});
    colorbar
    xlabel('x','FontSize',15,'interpreter','latex')
    ylabel('y','FontSize',15,'interpreter','latex')
    % Set the remaining axes properties
    set(gca,'FontSize',15,'LineWidth',1.5);
    filename=sprintf('psit%d.png',i);
    img_name=fullfile(color_map_folder,filename);
    export_fig(img_name)
    %saveas(gcf,img_name,'png') 
    %saveas(gcf,sprintf('\psit%d.png',i))    
end