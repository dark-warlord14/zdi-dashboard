# ZDI-15-494: Adobe Acrobat Reader DC ANVerifyComments Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-494
- **ZDI-CAN:** ZDI-CAN-3073
- **Date:** 2015-10-13
- **CVE:** CVE-2015-7616
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-494/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ANVerifyComments method. By creating a specially crafted PDF with specific Javascript instructions, it is possible to bypass the Javascript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-07-27 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
