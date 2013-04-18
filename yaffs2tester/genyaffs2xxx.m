
function [x] = getcov()

blk = getcovext('block');
branch=getcovext('branch');

x = [blk, branch];

for i = 1:size(x,1)
    s = sprintf('%4.2f, %4.2f, %4.2f, %4.2f', x(i,1), x(i,2), x(i,3), x(i,4));
    disp(s);
end;

end

function [all] = getcovext(ext)
  all = [];
  for i = 1:10
      filename = sprintf('50KSwarm%d00/coverage/%s.*',i, ext);
      files = dir(filename);
      ds = [];
      for j = 1:size(files,1)
          file = files(j,:);
          file = strcat( sprintf('50KSwarm%d00/coverage/', i), file.name);
          fp = fopen(file);
          d = fread(fp);
          ds = [ds;d'];
          fclose(fp);          
      end;
      
      % ds should have all data
      allcov = sum(sum(ds)>0);
      avg = 0.0;
      for j = 1:size(ds,1)
          t = ds(j,:);
          avg = avg + sum(t);          
      end;
      avg = avg/(size(ds,1));
      
      all = [all; avg, allcov];
  end;
end

