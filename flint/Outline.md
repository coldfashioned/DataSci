## Project Outline

### Satellite Imagery & Deep Learning

Due to the recent water crisis in Flint, MI, there is a wealth of GIS data for the city. I have recently completed some online courses in deep learning and I am researching various projects that use deep learning on satellite imagery. I have found several articles that pertain to semantic segmentation of satellite images of urban areas (cities). I think I can tweak a couple of these examples into something that will be useful for our purposes. If nothing else, it will be a great exercise that should drive home the adapting and development of a deep learning model for satellite imagery using the PyTorch framework.

Using semantic segmentation, I hope to categorize the city and gain some insight into how Flint compares to other major cities. From there, maybe we can find some ways to optimize the layout & zoning of the land as they redevelop.

### Resources

Kurt has provided me with a handful of resources that should provide a great jumping off point for this project.

[Genesee County Land Bank](http://www.thelandbank.org)

[Flint Property Portal](https://www.flintpropertyportal.org)

[National Renewable Energy Laboratory (NREL)](https://www.nrel.gov/)

I still need to do some research on these sites, but I have a feeling there's a ton of great information.

### Geo data usage

Something that could come out of this is to overlay population information on maps that have been run through the semantic segmentation model. That way, we could see how many people live near parks/highways/points of interest etc. This could also be useful in defining where new parks, roads, or other points of interest could/should go in. Another data science project would be to gather location data (via cell phone API's, perhaps) and using that to identify where people are hanging out at various times during the day. All of this is great practice for matplotlib and other visualization packages (bokeh, e.g.).
