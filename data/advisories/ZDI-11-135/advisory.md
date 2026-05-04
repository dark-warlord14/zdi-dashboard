# ZDI-11-135: (Pwn2Own) WebKit WBR Tag Removal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-135
- **ZDI-CAN:** ZDI-CAN-1168
- **Date:** 2011-04-14
- **CVE:** CVE-2011-1344
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** WebKit
- **Affected Products:** WebKit
- **Credit:** Vupen Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-135/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the Webkit library handles WBR tags on a webpage. By adding children to a WBR tag and then consequently removing the tag through, for example, a 'removeChild' call it is possible to create a dangling pointer that can result in remote code execution under the context of the current user.

## Additional Details

Google patch on March 12, 2011: http://googlechromereleases.blogspot.com/2011/03/stable-and-beta-channel-updates.html Apple patch on April 14, 2011: http://support.apple.com/kb/HT4606 http://support.apple.com/kb/HT4607 http://support.apple.com/kb/HT4596 Webkit fix: http://trac.webkit.org/changeset/79689

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-04-14 - Coordinated public release of advisory
