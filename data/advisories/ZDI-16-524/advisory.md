# ZDI-16-524: Google Chrome Logic Error Safe Browsing Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-524
- **ZDI-CAN:** ZDI-CAN-3624
- **Date:** 2016-09-21
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-524/
## Vulnerability Details

This vulnerability allows remote attackers to bypass restrictions on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Safe Browsing. The issue lies in failure to properly check URLs. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://googlechromereleases.blogspot.com/2016/09/stable-channel-update-for-desktop_13.html

## Disclosure Timeline

- 2016-03-19 - Vulnerability reported to vendor
- 2016-09-21 - Coordinated public release of advisory
