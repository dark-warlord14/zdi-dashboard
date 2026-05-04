# ZDI-16-361: (Pwn2Own) Apple OS X libATSServer Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-361
- **ZDI-CAN:** ZDI-CAN-3605
- **Date:** 2016-05-27
- **CVE:** CVE-2016-1796
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-361/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the GetUncompressedBitmapRepresentation method. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-27 - Coordinated public release of advisory
