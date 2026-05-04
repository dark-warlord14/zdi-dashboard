# ZDI-18-1317: Saga Radio SAGA1-L8B Remote Controller Forced-Pairing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1317
- **ZDI-CAN:** ZDI-CAN-6526
- **Date:** 2018-10-25
- **CVE:** CVE-2018-17921
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAGA
- **Affected Products:** SAGA1-L8B
- **Credit:** Philippe Lin, Jonathan Andersson, Rainer Vosseler, Federico Maggi, Urano Akira, Stephen Hilt, Marco Balduzzi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1317/
## Vulnerability Details

This vulnerability allows remote attackers to issue commands on vulnerable installations of Saga Radio equipment. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of communication between the transmitter and receiver. By sending a crafted re-pairing packet an attacker can force a receiver to pair with a new transmitter without user interaction. An attacker can leverage this vulnerability to issue commands to the physical equipment controlled by the device.

## Additional Details

SAGA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-296-02

## Disclosure Timeline

- 2018-06-29 - Vulnerability reported to vendor
- 2018-10-25 - Coordinated public release of advisory
