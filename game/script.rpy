# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define m = Character('Chairman Mao', color="#990000", show_two_window=True, image = "mao")
define l = Character('Lin Biao', color="#19B4E3", show_two_window=True, image = "lin")
define j = Character('Jiang Qing', color = "#FFFF47", show_two_window=True, image = "jiang")
define z = Character('Zhou Enlai', color = "#00CC00", show_two_window=True, image = "zhou")
define k = Character('Henry Kissinger',color = "#B2B2B2", show_two_window=True, image = "kissinger")
define n = Character('Richard Nixon', color = "#0099FF", show_two_window=True, image = "nixon")
define b = Character('Bodyguard', color = "#FFFFFF", show_two_window=True)
define d = Character('Deng Xiaoping', color = "#FF9900", show_two_window=True, image = "deng")

image mao = "images/characters/mao_small.png"
image lin = "images/characters/lin_biao_small.png"
image jiang = "images/characters/jiang_qing_small.png"
image nixon = "images/characters/nixon_small.png"
image deng = "images/characters/deng_xiaoping_small.png"
image kissinger = "images/characters/kissinger_small.png"
image zhou = "images/characters/zhou_enlai_small.png"

image bg bedroom = "images/bg/bedroom.png"
image bg bomb = "images/bg/bomb.jpg"
image bg black = "images/bg/black.jpg"
image bg train = "images/bg/train.jpg"
image bg bodies = "images/bg/bodies.jpg"
image bg tech = "images/bg/tech.jpg"
image bg thanks = "images/thanks.png"

# The game starts here.
label start:

scene bg black

$lin_dead = False

"October 16, 1964"

play sound "sounds/atomic.mp3"
scene bg bomb
with vpunch

"BOOOOOOOOOOOOOOM"

show zhou at left

z "It is a success dear Chairman!"

show lin at right

l "America and Russia do not stand a chance!"

show jiang

j "Now all of the world will fear us!"

hide jiang
hide zhou
hide lin
show mao

m "With this, China has joined the international stage. We have made another great step in the name of the revolution."
m "No longer will America or the Soviets oppress us, China will stand on its own."

stop sound fadeout 1.0

"This was the first successful nuclear test accomplished by the People’s Republic of China."
"It marked the beginning of China becoming a nuclear power and standing equal with the United States and the USSR as an armed nation."
"Up until now, the nation had been led by Mao Zedong, the Great Chairman."
"However, the Chairman's health has and will continue to decline in the coming years, leading him to search for a worthy candidate to take his place after his death."

scene bg bedroom
with fade

"The year is 1970. Forbidden City, China. You are Mao Zedong."
"You have risen from the peasantry of China to become the leader of one of the two powerful Communist nations in the world at the height of the cold war."
"Throughout your struggle you have created many enemies, from the war against Chiang Kai-shek’s Kuomingtang and the economic initiatives of the Five Year Plan and the disastrous Great Leap Forward, as well as the ongoing Cultural Revolution." 

"You know your time is shortly coming to an end. You have had an unhealthy smoking habit for a long part of your life, and have not maintained the best shape as you slowly transformed from Communist commander to Chairman of the People’s Republic of China."
"You’ve felt your life slowly draining away, from difficulty moving to heart pains."
"However, despite the fact that you’re about to pass on, you have yet to definitely name a successor." 

"There are several candidates, all poised to take up the mantle of Chairman."
"They are all old comrades of the Communist Revolution, having been by your side for decades."
"Now, they are all poised against each other, willing to backstab and concoct any lie in order to win your favor."
"It is now up to you to decide who is telling the truth, who is lying, who deserves to lead China from now on."

show lin

l "Chairman Mao! I apologize for disturbing you, but I bring you joyous news regarding Dangfanghong!"

"This man is Lin Biao, the minister of National Defense. He is also currently the second most powerful man in China, the Vice Chairman of the Communist Party of China elected by the 9th Central Committee of the Communist Party of China."
"He has long been an ally of the party, fighting alongside you since the Chinese Civil War in the 1930’s and one of the most successful commanders in China’s historic Long March."

m "What of the Dangfanghong, Lin Biao? I take it by your attitude that the launch of our first satellite was a success?"

l "Yes Chairman! It is a wondrous day for all of China!"

m "Indeed it is Lin Biao. Now we have shown both those stalwart Russians and pesky Americans that China is also capable of space exploration."
m "We are a superpower quickly on the rise Lin Biao! Give Qian Xuesen my regards."

l "Sir, Professor Xuesen said that we should be able to hear the satellite broadcast “The East is Red” for the next 20 days. He gave me a transmitter so we can get the satellite’s radio waves."

m "Well, let us hear our national anthem then, to celebrate China’s advancement towards the stars."

play music "sounds/east_is_red.mp3"
#[The East is Red starts playing quietly]

show lin at left
show jiang at right
with dissolve

j "Chairman Mao, I bring excellent news!"

m "If it is of the satellite, then Comrade Lin Biao here has already informed me of our success in launching to space."

j "Oh, I see. I apologize for being late Chairman." 

"This woman is Jiang Qing, your wife since 1938 and first lady of China. She has been a key leader in the Cultural Revolution, and developed new propaganda such as eight model plays to teach China the struggles of the revolution."

m "Do not be apologize. Let us all bask in the glory of today's success."

j "We would love to join you Dear Chairman, however today there is a meeting of the Central Politiburo. We must maintain the momentum of our Great Proletarian Cultural Revolution after all."

m "Ah yes, of course. I am so forgetful. I’m sorry for keeping you two. I would not want to be the one restraining the revolution, it was my own idea after all!"

l "Of course, Great Leader. I will return with a report immediately after the meeting has adjourned."

m "Please do Lin Biao, I look forward to good news."

hide jiang
with dissolve

hide lin
with dissolve

stop music fadeout 1.0

"6 hours later." 

"*knock*"

l "Great Leader, are you there? The committee meeting has just finished. I have much to report."

m "Yes, come in my Vice Chairman Lin Biao. Tell me of how the revolution goes."

show lin
with dissolve

l "Yes, the meeting started off well. The first issue discussed was the recent border clashes with the Soviet Union."
l "We still fear they may try and seek an opportunity to attack us, so we have bolstered our forces along the Ussuri River in the north."

m "I see. I don’t recall being consulted about this Lin. The army seems to be making lots of movements without my oversight lately."

l "I apologize Dear Leader! I thought time was of the essence in order to not appear weak in front of those Soviets, so I organized the military with utmost urgency in order to scare them off."

m "Well, from now on I would prefer to be informed of the military’s movements so I can provide my own input."

l "Of course Chairman."

m "And what of the rest of the meeting?"

l "Afterwards, I have to say that something...happened."

m "“Something” happened? Well what Lin Biao ?"

l "Madame Jiang made some remarks that brought about great debate in the hall. She accused Chen Boda, her former Propaganda co-head, of colluding with the People’s Liberation Army."
l "She claimed that his attempts to restore the office of State Chairman is an attempt to usurp you, Great Leader, which is ridiculous claim!"
l "Chen only has the nation’s interests at heart, I think Jiang is harboring old grudges from their time at the Propaganda office."

m "I see… You accuse my wife of not having the nation’s interests at heart?"

l "No, not at all Great Chairman. I simply believe she may be trying to find treachery where none exists."
l "She, Zhang Chunqiao, Yao Wenyuan, and Wang Hongwen are seeking to gain power through dubious means."
l "You know he or I would never attempt any sort of betrayal upon you. Do you not remember when we first met? As leader of the First Red Army against the Kuomingtang?"
l "I never questioned your authority. Even when the central Communist party had abandoned you, I never gave up on your ideologies and defended you against those Soviet “advisors.”"
l "I have always had faith in your thoughts on Communism and our great nation."

m "I remember Lin Biao. You have always been a faithful ally to the cause.  I’ll have to talk to Jiang Qing about her conduct."
m "For now you can leave me. Thank you for your report."

hide lin
with dissolve

m "Well Jiang Qing, what do you have to say about this?"

#-Jiang Qing emerges from back-
show jiang
with dissolve

j "It is as I told you Chairman. Lin Biao is seeking to raise his own power using the PLA (People’s Liberation Army)."
j "He organized the military without your involvement, does that not demonstrate to you how much power he has started to wield?"
j "Chen Boda is also looking to bring back the position of State Chairman. That’s the same position you once held as head of our state!"
j "Can you not see he’s trying to usurp your power?!"

menu:
    "“Calm down, Jiang Qing. Lin Biao is doing nothing of the sort. I think you’re mistaken.”":
        jump lin_biao_approve
    "“You may be right Jiang Qing. I see your point. Lin Biao has been making very suspicious moves lately.”":
        jump jiang_qing_approve

label lin_biao_approve:
    m "Lin Biao has always been loyal to me and my leadership."
    m "When I was thrown out by the central Communist command during the Chinese Civil War, his army was one of the few that supported me and accompanied me on the Long March so I could gain the leadership I have now."
    m "To accuse  him of treachery is a grave accusation, I hope you understand this Jiang Qing."
    m "Even if you are my wife I have no sympathy for those who seek to gain power using false statements."
    m "You and your “Gang of Four”, Zhang Chunqiao, Yao Wenyuan, and Wang Hongwen, have quickly risen through the ranks of the Communist party to sit at the Politburo."
    m "However, I suggest it might be time for some self-reflection as to how you’ve gotten to where you are and to control your ambitions."

    j "... I see Chairman. I apologize for my outlandish statements. I see now that I was definitely in the wrong."

    m "I’m glad you’ve seen the errors of your ways. I hope the “Gang of Four” will share with the rest of the committee these transgressions which you have committed."
    m "I’m sure it would help other Politburo members avoid the same mistakes and strengthen the party as a whole, allowing us to better pursue our goal of revolution to purge capitalism from our country and reaffirm China’s political ideology."
    
    hide jiang
    with fade

    $lin_biao = 1
    $jiang_qing = 0


    jump resume

label jiang_qing_approve:
    m "Lin Biao has always been a quiet man by my side and has always appeared to support me."
    m "However I have heard that he has made not so flattering remarks about me in private."
    m "I never took them seriously, but I have always wondered whether he actually believes in my theories and conclusions regarding Communism in China, or has only supported me as a method to gain power."
    m "Ever since he’s been named as Vice Chairman, he seems to have become actively making decisions without consulting me. Chen Boda has also been throwing a lot of support behind Lin Biao."
    m "I don’t understand why Boda wants reinstitute the State Chairman position.  I’ve never liked the position of State Chairman ever since that traitor Liu Shaoqi held the post."
    m "No one is suited to be State Chairman, not even me. Lin seems to have found himself questionable allies."

    j "I most certainly agree Chairman. Did I tell you that Chen Boda today went on a tirade against Zhang Chunqiao?"

    m "Zhang Chunqiao!? One of my most ardent followers of the Cultural Revolution?! How dare he!"
    m "To criticize Zhang is to criticize the revolution itself. And to criticize the revolution is to criticize me!"
    m "Lin Biao has made some foolish allies."

    j "And what of him moving the PLA without your permission?"

    m "How dare he! The soldiers are the backbone of this country and if he is to declare a state of war without my consultation then he has gotten too greedy with power."
    m "The PLA cannot be allowed to gain too much influence, especially if war is to break out. The generals in the politburo must be shown their place. Military might is not everything."

    j "Well said, Chairman Mao."

    m "I must have Chen Boda removed from the committee, and Lin Biao must come to see the errors of his allegiances."
    m "He has started to think himself too high in command, and needs to be reminded that I am the one who is at the top."
    m "I must reconsider whether he should continue to be Vice Chairman. Perhaps I was misguided in advocating for him."
    m "I might have been deceived the whole time…"

    j "I shall take my leave for now, so you may ponder these issues further."
    j "I am glad I have been helpful in having you see the dangers of Lin Biao and his followers."

    m "Thank you Jiang Qing, my great wife dedicated to the cause."

    hide jiang
    with fade

    $jiang_qing = 1
    $lin_biao = 0

scene bg bedroom
with wipeleft

label resume:

show zhou
with dissolve

z "Chairman Mao, I hope I do not find you at a bad time. I have an important matter to discuss with you."

"Zhou Enlai is the Premier of the People’s Republic of China ever since its founding in 1949. A very pragmatic individual, he was always the first to see where the tides of power went and was quick to follow."
"A loyal Chinese Communist member since the 1920’s, he is one of the most respected and talented of all the individuals working for the Chinese Communist Party."

