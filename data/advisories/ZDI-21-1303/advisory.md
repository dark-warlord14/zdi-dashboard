# ZDI-21-1303: NETGEAR R6400v2 UPnP uuid Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1303
- **ZDI-CAN:** ZDI-CAN-14110
- **Date:** 2021-11-11
- **CVE:** CVE-2021-34991
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6400v2
- **Credit:** anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1303/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6400v2 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the UPnP service, which listens on TCP port 5000 by default. When parsing the uuid request header, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064361/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Multiple-Products-PSV-2021-0168

## Disclosure Timeline

- 2021-07-07 - Vulnerability reported to vendor
- 2021-11-11 - Coordinated public release of advisory
- 2021-12-23 - Advisory Updated
