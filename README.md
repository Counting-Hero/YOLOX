# Setup venv and install
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- pip install -r YOLO2COCO/requirements.txt
- pip install -v -e .

# prepare data and train
- With a folder of yolo images/labelfiles + labels.txt, create a darknet dataset with tools/create_darknet_dataset.py by changing the value of root_dataset to your data folder
- Now convert this to coco with YOLO2COCO/darknet2coco.py, you might need to change the value of coco_tran, coco_val, etc... to fit with your dataset
- Now you can train with python tools/train.py -f exp.py -d 8 -b 64 --fp16 -o -c pretrained_coco.pth --cache