m "Not at all, Comrade Zhou. I always have time for one of my longest and oldest allies. What is it?"

z "Please allow me to first check the room. I have something of the utmost importance to tell you that must not be heard by outside ears."

m "Of course."

"*Zhou paces around the room, closing doors and windows*"

z "I just recently received a communication from President Yayah Khan of Pakistan. As you are aware we signed several agreements to supply Pakistan with armaments in future months to aid in their development."
z "In passing mention he said that he was visiting America several months prior, and that President Nixon was thinking about reestablishing contact with us."
z "They wish to send an envoy in secret to discuss the problems we have with one another."
z "As you know we have had disagreements with the Americans in the past, but I think now would be a good time to establish relations with them."
z "It would be a blow to the Soviets to show we have such a powerful ally. As it stands they are harassing our borders almost daily."
z "With the United States at our side they would have to stop encroaching on our territory. And as it stands, America seems to have given up on taking land in Asia, backing out of Vietnam and lightening their trade restrictions with us."
z "What do you think Great Chairman, would you accept a visit from an American envoy to begin negotiations of diplomatic relations with them?"

m "Leave me to ponder this for a moment Zhou. This is not something that should be hastily decided."

z "Of course Great Leader."

hide zhou
with dissolve

if lin_biao == 1: 
    m "*telephone* Please summon Lin Biao to my quarters."
    $t = l
    $speaker = "Lin Biao"
elif jiang_qing == 1:
    m "*telephone* Please summon Jiang Qing to my quarters."
    $t = j
    $speaker = "Jiang Qing"

"Operator" "At once Chairman."

if t == j:
    show jiang
    with dissolve

if t == l:
    show lin
    with dissolve

t "You wished to see me Chairman?"

m "Yes. Prime Minister Zhou Enlai just recently came to me with some very intriguing news. He told me that the Americans are interested in establishing relations with us and wish to have a secret meeting to discuss a possible visit from the President of the United States."
m "I have called on you here to see what you think."

t "I think this is a ridiculous request, Great Leader. What do we have to gain from allying with America? They only seek to infiltrate us, to make us seem like a weaker power."
t "We have an atomic bomb, we are just as powerful as them or Moscow. Our military might is unparalleled! We must stand firm to demonstrate to the Americans that we our own superpower."
t "Even the Russians are already too afraid of us. All they can do is beat their chests along the border, fearing any sort of invasion as they know we will defeat them."
t "If we invite America to our shores, we will be admitting that we need help to stave off the Russians. Besides, America has never done anything for us."
t "Starting wars in both Korea and Vietnam, funding Chiang Kai-shek and his traitorous army, they have tried to tear us down multiple times, and now seek to reciprocate?"
t "I would not trust any words coming from them, Dear Chairman. This must be some sort of ploy; we cannot fall into their hands."
t "Zhou Enlai simply wants to work with the Americans as he is a filthy moderate. He is not truly committed to the Maoist ways!"
t "Even as the Red Guard sought to destroy the old Chinese traditions, he convinced them to spare the Forbidden City, the oldest of all Chinese cities!"
t "How can we move into the future if Zhou allows the past to haunt us?"

m "Thank you for your advice [speaker]. Your opinion does not go unheard. Please leave me while I talk to Zhou Enlai about my decision."

t "Of course Dear Leader."

if t == j:
    hide jiang
    with fade

if t == l:
    hide lin
    with fade

show zhou
with dissolve

z "I heard you had reached a decision Chairman?"
m "Yes Zhou. After hearing differing opinions, I believe I have."

menu: 
    "“I see the value of allying with America, Premier Zhou.”":
        jump ally
    "“I do not think the time is right.”":
        jump not_time

label ally:
m "These are all good points Zhou Enlai. I do believe that becoming closer with the Americans can only benefit us."
m "President Nixon expressing his wishes to normalize relations is certainly a step in the right direction."
m "To think we have made the Americans come to us! Truly they are starting to recognize us as a world power."
m "Now that we can make even America see the glory of the People’s Republic of China, soon other Western nations will come around to see the success of Communism."
m "With this, we can expand our economic influence."

z "I am glad you agree Chairman. It seems like the Americans wish to send their National Security Advisor Henry Kissinger."
z "I have heard of his policy called “detente”, which supposedly involves a relaxation of our strained relations."
z "In accordance with this policy both the Americans and the Soviets have held discussions regarding reducing their nuclear armaments."

m "And it seems like we are to be next on America’s list. Well, let them come."

z "Understood Chairman, I shall let the Americans know accordingly."

hide zhou
with fade

jump kissinger

label not_time:

m "Ally with the Americans? Is this some sort of joke Zhou? The Americans stand against everything we have struggled for."
m "They are the embodiment of capitalism, and have tried multiple times to bring down our Republic."
m "From the Korean War to the Vietnam War all they have done is meddle in Asian affairs in their pursuit to “contain” communism."
m "I see no benefit into giving into the pressure of the United States. It would be like surrendering and admitting that our revolution is wrong."
m "That China needs the help of the West to succeed."

z "I understand your viewpoint Chairman. However this new Nixon fellow seems to have a different point of view than previous leaders, he genuinely wants to meet on equal terms."
z "They have already began to lift economic embargoes they had placed on us which has brought much profit to merchants and boosted our GDP."
z "I feel like we have much to gain from this proposal."

m "Comrade Zhou, you have done much for the Cultural Revolution and for our country until now. I appreciate it immensely."
m "Sometimes I think this country would not be standing as well as it is now were it not for you."
m "However, for you to advocate for meeting with America is not something I could say would be healthy for our cause."
m "They have at multiple turns tried to destroy us, and now you suggest allying with them? This is a preposterous request. China can survive on its own!"

z "I'm sorry for offending you Chairman. I see the error of recommending cooperation with the Americans and will take time to reflect on my thoughts from now on."

jump not_america

label kissinger:

"*murmuring outside door*"

k "This is the Chairman’s room? Is he well enough to see me?"

z "Yes, the Chairman is in excellent health. Do not worry, although he may be old he is sturdy."

#*door opens*
show zhou
with dissolve

z "Great Leader, I have brought Henry Kissinger. The U.S. ambassador here to negotiate a visit." 

show zhou at left
show kissinger at right
with dissolve

m "It is good to meet you, Mr. Kissinger. I have heard much about you from the papers. You look just as impressive as they make you out to be."

