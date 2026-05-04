# ZDI-14-087: (Pwn2Own) Google Chrome Clipboard Sandbox Escape Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-087
- **ZDI-CAN:** ZDI-CAN-2230
- **Date:** 2014-04-11
- **CVE:** CVE-2014-1714
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** VUPEN
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-087/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the Microsoft Windows Clipboard. An attacker can leverage this vulnerability to execute code under the context of the broker process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2014/03/stable-channel-update_14.html

## Disclosure Timeline

- 2014-03-13 - Vulnerability reported to vendor
- 2014-04-11 - Coordinated public release of advisory
