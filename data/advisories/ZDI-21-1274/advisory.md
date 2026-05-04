# ZDI-21-1274: NETGEAR Multiple Routers httpd Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1274
- **ZDI-CAN:** ZDI-CAN-13709
- **Date:** 2021-10-29
- **CVE:** CVE-2021-34982
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** Multiple Routers
- **Credit:** Sungur Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1274/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of multiple NETGEAR routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the httpd service, which listens on TCP port 80 by default. When parsing the strings file, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064313/Security-Advisory-for-Pre-Authentication-Buffer-Overflow-on-Some-Extenders-Routers-and-DSL-Modem-Routers-PSV-2021-0159

## Disclosure Timeline

- 2021-06-30 - Vulnerability reported to vendor
- 2021-10-29 - Coordinated public release of advisory
