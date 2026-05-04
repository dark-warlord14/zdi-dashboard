# ZDI-17-234: (Pwn2Own) Mozilla Firefox createImageBitmap Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-234
- **ZDI-CAN:** ZDI-CAN-4620
- **Date:** 2017-03-30
- **CVE:** CVE-2017-5428
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Mozilla
- **Affected Products:** Firefox
- **Credit:** Chaitin Security Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-234/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of createImageBitmap. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

Mozilla has issued an update to correct this vulnerability. More details can be found at: https://www.mozilla.org/en-US/security/advisories/mfsa2017-08/

## Disclosure Timeline

- 2017-03-18 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
