# smite-party-api
Server-side service for smite-party application

Please support the official game:
[Smite Official Site](https://www.smitegame.com/ "Smite Official Site")

## Functionality

This is a purely backend service that will receive requests for randomized Smite assignments and return randomized roles in its response. 

[Link to Frontend Client](https://github.com/cptran777/smite-party)

- The server expects 5 names and 5 roles.
- The randomized roles take into account team balance by detecting team composition issues as roles are filled.

## Extensions

Currently, the first iteration of the API will be a single file that contains the available roles inside lists on the server. A request is received and the response will be sent after randomization functionality has been called.

Need to create the store in a way that's closer to a database entry and assign images there instead of in the index. 

### Iteration Plans: 

1) Customized lists. Basic lists of gods should include them purely sorted by type (Warrior, Mage, etc). Then there should be role-based lists (Healer, Tank, CC, etc) in addition to the fixed role lists (Jungler, Mid, etc). The goal will be to allow people to choose what type or role based list should be included in a role instead of a purely fixed list. 

2) Move these lists to a relational database, probably MySQL or Postgres. 
Edit: Since the lists should be fairly consistent, and each character should be a set of information for themselves, the better form to put the lists in would be a non-relational database such as MongoDB. Additionally, Node is apparenty not as good when it comes to relational databases, so switching to MongoDB would actually be better perfromance-wise as well. 

3) Customized queries for different numbers of players, inclusion or exclusion of roles or gods from each pool for the query.

## Architecture

This is purely a backend service, so it operates independently of the main app. The only functionality of this service right now is to take a request and respond with randomized roles. This service can probably be used to randomize roles for requests coming from both a web and mobile request to a backend. As the application itself begins to expand to become more of a Smite resource, the service might expand to include details about each god. However, that may be a separate service altogether. 

## Deployment

This application will be deployed on Heroku for simplicity. 

## Issues and Challenges 
