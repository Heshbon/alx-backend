# Queuing_system_in_js

This project is intended to create a simple queuing implementation using JavaScript and Node. js, Redis, and Express. js. The goal is to understand and apply various operations with Redis, including how to integrate it with a Node.js application and manage asynchronous tasks using Kue.

# Tasks 📃

# 1. Node Redis Client

  + <u>[0-redis_client.js]()</u> A script named 0-redis_client.js which connect to the Redis server running on my local machine.

# 2. Node Redis client and basic operation

  + <u>[1-redis_op.js]()</u> A script that implements basic operations using the Node Redis client.

# 3. Node Redis client and async operations

  + <u>[2-redis_op_async.js]()</u> This file builds upon the previous code from 1-redis_op.js and introduces asynchronous operations using ES6 async/await with the Node Redis client.

# 4. Node Redis client and advanced operations

  + <u>[4-redis_advanced_op.js]()</u> This file demonstrates how to store and retrieve hash values using the Node Redis client.

# 5. Node Redis client publisher and subscriber

  + <u>[5-subscriber.js]()</u> This file creates a Redis subscriber client that listens for messages on a specific channel and handles incoming messages accordingly.

  + <u>[5-publisher.js]()</u> This file creates a Redis publisher client that sends messages to a specific channel after a specified delay.

# 6. Create the Job creator

  + <u>[6-job_creator.js]()</u> File script that sets up a job queue using Kue, allowing to manage push notification jobs.

# 7. Create the Job processor

  + <u>[6-job_processor.js]()</u>: File script that sets up a job processor using Kue to handle push notification jobs from the push_notification_code queue.

# 8. Track progress and errors with Kue: Create the Job creator

  + <u>[7-job_creator.js]()</u> Script file that creates a job queue using Kue for managing notification jobs.

# 9. Track progress and errors with Kue: Create the Job processor

  + <u>[7-job_processor.js]()</u> Creates a job processor using Kue that processes notification jobs from the push_notification_code_2 queue.

# 10. Writing the job creation function

  + <u>[8-job.js]()</u> Contains a function named createPushNotificationsJobs, which creates jobs for push notifications in a Kue queue.

# 11. Writing the test for job creation

  + <u>[8-job.test.js]()</u> Contains the implementation of the createPushNotificationsJobs function, which creates jobs in a Kue queue for sending notifications.

#  12. In stock?

  + <u>[9-stock.js]()</u> Implements an Express server that manages a product inventory system using Redis.
