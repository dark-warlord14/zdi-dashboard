# ZDI-21-206: NETGEAR Multiple Routers SSDP Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-206
- **ZDI-CAN:** ZDI-CAN-11851
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27239
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-206/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6400 and R6700 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the upnpd service, which listens on UDP port 1900 by default. A crafted MX header field in an SSDP message can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000062820/Security-Advisory-for-Stack-based-Buffer-Overflow-Remote-Code-Execution-Vulnerability-on-Some-Routers-PSV-2020-0432

## Disclosure Timeline

- 2020-09-23 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
