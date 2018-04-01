# This file will be a place for me to collect notes gained from the fast.ai course.

**cycle_len & cycle_mult**
There's a section that offers a tip regarding the .fit() method for training your model. Jeremy suggests that when you use the following parameters, you get a "pretty good" result just about every time.
`learn.fit(lr, 3, cycle_len=1, cycle_mult=2)`

The 3 denotes the number of cycles (sort of like epochs) for training the model. However, when using the cycle_mult parameter, your cycle is doubled after each epoch, which allows more time for your model to converge and achieve higher accuracy.

**Sidenote** I also found that there's a website for previewing markdown. That will come in handy when working on this project, as well as when proofing other github and jupyter notebook work. 
