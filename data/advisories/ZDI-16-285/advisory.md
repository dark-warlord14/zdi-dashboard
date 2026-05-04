# ZDI-16-285: Adobe Acrobat Reader DC app.launchURL Command Execution Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-285
- **ZDI-CAN:** ZDI-CAN-3365
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1117
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** AbdulAziz Hariri - HPE Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Reader DC. Authentication is not required to exploit this vulnerability. The specific flaw exists within handling URL's passed to app.launchURL. A specially crafted cURL passed to app.launchURL can force a command to be executed. A remote attacker could exploit this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2015-10-20 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
