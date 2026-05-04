# ZDI-22-1155: (Pwn2Own) Softing Secure Integration Server Cleartext Transmission of Sensitive Information Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1155
- **ZDI-CAN:** ZDI-CAN-17214
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2338
- **CVSS:** 5.7
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1155/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Softing Secure Integration Server. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of administrator credentials provided to the endpoint. The issue results from transmitting sensitive information in plaintext. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-5.html

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
