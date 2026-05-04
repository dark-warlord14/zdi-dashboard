# ZDI-17-188: Apple macOS ImageIO JPEG Parsing Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-188
- **ZDI-CAN:** ZDI-CAN-4329
- **Date:** 2017-03-28
- **CVE:** CVE-2017-2432
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-188/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG files. The issue results from the lack of proper validation of user-supplied data which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT201222

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2017-03-28 - Coordinated public release of advisory
