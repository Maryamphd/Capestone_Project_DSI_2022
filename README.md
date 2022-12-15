![iStock-1304919777](https://user-images.githubusercontent.com/68198656/205503706-58b76f14-c104-4f65-a88c-0471d1fa0d5e.jpg)
# Classifying Skin Lesions from Dermoscopic Images using CNN Model

## Dataset
In June 2018, the Harvard database released the HAM10000 ("Human Against Machine with 10000 training images") dataset, which includes 10,015 dermatoscopic images, in an effort to provide training data for automating the process of skin cancer lesion classifications. The goal of this action was to give people access to a large and diverse dataset for training machine learning systems, so that the systems' performance could be evaluated against that of human experts. The applications, if implemented, would allow medical facilities and professionals to save money and time.

Also included with the 10,015 images is a metadata file detailing the demographics of each lesion. Histopathology (histo) is the gold standard for confirming more than half of all lesions; in the remaining cases, follow-up examination (follow up), expert consensus (consensus), or confirmation by in-vivo confocal microscopy provide the real evidence (confocal).

The 7 classes of skin cancer lesions included in this dataset are: Melanocytic nevi (nv), Melanoma (mel), Benign keratosis-like lesions (bkl), Basal cell carcinoma (bcc) 
,Actinic keratoses (akiec), Vascular lesions (vas) and Dermatofibroma (df).

### Data Availability
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T

## Analysis Content
* Download the data
* Exploratory data analysis (EDA).
* Image Preprocessing
* Evaluation Protocol
* Set Training option
* Training the CNN model
* Test the model
* Expermental Results

## References:
[1] Noel Codella, Veronica Rotemberg, Philipp Tschandl, M. Emre Celebi, Stephen Dusza, David Gutman, Brian Helba, Aadi Kalloo, Konstantinos Liopyris, Michael Marchetti, Harald Kittler, Allan Halpern: “Skin Lesion Analysis Toward Melanoma Detection 2018: A Challenge Hosted by the International Skin Imaging Collaboration (ISIC)”, 2018; https://arxiv.org/abs/1902.03368.

[2] Tschandl P., Rosendahl C. & Kittler H. The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Sci. Data 5, 180161 doi.10.1038/sdata.2018.161 (2018)

[3] Noel C. F. Codella, David Gutman, M. Emre Celebi, Brian Helba, Michael A. Marchetti, Stephen W. Dusza, Aadi Kalloo, Konstantinos Liopyris, Nabin Mishra, Harald Kittler, Allan Halpern: "Skin Lesion Analysis Toward Melanoma Detection: A Challenge at the 2017 International Symposium on Biomedical Imaging (ISBI), Hosted by the International Skin Imaging Collaboration (ISIC)", 2017; arXiv:1710.05006.

[4] Marc Combalia, Noel C. F. Codella, Veronica Rotemberg, Brian Helba, Veronica Vilaplana, Ofer Reiter, Allan C. Halpern, Susana Puig, Josep Malvehy: "BCN20000: Dermoscopic Lesions in the Wild", 2019; arXiv:1908.02288.

[5] Tschandl, P., Rosendahl, C. & Kittler, H. The HAM10000 dataset, a large collection of multi-source dermatoscopic images of common pigmented skin lesions. Sci. Data 5, 180161 doi:10.1038/sdata.2018.161 (2018).

[6] https://www.tensorflow.org/

[7] https://challenge.isic-archive.com/landing/2018/47/

[8] Pham, Tri-Cong, et al. “A Comparative Study for Classification of Skin Cancer.” 2019 International Conference on System Science and Engineering (ICSSE) (2019): 267-272.

[9] Radosavovic, Ilija et al. “Designing Network Design Spaces.” 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) (2020): 10425-10433.

[10] https://towardsdatascience.com/building-a-skin-lesion-classification-web-app-16fd2c422b9d



