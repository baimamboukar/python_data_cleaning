for file in * 
do
        git add $file
        git commit -m "adding $file"
        git push
done

cd datasource
for file in * 
do
        git add $file
        git commit -m "adding $file"
        git push
done

cd - 

cd cleandata
for file in * 
do
        git add $file
        git commit -m "adding $file"
        git push
done