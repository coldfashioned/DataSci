## Project Outline

### Satellite Imagery & Deep Learning

Due to the recent water crisis in Flint, MI, there is a wealth of GIS data for the city. I have recently completed some online courses in deep learning and I am researching various projects that use deep learning on satellite imagery. I have found several articles that pertain to semantic segmentation of satellite images of urban areas (cities). I think I can tweak a couple of these examples into something that will be useful for our purposes. If nothing else, it will be a great exercise that should drive home the adapting and development of a deep learning model for satellite imagery using the PyTorch framework.

Using semantic segmentation, I hope to categorize the city and gain some insight into how Flint compares to other major cities. More specifically, we hope to learn about the unused land in the city (amount, proximity to other landmarks & zones, etc.). From there, maybe we can find some ways to optimize the layout & zoning of the land as they redevelop.

### Resources

Kurt has provided me with a handful of resources that should provide a great jumping off point for this project.

[Genesee County Land Bank](http://www.thelandbank.org)

[Flint Property Portal](https://www.flintpropertyportal.org)

[National Renewable Energy Laboratory (NREL)](https://www.nrel.gov/)

I still need to do some research on these sites, but I have a feeling there's a ton of great information.

### Geo Data Usage

Something that could come out of this is to overlay population information on maps that have been run through the semantic segmentation model. That way, we could see how many people live near parks/highways/points of interest etc. This could also be useful in defining where new parks, roads, or other points of interest could/should go in. Another data science project would be to gather location data (via cell phone API's, perhaps) and using that to identify where people are hanging out at various times during the day. All of this is great practice for matplotlib and other visualization packages (Tableau, bokeh).

### Example Project and Next Steps

I found a project and paper on arxiv.org of a project that has an approach that I would like to apply to this project. After some finagling with cloning the project's github repository, I now have that project in the "urban-env" folder in this repo. I was hoping to just jump into training the model and applying it to satellite images of Flint, MI, but the original project used data for European cities. I suppose I could continue that way, but it might make more sense to gather GIS and satellite data of U.S. cities that are similar to Flint. There are many different ways I can go with developing deep learning models. The key, I think is to take things in manageable chunks. If I try to "eat the elephant", the project could overwhelm me. Here is what I think is a reasonable way to start.

* **Step 1:**
    * Using the above-mentioned model and lessons learned from [Fast.ai](http://www.course.fast.ai), build a deep learning model to perform semantic segmentation of aerial satellite imagery.        
    * Train the model with the data from European cities and then apply that learning to Flint GIS info & sat images.
    * Refine the model as needed & determine what the current state land usage is in Flint.
* **Step 2:**
    * Create a similar list of U.S. cities and gather GIS data.
    * Retrain the model using the U.S. city data (including Flint).
    * Bonus: Try to craft some sort of similarity index and determine what other U.S. cities are most similar to Flint. Or, try to create a desired state for land usage in Flint, based on other model cities.

The good news is that my brother will be getting a GIS intern starting in 2018 from the University of Michigan, Flint. This could be a huge help in moving this project along. This frees up my time to focus on the machine learning aspect, so I can deliver information to my brother in a more timely manner. The next step for me is to dig into the example project and see if I can make it run on my local machine. One other resource that I have come across is the revised version of the deep learning course on fast.ai. I started this course last year, but got bogged down. The revised version of the course uses PyTorch, which is currently my favorite deep learning framework in Python. I recently started this course again and I'm excited to take it through to completion. This course includes a section on satellite imagery, which should prove extremely valuable to this project.
