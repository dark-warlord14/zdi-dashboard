# ZDI-21-1239: NETGEAR R7000 SOAP ParentalControl Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1239
- **ZDI-CAN:** ZDI-CAN-13483
- **Date:** 2021-10-28
- **CVE:** CVE-2021-34977
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R7000
- **Credit:** Xinan Zhou (the University of California, Riverside and Fudan University)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1239/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR R7000 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of SOAP requests. The issue results from the lack of proper authentication verification before performing a password reset. An attacker can leverage this vulnerability to reset the admin password.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064046/Security-Advisory-for-Authentication-Bypass-on-Some-Routers-and-DSL-Modem-Routers-PSV-2021-0134

## Disclosure Timeline

- 2021-06-02 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
