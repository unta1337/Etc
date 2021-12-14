const tcpPortUsed = require('tcp-port-used');

// enter your host (ip adress or domain name)
let host = 'localhost';

// enter your port range (0 to 65535)
let start = 0;
let end = 65535;

// show ports option (all, used, free)
let show = 'all';

console.log('true means the port is opened and cannot be used. (some service is already using that port.).');
console.log('false means the port is opened and can be used.');
console.log('if some port is not printed then that port is closed.');
console.log();
console.log(`sacnning ports on ${host}`);
console.log(`scan range: ${start} to ${end}`);

for (let port = start; port <= end; port++) {
	tcpPortUsed.check(port, host).then(
		function(inUse) {
			switch (show) {
				case 'all':
					console.log(`${port}, ${inUse}`);
					break;
				case 'used':
					if (inUse)
						console.log(`${port}, ${inUse}`);
					break;
				case 'free':
					if (!inUse)
						console.log(`${port}, ${inUse}`);
					break;
			}
		}, function(err) {
			//console.log(`${port}, ${err}`);
		}
	);
}
