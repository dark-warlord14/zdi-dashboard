# ZDI-15-123: (Pwn2Own) Apple Safari Uninitialized Buffer Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-123
- **ZDI-CAN:** ZDI-CAN-2836
- **Date:** 2015-04-08
- **CVE:** CVE-2015-1069
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments to JavaScript functions. The issue lies in the failure to fully initialize a buffer. By manipulating a function's arguments an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204661

## Disclosure Timeline

- 2015-04-08 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
