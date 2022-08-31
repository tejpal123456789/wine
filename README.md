create env

'''bash

conda create -n python=3.7 -y

activate env
'''bash
conda activate envname

create requirement.txt file 
install requirements
'''bash
pip install -r requirements.txt



git init
dvc init
dvc add data_given/winequality.csv

git add .

git commit -m 'first commit'
