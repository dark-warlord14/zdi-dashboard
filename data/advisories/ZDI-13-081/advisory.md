# ZDI-13-081: (Pwn2Own) Microsoft Internet Explorer Protected Mode Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-081
- **ZDI-CAN:** ZDI-CAN-1872
- **Date:** 2013-05-29
- **CVE:** N/A
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** VUPEN Security [ http://www.vupen.com ]
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of pop-up windows. The issue lies in a failure to properly validate the type of object being passed to the broker. An attacker can leverage this vulnerability to execute code under the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-037

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
