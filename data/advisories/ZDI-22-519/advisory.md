# ZDI-22-519: (Pwn2Own) NETGEAR R6700v3 upnpd Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-519
- **ZDI-CAN:** ZDI-CAN-15692
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27643
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Stephen Fewer of Relyze Software Limited (www.relyze.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-519/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of SOAP requests. When parsing the SOAPAction header, the process does not properly validate the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064720/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0323

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
