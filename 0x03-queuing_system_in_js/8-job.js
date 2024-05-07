#!/usr/bin/node
/**
 * Creates push notification jobs.
 * @param {Array} jobs - Array of objects representing jobs.
 * @param {Object} queue - Kue queue.
 */
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over each job and create a job in the queue
  jobs.forEach((job) => {
    const pushNotificationJob = queue.create('push_notification_code_3', job);

    // Event listeners for job creation, completion, failure, and progress
    pushNotificationJob.on('complete', () => {
      console.log(`Notification job ${pushNotificationJob.id} completed`);
    });

    pushNotificationJob.on('failed', (err) => {
      console.log(`Notification job ${pushNotificationJob.id} failed: ${err}`);
    });

    pushNotificationJob.on('progress', (progress) => {
      console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
    });

    // Save the job and log its creation
    pushNotificationJob.save((err) => {
      if (!err) {
        console.log(`Notification job created: ${pushNotificationJob.id}`);
      }
    });
  });
}

export default createPushNotificationsJobs;
