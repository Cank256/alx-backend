#!/usr/bin/node
import kue from 'kue';

const queue = kue.createQueue();

queue.process('notification', (job, done) => {
  console.log(`Processing job ${job.id}`);

  // Simulate success or failure randomly
  const success = Math.random() < 0.5;
  if (success) {
    console.log(`Notification job ${job.id} processed successfully`);
    done();
  } else {
    console.error(`Notification job ${job.id} failed`);
    done(new Error('Failed to process job'));
  }
});

queue.on('error', (err) => {
  console.error('Kue error:', err);
});
