# OpenSW_Team5_MLOps_Master!!!๐ฅ
*Final_Project: mmdetection ๊ธฐ๋ฐ K-fashion ๋ฐ์ดํฐ ํ์ต

## Introduction

๋ณธ ํ๋ก์ ํธ๋ ์คํ์์ค ๋ชจ๋ธ์ธ mmdetection์ ํ์ฉํ์ฌ custom ๋ฐ์ดํฐ๋ก AI ๋ชจ๋ธ์ ํ์ตํ๊ณ  ์ต์ข์ ์ผ๋ก๋ docker image๋ก ๋ชจ๋ธ ๊ฐ๋ฐ ํ๊ฒฝ์ ๋ฐฐํฌํ๋ ๊ฒ์ ๋ชฉํ๋ก ํ๊ณ  ์๋ค. ๋ํ ๊ทธ ๊ณผ์ ์์ ์คํ์์ค ํ์ ์ํํธ์จ์ด๋ฅผ ํ์ฉํ์ฌ ํ์๋ค๊ณผ ์ด์ ๋ฐ ํ์๊ด๋ฆฌ๋ฅผ ์ค์ํ๋ค.

![predict](https://github.com/SangBeom-Hahn/OpenSW_Team5/blob/main/sample_image/main.jpg)


## Dataset

|Data|๋ฐ์ดํฐ ์|Train ๋ฐ์ดํฐ ์|Val ๋ฐ์ดํฐ ์|์ธ๋ถ์ฌํญ|
|:-:|:-:|:-:|:-:|:-:|
|1|5826|4740|1186|K-fashion|


ํ์ต์๋ K-fashion ๋ฐ์ดํฐ ์์ ์ฌ์ฉ, ๊ฐ ์ด๋ฏธ์ง๋ ๋ฐ์ดํฐ ๊ตฌ์ถ ์ฌ์์ ์ํด ์ ์๋ ๋ฐ์ดํฐ๋ก ์ด๋ฏธ์ง jpg ํ์ผ๊ณผ ๊ทธ์ ๋์ํ๋ annotation json ํ์ผ๋ก ์กด์ฌํ๋ค.

## Model

![project_pipeline](https://github.com/SangBeom-Hahn/OpenSW_Team5/blob/main/sample_image/mmdetection.PNG)

OpenMMLab์ Pytorch ๊ธฐ๋ฐ์ผ๋ก ์์ฑ๋ ์คํ ์์ค ํ๋ก์ ํธ์ด๋ฉฐ ํ์  ์ฐ๊ตฌ ๋ฐ ์ฐ์ ๋ถ์ผ์์๋ ๋๋ฆฌ ์ฌ์ฉ๋๋ค. OpenMMLab์ Computer Vision ๋ถ์ผ์ ์ฌ๋ฌ Vision Library์ ์ต์  ์๊ณ ๋ฆฌ์ฆ๋ค ๊ทธ๋ฆฌ๊ณ  ์๋ง์ pretrained model์ ์ ๊ณตํ๋๋ฐ ๋ฐ์ด๋ ๊ตฌํ ์ฑ๋ฅ, ํจ์จ์  Module ์ค๊ณ์ Config ์์คํ ๊ธฐ๋ฐ์ ํตํด Data๋ถํฐ Model ํ์ต, ํ๊ฐ๊น์ง ์์ฐ๋ฅด๋ ๊ฐํธํ Pipeline์ ์ ์ฉํ์๋ค.

OpenMMLab์์ ์ ๊ณตํ๋ Detection ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ธ MMDetection์ MASK-RCNN์ ์ฌ์ฉํ์ฌ instace segmentation๋ฅผ ์งํํ๋ค.

https://github.com/open-mmlab/mmdetection



## Project Structure

```
OpenSW_Team5
โโโ Final Project_MMDetection
โโโ mmdetection_code
โโโ team_assignment
โโโ bot.py
```

- Final Project_MMDetection : ๋ฐ์ดํฐ ์ ์ฒ๋ฆฌ
- mmdetection_code : MASK-RCNN ์ฝ๋
- bot.py : ํ๋ ๊ทธ๋จ ๋ด ์คํ ์ฝ๋

## Getting started
- Download the code from GitHub:
```bash
git clone https://github.com/SangBeom-Hahn/OpenSW_Team5
cd OpenSW_Team5/mmdetection_code
```

- Install the python libraries.
```bash
pip install -r requirements.txt
```

- Run the python script
```bash
python demo/image_demo.py ${IMAGE_FILE} \
    configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py \
    checkpoints/epoch_12.pth \
    --device cuda:0
```

## Local
```
python==3.7.13
cuda 10.0 - rtx 2080 super
```

## Requirements
```
pytorch==1.6.0
torchvision==0.7.0
mmcv(mmcv-full)==1.7.0
mmdet==2.26.0
```

## Using k_fashion with Docker

```shell
docker pull hsb422/k_fashion:0.01
```

- Run it with

Download model checkpoint and move it to mmdetection_volume directory

```shell
docker run -it -v mmdetection_volume:/mmdetection/data hsb422/k_fashion
```


## Authors

|ํผ์ ์ฐ|ํ์๋ฒ|ํ์ฐฌ์|
|:-:|:-:|:-:|
|[Github](https://github.com/SunWoo98Pi)|[Github](https://github.com/SangBeom-Hahn)|[Github](https://github.com/hcu55)|

- Blog : [Tistory(openSW)](https://hsb422.tistory.com/entry/%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-SW-%EC%8B%A4%EC%8A%B5-final-project)
