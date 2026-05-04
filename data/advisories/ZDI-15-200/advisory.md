# ZDI-15-200: Adobe Acrobat Reader SharedReviewDocCenterInitiator onError Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-200
- **ZDI-CAN:** ZDI-CAN-2690
- **Date:** 2015-05-12
- **CVE:** CVE-2015-3066
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-200/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the SharedReviewDocCenterInitiator onError event. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to bypass the JavaScript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-10.html

## Disclosure Timeline

- 2015-01-20 - Vulnerability reported to vendor
- 2015-05-12 - Coordinated public release of advisory
