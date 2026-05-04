# ZDI-23-1494: Apple Safari TypedArray copyWithin Integer Underflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1494
- **ZDI-CAN:** ZDI-CAN-21167
- **Date:** 2023-09-29
- **CVE:** CVE-2023-38600
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1494/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the copyWithin method on typed arrays. The issue results from the lack of proper validation of user-supplied data, which can result in an integer underflow before writing to memory. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213847

## Disclosure Timeline

- 2023-05-23 - Vulnerability reported to vendor
- 2023-09-29 - Coordinated public release of advisory
