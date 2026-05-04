# ZDI-23-502: (Pwn2Own) NETGEAR RAX30 SOAP Request SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-502
- **ZDI-CAN:** ZDI-CAN-19754
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27358
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Interrupt Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-502/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of specific SOAP requests. The issue results from the lack of proper validation of a user-supplied string before using it to construct SQL queries. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065617/Security-Advisory-for-Authentication-Bypass-on-Some-Routers-PSV-2022-0349

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
