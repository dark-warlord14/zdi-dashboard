# ZDI-21-1275: NETGEAR Multiple Routers httpd Missing Authentication for Critical Function Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1275
- **ZDI-CAN:** ZDI-CAN-13708
- **Date:** 2021-10-29
- **CVE:** CVE-2021-34983
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Sungur Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1275/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of multiple NETGEAR routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. The issue results from the lack of authentication prior to allowing access to system configuration information. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064313/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Some-Extenders-Routers-and-DSL-Modem-Routers-PSV-2021-0159

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-10-29 - Coordinated public release of advisory
