
# Pre-requisite:

Follow this guide to deploy Hasura GraphQL (on EC2) on RDS:
https://blog.hasura.io/instant-graphql-on-aws-rds-1edfb85b5985

# Setup our tables
1. Create table: `notes`: `id: int`, `note: text`

# Setup AWS Lambda
Create a lambda function in AWS. This will be our webhook.

1. Create a function.
2. Select Python 3.6 as the runtime.
3. Select "start from scratch".
4. Add API gateway as a trigger.
5. Add an API to API gateway.

6. Add the corresponding code and save. The handler function of your lambda will be the `<filename>.handler`.


# Add events in Hasura GraphQL

1. In events tab, add a trigger
2. Select all insert, update, delete operations for the trigger.
3. Paste the API endpoint of your AWS lambda as the webhook.
