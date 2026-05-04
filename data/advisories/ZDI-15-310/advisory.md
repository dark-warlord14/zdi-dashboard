# ZDI-15-310: Adobe Reader Folder Level Scripts Unload Denial Of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-310
- **ZDI-CAN:** ZDI-CAN-2936
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5085
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri and Jasiel Spelman - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-310/
## Vulnerability Details

This vulnerability allows remote attackers to unload folder level scripts on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the app.doc object. By creating a specially crafted PDF with specific JavaScript instructions, it is possible to unload folder level scripts from the document level. A remote attacker could exploit this to create a denial of service condition.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-05-14 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
