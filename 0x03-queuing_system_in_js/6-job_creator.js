#!/usr/bin/node
import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a notification message',
};

const job = queue.create('notification', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

queue.on('error', (err) => {
  console.error('Kue error:', err);
});
