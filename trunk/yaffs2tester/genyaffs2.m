
covtypes={'Block', 'Branch','Path','PCT(BB)', 'PCT(ST)'};

cm=load('covmukill_yaffs2');

for i = 1:5
    figure
    scatter(cm(:,i),cm(:,6) );
    xlabel(sprintf('%s Coverage',char(covtypes(i))));
    ylabel('Killed Mutants')
    title('YAFFS2 Coverage - Killed Mutants Scatter Plot')
end;

% rsquares
x=[1:5];
figure

rsquares = [];
for i = 1:5
    whichstats = {'rsquare'};
    stats = regstats(cm(:,6),cm(:,i),'linear',whichstats);
    rsquares = [rsquares, stats.rsquare];
end;
bar(x,rsquares);
title('YAFFS2 Coverage-Killed Mutants R^2 Values');
set(gca, 'XTickLabel',covtypes);
ylabel('R^2 Values')
xlabel('Coverage Type');
for i = 1:5
    text(x(1,i),rsquares(1,i),num2str(rsquares(1,i)),'horiz','center','vert','bottom')
end;
% kendall
figure

kendalls = [];
for i = 1:5
    kendall=corr(cm(:,6),cm(:,i),'type','Kendall');
    kendalls=[kendalls,kendall];
end;
bar(x,kendalls);
title('YAFFS2 Coverage-Killed Mutants Kendall Correlation Coefficients');
set(gca, 'XTickLabel',covtypes);
ylabel('Kendall Correlation');
xlabel('Coverage Type');
for i = 1:5
    text(x(1,i),kendalls(1,i),num2str(kendalls(1,i)),'horiz','center','vert','bottom')
end;