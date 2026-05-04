# ZDI-22-523: (Pwn2Own) NETGEAR R6700v3 circled Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-523
- **ZDI-CAN:** ZDI-CAN-15879
- **Date:** 2022-03-23
- **CVE:** CVE-2022-27646
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Kevin Denis (@0xmitsurugi) and Antide Petit (@xarkes_) from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-523/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NETGEAR R6700v3 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the circled daemon. A crafted circleinfo.txt file can trigger an overflow of a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064721/Security-Advisory-for-Multiple-Vulnerabilities-on-Multiple-Products-PSV-2021-0324

## Disclosure Timeline

- 2021-12-01 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
