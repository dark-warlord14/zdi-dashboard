# ZDI-13-064: (Pwn2Own) Google Chrome Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-064
- **ZDI-CAN:** ZDI-CAN-1824
- **Date:** 2013-05-10
- **CVE:** CVE-2013-0912
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Nils and Jon of MWR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-064/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the usage of static_cast. The issue lies in the ability to create an object that is a smaller size than it is treated after a static_cast. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2013/03/stable-channel-update_7.html

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
