# ZDI-18-1336: (0Day) Juuko JK-800 Replay Attack Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1336
- **ZDI-CAN:** ZDI-CAN-6184
- **Date:** 2018-11-02
- **CVE:** N/A
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Juuko
- **Affected Products:** JK-800
- **Credit:** Stephen Hilt Marco Balduzzi Akira Urano Philippe Z Lin Federico Maggi Jonathan Andersson Rainer Vosseler
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1336/
## Vulnerability Details

This vulnerability allows remote attackers to issue commands on vulnerable installations of Juuko equipment. Authentication is not required to exploit this vulnerability. The specific flaw exists with the communication between the transmitter and receiver pair. By using a fixed control code, an attacker can obtain and replay commands to the receiver. An attacker can leverage this vulnerability to issue commands to the physical equipment controlled by the device.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/09/18 - ZDI reported the issue to ICS-CERT 05/15/18 - ICS-CERT acknowledged receipt of the report and provided an ICS-VU# 09/14/18 - ZDI sent a follow-up to ICS-CERT 09/17/18 - ICS-CERT replied that they have had no updates from the vendor 10/04/18 - ZDI asked ICS-CERT if they had any replies from the vendor 10/04/18 - ICS-CERT replied that they haven't had a response from the vendor since 05/31/18 10/22/18 - ZDI notified ICS-CERT that the report would be moved to 0-day the week of 10/29/18 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the machine to trusted devices.

## Disclosure Timeline

- 2018-05-09 - Vulnerability reported to vendor
- 2018-11-02 - Coordinated public release of advisory
- 2018-11-02 - Advisory Updated
