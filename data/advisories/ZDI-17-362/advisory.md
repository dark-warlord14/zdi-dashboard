# ZDI-17-362: (Pwn2Own) Apple Safari ProcessingInstruction Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-362
- **ZDI-CAN:** ZDI-CAN-4598
- **Date:** 2017-05-18
- **CVE:** CVE-2017-2538
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Richard Zhu (fluorescence)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-362/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of cached stylesheets. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207804

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
