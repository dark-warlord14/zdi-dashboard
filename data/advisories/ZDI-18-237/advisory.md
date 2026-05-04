# ZDI-18-237: Apple macOS QuartzCore render_mask Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-237
- **ZDI-CAN:** ZDI-CAN-5245
- **Date:** 2018-03-07
- **CVE:** CVE-2018-4085
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Ret2 Systems Inc.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-237/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the QuartzCore module. The issue results from the lack of proper handling of error conditions prior to indexing into a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208463

## Disclosure Timeline

- 2017-11-14 - Vulnerability reported to vendor
- 2018-03-07 - Coordinated public release of advisory
- 2018-03-07 - Advisory Updated
