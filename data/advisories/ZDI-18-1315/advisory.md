# ZDI-18-1315: Telecrane F25 Replay Attack Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1315
- **ZDI-CAN:** ZDI-CAN-6188
- **Date:** 2018-10-24
- **CVE:** CVE-2018-17935
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Telecrane
- **Affected Products:** F25
- **Credit:** Jonathan Andersson Philippe Z Lin Akira Urano Marco Balduzzi Federico Maggi Stephen Hilt Rainer Vosseler
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1315/
## Vulnerability Details

This vulnerability allows remote attackers to issue commands on vulnerable installations of Telecrane equipment. Authentication is not required to exploit this vulnerability. The specific flaw exists with the communication between the transmitter and receiver pair. By using a fixed control code an attacker can obtain and replay commands to the receiver. An attacker can leverage this vulnerability to issue commands to the physical equipment controlled by the device.

## Additional Details

Telecrane has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-296-03

## Disclosure Timeline

- 2018-05-09 - Vulnerability reported to vendor
- 2018-10-24 - Coordinated public release of advisory
- 2018-10-24 - Advisory Updated
