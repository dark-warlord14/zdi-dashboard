# ZDI-22-1160: Softing Secure Integration Server Content-Length Integer Underflow Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1160
- **ZDI-CAN:** ZDI-CAN-17058
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2335
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Flashback Team: Pedro Ribeiro (@pedrib1337) && Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1160/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Softing Secure Integration Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of the Content-Length HTTP header. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-4.html

## Disclosure Timeline

- 2022-04-15 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