k "To hear that from the Great Chairman of China is certainly an honor. Reports of your illness seem to be heavily exaggerated, you look very well for a man of your age."

m "Thank you Mr Kissinger, but do not let appearances fool you. I am not as healthy as I appear, haha. It is simply a matter of time."
m "But let us not fret about such things, you are here for business yes? It has been a long time since we’ve had an American politician on our shores."

k "Yes, it has been too long in fact. I am here today to see if we might change that. I’ve been sent directly by President Nixon to see if we might arrange a visit of some sort."
k "The President has long been interested in normalizing relations between China and America." 

m "What should I make of those wars that occurred on China’s borders?"

k "Those were the views of an older America. One rooted in an irrational fear of “containment.” The President’s new policy is one of openness."

m "So this President says. Who knows what the next one will believe."

k "I assure you Chairman, if you make good terms with the President now, it will be very difficult for the next one to undo the groundwork we lay."
k "Once the wheels are in motion they will only continue to keep turning."

m "I trust you know your politics much more than I do Mr. Kissinger. Very well, I agree to meet your President Nixon in the coming months."

hide zhou with dissolve

hide kissinger
with fade

$met_usa = True

if lin_biao == 0:
    jump betrayal
else:
    jump nixon

label betrayal:

show lin
with fade

l "Great Leader, I wish to speak with you at once."

m "Lin Biao, what could be so urgent?"

l "I heard you agreed to meet with the Americans? What is the meaning of this? This will surely lead us to ruin!"

m "I assure you Lin Biao that I did not make this decision lightly. Are you questioning my authority?"
m "By accepting the Americans’ offer of communication we will be able to expand our economy, as well as disperse of the Russians on our border."

l "But at what cost Chairman! Our independence? What of China being the leader of the third world, of becoming a superpower in its own right?"
l "What of all the training of the military? For what purpose did we create a nuclear bomb, if not to stand even with America and Russia?"
l "Now we’ll just become an American colony as we were a British colony before. In the end, the army is everything."

m "Do you believe I would simply abandon the progress China has made to ally with the Americans?"
m "Do you think I would give up the China I’ve created?"
m "Your insanity knows no bounds Lin. Have you taken your pills today?"
m "I believe you need to reevaluate your own commitment to the party. If you cannot trust me to lead, then I should think you might be getting over ambitious."
m "Ambition is dangerous Vice Premier Biao. And no, the people are everything Lin Biao."
m "Communism is based off the people, not the army. The party controls the gun, not the gun the party."

l "I apologize for speaking out of turn Chairman. I am obviously misguided in my assessment of the situation."
l "Of course the Chairman knows best, and I trust you to lead. I would never dream of taking China from our Great Leader."

m "Leave me, Lin Biao."

l "At once Chairman. Please forgive me."

hide lin
with dissolve

scene bg train
with wipeleft

"Sept 11, 1971"

"Mao Zedong left in August 1971 to discuss the possibility of purging Lin Biao from the Communist party after his displays of ambition of power and a general lack of trust in the man as Vice Chairman."

"On a train back from southern China:"

b "Chairman! You must escape at once! It is not safe here."

m "What has happened?"

b "We have just heard news that the other train you were initially scheduled to take back from Shanghai had a gunman targeting it."
b "We have no idea if it safe on this train any longer. We must switch to a different mode of transportation."

m "Another threat upon my life? I wonder which old enemy it is this time."

b "By our preliminary reports Chairman, it seems the orchestrator is from the military. Specifically from the Air Force base in Shanghai."

m "The Air Force? Isn’t that where Lin Biao’s son, Lin Liguo is a commander?"
m "I guess Lin Biao has let his ambition consume him."

b "We will apprehend the culprit at once."

m "Excellent."

scene bg bedroom
with wipeleft

"*several days later*"

show zhou

z "Chairman Mao, I have news regarding the attempt on your life that occurred two days ago."
z "Lin Biao and his son, Lin Liguo have been found to be perpetrators. They have admitted their own guilt by attempting to escape."
z "This morning, Lin Biao, his wife Ye Qun, Lin Liguo, were all found dead at a plane crash in Mongolia."
z "It seems as if they did not have enough fuel on the plane and were forced to make an emergency landing, killing them all."

m "I see. Have we confirmed they were truly on board and no decoys of some sort?"

z "No. The Mongolian authorities unfortunately buried them on site, but they found an ID card belonging to Lin Liguo so I think we can safely assume they are all dead."

m "Wanton ambition consumes another soul."
m "If the fool had simply heeded my advice and not tried to grab more power than he could handle, he would have not found himself in this situation."

z "Regrettable indeed, Dear Chairman."

m "Oh well, I guess this means I must seek a different successor to Vice Chairman. One more deserving and understanding of my policies."

hide zhou with fade

scene bg black
with wipeleft

$lin_dead = True

label nixon:

"February 21, 1972"

scene bg bedroom
with wipeleft

show zhou
with dissolve

z "Chairman Mao, I am here to report that President Nixon has just arrived in Beijing." 

m "Excellent Zhou. Would you please go and fetch him for a visit to my quarters?"

z "Most immediately sir. I’m sure he will be honored to have an audience with the Chairman."

n "This is the Chairman’s room?"

z "Yes Mr. President, if you’ll please come in."

#Nixon, Kissinger, Zhou enter room.
show zhou at left

show nixon
with dissolve

show kissinger at right
with dissolve

#*actual transcript of what happened*

z "Great Chairman, this is the President of the United States, Richard Nixon."

n "It is an honor to meet you after so long Chairman. I’ve heard you read a great deal. The Prime Minister said that you read more than he does."

m "Yesterday in the airplane you put forward a very difficult problem for us. You said that what it is required to talk about are philosophic problems, not Taiwan."

n "I said that because I have read the Chairman’s poems and speeches, and I know he was a professional philosopher. (Chinese laugh.)"

m "Kissinger is a doctor of philosophy?"

n "He is a doctor of brains."

m "What about asking him to be the main speaker today?"

n "He is an expert in philosophy."

k "I used to assign the Chairman’s collective writings to my classes at Harvard."

m "Those writings of mine aren’t anything. There is nothing instructive in what I wrote."

n "The Chairman’s writings moved a nation and have changed the world."

