# EHRoes 🦸: an all-in-one web application for patients’ data digitization and exploration

**EHRoes** is developped for my thesis within the **MYO-xIA project**.
It features a standard vocabulary creator, optical character recognition (OCR), natural language processing (NLP), image annotation and segmentation using machine learning, interactive visualizations and automatic diagnosis prediction.

## Demo Usage Instructions

If you are on the demo instance (https://ehroes.lbgi.fr), you can login on top right with **login: demo ; password: demo**
The application is preloaded with a database of histology reports and a standard vocabulary for muscle biopsy. Data on this demo instance is reset once every day.
For the PDF automatic analysis, you can find a sample PDF [HERE](https://www.lbgi.fr/~meyer/EHRoes/sample_demo_report.pdf) working with the preinstalled standard vocabulary. A sample image for image annotation can be found [HERE](https://www.lbgi.fr/~meyer/EHRoes/sample_image_histo.jpg).
## Partners
EHRoes is developped and used in collaboration with the [Morphological Unit of the Institute of Myology of Paris](https://www.institut-myologie.org/en/recherche-2/neuromuscular-exploration-and-evaluation-centre/laboratoire-dhistopathologie-dr-norma-b-romero/). A production instance is deployed to help discovering new relevant features for congenital myopathies classification and diagnosis.

## EHRoes Abstract

**Background**
With a growing amount of patient data such as sequencing, imaging, and medical records, electronic health records (EHR) became central to drive research and improve diagnosis of patients by using multimodal data. But EHR usage is challenging as they require tools to format, digitize and interpret data. Today’s EHR exploitation tools ecosystem is heavily fragmented among tools to create EHR (format and digitize) and tools to interpret the data (exploration and diagnosis). Also most of the tools are specialized for one specific type of data, multiplying the number of different software needed for multimodal approaches. There is a strong need for a simple, all-rounder and flexible platform.
**Results**
In this paper we present EHRoes, an all-in-one web application for patients’ data digitization and exploration. With its module-based architecture, we developed four modules to: (i) create a set of standard vocabulary for a domain, (ii) automatically digitize free-text data to a set of standard terms, (iii) annotate images with standard vocabulary using automatic segmentation and (iv) generate an automatic visualization dashboard to provide insight on the data and perform automatic diagnosis suggestions. Using this platform, we successfully digitized 89 muscle histology reports from patients with congenital myopathies and we obtained an accuracy of 0.75 for congenital myopathy subtypes classification.
**Conclusions**
With EHRoes we created a platform for both patients data digitization and exploration that can handle image data and free-text data. As it uses user designed standard vocabulary, it is highly flexible to fit any domain of research. It can be used both as a patient registry with automatic diagnosis or as a research tool to explore a cohort of patients.
A demo instance of the application is available at https://ehroes.lbgi.fr.

## MYO-xIA Project

The MYO-xIA project aims to collect data from patients with **congenital myopathies** in order to analyse them using **explainable AI approaches**. In the field of congenital myopathies research, there is an important need for **digitization and standardization of patient data** in order to use modern data analysis methods.
This project has tree mains objectives:

- **Gather and format patient data** to be ready for automatic exploitation (patient histology-report form, image annotation, OCR/NLP)
- Help the **discovery of new phenotype-genotype-histology** association for each congenital myopathy subtype (standard vocabulary creation tool, per gene and per class histology feature statistics)
- Provide tools for **automatic diagnosis** based on patient data (live prediction of congenital myopathy subtype with histology reports, images, genetic data and phenotype)

## Contact

The main maintainer is:
**Corentin Meyer** - PhD Student @ CSTB Team - iCube - University Of Strasbourg [co.meyer@unistra.fr](mailto:co.meyer@unistra.fr)

## Citation

[placeholder]
