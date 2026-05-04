# ZDI-21-615: (Pwn2Own) Microsoft Exchange Server Missing Check of Message Integrity Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-615
- **ZDI-CAN:** ZDI-CAN-13594
- **Date:** 2021-05-26
- **CVE:** CVE-2021-31209
- **CVSS:** 3.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-615/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to tamper with update data on affected installations of Microsoft Exchange Server. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of Exchange Server Help updates. The issue results from a missing integrity check on update downloads. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31209

## Disclosure Timeline

- 2021-04-08 - Vulnerability reported to vendor
- 2021-05-26 - Coordinated public release of advisory
