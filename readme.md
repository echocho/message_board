A simple message board where visitors can come and post what they want to.
All posts are open to public -- all visitors can see. 
Sign-in not needed.

## Functionality ##
### Backend ###
- all posts listed in index page, order by created time desc
- posts time shown in format 'xx minutes/hours/months ago' (Flask-Moment)
- provides tooltip to show exact timestamp of a post (tooltip())
- visitor could post, provided name (less than 20 characters) and message (less than 100 characters) (Flask-WTForm)
- provides commands to forge posts (Click + Faker)

### Frontend ###
- beautify page (bootstrap)
wip...