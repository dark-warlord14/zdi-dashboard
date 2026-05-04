# ZDI-21-769: (Pwn2Own) Apple Safari Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-769
- **ZDI-CAN:** ZDI-CAN-13591
- **Date:** 2021-06-25
- **CVE:** CVE-2021-30734
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Jack Dates of RET2 Systems, Inc. (@ret2systems)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-769/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the LLIntGenerator object. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-06-25 - Coordinated public release of advisory
- 2022-01-03 - Advisory Updated
