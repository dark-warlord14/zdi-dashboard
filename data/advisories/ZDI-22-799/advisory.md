# ZDI-22-799: (Pwn2Own) Mozilla Firefox Top-Level Await Prototype Pollution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-799
- **ZDI-CAN:** ZDI-CAN-17469
- **Date:** 2022-05-27
- **CVE:** CVE-2022-1802
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-799/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Top-Level Await implementation. The issue results from the lack of control over modifications to attributes of object prototypes. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2022-19/

## Disclosure Timeline

- 2022-05-26 - Vulnerability reported to vendor
- 2022-05-27 - Coordinated public release of advisory
