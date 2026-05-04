# ZDI-16-190: Adobe Acrobat Pro DC DLL Planting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-190
- **ZDI-CAN:** ZDI-CAN-3111
- **Date:** 2016-03-08
- **CVE:** CVE-2016-1008
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AbdulAziz Hariri and Jasiel Spelman of HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-190/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the handling of DLL search paths. In specific situations an attacker can force Acrobat Pro DC to load an arbitrary DLL from specific locations. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-09.html

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
