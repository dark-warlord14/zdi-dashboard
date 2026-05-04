# ZDI-18-781: (Pwn2Own) Apple Safari SVG Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-781
- **ZDI-CAN:** ZDI-CAN-5828
- **Date:** 2018-07-26
- **CVE:** CVE-2018-4199
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** MWR Labs - Alex Plaskett Georgi Geshev Fabian Beterke
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-781/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of SVG elements. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT208849

## Disclosure Timeline

- 2018-02-20 - Vulnerability reported to vendor
- 2018-07-26 - Coordinated public release of advisory
- 2018-12-20 - Advisory Updated
