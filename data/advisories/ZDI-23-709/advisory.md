# ZDI-23-709: (Pwn2Own) Prosys OPC UA Simulation Server Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-709
- **ZDI-CAN:** ZDI-CAN-20503
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32787
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Prosys OPC
- **Affected Products:** UA Simulation Server
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Vera Mens, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-709/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Prosys OPC UA Simulation Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of message chunks. By sending a large number of requests, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Prosys OPC has issued an update to correct this vulnerability. More details can be found at: https://www.prosysopc.com/blog/pwn2own-2023-resource-exhaustion-exploit/

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
- 2023-05-30 - Advisory Updated
