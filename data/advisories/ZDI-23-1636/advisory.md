# ZDI-23-1636: NETGEAR CAX30 SSO Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1636
- **ZDI-CAN:** ZDI-CAN-19058
- **Date:** 2023-11-14
- **CVE:** CVE-2023-44445
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** CAX30
- **Credit:** Amol Dosanjh
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1636/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR CAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the sso binary. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065859/Security-Advisory-for-Pre-authentication-Buffer-Overflow-on-the-CAX30-PSV-2023-0093

## Disclosure Timeline

- 2023-07-11 - Vulnerability reported to vendor
- 2023-11-14 - Coordinated public release of advisory
