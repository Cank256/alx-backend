#!/usr/bin/node

import kue from 'kue';

const queue = kue.createQueue();

queue.process('notification', (job, done) => {
  console.log(`Processing job ${job.id}`);
  console.log('Notification:', job.data);
  done();
});

queue.on('error', (err) => {
  console.error('Kue error:', err);
});
