# ZDI-21-264: (Pwn2Own) NETGEAR R7800 ready-genie-cloud Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-264
- **ZDI-CAN:** ZDI-CAN-12362
- **Date:** 2021-02-26
- **CVE:** CVE-2021-27257
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** Team FLASHBACK: Pedro Ribeiro (@pedrib1337 | pedrib@gmail.com) + Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-264/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of NETGEAR R7800. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloading of files via FTP. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-12-31 - Vulnerability reported to vendor
- 2021-02-26 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
