# ZDI-15-314: Adobe Reader ARMSvc Elevation of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-314
- **ZDI-CAN:** ZDI-CAN-2907
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5090
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri and Jasiel Spelman - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-314/
## Vulnerability Details

This vulnerability allows local attackers to elevate privileges on vulnerable installations of Adobe Reader. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ARMSvc service. An attacker can force the service to overwrite the Adobe updater with any file signed by Adobe. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-04-28 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
