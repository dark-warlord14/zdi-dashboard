# ZDI-11-242: Apple Safari Rendering Object Body Detachment Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-242
- **ZDI-CAN:** ZDI-CAN-1317
- **Date:** 2011-07-27
- **CVE:** CVE-2011-0255
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-242/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application frees references from a particular element. When freeing these references, the application will fail to remove the reference from the rendering object. Later upon trying to free the element again, the application will access the freed reference which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-07-12 - Vulnerability reported to vendor
- 2011-07-27 - Coordinated public release of advisory
