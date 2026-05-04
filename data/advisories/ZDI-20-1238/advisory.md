# ZDI-20-1238: Apple macOS CoreGraphics JBIG2Bitmap Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1238
- **ZDI-CAN:** ZDI-CAN-11184
- **Date:** 2020-10-08
- **CVE:** CVE-2020-9883
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin of Trend Micro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1238/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple macOS. Interaction with the CoreGraphics library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the JBIG2Bitmap::expand method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211288

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-10-08 - Coordinated public release of advisory
