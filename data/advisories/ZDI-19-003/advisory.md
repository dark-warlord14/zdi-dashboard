# ZDI-19-003: Hetronic Nova-M Replay Attack Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-003
- **ZDI-CAN:** ZDI-CAN-6182
- **Date:** 2019-01-04
- **CVE:** CVE-2018-19023
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hetronic
- **Affected Products:** Nova-M
- **Credit:** Akira Urano Marco Balduzzi Stephen Hilt Federico Maggi Philippe Z Lin Rainer Vosseler Jonathan Andersson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-003/
## Vulnerability Details

This vulnerability allows remote attackers to issue commands on vulnerable installations of Hetronic equipment. Authentication is not required to exploit this vulnerability. The specific flaw exists with the communication between the transmitter and receiver pair. By using a fixed control code an attacker can obtain and replay commands to the receiver. An attacker can leverage this vulnerability to issue commands to the physical equipment controlled by the device.

## Additional Details

Hetronic has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-19-003-03

## Disclosure Timeline

- 2018-05-09 - Vulnerability reported to vendor
- 2019-01-04 - Coordinated public release of advisory
- 2019-01-04 - Advisory Updated
