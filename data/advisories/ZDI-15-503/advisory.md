# ZDI-15-503: Adobe Acrobat Reader DC CBSharedReviewIfOfflineDialog Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-503
- **ZDI-CAN:** ZDI-CAN-3087
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6718
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Matt Molinyawe and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-503/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CBSharedReviewIfOfflineDialog method. By creating a specially crafted PDF with specific Javascript instructions, it is possible to bypass the Javascript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-07-24 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
