# ZDI-21-263: (Pwn2Own) NETGEAR R7800 funjsq_httpd Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-263
- **ZDI-CAN:** ZDI-CAN-12360
- **Date:** 2021-02-26
- **CVE:** CVE-2021-27255
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7800
- **Credit:** STARLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-263/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of NETGEAR R7800. Authentication is not required to exploit this vulnerability. The specific flaw exists within the refresh_status.aspx endpoint. The issue results from a lack of authentication required to start a service on the server. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062883/Security-Advisory-for-Multiple-Vulnerabilities-on-Some-Routers-Satellites-and-Extenders

## Disclosure Timeline

- 2020-12-31 - Vulnerability reported to vendor
- 2021-02-26 - Coordinated public release of advisory
