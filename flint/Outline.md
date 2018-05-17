## Project Outline

### Satellite Imagery & Deep Learning

Due to the recent water crisis in Flint, MI, there is a wealth of GIS data for the city. I have recently completed some online courses in deep learning and I am researching various projects that use deep learning on satellite imagery. I have found several articles that pertain to semantic segmentation of satellite images of urban areas (cities). I think I can tweak a couple of these examples into something that will be useful for our purposes. If nothing else, it will be a great exercise that should drive home the adapting and development of a deep learning model for satellite imagery using the PyTorch framework.

Using semantic segmentation, I hope to categorize the city and gain some insight into how Flint compares to other major cities. More specifically, we hope to learn about the unused & underutilized land in the city (amount, proximity to other landmarks & zones, etc.). One subset of this underutilized land is parking lots. One of the first goals of this project is to use satellite imagery to identify parking lot area in the city.

### Resources

Here are a handful of resources that should provide a great jumping off point for this project.

[Genesee County Land Bank](http://www.thelandbank.org)

[Flint Property Portal](https://www.flintpropertyportal.org)

[National Renewable Energy Laboratory (NREL)](https://www.nrel.gov/)

I still need to do some research on these sites, but I have a feeling there's a ton of great information.

### Example Project and Next Steps

In the early stages of research, I found a project and paper on arxiv.org that took an insightful approach to segmentation of satellite imagery. However, flash-forward to May, 2018, and I'm starting to think about taking a different approach to this project. In order to focus on achievable results, I'm scaling back on what I want to tackle for the first stage of this project. The key is to think of this as a multi-generational project that can grow and change over the course of a year or two.

* **Phase 1:**
    * Using the above-mentioned model and lessons learned from [Fast.ai](http://course.fast.ai), build a deep learning model to perform semantic segmentation of aerial satellite imagery.        
    * Train the model with the image data obtained from existing datasets (if any exist!), or with images gathered by the GIS intern (see below).
    * Apply that learning to Flint image data.
    * Goal 1: train the model to be able to classify parking lot area in the city of Flint.

The good news is that my brother will be getting a GIS intern starting in mid-2018 from the University of Michigan, Flint. This will be a huge help in moving this project along. One other resource that I have come across is the revised version of the deep learning course on fast.ai. I started this course last year, but got bogged down. The revised version of the course uses PyTorch, which is currently my favorite deep learning framework in Python. I recently started this course again and I'm excited to take it through to completion. This course includes a section on satellite imagery, which should prove extremely valuable to this project.

### Geo Data Usage (Future Goals)

Something that could come out of this is to overlay population information on maps that have been run through the semantic segmentation model. That way, we could see how many people live near parks/highways/points of interest etc. This could also be useful in defining where new parks, roads, or other points of interest could/should go in. Another data science project would be to gather location data (via cell phone API's, perhaps) and using that to identify where people are hanging out at various times during the day. All of this is great practice for matplotlib and other visualization packages (Tableau, bokeh).
