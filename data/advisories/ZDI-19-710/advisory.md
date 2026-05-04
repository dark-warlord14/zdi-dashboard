# ZDI-19-710: Microsoft Windows XmlLite XML space Attribute Denial-Of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-710
- **ZDI-CAN:** ZDI-CAN-8494
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1187
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Catxploit
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-710/
## Vulnerability Details

This vulnerability allows remote attackers to produce a denial-of-service condition on affected installations of Microsoft Windows. Interaction with the XmlLite.dll library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the handling of xml:space attributes in XmlLite.dll. A crafted xml:space attribute can cause a write to a read-only memory page. An attacker can leverage this vulnerability to produce a denial-of-service condition.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1187

## Disclosure Timeline

- 2019-05-02 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory
