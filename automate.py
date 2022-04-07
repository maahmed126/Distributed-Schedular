import sys
import os 

#1
START_INDEX = int(sys.argv[1])

#100
END_INDEX = int(sys.argv[2])

#5
SUB_PROCESS_COUNT = int(sys.argv[3])

#20
NUMBER_OFFSET = (START_INDEX + END_INDEX)//(SUB_PROCESS_COUNT)

print (NUMBER_OFFSET)

for i in range(START_INDEX, END_INDEX, NUMBER_OFFSET):
  
  offset = i + NUMBER_OFFSET

  COMMAND='''cp ./k8s-yaml/print_number.yaml ./k8s-yaml/deploy-{1}.yaml 
             sed -i '' 's|{0}|{1}|g' ./k8s-yaml/deploy-{1}.yaml 
             sed -i '' 's|{2}|{3}|g' ./k8s-yaml/deploy-{1}.yaml 
             kubectl apply -f ./k8s-yaml/deploy-{1}.yaml
          '''.format("BEGIN_VALUE", i, "LAST_VALUE", offset)
  os.system(COMMAND)
  print(i)

