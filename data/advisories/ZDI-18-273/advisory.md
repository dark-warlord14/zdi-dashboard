# ZDI-18-273: Apple Safari WebGL BufferSubData Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-273
- **ZDI-CAN:** ZDI-CAN-5515
- **Date:** 2018-04-06
- **CVE:** CVE-2018-4130
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-273/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebGL. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-12-21 - Vulnerability reported to vendor
- 2018-04-06 - Coordinated public release of advisory
- 2018-04-06 - Advisory Updated
