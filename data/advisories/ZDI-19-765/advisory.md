# ZDI-19-765: Apple Safari Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-765
- **ZDI-CAN:** ZDI-CAN-8359
- **Date:** 2019-08-27
- **CVE:** CVE-2019-8601
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-765/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the emitAllocateButterfly method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210125

## Disclosure Timeline

- 2019-08-20 - Vulnerability reported to vendor
- 2019-08-27 - Coordinated public release of advisory
