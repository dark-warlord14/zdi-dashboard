# ZDI-15-191: Microsoft Windows .MSC Stack Buffer Overflow Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-191
- **ZDI-CAN:** ZDI-CAN-2759
- **Date:** 2015-05-12
- **CVE:** CVE-2015-1681
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Michael Heerklotz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-191/
## Vulnerability Details

This vulnerability allows an attacker to cause a denial of service condition on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit open a malicious directory or device. The specific flaw exists within the handling of Microsoft Management Console Snap-in Control files (.msc files). These files can contain encoded icons for display in the Windows shell or common file dialogs. By malforming this icon information, an attacker can overflow a statically allocated buffer on the stack and cause a denial of service condition. Because this is exposed through the common file dialogs, third-party applications or extensions may also be vulnerable to denial of service or execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-054

## Disclosure Timeline

- 2015-02-17 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
