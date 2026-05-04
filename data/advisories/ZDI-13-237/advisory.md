# ZDI-13-237: Microsoft Windows OpenType Font Parsing Persistent Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-237
- **ZDI-CAN:** ZDI-CAN-1754
- **Date:** 2013-10-11
- **CVE:** CVE-2013-3128
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:M/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows XP SP3
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-237/
## Vulnerability Details

This vulnerability allows remote attackers to causes a persistent Denial-of-Service on machines running vulnerable versions of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must open a vulnerable font. The specific flaw exists within the handling of OpenType Fonts in the Windows Kernel. The machine will immediately crash and be unable to restart if a user attempts to use the malicious font.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-081

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-10-11 - Coordinated public release of advisory
