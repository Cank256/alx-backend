#!/usr/bin/node
import kue from 'kue';

const queue = kue.createQueue();

const jobs = [
  { phoneNumber: '1234567890', message: 'Message 1' },
  { phoneNumber: '0987654321', message: 'Message 2' },
];

jobs.forEach((data) => {
  const job = queue.create('notification', data).save((err) => {
    if (err) console.error('Error creating job:', err);
    else console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.error(`Notification job ${job.id} failed: ${errorMessage}`);
  });
});

queue.on('error', (err) => {
  console.error('Kue error:', err);
});
