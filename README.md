# text_summarizer
Models for text summarization task

## Usage

- getting summary

original text:
```
The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price.
The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal.
Mubadala, an Abu Dhabi investment fund, purchased 90% of the building for $800 million in 2008.
Real estate firm Tishman Speyer had owned the other 10%.
The buyer is RFR Holding, a New York real estate company.
Officials with Tishman and RFR did not immediately respond to a request for comments.
It's unclear when the deal will close.
The building sold fairly quickly after being publicly placed on the market only two months ago.
The sale was handled by CBRE Group.
The incentive to sell the building at such a huge loss was due to the soaring rent the owners pay to Cooper Union, a New York college, for the land under the building.
The rent is rising from $7.75 million last year to $32.5 million this year to $41 million in 2028.
Meantime, rents in the building itself are not rising nearly that fast.
While the building is an iconic landmark in the New York skyline, it is competing against newer office towers with large floor-to-ceiling windows and all the modern amenities.
Still the building is among the best known in the city, even to people who have never been to New York.
It is famous for its triangle-shaped, vaulted windows worked into the stylized crown, along with its distinctive eagle gargoyles near the top.
It has been featured prominently in many films, including Men in Black 3, Spider-Man, Armageddon, Two Weeks Notice and Independence Day.
The previous sale took place just before the 2008 financial meltdown led to a plunge in real estate prices.
Still there have been a number of high profile skyscrapers purchased for top dollar in recent years, including the Waldorf Astoria hotel, which Chinese firm Anbang Insurance purchased in 2016 for nearly $2 billion, and the Willis Tower in Chicago, which was formerly known as Sears Tower, once the world's tallest.
Blackstone Group (BX) bought it for $1.3 billion 2015.
The Chrysler Building was the headquarters of the American automaker until 1953, but it was named for and owned by Chrysler chief Walter Chrysler, not the company itself.
Walter Chrysler had set out to build the tallest building in the world, a competition at that time with another Manhattan skyscraper under construction at 40 Wall Street at the south end of Manhattan. He kept secret the plans for the spire that would grace the top of the building, building it inside the structure and out of view of the public until 40 Wall Street was complete.
Once the competitor could rise no higher, the spire of the Chrysler building was raised into view, giving it the title.
```

request:
```
curl -X 'GET' \
  'http://0.0.0.0:8000/get_summary?t=The%20Chrysler%20Building%2C%20the%20famous%20art%20deco%20New%20York%20skyscraper%2C%20will%20be%20sold%20for%20a%20small%20fraction%20of%20its%20previous%20sales%20price.%20The%20deal%2C%20first%20reported%20by%20The%20Real%20Deal%2C%20was%20for%20%24150%20million%2C%20according%20to%20a%20source%20familiar%20with%20the%20deal.%20Mubadala%2C%20an%20Abu%20Dhabi%20investment%20fund%2C%20purchased%2090%25%20of%20the%20building%20for%20%24800%20million%20in%202008.%20Real%20estate%20firm%20Tishman%20Speyer%20had%20owned%20the%20other%2010%25.%20The%20buyer%20is%20RFR%20Holding%2C%20a%20New%20York%20real%20estate%20company.%20Officials%20with%20Tishman%20and%20RFR%20did%20not%20immediately%20respond%20to%20a%20request%20for%20comments.%20It%27s%20unclear%20when%20the%20deal%20will%20close.%20The%20building%20sold%20fairly%20quickly%20after%20being%20publicly%20placed%20on%20the%20market%20only%20two%20months%20ago.%20The%20sale%20was%20handled%20by%20CBRE%20Group.%20The%20incentive%20to%20sell%20the%20building%20at%20such%20a%20huge%20loss%20was%20due%20to%20the%20soaring%20rent%20the%20owners%20pay%20to%20Cooper%20Union%2C%20a%20New%20York%20college%2C%20for%20the%20land%20under%20the%20building.%20The%20rent%20is%20rising%20from%20%247.75%20million%20last%20year%20to%20%2432.5%20million%20this%20year%20to%20%2441%20million%20in%202028.%20Meantime%2C%20rents%20in%20the%20building%20itself%20are%20not%20rising%20nearly%20that%20fast.%20While%20the%20building%20is%20an%20iconic%20landmark%20in%20the%20New%20York%20skyline%2C%20it%20is%20competing%20against%20newer%20office%20towers%20with%20large%20floor-to-ceiling%20windows%20and%20all%20the%20modern%20amenities.%20Still%20the%20building%20is%20among%20the%20best%20known%20in%20the%20city%2C%20even%20to%20people%20who%20have%20never%20been%20to%20New%20York.%20It%20is%20famous%20for%20its%20triangle-shaped%2C%20vaulted%20windows%20worked%20into%20the%20stylized%20crown%2C%20along%20with%20its%20distinctive%20eagle%20gargoyles%20near%20the%20top.%20It%20has%20been%20featured%20prominently%20in%20many%20films%2C%20including%20Men%20in%20Black%203%2C%20Spider-Man%2C%20Armageddon%2C%20Two%20Weeks%20Notice%20and%20Independence%20Day.%20The%20previous%20sale%20took%20place%20just%20before%20the%202008%20financial%20meltdown%20led%20to%20a%20plunge%20in%20real%20estate%20prices.%20Still%20there%20have%20been%20a%20number%20of%20high%20profile%20skyscrapers%20purchased%20for%20top%20dollar%20in%20recent%20years%2C%20including%20the%20Waldorf%20Astoria%20hotel%2C%20which%20Chinese%20firm%20Anbang%20Insurance%20purchased%20in%202016%20for%20nearly%20%242%20billion%2C%20and%20the%20Willis%20Tower%20in%20Chicago%2C%20which%20was%20formerly%20known%20as%20Sears%20Tower%2C%20once%20the%20world%27s%20tallest.%20Blackstone%20Group%20%28BX%29%20bought%20it%20for%20%241.3%20billion%202015.%20The%20Chrysler%20Building%20was%20the%20headquarters%20of%20the%20American%20automaker%20until%201953%2C%20but%20it%20was%20named%20for%20and%20owned%20by%20Chrysler%20chief%20Walter%20Chrysler%2C%20not%20the%20company%20itself.%20Walter%20Chrysler%20had%20set%20out%20to%20build%20the%20tallest%20building%20in%20the%20world%2C%20a%20competition%20at%20that%20time%20with%20another%20Manhattan%20skyscraper%20under%20construction%20at%2040%20Wall%20Street%20at%20the%20south%20end%20of%20Manhattan.%20He%20kept%20secret%20the%20plans%20for%20the%20spire%20that%20would%20grace%20the%20top%20of%20the%20building%2C%20building%20it%20inside%20the%20structure%20and%20out%20of%20view%20of%20the%20public%20until%2040%20Wall%20Street%20was%20complete.%20Once%20the%20competitor%20could%20rise%20no%20higher%2C%20the%20spire%20of%20the%20Chrysler%20building%20was%20raised%20into%20view%2C%20giving%20it%20the%20title' \
  -H 'accept: application/json'
```

answer:
```
{
  "summary": "The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price. Mubadala, an Abu Dhabi investment fund, purchased 90% of the building for $800 million in 2008. Blackstone Group (BX) bought it for $1.3 billion 2015. He kept secret the plans for the spire that would grace the top of the building, building it inside the structure and out of view of the public until 40 Wall Street was complete."
}
```
