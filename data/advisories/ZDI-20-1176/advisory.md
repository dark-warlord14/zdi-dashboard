# ZDI-20-1176: NETGEAR Multiple Routers mini_httpd Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1176
- **ZDI-CAN:** ZDI-CAN-10754
- **Date:** 2020-09-15
- **CVE:** CVE-2020-17409
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1176/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of NETGEAR R6120, R6080, R6260, R6220, R6020, JNR3210, and WNR2020 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the mini_httpd service, which listens on TCP port 80 by default. The issue results from incorrect string matching logic when accessing protected pages. An attacker can leverage this vulnerability to disclose stored credentials, leading to further compromise.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062304/Security-Advisory-for-Authentication-Bypass-on-Some-Routers-PSV-2020-0258

## Disclosure Timeline

- 2020-05-22 - Vulnerability reported to vendor
- 2020-09-15 - Coordinated public release of advisory
