# ZDI-14-385: Dell Sonicwall GMS Virtual Appliance Multiple Remote Code Execution Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-14-385
- **ZDI-CAN:** ZDI-CAN-2286
- **Date:** 2014-11-21
- **CVE:** CVE-2014-8420
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** SonicWALL
- **Affected Products:** GMS Virtual Appliance
- **Credit:** Brandon Perry
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-385/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Dell SonicWALL Global Management System (GMS) virtual appliance. Authentication is required to exploit this vulnerability. The specific flaw exists within the GMS ViewPoint (GMSVP) web application. The issue lies in the handling of configuration input due to a failure to safely sanitize user data before executing a command. An attacker could leverage this vulnerability to execute code with root privileges on the underlying operating system.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://support.software.dell.com/product-notification/136814

## Disclosure Timeline

- 2014-07-21 - Vulnerability reported to vendor
- 2014-11-21 - Coordinated public release of advisory
