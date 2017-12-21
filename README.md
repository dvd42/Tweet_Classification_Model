# Tweet_Classification_Model
A Tweet Classification Model based on Bayesian Networks

### Synopsis
The purpose of the model is to classify tweets based on the sentiment they express. If it is a sad tweet the class will be Negative(0), otherwise the class will be Positive(1).

With this approach we can classify users or hashtags as Positives or Negatives based on their tweets and retweets. 

The algorithm scans the tweets related to an user or hashtag using a webcrawler and extracts them for classification (only tweets in English will be selected for analysis).

### Requirements
To test the model you will need:
- Anaconda2
- Firefox browser 
- splinter library: pip install splinter  
- Geckodriver: https://github.com/mozilla/geckodriver  
- Lang_detect library: pip install langdetect  
- ntlk library: conda install -c anaconda nltk   

### Installation
0. Install all the required packages listed above
1. Clone this repository
2. Execute `main.py --target @user` or `main.py --target hashtag` (~~`--target #hashtag`~~)
      - Like so: `main.py --target @realdonaldtrump` or `main.py --target tbt`
  

3. There is a more detailed guide indicating some optional parameters inside the repo.
    * If you want to check it out just execute `main.py --help`
    
    
### Results
The **accuracy** classifying a single tweet is around **78%**. If we are evaluating users or hashtags this is a very good accuracy since given 800 tweets only the probability of the model misclassifying 400 of them is around 2.582249878086966e-280. Here we show a couple of examples. 

If you analyze **#sad** you will get:  
Sad is a negative hashtag   
Positive Ratio: 0.16  

If you analyze **#happy** you will get:  
Happy is a positive hashtag  
Positive Ratio: 0.98

### Contribute
If you want to contribute in any way or point out any improvement that can be done to our project feel free to open an issue or contact me at **diegovd0296@gmail.com**.   
Also feel free to train the model with any other tweet related database.
