# ZDI-23-496: NETGEAR RAX30 lighttpd Misconfiguration Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-496
- **ZDI-CAN:** ZDI-CAN-19398
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27360
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Rocco Calvi and Steven Seeley of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-496/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the lighttpd HTTP server. The issue results from allowing execution of files from untrusted sources. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065559/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0352

## Disclosure Timeline

- 2022-11-30 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
