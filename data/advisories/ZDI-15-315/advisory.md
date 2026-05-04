# ZDI-15-315: Adobe Reader AdobeARM Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-315
- **ZDI-CAN:** ZDI-CAN-2908
- **Date:** 2015-07-14
- **CVE:** CVE-2015-5091
- **CVSS:** 6.3
- **CVSS Vector:** AV:L/AC:M/Au:N/C:N/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** AbdulAziz Hariri and Jasiel Spelman - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-315/
## Vulnerability Details

This vulnerability allows local attackers to delete files on vulnerable installations of Adobe Reader. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of junction points in AdobeARM.exe. A local attacker running code as a normal user can set up a junction point in the ARM folder and then run a user control which will delete the contents of the folder. An attacker could use this to create a denial-of-service condition under the context of the SYSTEM user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/reader/apsb15-15.html

## Disclosure Timeline

- 2015-04-28 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