m "I haven’t been able to change it. I’ve only been able to change a few places in the vicinity of Peking."
m "Our common old friend, Generalissimo Chiang Kai-shek, doesn’t approve of this. He calls us communist bandits. He recently issued a speech. Have you seen it?"

n "Chiang Kai-shek calls the Chairman a bandit. What does the Chairman call Chiang Kai-shek?"

z "In the newspapers sometimes we call him a bandit; we are also called bandits in turn. Anyway, we abuse each other."

m "Actually, the history of our friendship with him is much longer than the history of your friendship with him."

n "Yes, I know."

m "We two must not monopolize the whole show. It won’t do if we don’t let Dr. Kissinger have a say. You have been famous about your trips to China."

k "It was the President who set the direction and worked out the plan."

n "He is a very wise assistant to say it that way."

m "He is praising you, saying you are clever in doing so."

n "He doesn’t look like a secret agent. He is the only man in captivity who could go to Paris 12 times and Peking once and no one knew it, except possibly a couple of pretty girls."

k "They didn’t know it; I used it as a cover."

m "In Paris?"

n "Anyone who uses pretty girls as a cover must be the greatest diplomat of all time."

m "So your girls are very often made use of?"

n "His girls, not mine. It would get me into great trouble if I used girls as a cover."

z "Haha, especially during elections. Dr. Kissinger doesn’t run for President because he wasn’t born a citizen of the United States."

m "It would be very dangerous if you have such a candidate. But let us speak the truth. As for the Democratic Party, if they come into office again, we cannot avoid contacting them."

n "We understand. We will hope that we don’t give you that problem."

m "Those questions are not questions to be discussed in my place. They should be discussed with the Premier."
m "I discuss the philosophical questions. That is to say, I voted for you during your election."
m "There is an American here called Mr. Frank Coe, and he wrote an article precisely at the time when your country was in havoc, during your last electoral campaign."
m "He said you were going to be elected President. I appreciated that article very much."

n "When the Chairman says he voted for me, he voted for the lesser of two evils."

m "I like rightists. People say you are rightists, that the Republican Party is to the right, that Prime Minister Heath of the UK is also to the right."

n "And General DeGaulle of France."

m "DeGaulle is a different question. They also say the Christian Democratic Party of West Germany is also to the right."
m "I am comparatively happy when these people on the right come into power."

n "I think the important thing to note is that in America, at least at this time, those on the right can do what those on the left talk about."

k "There is another point, Mr. President. Those on the left are pro-Soviet and would not encourage a move toward the People’s Republic, and in fact criticize you on those grounds."

m "Exactly that. Some are opposing you. In our country also there was a reactionary group which is opposed to our contact with you."
m "The result was that they got on an airplane and fled abroad."

z "Maybe you know about this."

m "Throughout the whole world, the U.S. intelligence reports are comparatively accurate. As for the Soviet Union, they finally went to dig out the corpses, but they didn’t say anything about it."

z "In Outer Mongolia."

n "We had similar problems recently in the crisis between India and Pakistan. The American left criticized me very heavily for failing to side with India."
n "This was for two reasons: they were pro-Indian and they were pro-Soviet."
n "I thought it was important to look at the bigger issue. We could not let a country, no matter how big, gobble up its neighbor."
n "It cost – I don’t say this with sorrow because it was right – it cost me politically, but I think history will record that it was the right thing to do."

m "As a suggestion, may I suggest that you do a little less briefing? Do you think it is good if you brief others on what we talk about, our philosophic discussions here?"

n "The Chairman can be sure that whatever we discuss, or whatever I and the Prime Minister discuss, nothing goes beyond the room."
n "That is the only way to have conversations at the highest level."

m "That’s good."

n "For example, I hope to talk with the Prime Minister and later with the Chairman about issues like Taiwan, Vietnam and Korea."
n "I also want to talk about— and this is very sensitive — the future of Japan, the future of the subcontinent, and what India’s role with be; and on the broader world scene, the future of US-Soviet relations."
n "Because only if we see the whole picture of the world and the great forces that move the world will we be able to make the right decisions about the immediate and urgent problems that always completely dominate our vision."

m "All those troublesome problems I don’t want to get into very much. I think your topic is better—philosophic questions."

n "For example, Mr. Chairman, it is interesting to note that most nations would approve of this meeting, but the Soviets disapprove, the Japanese have doubts which they express,"
n "and the Indians disapprove. So we must examine why, and determine how our policies should develop to deal with the whole world, as well as the immediate problems such as Korea, Vietnam, and of course, Taiwan."

m "Yes, I agree."

n "We, for example, must ask ourselves—again in the confines of this room—why the Soviets have more forces on the border facing you than on the border facing Western Europe."
n "We must ask ourselves, what is the future of Japan? Is it better — here I know we have disagreements — is it better for Japan to be neutral, totally defenseless, or is it better for a time for Japan to have some relations with the United States?"
n "The point being — I am talking now in the realm of philosophy — in international relations there are no good choices."
n "One thing is sure — we can leave no vacuums, because they can be filled. The Prime Minister, for example, has pointed out that the United States reaches out its hands and that the Soviet Union reaches out its hands."
n "The question is which danger the People’s Republic faces, whether it is the danger of American aggression or Soviet aggression."
n "There are hard questions, but we have to discuss them."

m "At the present time, the question of aggression from the United States or aggression from China is relatively small; that is, it could be said that this is not a major issue, because the present situation is one in which a state of war does not exist between our two countries."
m "You want you to withdraw some of your troops back on your soil; ours do not go abroad."
m "The former President of Pakistan introduced President Nixon to us. At that time, our Ambassador to Pakistan refused to agree on our having a contact with you."
m "He said it should be compared to whether President Johnson or President Nixon would be better. But President Khan said the two men cannot be compared, that these two men are incomparable."
m "He said that one was like a gangster — he meant President Johnson. I don’t know how he got that impression. We on our side were not very happy with that President either."
m "We were not very happy with your former Presidents, beginning with Truman and through Johnson. We were not very happy with these Presidents, Truman and Johnson."
m "In between there were eight years of Republican presidents. During that period probably you hadn’t thought things out either."

z "The main thing was John Foster Dulles’ containment policy."

m "Zhou also discussed this with Dr. Kissinger before."

n "But those two shook hands."

z "Haha!"

m "Do you have anything to say, Doctor?"

