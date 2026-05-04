# ZDI-15-509: Adobe Acrobat Reader DC app.launchURL Command Execution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-509
- **ZDI-CAN:** ZDI-CAN-3103
- **Date:** 2015-10-13
- **CVE:** CVE-2015-7614
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-509/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling URL's passed to app.launchURL. A specially crafted cURL passed to app.launchURL can force a command to be executed. A remote attacker could exploit this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
