# ZDI-22-873: (Pwn2Own) Prosys OPC UA SDK for Java OPC UA Messages Resource Exhaustion Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-873
- **ZDI-CAN:** ZDI-CAN-16441
- **Date:** 2022-06-27
- **CVE:** CVE-2022-30551
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Prosys OPC
- **Affected Products:** UA SDK for Java
- **Credit:** Vera Mens, Uri Katz, Sharon Brizinov of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-873/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Prosys OPC UA SDK for Java. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling of OPC UA messages. By sending a large number of requests, an attacker can consume all available resources on the server. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Prosys OPC has issued an update to correct this vulnerability. More details can be found at: https://www.prosysopc.com/blog/pwn2own-resource-exhaustion-exploit/

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-06-27 - Coordinated public release of advisory
