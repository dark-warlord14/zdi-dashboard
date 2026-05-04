# ZDI-17-821: Apple Safari String link Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-821
- **ZDI-CAN:** ZDI-CAN-4712
- **Date:** 2017-09-26
- **CVE:** CVE-2017-7092
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Samuel Gro and Niklas Baumstark
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-821/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the String.link method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/HT208116

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
