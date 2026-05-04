# ZDI-18-1362: Juuko DATA Packet Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1362
- **ZDI-CAN:** ZDI-CAN-6462
- **Date:** 2022-08-22
- **CVE:** CVE-2018-19025
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Juuko
- **Affected Products:** JK-808
- **Credit:** Federico Maggi, Marco Balduzzi, Stephen Hilt, Philippe Lin, Akira Urano, Rainer Vosseler of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1362/
## Vulnerability Details

This vulnerability allows remote attackers to issue commands on vulnerable installations of Juuko equipment. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of communication between the transmitter and receiver. By using a fixed control code that is used to encode data sent over RF, an attacker can forge unauthorized commands to the receiver. An attacker can leverage this vulnerability to issue commands to the physical equipment controlled by the device.

## Additional Details

07/19/18 - ZDI reported vulnerability to ICS-CERT 07/24/18 - ICS-CERT provided ZDI with ICS-VU # and requested missing details 07/25/18 - ZDI provided ICS-CERT the missing information 11/02/18- ZDI contacted ICS-CERT requesting a status update 11/02/18- ICS-CERT replied they had been regularly contacting the vendor without a response for months. 11/16/18- ZDI contacted ICS-CERT requesting a new status update 11/16/18- ICS-CERT replied they had received a reply from the vendor but no details or deadline for the fix. 11/21/18 - ZDI notified ICS-CERT the case will 0-day on November 26th

## Disclosure Timeline

- 2018-07-19 - Vulnerability reported to vendor
- 2022-08-22 - Coordinated public release of advisory
