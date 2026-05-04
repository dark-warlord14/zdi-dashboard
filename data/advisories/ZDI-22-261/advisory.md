# ZDI-22-261: (Pwn2Own) Sonos One Speaker ALAC Frame Parser Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-261
- **ZDI-CAN:** ZDI-CAN-15798
- **Date:** 2022-02-10
- **CVE:** CVE-2022-24049
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Sonos
- **Affected Products:** One Speaker
- **Credit:** David BERARD (@_p0ly_) from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Sonos One Speaker. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ALAC audio codec. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in S2 software version 13.4.1 or later and S1 software version 11.2.13 build 57923290 or later.

## Disclosure Timeline

- 2021-12-08 - Vulnerability reported to vendor
- 2022-02-10 - Coordinated public release of advisory
- 2022-02-14 - Advisory Updated
