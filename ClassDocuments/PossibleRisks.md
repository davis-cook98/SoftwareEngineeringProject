# Possible Risks

This document will serve as a checklist for possible risks that we may run into while creating our application, and what we will do to 
mitigate them.

**1. Duplicate articles:** We may by accident display the same article more than once because two or more of our sources passed it to our 
reccomender. We will solve this by having our reccomendation algorithm check for similar names in the articles it gets.

**2. Useless information:** We may possibly get articles that are not relevant or useless to our users.  To try and solve this we will check the
content of the articles against some given keywords and if there is sufficient overlap we will not display the article or place it in a 
different area.

**3. Wrong information:** This is self explanatory and to avoid it we will try to get our articles from unbiased sources.

**4. False information:** We are labeling this different from Wrong information, as this is info that was put our by another school. Sometimes 
there is banter between rival schools so we have to avoid pushing this information. We will determine later how to avoid this.
