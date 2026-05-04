# ZDI-15-231: Dell Sonicwall GMS Virtual Appliance Multiple Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-15-231
- **ZDI-CAN:** ZDI-CAN-2659
- **Date:** 2015-05-15
- **CVE:** CVE-2015-3990
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** kernelsmith - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Dell SonicWALL Global Management System (GMS) virtual appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the GMS ViewPoint (GMSVP) web application. The issue lies in the handling of configuration input due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges on the underlying operating system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://support.software.dell.com/product-notification/152178?productName=SonicWALL%20GMS

## Disclosure Timeline

- 2015-01-13 - Vulnerability reported to vendor
- 2015-05-15 - Coordinated public release of advisory
