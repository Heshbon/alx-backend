import kue from 'kue';

// Creates queue
const queue = kue.createQueue();

// Creates job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message'
};

// Creates a job notification
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Event listener
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
