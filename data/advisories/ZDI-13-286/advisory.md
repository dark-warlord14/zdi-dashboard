# ZDI-13-286: (Mobile Pwn2Own) Apple iOS Safari DocumentOrderedMap Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-286
- **ZDI-CAN:** ZDI-CAN-2071
- **Date:** 2013-12-20
- **CVE:** CVE-2013-5228
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** KEENTeam
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of WebCore::DocumentOrderedMap objects. By manipulating a document's elements an attacker can free arbitrary memory and force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6082

## Disclosure Timeline

- 2013-08-28 - Vulnerability reported to vendor
- 2013-12-20 - Coordinated public release of advisory
