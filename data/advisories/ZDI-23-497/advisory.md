# ZDI-23-497: (Pwn2Own) NETGEAR RAX30 GetInfo Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-497
- **ZDI-CAN:** ZDI-CAN-19608
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27357
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Claroty Research - Vera Mens, Noam Moshe, Uri Katz, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-497/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SOAP requests. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose sensitive information, leading to further compromise.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065619/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2022-0348

## Disclosure Timeline

- 2023-01-25 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
