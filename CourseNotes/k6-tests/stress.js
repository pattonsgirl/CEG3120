// Stress test: steps load up in stages, holding at each level so you can see
// where response times climb and errors start, then ramps down to check recovery.
// Total run time: about 23 minutes.
//
// Run from the folder that contains k6/:
//   docker run --rm -i -v "$PWD/k6:/scripts:ro" -e BASE_URL=http://10.0.0.10 grafana/k6 run /scripts/stress.js

import http from 'k6/http';
import { check, sleep } from 'k6';

const BASE_URL = __ENV.BASE_URL;
if (!BASE_URL) {
  throw new Error('Set BASE_URL, e.g. BASE_URL=http://10.0.0.10');
}

export const options = {
  stages: [
    { duration: '2m', target: 50 },   // warm up
    { duration: '3m', target: 50 },   // hold: normal load
    { duration: '2m', target: 100 },
    { duration: '3m', target: 100 },  // hold: above normal
    { duration: '2m', target: 200 },
    { duration: '3m', target: 200 },  // hold: heavy
    { duration: '2m', target: 300 },
    { duration: '3m', target: 300 },  // hold: beyond expected capacity
    { duration: '3m', target: 0 },    // ramp down: does it recover?
  ],
  thresholds: {
    // Stop the test early if more than 10% of requests fail for over a minute,
    // since by then the breaking point has been found.
    http_req_failed: [{ threshold: 'rate<0.10', abortOnFail: true, delayAbortEval: '1m' }],
    // Reported pass/fail only; does not stop the test.
    http_req_duration: ['p(95)<1000'],
  },
};

export default function () {
  const res = http.get(`${BASE_URL}/`, { timeout: '10s' });
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(0.5);  // each virtual user makes about 2 requests per second
}