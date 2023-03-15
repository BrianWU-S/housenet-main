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

## housenet-backend
this is located in /api

## housenet-frontend
this is located in /app

## CI/CD
There is currently a github action that triggers a build to gcp when a push or merge is done to main branch. It is described in .github/workflows and the dockerfile is present in the root directory