k "Mr. Chairman, the world situation has also changed dramatically during that period. We’ve had to learn a great deal. We thought all socialist/communist states were the same phenomenon."
k "We didn’t understand until the President came into office the different nature of revolution in China and the way revolution had developed in other socialist states."

n "Mr. Chairman, I am aware of the fact that over a period of years my position with regard to the People’s Republic was one that the Chairman and Prime Minister totally disagreed with."
n "What brings us together is a recognition of a new situation in the world and a recognition on our part that what is important is not a nation’s internal political philosophy."
n "What is important is its policy toward the rest of the world and toward us. That is why — this point I think can be said to be honest  — we have differences."
n "The Prime Minister and Dr. Kissinger discussed these differences."
n "It also should be said—looking at the two great powers, the United States and China—we know China doesn’t threaten the territory of the United States; I think you know the United States has no territorial designs on China."
n "We know China doesn’t want to dominate the United States. We believe you too realize the United States doesn’t want to dominate the world."
n "Also — maybe you don’t believe this, but I do — neither China nor the United States, both great nations, want to dominate the world." 
n "Because our attitudes are the same on these two issues, we don’t threaten each others’ territories."
n "Therefore, we can find common ground, despite our differences, to build a world structure in which both can be safe to develop in our own way on our own roads."
n "That cannot be said about some other nations in the world."

m "Neither do we threaten Japan or South Korea."

n "Nor any country. Nor do we."

m "Zhou, do you think we have covered enough today?"

n "Yes. I would like to say as we finish, Mr. Chairman, we know you and the Prime Minister have taken great risks in inviting us here. For us also it was a difficult decision."
n "But having read some of the Chairman’s statements, I know he is one who sees when an opportunity comes, that you must seize the hour and seize the day."
n "I would also like to say in a personal sense – and this to you Mr. Prime Minister — you do not know me."
n "Since you do not know me, you shouldn’t trust me. You will find I never say something I cannot do. And I always will do more than I can say."
n "On this basis I want to have frank talks with the Chairman and, of course, with the Prime Minister."

m "“Seize the hour and seize the day.” I think that, generally speaking, people like me sound a lot of big cannons."
m "That is, things like “the whole world should unite and defeat imperialism, revisionism, and all reactionaries, and establish socialism.”"

n "Like me. And bandits."

m "But perhaps you as an individual may not be among those to be overthrown. They say that Dr. Kissinger is also among those not to be overthrown personally."
m "And if all of you are overthrown we wouldn’t have any more friends left."

n "Mr. Chairman, the Chairman’s life is well-known to all of us. He came from a very poor family to the top of the most populous nation in the world, a great nation."
n "My background is not so well known. I also came from a very poor family, and to the top of a very great nation. History has brought us together."
n "The question is whether we, with different philosophies, but both with feet on the ground, and having come from the people, can make a breakthrough that will serve not just China and America, but the whole world in the years ahead."
n "And that is why we are here."

m "Your book, “The Six Crises,” is not a bad book."

n "You read too much."

m "Too little. I don’t know much about the United States. I must ask you to send some teachers here, mainly teachers of history and geography."

n "That’s good, the best."

m "That’s what I said to Mr. Edgar Snow, the correspondent who passed away a few days ago."

n "That was very sad."

m "I am afraid I feel unwell. We should probably stop this conversation now."

n "You look good Mr. Chairman. I understand. I was a great honor to meet and talk with you."

m "Ah buy appearances are deceiving Mr. President. It was an honor to meet you too. I hope Zhou takes good care of you on the rest of your trip."

z "Rest assured I will Chairman."

m "Farewell then Doctor Kissinger and President Nixon."

n "Goodbye Mr. Chairman. Stay in good health."

k "I hope to see you again soon."

z "Please follow me."

hide zhou
with dissolve

hide kissinger
with dissolve

hide nixon
with dissolve

jump zhou_deng

label not_america:

show lin
with dissolve

l "I am glad you were inclined to agree with my reasoning Chairman."

m "China should never have to rely on America or Russia in order to advance it’s interests."
m "These China I lead will be independent, and a model to other nations on how to gain power by your own hands."

l "On that note Chairman, do you not think it might be appropriate to start leading other nations?"
l "The Americans have NATO and the Russians the Warsaw Pact, why do we, China, not have an alliance with other nations?"

m "This is an interesting proposition Lin Biao. And who exactly do you believe should we ally with an lead into the new world as a third superpower?"
 
l "I would think the obvious choices are the recently troubled nations to our South."
l "The Americans have long been meddling in Southeast Asian affairs and I believe it is China’s duty to prevent America from running their affairs and creating war."

m "I would assume then you mean Cambodia, Vietnam, and Laos then?"

l "Yes, these are all countries whose people share some of the ideologies preached by Chairman Mao, and I believe we can help them achieve the revolution in their states and kick out the imperialist United States."

m "I would like to see America leave those Asian countries alone and let them govern themselves."

l "In addition to these nations, I think Pakistan might also be a useful ally."

m "Pakistan? Why do you say that Lin Biao. Are they not closely tied to the Americans?"

l "True, but we have an armament agreement with them and clearly the Americans see us and Pakistan as close allies. We may as well take advantage of this."
l "Plus having Pakistan on our side could help us build ties in the middle east as well."

m "A daring proposition Lin Biao."

l "Daring perhaps, but China will not grow without taking risks. Much like your Great Leap Forward and Cultural Revolution, the risk allowed the nation to progress towards the Chairman’s ideal."
l "I foresee China as being a leader of the third world, the nations abandoned by both Russia and America can stand united against them under a Chinese banner."
l "China can prevent the continued exploitation of the third world."

m "Sounds like you have studied my Three Worlds Theory extensively Lin. This certainly does seem like a worthy avenue to explore."
m "Let us get in contact with Tôn Đức Thắng, the Khmer Rouge,  and Yahya Khan to discuss this matter in depth."

l "I will do so at once Chairman."

hide lin
with dissolve

$lin_dead = False

label zhou_deng:

"June, 1973"

"*knock*"

z "Chairman, may I have a moment?"

m "Come in Zhou Enlai, what do you require?"

show zhou
with dissolve

z "I have most regrettable news. I know you are aware that I have been in and out of the hospital lately."

m "Yes I am aware, have they discovered what "
m "Well, out with it. What did he diagnose you with?"

