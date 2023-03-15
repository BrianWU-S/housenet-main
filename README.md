# HouseNet
With the rising number of students enrolling at UCSD year after year, there is an immense problem regarding student housing which only grows larger as the year goes by. What our team hopes to accomplish is to assist in this tedious housing process, helping to provide a resource which will help UCSD students find housing with minimum hassle so they can focus more on their academics than having to find a place to sleep at night. We want to go beyond what the current housing solutions provide which seems to be filled with holes and frustrations for the students who have searched for housing earlier.

In particular, what we hope to accomplish is to make a comprehensive marketplace that is trusted so that students don't have to search through an abundance of scams and untrustworthy listings all over the internet. This will primarily be focused on students, and for students to transfer leases from the houses they love. We hope that by providing a platform for students to interact with one another, we can create a sort of shared housing community which UCSD students can trust. We hope to be able to form a network for students who are searching and a one stop shop for everything housing search related.

## Main Features

The primary features we hope to implement are described in the form of epics and features as described below. This is the list of features that is derived from our requirement gathering experiment, and we are still in the process of sprint planning and feature finalization and will most likely be shortening this list to deliverables we think are reasonable to accomplish and integrate into our project given the time we have.
- User verification system
- Locate housing services
    - Map with current location and place pin search
    - Search near location
- Functional filters to help student choose their ideal houses
    - Price
    - Location
    - rDietary restrictions
    - Transport
    - Number of rooms
    - Space of room/living room/house
- Aesthetics and design
    - Carousel for apartment pictures
    - UX for navigation
- Detailed information pages for more than necessary information
    - neighbor information
    - Society and hobbies nearby
    - Area, vibe and safety of the street

## Customers

Our customers will primarily be the students who are currently searching for housing within San Diego, and we also aim to cater to landlords who the potential tenants can chat with in app. Our carpool feature if implemented will not be drivers who get paid, but rather it will be potential tenants going to see a house together. Our competitors are essentially facebook marketplaces, apartment housing websites which have been doing this for quite some time now. There are buggy and untrustworthy implementations of a network within some of these housing websites right now, but we aim to be more trustworthy and transparent with our user base.

## Potential risks

We have identified a few potential risks that could hamper the success or be the setback of our plans for this project. Some of these are listed below:

### Time constraints:

Our primary risk at this moment is that we are a fairly new team and we are aiming for the skies within 6 weeks. We will have to cut down on our product features before the start of our sprint to ensure that we don’t overcommit and fall behind sprint after sprint. Our plans for this product are huge and we hope to implement a product that could be of use and different from the current products in the market.

### User validation and security concerns:

Security and privacy is an extremely important aspect of our project and trust is our topmost priority as most users of current housing apps mainly have a problem with this aspect. This is a little bit tricky since we have to be affiliated with UC San Diego to onboard the SSO and duo mobile integration. If we are implementing the carpool feature, we have to ensure that the users background checking is done, or we have to be extremely explicit in our disclaimer that eventually the trust is relayed back to the users who consent to risks with carpooling.

### Number of house listings:

To get the number of listings same or higher than other apartment listings out there, we have to do a lot of groundwork to get these listings and verify them since we don’t have a lot of time nor do we have an operations employee to get on ground and get the necessary information to onboard these rental locations for us.

### Advertising and competing products:

Our approach to advertising is still uncertain and we can’t afford to spend any resources for this task either. Since we are a UCSD only app, we could work with word of mouth, but we also need to prove that we are better than the competition and that could take time after the engineering which we don’t have the bandwidth to do. Also, there may already be established and popular housing finding solutions that offer similar features, which could make it difficult for our application to stand out.

## What is our USP?

Our unique selling proposition is that we aim to build a one stop shop for everything housing related on our app. If our app kicks off and gains users as we expect it to(but we never know with consumer apps) we aim to also incorporate landlord communication and post lease agreement problems and services for hire. Essentially our app will not only be the app for searching housing, but an app for everything housing related. The users will be able to network with their friends and family in the app, and be able to see what they are considering as well, and if they want they can schedule visits together and sign leases together. Right now, since these apps only support housing searches and details of the houses, the students and potential tenants have to resort to other messaging apps to coordinate their travel and housing search. This is definitely something that the users desire along with the trust with rental locations.

## Risk Management

For time constraints of this project, we aim to cut down on our features after our first backlog grooming session, but we also want to be able to implement features that sets us apart from our competitors as described by our USP. User validation and security concerns is something that involves us having to communicate with UCSD after the app is established, and if we deem that user verification for carpooling too expensive, we will leave it to the users to accept the terms and conditions where they will consent to full trust if they accept the car pooling arrangement. We aren’t exactly sure how Uber or other car booking services deal with this, but if it is different and if not very expensive, we will consider that route as well.

With respect to advertising and number of listings, the primary limitation is the resources with time and employees and if time permits, we will attempt to spread the word and go on ground or build scripts to fetch data from the competitors API, if present. When concerning the competition issue, we will try to provide unique features as described above and focus on delivering a seamless and user friendly experience to make our app appealing to targeted groups.

## General plan for technology

Our plan for technology includes the development of a web application that is compatible with most popular browsers such as Google Chrome, Mozilla Firefox, and Safari. The main technologies we plan to use are:

1. Front-end: **React**, a library for building user interfaces, for a responsive and seamless user experience.
2. Back-end: **Flask** for building the application's server-side logic.
3. Database: **PostgreSQL**, a SQL database, for storing and retrieving data efficiently.
4. Deployment: **GCP** for hosting the application and providing scalable infrastructure.

We have selected these technologies based on their appropriateness for building a web application, as well as the skills and experience of our team. The use of React on the front-end and Flask on the back-end enables efficient and effective collaboration between the two sides. Additionally, GCP provides a secure and reliable platform for hosting our application, and Firebase offers flexible and scalable data storage. Some more relevant details regarding our project is its existence as a web app focused on Chrome.

Furthermore, a general development plan is described as below:

- Select the programming language and corresponding framework the system wants to base on. So that if some of the teammates aren't familiar with the language or framework, they can start earlier to get familiar with them.
- List the basic requirements ((top 3: scalability, availability, performance)
- System architecture design
- Decompose the work for each teammates
- Dive deep into each component,
- Iteration (remove the trivial functionalities, simplify the implementation, etc.)
- Test
- Deploy

# Code Structure

## housenet-backend
this is located in /api

## housenet-frontend
this is located in /app

## CI/CD
There is currently a github action that triggers a build to gcp when a push or merge is done to main branch. It is described in .github/workflows and the dockerfile is present in the root directory
