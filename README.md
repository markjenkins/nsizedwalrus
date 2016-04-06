https://NsizedWalrus.ninja

The 100 duck-sized horses meme meets a Zuckerberg-style Facemash. Barnyard animals and more.

Written as an audition application. Technologies I was trying for the first time marked with #.

Glicko2 ratings and stress testing still to come.

* Application logic: Two Python functions written for AWS Lambda#.
* Templating: AWS API Gateway# mapping templates.
* Database: Two tables, AWS DynamoDB#.
* Static file CDN: AWS CloudFront backed by S3.
* DNS registration and TLS certificate: Namecheap.
* DNS: AWS Route 53 with aliases feature used to CloudFront endpoints for static files and API.
* Image scraping from Wikipedia: "Let the hacking begin". Firefox, LibreOffice, find, xargs, sed, awk, grep, bash, and wget.
* Creation of combinations: Python's random.sample and random.choice and a set comprehension for implicit duplicate avoidance.

No JavaScript, pure old-school form submission with a redirect and a page load. Should run on ancient and terminal based browsers. Use of AWS API Gateway would have been much easier if I had used JavaScript, but this was cooler.
