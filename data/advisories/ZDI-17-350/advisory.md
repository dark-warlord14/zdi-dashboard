# ZDI-17-350: (Pwn2Own) Apple Safari Array concat Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-350
- **ZDI-CAN:** ZDI-CAN-4613
- **Date:** 2017-05-15
- **CVE:** CVE-2017-2544
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Liu Long of 360Vulcan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-350/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Array.concat method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207804

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
