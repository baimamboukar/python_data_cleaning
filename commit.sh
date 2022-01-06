for file in * 
do
        git add $file
        git commit -m "commit $file"
        git push
done