z "It appears to be cancer, Chairman. I am not long for this world."

m "Nonsense Zhou! You of all people know how long I've been ill, and I'm still here leading China."

z "I cannot hope to measure up to the livelihood of the Great Chairman. In the light of this news, I would like to discuss the possibility of having a successor in  the event of my death."

m "A successor? Who in all of China could ever be worthy enough to inherit your legacy Prime Minister?"

z "I believe Deng Xiaoping would be a good consideration as Vice Premier."

m "Deng Xiaoping? The man I sent to out to take care of the tractors out in Jiangxi province?"

z "Yes. Comrade Deng has spent his time after being purged writing many reflections on his mistakes during the Cultural Revolution."
z "As of now, he has stacks of papers detailing his folly in not adhering to Maoist thought."

m "I see. Well if he comes with your recommendation Zhou he must have made a great impression upon you."
m "You may rehabilitate him as you wish. I trust your decision in this matter."

z "Thank you Chairman. I will place him as Vice Premier to oversee daily duties. I am confident he will be useful for the party."

hide zhou
with dissolve

label zhou_death:

"January 8, 1976"

show deng
with dissolve

d "I am sorry to disturb you Chairman, but I come bearing most dire news."

m "What is it, Vice Premier Xiaoping?"

d "As you’ve been aware, our great Prime Minister Zhao Enlai has been in the hospital the past few days due to the advancement of his bladder cancer."
d "Well this morning we received terrible news:"
d "Prime Minister Zhou Enlai has passed away."

m "I see."
m "The nation has lost one of its greatest public servants."
m "We will have to find a new Prime Minister quickly then."

d "I will see to the arrangement of his funeral services."

hide deng
with dissolve

scene bg black
with wipeleft

"April 4, 1976"

"Today is the evening of Qingming Festival, where Chinese pay homage to deceased ancestors."
"In honor of the late Prime Minister, Zhou Enlai, thousands of Chinese have gathered in Tiananmen Square, at the Monument to the People’s Heroes."
"Mourners have been placing memoirs, poems, and wreaths praising Zhou Enlai and his long life of work for China."

scene bg bedroom
with fade

if lin_dead == False:
    show lin at left

show jiang
with vpunch

j "Chairman, Chairman, there is a great gathering outside."
j "They are all singing praise of Zhou Enlai."
j "I do not believe you should let this continue, dear Chairman."
j "The eulogies that the people are leaving, they are direct attacks upon the current government."
j "They bring into question our loyalty to the nation, and have even claimed the Cultural Revolution a failure."
j "This is nothing short of an anti-government protest!"
j "We cannot let this go on. There are thousands signing praise of Zhou Enlai."
j "You know that he was nothing but a moderate who never truly believed in your ideals."

m "Please slow down Jiang Qing."
m "I do agree that the demonstrations in Tiananmen Square are disconcerting."
m "And Zhou Enlai never truly revealed his ideologies to me. But he was a loyal worker to the state."

show deng at right
with dissolve

d "Exactly Chairman Mao! I'm sorry to disturb, but I could not help but interrupt after hearing Jiang Qing."
d "Those gathered in the square are simply patriots dedicated to honoring a loyal member of the revolution."
d "Zhou Enlai was not a traitor, he helped ensure that China could get to where it is today."

j "Shut up you puppet of Zhou! You're only here because he took pity on you."
j "As if we need another moderate in the government."
j "It's because of you that we've been lacking behind the Americans lately!"
j "They continue to advance in science and technology while we languish!"

d "Please Jiang Qing, do not speak as if you understand international politics or recent technological advancements."
d "You are merely a propoganda officer, nothing more."
d "What do you understand of running a country, like Zhou Enlai did?"

m "Enough! Stop bickering. We are discussing what to do with the demonstrators in the plaza."

j "I apologize Chairman. Anyway, it is as I said. The demonstrators are nothing more than thinly veiled traitors."
j "We cannot allow them to stay in Tiananmen Square any longer to defame our revolution."
j "We should evict them immediately. Using force if need to be, to show our regime will not stand for open rebellion."

d "Jiang Qing, you are being ridiculous."
d "These people aren't protesters. They're citizens demonstrating their loyalty to a leading member of the party."
d "It would be no different if you, Jiang Qing, where to die. I imagine you would want the people to mourn your death as well."
d "Do I sense some jealousy over how popular Zhou Enlai seems to be?"

j "Don't be ridiculous Deng Xiaoping."

d "We should allow the protesters to have their voice."
d "If we do not listen to the people, we will never change to what they want."
d "The people are the ones who make up a nation."
d "If we do not listen to their concerns, we will very soon find ourselves at their mercy."
d "They wish to honor Zhou Enlai and want to ensure the efforts he made for China are not forgotten and that his legacy is continued."

if lin_dead == False:
    l "We need to demonstrate the military might to the people."
    l "They will understand that the nation will not tolerate this insolence towards Mao and China."
    l "If we allow the citizens to protest on our front door, it will show the rest of the world our government is weak, and may leave us open to attack from within."
    l "Thus we must give a strong showing Chairman."

j "I propose a somewhat more peaceful suggestion, let us wait until the protesters leave for the night and remove their mementos."
j "This avoids a confrontation with the protesters but still allows us to get our message across. The protesters’ message cannot be allowed to propagate."
j "We should ban all imagery of Zhou Enlai, and cannot let his mourning to be so open."

if lin_dead == False:
    menu:
        "“Deng is correct.”":
            jump peace
        "“Lin Biao, you are right.”":
                jump force
        "“Jiang Qing, you have a valid point.":
            jump prop
else:
    menu:
        "“Deng is correct.”":
            jump peace
        "“Jiang Qing, you have a valid point.":
            jump prop

label peace:

m "Deng is correct. Zhou was a great man who helped me build this nation up to where it is now, and I never questioned his good intentions for the country."

j "Are you mad Chairman? This will lead to our downfall. All of them out there are counter revolutionaries!"

m "Jiang Qing, at one point I was a counterrevolutionary. I should hear what the people have to say and take their concerns into consideration."
m "I am a leader from a different time."
m "Zhou helped my ideas remain relevant through the years, and now I should listen to what Zhou’s followers think should be the next step."

d "This is a very wise decision Chairman. I am humbled at how stoic our Chairman is and how he is willing to listen to the common man."

