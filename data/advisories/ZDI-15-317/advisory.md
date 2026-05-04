# ZDI-15-317: Adobe Reader ANSendForReview Javascript API Restrictions Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-317
- **ZDI-CAN:** ZDI-CAN-2995
- **Date:** 2015-07-14
- **CVE:** CVE-2015-4438
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader DC
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-317/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the ANSendForReview method. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to bypass the Javascript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-06-01 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
