<h1>Introduction</h1>

We'll start with an overview of how machine learning models work and how they are used. This may feel basic if you've done statistical modeling or machine learning before. Don't worry, we will progress to building powerful models soon.
This micro-course will have you build models as you go through following scenario:
Your cousin has made millions of dollars speculating on real estate. He's offered to become business partners with you because of your interest in data science. He'll supply the money, and you'll supply models that predict how much various houses are worth.
You ask your cousin how he's predicted real estate values in the past. and he says it is just intuition. But more questioning reveals that he's identified price patterns from houses he has seen in the past, and he uses those patterns to make predictions for new houses he is considering.
Machine learning works the same way. We'll start with a model called the Decision Tree. There are fancier models that give more accurate predictions. But decision trees are easy to understand, and they are the basic building block for some of the best models in data science.

For simplicity, we'll start with the simplest possible decision tree.<br>
![sample1](http://i.imgur.com/7tsb5b1.png) <br>
It divides houses into only two categories.The predicted price for any house under consideration is the historical average price of houses in the same category. We use data to decide how to break the houses into two groups, and then again to determine the predicted price in each group. This step of capturing patterns from data is called <b>fitting</b>or <b>training</b> the model.
The data used to <b>fit</b> the model is called the training data. The details of how the model is fit (e.g. how to split up the data) is complex enough that we will save it for later.
After the model has been fit, you can apply it to new data to predict prices of additional homes.
<Br>
<h1>Improving the Decision Tree </h1> 

Which of the following two decisions trees is more likely to result from fitting the real estate training data? <Br>
![a](http://i.imgur.com/prAjgku.png) <br>
The decision tree on the left (Decision Tree 1) probably makes more sense, because it captures the reality that houses with more bedrooms tend to sell at higher prices than houses with fewer bedrooms. The biggest shortcoming of this model is that it doesn't capture most factors affecting home price, like number of bathrooms, lot size, location, etc.
You can capture more factors using a tree that has more "splits." These are called "deeper" trees. A decision tree that also considers the total size of each house's lot might look like this:
 <br>![b](http://i.imgur.com/R3ywQsR.png) <Br>
You predict the price of any house by tracing through the decision tree, always picking the path corresponding to that house's characteristics. The predicted price for the house is at the bottom of the tree. The point at the bottom where we make a prediction is called a <b>leaf</b>.
The splits and values at the leaves will be determined by the data, so it's time for you to check out the data you will be working with.
