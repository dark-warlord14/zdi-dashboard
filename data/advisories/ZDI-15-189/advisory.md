# ZDI-15-189: (Pwn2Own) Microsoft Windows CNG Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-189
- **ZDI-CAN:** ZDI-CAN-2834
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1674
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-189/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the cng.sys driver. The issue lies in a series of IOCTLs that return pointers to functions within the driver. An attacker can leverage this together with another vulnerability to achieve code execution under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-052

## Disclosure Timeline

- 2015-03-19 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
