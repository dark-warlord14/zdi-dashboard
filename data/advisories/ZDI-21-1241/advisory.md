# ZDI-21-1241: NETGEAR R6260 mini_httpd Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1241
- **ZDI-CAN:** ZDI-CAN-13512
- **Date:** 2021-10-28
- **CVE:** CVE-2021-34979
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6260
- **Credit:** Sherman Chann Zhi Shen & Hoang Thach Nguyen (d4rkn3ss)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1241/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SOAP requests. When parsing the SOAPAction header, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064261/Security-Advisory-for-Vertical-Privilege-Escalation-on-Some-Routers-PSV-2021-0152?article=000064261

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