m "Of course I am Deng. A nation is built upon by its people."
m "If I do not listen to the people what sort of leader am I?"

"Following this conversation, Mao invited the protesters to leave their comments towards the government and sentiments toward Zhou Enlai."
"Deng Xiaoping sat with several of the protesters to listen to their concerns. He then passed those ideas along to Mao."
"Deng also gave a speech to memorialize Zhou to the protesters."

d "He was open and aboveboard, paid attention to the interests of the whole, observed Party discipline, was strict in \"dissecting\" himself and good at uniting the mass of cadres, and upheld the unity and solidarity of the Party."
d "He maintained broad and close ties with the masses and showed boundless warmheartedness towards all comrades and the people...."
d "We should learn from his fine style – being modest and prudent, unassuming and approachable, setting an example by his conduct, and living in a plain and hard-working way."
d "We should follow his example of adhering to the proletarian style and opposing the bourgeois style of life."

hide deng
hide lin
hide jiang

scene bg tech

"Under Deng Xiaoping’s guidance, China began to embrace the West more, inviting Kissinger back for more talks and gradual opening up to West."
"With America’s help, more teachers and educators were sent to universities within China, much like efforts from the Self Strengthening Movement of late 1880’s China."
"With these educators, China quickly propelled itself into a more scientific and technological society, going on to become launch more space satellites and begin to develop computers."
"After Mao’s death on September 6, Deng naturally took up leadership due to massive support of the people he had."
"Ties with the United States continued to improve, and collaboration between the two nations led China to develop its economy rapidly to the levels its at today in the 1990’s."
"Then China quickly began to innovate instead of merely copy, creating technical giants such as Xiami, Baidu, and Weibo which became international hits and not just Chinese products for the Chinese."
"However, Deng was not willing to relinquish all power and the government still operates much as it does today, with a censorship wall and corruption still prevalent in the government."

jump end

label force:

m "The military is certainly the backbone of the country and we must show we will not blend to rampant criticism of the revolution from traitorous intellectuals."
m "We cannot allow these transgressions to stand."

hide deng
hide lin
hide jiang

scene bg bodies

"The military moved in at the end of the night, where thousands of protesters still remained."
"They were told to leave immediately, as they were trespassing on national territory and the Square was now closed."
"Some left, but many resisted, shouting “Long Live Zhou Enlai” and “Zhou’s ideals must live on!”"

"The protesters began to get rough, shouting at the police that they were supporting a corrupt regime and that Zhou deserved a better memorial than he received."
"The police responded roughly in turn. This led to an all out riot, citizens attacked police and set police cruisers on fire."
"Over 100,000 people in the square started to try and force themselves into government buildings around the square."
"However, due to Lin Biao’s foresight, the military was closeby the quickly quench the riot."
"The military brought in jeeps and tanks and threatened to fire upon the protesters."
"Many fled as soon as the army arrived, but the rest were arrested or refused to be arrested, leading the military to open fire."
"Thousands were arrested, and hundreds killed in Lin Biao’s wish to demonstrate the military’s power."
"Those who were arrested were then put on trial and sent to worker camps."

"Several months later, on September 6,  Mao passed away."
"With the previous series of approval he had awarded Lin Biao, and his position of Vice Chairman, he quickly took helm of the leadership with little opposition."
"After taking power, he dismissed Deng Xiaoping, seeing him as a moderate and remnant of Zhou Enlai’s policies."

"Biao focused on developing the military and strengthening the army, navy, and air force."
"Under his guidance China developed military ties with the Southeast Asian Nations, helping prop up the Khmer Rouge and Pol Pot taking over Cambodia."
"Lin also sent strengthened ties with Vietnam, as well as Indonesia and founded the Third World Alliance."
"An international group dedicated to advancing the status of Mao’s dubbed “Third World” countries, and elevating them to stand equal to the superpowers."
"Lin Biao created China to develop a third sphere of international power, and rebuffed the Americans attempts to normalize relations."
"This leaves China, Russia, and the United States at a three way Cold War by the end of the 80’s."

jump end

label prop:

m "If I allow these commoners to openly criticize me and the Politburo, how can I maintain a strong image to all of China and to the political world?"
m "We must silence their protests, and show China is resolute."

j "I shall send out the word at once Chairman."

hide deng
hide lin
hide jiang

scene bg bodies

"The police moved in at the end of the night, after protesters had left for the night."
"They returned the next morning, to an empty plaza and police patrolling the Square in order to prevent demonstrations."
"Protesters were told to leave immediately, as they were trespassing on national territory and the Square was now closed."
"Some left, but many resisted, shouting “Long Live Zhou Enlai” and “Zhou’s ideals must live on!”"
"The protesters began to get rough, shouting at the police that they were supporting a corrupt regime and that Zhou deserved a better memorial than he received."
"The police responded roughly in turn. This led to an all out riot, citizens attacked police and set police cruisers on fire."
"Over 100,000 people in the square started to try and force themselves into government buildings around the square."
"More police were brought in, and thousands were arrested."
"Those who were arrested were then put on highly public trials in order for Jiang Qing to convey the consequences of going against the State."
"Jiang issued several high profile reports against the protesters and banned public mourning of Zhou Enlai."

"September 6th, 1976."
"Mao Zedong passes away due to a heart attack."
"Jiang Qing arranges for his body to be embalmed and placed in a Mausoleum so that the Chinese people may never forget Chairman Mao, despite his wishes he be cremated."
"Afterwards, Jiang Qing and her “Gang of Four” take power, leading to a very anti-west sentiment in China."
"Jiang Qing focuses on continuing the cultural revolution, by producing more eight stage plays and throwing Deng Xiaoping out of the Party." 

"Jiang Qing’s China remains largely out of the international political sphere, instead aiming to consolidate the power in China and rooting out those elements not faithful to her."
"China’s economy declines as relations with the West degrade and trade restrictions are placed upon the nation."
"A general recession occurs, but with Jiang Qing’s tight grip on power not much can be done."
"China’s world power declines as Jiang Qing is unable to adapt Mao Zedong thought to the ever interconnected and global world politics and economy."
"China begins to fade into obscurity as another nation where Communism has been shown to be failure in the 21st century..."

jump end

label end:

scene thanks
with wipeup

"Credits: Script/Programming by Philippe Kimura-Thollander. Art by Regine Cuenca. Advised by Peggy Christoff."

return
