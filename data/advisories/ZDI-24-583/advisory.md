# ZDI-24-583: (Pwn2Own) NETGEAR RAX30 Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-583
- **ZDI-CAN:** ZDI-CAN-19589
- **Date:** 2024-06-10
- **CVE:** CVE-2023-51634
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Neodyme
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-583/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to compromise the integrity of downloaded information on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the downloading of files via HTTPS. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065928/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2023-0139

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2024-06-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
