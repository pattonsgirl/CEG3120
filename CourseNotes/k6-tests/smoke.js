// Basic load test: ramps up virtual users, holds, then ramps down.
// Run from the folder that contains k6/:
//   docker run --rm -i -v "$PWD/k6:/scripts:ro" -e BASE_URL=http://10.0.0.10 grafana/k6 run /scripts/smoke.js

import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = __ENV.BASE_URL;
if (!BASE_URL) {
  throw new Error('Set BASE_URL, e.g. BASE_URL=http://34.196.111.132/');
}

export const options = {
  stages: [
    { duration: '30s', target: 10 },  // ramp up to 10 virtual users
    { duration: '1m',  target: 10 },  // hold
    { duration: '30s', target: 0 },   // ramp down
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],    // fewer than 1% of requests fail
    http_req_duration: ['p(95)<500'],  // 95% of requests finish under 500 ms
  },
};

export default function () {
  const res = http.get(`${BASE_URL}/`);
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);  // each virtual user waits 1s between requests
}