# ZDI-20-647: Microsoft Windows EMF EMR_SETDIBITSTODEVICE Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-647
- **ZDI-CAN:** ZDI-CAN-10743
- **Date:** 2020-05-12
- **CVE:** CVE-2020-0987
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-647/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of EMF images in gdi32full.dll. A crafted EMR_SETDIBITSTODEVICE record in an EMF image can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0987

## Disclosure Timeline

- 2020-03-31 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
