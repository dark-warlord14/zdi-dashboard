# ZDI-21-1240: NETGEAR R6260 setupwizard.cgi Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1240
- **ZDI-CAN:** ZDI-CAN-13511
- **Date:** 2021-10-28
- **CVE:** CVE-2021-34978
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6260
- **Credit:** Sherman Chann Zhi Shen & Hoang Thach Nguyen (d4rkn3ss)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1240/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6260 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the setupwizard.cgi page. A crafted SOAP request can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064258/Security-Advisory-for-Vertical-Privilege-Escalation-on-Some-Routers-DSL-Modem-Routers-and-Access-Points-PSV-2021-0151-and-PSV-2021-0170?article=000064258

## Disclosure Timeline

- 2021-06-16 - Vulnerability reported to vendor
- 2021-10-28 - Coordinated public release of advisory
