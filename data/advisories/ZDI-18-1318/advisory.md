# ZDI-18-1318: Saga Radio SAGA1-L8B Firmware Upgrade Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1318
- **ZDI-CAN:** ZDI-CAN-6542
- **Date:** 2018-10-25
- **CVE:** CVE-2018-17923
- **CVSS:** 6.1
- **CVSS Vector:** AV:P/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAGA
- **Affected Products:** SAGA1-L8B
- **Credit:** Philippe Lin, Jonathan Andersson, Rainer Vosseler, Federico Maggi, Urano Akira, Stephen Hilt, Marco Balduzzi
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1318/
## Vulnerability Details

This vulnerability allows attackers with physical access to modify firmware on vulnerable installations of Saga Radio equipment. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the device programming mechanism. The device is insufficiently protected from unauthorized firmware updates. An attacker can leverage this vulnerability to bypass authentication and install persistent malicious firmware on the device.

## Additional Details

SAGA has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-296-02

## Disclosure Timeline

- 2018-06-29 - Vulnerability reported to vendor
- 2018-10-25 - Coordinated public release of advisory
