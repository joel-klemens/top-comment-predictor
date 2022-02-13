# Reddit Top Comment Predictor

The goal of this project is to use a neural network to predict what the top comment will be based off of the title of the post.

### To achieve goal

I want to start with a subreddit where the top comments could be more basic (start with r/funny appose to r/askhistorians)

#### Step 1

Gather data from a subreddit to test with.

#### Set up requirements

Tensorflow
GPU capable of using tensorflow gpu (https://www.tensorflow.org/install/gpu)
Follow installation instructions

Anaconda virtual environment running tensorflow gpu
set up instructions (in anaconda prompt):
Create an anaconda environment conda create --name tf_gpu

    Activate the environment: conda activate tf_gpu

    Install tensorflow-GPU conda install tensorflow-gpu

    one set-up you can just start it with "conda activate tf_gpu"

# First test using r/funny

Best loss down to 0.5068 (really good for this model)

#### Seed:

d on the public...
evaluation "this is the most uncomfortable chair i've ever sat in"
magicians are

#### Output:

nothing without their asd catsel on bale at a cam ladtel lore thosghts are hase and asd this gersage is a friendly reminder of the following:

-   absolutely no political content or political figures, regardless of context or focus.

-   absolutely no memes or memetic content of any kind.

-   absolutely no social media screenshots, videos, or other such content.
    a complete breakdown of our rules can be found [here](https://www.reddit.com/r/funny/wiki/rules).

please report rule-breaking content when you see it. thank you!

---

_i am a bot, and this action was performed automatically. please [contact the moderators of this subreddit](/message/compose/?to=/r/funny) if you have any questions or concerns._
dnd af fan if mtiss tige it the home fo a gatter balknar and hotter thae. ever if her aamar saat ie he can's alfand alot htsertment wat memesil lu tand it paserial. toop inken eecose i doure af a grect memhie so bes thu curk kfkeled hamkve she mades a gois the game whis mome wo goteht b

#### First test conclusions

adjust the gather data script to avoid comments that have been stickied. These are always copy paste comments from the moderator bot for the subreddit.

### Test 2

During test one I was quite excited to see that the loss was down to 0.5, however, this was most likely due to the copy paste comments from mod bots.

#### Seed:

spotted at my local mcdonald's. i feel uhhhh... mocked.

#### Output:

ille cot the ham bne the moatirgle loge the hou on has lele cecakend rore he's let a look an thi fame belt thass back and he flen torre clelkr bromnt the sncture ou hong piiher.
thes ald toes aacy and the way hols so geck tour of het was a lookl on of the cmer sith this foreh them in the rasd and hot woalled ly dou tha wookdnt. i tisd nav a fan an the way stolled bnou heme a poouleede white of homd brower if herpsn oe stertre teat you shanler ro back aloont thet i lad access thes trre hnm and they secl. a mart tf mook a looe in and tas to face on hteeast ied and guarer.
i hulk want so the a coer of alnieas in he head thone seine poo soe comw and thu dace to go cace oo hoeda senhe beoaser bno the rase and hom toalky frr the wire and hom wouldlt woong the gouilna wicterert.

gone so soon, rip kid caught me the wianter room. the duutrrealen wanesee to bet inassse dsaleanid. to repe soneengs seougd to met anl the way honn fir tiatever and femdln thes frrnd be thein toone of get a looko

### Get more Data

funny
AskReddit
Wallstreetbets
gaming
movies
science
music
showerthoughts
lifeprotips
books

### test 3 - training patterns used 250k as appose to 14k in previous tests

loss only got down to 1.80483

#### seed:

spotted at my local mcdonald's. i feel uhhhh... mocked.

#### output: it started out really good with little spelling mistakes but quickly went into a loop

i was a computer as a seletiing couid better than the semestire compent of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester

### Test 4 - going to try out some different seeds to see if output can be improved - reduced output to 500 chars

#### Seed:

What is a red flag from an employer that people might not immediately recognize as a red flag?

#### output:

i was a computer and the for of the seme to the only the person of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of

#### Seed:

Official pinning ceremony for promotion to Sergeant. They let you pick where you want to have the ceremony. New Sargeant chose to have it in the swimming pool.

#### output:

i was a computer and the for of the seme to the only the person of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of the semester of

### Test 4 conclusion:

It just outputs the same thing regardless of the seed. Will have to train a new model, maybe additional epochs are needs. Still successful in the fact that there are more recognizable words.

### Test 5

Increase number of epochs, increase batch size
