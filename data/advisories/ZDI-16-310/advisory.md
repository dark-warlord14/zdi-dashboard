# ZDI-16-310: Adobe Acrobat Pro DC WillClose JavaScript API Restrictions Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-310
- **ZDI-CAN:** ZDI-CAN-3491
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1062
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-310/
## Vulnerability Details

This vulnerability allows remote attackers to bypass API restrictions on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WillClose event. By creating a specially crafted PDF with a specific WillClose event, it is possible to bypass the Javascript API restrictions. A remote attacker could exploit this vulnerability to execute arbitrary code.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-01-05 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
